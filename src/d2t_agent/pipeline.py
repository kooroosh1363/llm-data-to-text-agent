from __future__ import annotations

import os
import tempfile
from pathlib import Path

from d2t_agent.analysis import analyze
from d2t_agent.loaders import load_config, load_records
from d2t_agent.models import ReportConfig
from d2t_agent.providers import DeterministicProvider, ReportProvider


def generate_report(
    input_path: Path,
    config_path: Path,
    output_path: Path,
    provider: ReportProvider | None = None,
) -> str:
    """Validate input, compute facts, render narrative, and atomically write Markdown."""
    records, columns = load_records(input_path)
    config = ReportConfig.from_dict(load_config(config_path))
    facts = analyze(records, columns, config, input_path.name)
    report = (provider or DeterministicProvider()).render(facts, config.title)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary_name = tempfile.mkstemp(
        prefix=f".{output_path.name}.", suffix=".tmp", dir=output_path.parent, text=True
    )
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8") as handle:
            handle.write(report)
        Path(temporary_name).replace(output_path)
    except Exception:
        Path(temporary_name).unlink(missing_ok=True)
        raise
    return report

