from __future__ import annotations

import argparse
import sys
from pathlib import Path

from d2t_agent.pipeline import generate_report
from d2t_agent.providers import DeterministicProvider, OllamaProvider


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Turn CSV or JSON facts into an evidence-bound Markdown brief.")
    parser.add_argument("--input", required=True, type=Path, help="Local .csv or .json input")
    parser.add_argument("--config", required=True, type=Path, help="Strict JSON report config")
    parser.add_argument("--output", required=True, type=Path, help="Markdown output path")
    parser.add_argument("--provider", choices=("deterministic", "ollama"), default="deterministic")
    parser.add_argument("--ollama-model", default="llama3.2")
    parser.add_argument("--ollama-endpoint", default="http://127.0.0.1:11434/api/generate")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        provider = (
            DeterministicProvider()
            if args.provider == "deterministic"
            else OllamaProvider(model=args.ollama_model, endpoint=args.ollama_endpoint)
        )
        generate_report(args.input, args.config, args.output, provider)
    except (OSError, RuntimeError, ValueError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    print(f"Report written to {args.output}")
    return 0

