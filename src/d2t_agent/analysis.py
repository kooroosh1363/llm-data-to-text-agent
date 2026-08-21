from __future__ import annotations

from collections import defaultdict
from decimal import Decimal, InvalidOperation
from typing import Any, Iterable

from d2t_agent.models import FactBundle, GroupResult, MetricResult, MetricSpec, ReportConfig


def _decimal(value: Any) -> Decimal | None:
    if value is None or value == "":
        return None
    if isinstance(value, bool):
        raise ValueError("boolean values are not numeric metrics")
    try:
        number = Decimal(str(value).strip())
    except (InvalidOperation, ValueError) as exc:
        raise ValueError(f"not a finite number: {value!r}") from exc
    if not number.is_finite():
        raise ValueError(f"not a finite number: {value!r}")
    return number


def _aggregate(values: Iterable[Decimal], operation: str) -> Decimal:
    items = list(values)
    if not items:
        raise ValueError("metric has no valid numeric values")
    if operation == "sum":
        return sum(items, Decimal(0))
    if operation == "mean":
        return sum(items, Decimal(0)) / Decimal(len(items))
    if operation == "min":
        return min(items)
    if operation == "max":
        return max(items)
    if operation == "count":
        return Decimal(len(items))
    raise ValueError(f"unsupported aggregation: {operation}")


def _metric_values(records: list[dict[str, Any]], spec: MetricSpec) -> tuple[list[Decimal], int]:
    values: list[Decimal] = []
    missing = 0
    for row_number, record in enumerate(records, start=2):
        try:
            value = _decimal(record.get(spec.column))
        except ValueError as exc:
            raise ValueError(f"Column {spec.column!r}, row {row_number}: {exc}") from exc
        if value is None:
            missing += 1
        else:
            values.append(value)
    return values, missing


def analyze(
    records: list[dict[str, Any]],
    columns: set[str],
    config: ReportConfig,
    source_name: str,
) -> FactBundle:
    required = {metric.column for metric in config.metrics}
    if config.group_by:
        required.add(config.group_by)
    missing_columns = sorted(required.difference(columns))
    if missing_columns:
        raise ValueError(f"Input is missing configured column(s): {missing_columns}")

    results: list[MetricResult] = []
    for spec in config.metrics:
        values, missing_count = _metric_values(records, spec)
        overall = _aggregate(values, spec.aggregation)
        groups: tuple[GroupResult, ...] = ()
        if config.group_by:
            grouped: dict[str, list[Decimal]] = defaultdict(list)
            for record in records:
                value = _decimal(record.get(spec.column))
                if value is None:
                    continue
                raw_group = record.get(config.group_by)
                group = str(raw_group).strip() if raw_group is not None else ""
                grouped[group or "(missing)"].append(value)
            ordered = sorted(
                (
                    GroupResult(group, _aggregate(group_values, spec.aggregation), len(group_values))
                    for group, group_values in grouped.items()
                ),
                key=lambda item: (-item.value, item.group.casefold()),
            )
            groups = tuple(ordered[: config.top_n])
        results.append(MetricResult(spec, overall, len(values), missing_count, groups))

    return FactBundle(source_name, len(records), config.group_by, tuple(results))

