from __future__ import annotations

import csv
import json
from pathlib import Path
from typing import Any


MAX_FILE_BYTES = 10 * 1024 * 1024
MAX_ROWS = 100_000


def _validate_path(path: Path) -> None:
    if not path.is_file():
        raise ValueError(f"Input file does not exist: {path}")
    if path.stat().st_size > MAX_FILE_BYTES:
        raise ValueError("Input exceeds the 10 MiB safety limit")


def _validate_records(records: list[Any]) -> tuple[list[dict[str, Any]], set[str]]:
    if not records:
        raise ValueError("Input contains no records")
    if len(records) > MAX_ROWS:
        raise ValueError(f"Input exceeds the {MAX_ROWS:,}-row safety limit")
    if not all(isinstance(record, dict) for record in records):
        raise ValueError("Every JSON record must be an object")
    if not all(all(isinstance(key, str) and key for key in record) for record in records):
        raise ValueError("Every record key must be a non-empty string")
    columns = set().union(*(record.keys() for record in records))
    if not columns:
        raise ValueError("Input records contain no columns")
    return records, columns


def load_records(path: Path) -> tuple[list[dict[str, Any]], set[str]]:
    """Load a bounded local CSV or JSON array without executing input content."""
    _validate_path(path)
    suffix = path.suffix.lower()
    if suffix == ".csv":
        with path.open("r", encoding="utf-8-sig", newline="") as handle:
            reader = csv.DictReader(handle)
            if reader.fieldnames is None:
                raise ValueError("CSV header is missing")
            if any(not field or not field.strip() for field in reader.fieldnames):
                raise ValueError("CSV headers must be non-empty")
            if len(reader.fieldnames) != len(set(reader.fieldnames)):
                raise ValueError("CSV headers must be unique")
            records = []
            for index, row in enumerate(reader, start=1):
                if index > MAX_ROWS:
                    raise ValueError(f"Input exceeds the {MAX_ROWS:,}-row safety limit")
                records.append(dict(row))
        return _validate_records(records)
    if suffix == ".json":
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            raise ValueError(f"Invalid JSON at line {exc.lineno}, column {exc.colno}") from exc
        if not isinstance(data, list):
            raise ValueError("JSON input must be an array of objects")
        return _validate_records(data)
    raise ValueError("Input must use the .csv or .json extension")


def load_config(path: Path) -> dict[str, Any]:
    _validate_path(path)
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ValueError(f"Invalid config JSON at line {exc.lineno}, column {exc.colno}") from exc
    if not isinstance(data, dict):
        raise ValueError("Config root must be a JSON object")
    return data

