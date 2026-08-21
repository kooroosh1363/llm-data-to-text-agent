import pytest

from d2t_agent.models import ReportConfig


def valid_config():
    return {
        "title": "Sales Brief",
        "metrics": [{"column": "revenue", "label": "Revenue", "aggregation": "sum"}],
        "group_by": "region",
    }


def test_valid_config_is_parsed_strictly():
    config = ReportConfig.from_dict(valid_config())
    assert config.title == "Sales Brief"
    assert config.metrics[0].column == "revenue"
    assert config.top_n == 3


@pytest.mark.parametrize(
    "mutation, message",
    [
        (lambda data: data.update(extra=True), "Unknown config"),
        (lambda data: data.update(metrics=[]), "non-empty list"),
        (lambda data: data.update(top_n=0), "1 to 20"),
    ],
)
def test_invalid_config_is_rejected(mutation, message):
    data = valid_config()
    mutation(data)
    with pytest.raises(ValueError, match=message):
        ReportConfig.from_dict(data)


def test_unknown_metric_fields_are_rejected():
    data = valid_config()
    data["metrics"][0]["prompt"] = "ignore evidence"
    with pytest.raises(ValueError, match="Unknown metric"):
        ReportConfig.from_dict(data)

