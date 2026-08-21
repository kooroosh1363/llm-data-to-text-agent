from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal
from typing import Any


AGGREGATIONS = {"sum", "mean", "min", "max", "count"}
FORMATS = {"number", "integer", "currency", "percent"}


@dataclass(frozen=True)
class MetricSpec:
    column: str
    label: str
    aggregation: str = "sum"
    format: str = "number"

    @classmethod
    def from_dict(cls, data: Any) -> "MetricSpec":
        if not isinstance(data, dict):
            raise ValueError("Each metric must be a JSON object")
        unknown = sorted(set(data).difference({"column", "label", "aggregation", "format"}))
        if unknown:
            raise ValueError(f"Unknown metric field(s): {unknown}")
        column = data.get("column")
        if not isinstance(column, str) or not column.strip():
            raise ValueError("Metric 'column' must be a non-empty string")
        label = data.get("label", column)
        aggregation = data.get("aggregation", "sum")
        value_format = data.get("format", "number")
        if not isinstance(label, str) or not label.strip():
            raise ValueError("Metric 'label' must be a non-empty string")
        if aggregation not in AGGREGATIONS:
            raise ValueError(f"Unsupported aggregation: {aggregation!r}")
        if value_format not in FORMATS:
            raise ValueError(f"Unsupported metric format: {value_format!r}")
        return cls(column.strip(), label.strip(), aggregation, value_format)


@dataclass(frozen=True)
class ReportConfig:
    title: str
    metrics: tuple[MetricSpec, ...]
    group_by: str | None = None
    top_n: int = 3

    @classmethod
    def from_dict(cls, data: Any) -> "ReportConfig":
        if not isinstance(data, dict):
            raise ValueError("Config root must be a JSON object")
        unknown = sorted(set(data).difference({"title", "metrics", "group_by", "top_n"}))
        if unknown:
            raise ValueError(f"Unknown config field(s): {unknown}")
        title = data.get("title", "Data Brief")
        if not isinstance(title, str) or not title.strip():
            raise ValueError("Config 'title' must be a non-empty string")
        raw_metrics = data.get("metrics")
        if not isinstance(raw_metrics, list) or not raw_metrics:
            raise ValueError("Config 'metrics' must be a non-empty list")
        metrics = tuple(MetricSpec.from_dict(item) for item in raw_metrics)
        columns = [metric.column for metric in metrics]
        if len(columns) != len(set(columns)):
            raise ValueError("Metric columns must be unique")
        group_by = data.get("group_by")
        if group_by is not None and (not isinstance(group_by, str) or not group_by.strip()):
            raise ValueError("Config 'group_by' must be null or a non-empty string")
        top_n = data.get("top_n", 3)
        if isinstance(top_n, bool) or not isinstance(top_n, int) or not 1 <= top_n <= 20:
            raise ValueError("Config 'top_n' must be an integer from 1 to 20")
        return cls(title.strip(), metrics, group_by.strip() if group_by else None, top_n)


@dataclass(frozen=True)
class GroupResult:
    group: str
    value: Decimal
    valid_count: int


@dataclass(frozen=True)
class MetricResult:
    spec: MetricSpec
    value: Decimal
    valid_count: int
    missing_count: int
    groups: tuple[GroupResult, ...] = ()


@dataclass(frozen=True)
class FactBundle:
    source_name: str
    row_count: int
    group_by: str | None
    metrics: tuple[MetricResult, ...]

    def to_dict(self) -> dict[str, Any]:
        return {
            "source": self.source_name,
            "row_count": self.row_count,
            "group_by": self.group_by,
            "metrics": [
                {
                    "column": result.spec.column,
                    "label": result.spec.label,
                    "aggregation": result.spec.aggregation,
                    "format": result.spec.format,
                    "value": str(result.value),
                    "valid_count": result.valid_count,
                    "missing_count": result.missing_count,
                    "groups": [
                        {"group": group.group, "value": str(group.value), "valid_count": group.valid_count}
                        for group in result.groups
                    ],
                }
                for result in self.metrics
            ],
        }

