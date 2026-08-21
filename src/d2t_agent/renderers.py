from __future__ import annotations

from decimal import Decimal

from d2t_agent.models import FactBundle, MetricResult


def format_value(value: Decimal, value_format: str) -> str:
    if value_format == "currency":
        return f"${value:,.2f}"
    if value_format == "percent":
        return f"{value:,.2f}%"
    if value_format == "integer":
        return f"{value.quantize(Decimal('1')):,}"
    rendered = f"{value:,.2f}"
    return rendered.rstrip("0").rstrip(".")


def _table_escape(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ").replace("\r", " ")


def _inline_escape(value: str) -> str:
    clean = value.replace("\n", " ").replace("\r", " ")
    for token in ("\\", "`", "*", "_", "[", "]"):
        clean = clean.replace(token, f"\\{token}")
    return clean


def evidence_markdown(facts: FactBundle) -> str:
    lines = [
        "## Auditable evidence",
        "",
        f"Source: `{_inline_escape(facts.source_name)}` · Records: **{facts.row_count:,}**",
        "",
        "| Metric | Aggregation | Value | Valid | Missing |",
        "|---|---:|---:|---:|---:|",
    ]
    for result in facts.metrics:
        lines.append(
            f"| {_table_escape(result.spec.label)} | {result.spec.aggregation} | "
            f"{format_value(result.value, result.spec.format)} | "
            f"{result.valid_count:,} | {result.missing_count:,} |"
        )
    if facts.group_by:
        lines.extend(["", f"## Top groups by `{_inline_escape(facts.group_by)}`"])
        for result in facts.metrics:
            lines.extend(
                [
                    "",
                    f"### {_inline_escape(result.spec.label)}",
                    "",
                    f"| {_table_escape(facts.group_by)} | Value | Valid records |",
                    "|---|---:|---:|",
                ]
            )
            for group in result.groups:
                lines.append(
                    f"| {_table_escape(group.group)} | {format_value(group.value, result.spec.format)} | "
                    f"{group.valid_count:,} |"
                )
    return "\n".join(lines)


def _summary_line(result: MetricResult, group_by: str | None) -> str:
    line = (
        f"**{_inline_escape(result.spec.label)}** ({result.spec.aggregation}) is "
        f"**{format_value(result.value, result.spec.format)}** across {result.valid_count:,} valid record(s)"
    )
    if result.missing_count:
        line += f", with {result.missing_count:,} missing value(s)"
    if group_by and result.groups:
        top = result.groups[0]
        line += (
            f". The highest `{_inline_escape(group_by)}` group is **{_inline_escape(top.group)}** at "
            f"**{format_value(top.value, result.spec.format)}**"
        )
    return line + "."


def deterministic_report(facts: FactBundle, title: str) -> str:
    lines = [
        f"# {title}",
        "",
        "> Generated locally from computed facts. No external model or paid API was used.",
        "",
        "## Executive summary",
        "",
    ]
    lines.extend(f"- {_summary_line(result, facts.group_by)}" for result in facts.metrics)
    lines.extend(["", evidence_markdown(facts), ""])
    return "\n".join(lines)
