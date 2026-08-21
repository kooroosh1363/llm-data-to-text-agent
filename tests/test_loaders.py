import json

import pytest

from d2t_agent.loaders import load_records


def test_loads_csv_and_json(tmp_path):
    csv_path = tmp_path / "data.csv"
    csv_path.write_text("region,revenue\nNorth,10\n", encoding="utf-8")
    json_path = tmp_path / "data.json"
    json_path.write_text(json.dumps([{"region": "North", "revenue": 10}]), encoding="utf-8")

    csv_records, csv_columns = load_records(csv_path)
    json_records, json_columns = load_records(json_path)
    assert csv_records[0]["revenue"] == "10"
    assert json_records[0]["revenue"] == 10
    assert csv_columns == json_columns == {"region", "revenue"}


@pytest.mark.parametrize("name", ["empty.csv", "empty.json"])
def test_empty_inputs_are_rejected(tmp_path, name):
    path = tmp_path / name
    path.write_text("region,revenue\n" if name.endswith("csv") else "[]", encoding="utf-8")
    with pytest.raises(ValueError, match="no records"):
        load_records(path)


def test_json_must_be_an_array_of_objects(tmp_path):
    path = tmp_path / "data.json"
    path.write_text('{"revenue": 10}', encoding="utf-8")
    with pytest.raises(ValueError, match="array"):
        load_records(path)


def test_unsupported_extension_is_rejected(tmp_path):
    path = tmp_path / "data.txt"
    path.write_text("revenue=10", encoding="utf-8")
    with pytest.raises(ValueError, match=".csv or .json"):
        load_records(path)

