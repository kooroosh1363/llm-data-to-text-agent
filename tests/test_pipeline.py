from pathlib import Path

from d2t_agent.cli import main
from d2t_agent.pipeline import generate_report


SAMPLE = Path("data/sample/sales.csv")
CONFIG = Path("data/sample/report_config.json")


def test_pipeline_generates_evidence_bound_report(tmp_path):
    output = tmp_path / "report.md"
    report = generate_report(SAMPLE, CONFIG, output)
    assert output.read_text(encoding="utf-8") == report
    assert "$7,266.50" in report
    assert "North" in report
    assert "No external model or paid API" in report
    assert "Records: **6**" in report


def test_checked_in_example_matches_generated_report(tmp_path):
    report = generate_report(SAMPLE, CONFIG, tmp_path / "report.md")
    assert Path("examples/sample-report.md").read_text(encoding="utf-8").rstrip() == report.rstrip()


def test_cli_success(tmp_path, capsys):
    output = tmp_path / "report.md"
    code = main(["--input", str(SAMPLE), "--config", str(CONFIG), "--output", str(output)])
    assert code == 0
    assert output.is_file()
    assert "Report written" in capsys.readouterr().out


def test_cli_failure_does_not_create_output(tmp_path, capsys):
    output = tmp_path / "report.md"
    code = main(["--input", "missing.csv", "--config", str(CONFIG), "--output", str(output)])
    assert code == 2
    assert not output.exists()
    assert "does not exist" in capsys.readouterr().err
