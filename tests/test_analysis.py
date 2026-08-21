from decimal import Decimal

import pytest

from d2t_agent.analysis import analyze
from d2t_agent.models import ReportConfig


def config():
    return ReportConfig.from_dict(
        {
            "title": "Brief",
            "metrics": [
                {"column": "revenue", "label": "Revenue", "aggregation": "sum", "format": "currency"}
            ],
            "group_by": "region",
            "top_n": 2,
        }
    )


def test_analysis_reconciles_total_and_ranked_groups():
    records = [
        {"region": "North", "revenue": "10.25"},
        {"region": "South", "revenue": "7.50"},
        {"region": "North", "revenue": "2.25"},
        {"region": "West", "revenue": ""},
    ]
    facts = analyze(records, {"region", "revenue"}, config(), "sales.csv")
    result = facts.metrics[0]
    assert result.value == Decimal("20.00")
    assert result.valid_count == 3
    assert result.missing_count == 1
    assert [(group.group, group.value) for group in result.groups] == [
        ("North", Decimal("12.50")),
        ("South", Decimal("7.50")),
    ]


def test_non_numeric_values_are_not_silently_ignored():
    with pytest.raises(ValueError, match="row 2"):
        analyze([{"region": "North", "revenue": "ten"}], {"region", "revenue"}, config(), "bad.csv")


def test_missing_configured_columns_are_actionable():
    with pytest.raises(ValueError, match="revenue"):
        analyze([{"region": "North"}], {"region"}, config(), "bad.csv")


def test_metric_requires_at_least_one_value():
    with pytest.raises(ValueError, match="no valid numeric"):
        analyze([{"region": "North", "revenue": ""}], {"region", "revenue"}, config(), "bad.csv")


def test_untrusted_group_text_is_escaped_by_report(tmp_path):
    from d2t_agent.pipeline import generate_report

    source = tmp_path / "sales.csv"
    source.write_text("region,revenue\n**fake**,10\n", encoding="utf-8")
    config_path = tmp_path / "config.json"
    config_path.write_text(
        '{"title":"Brief","metrics":[{"column":"revenue","label":"Revenue"}],"group_by":"region"}',
        encoding="utf-8",
    )
    report = generate_report(source, config_path, tmp_path / "report.md")
    assert "**\\*\\*fake\\*\\***" in report
