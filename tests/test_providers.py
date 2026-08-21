import json
from decimal import Decimal

import pytest

from d2t_agent.models import FactBundle, MetricResult, MetricSpec
from d2t_agent.providers import OllamaProvider


def facts():
    return FactBundle(
        "sales.csv",
        2,
        None,
        (MetricResult(MetricSpec("revenue", "Revenue", "sum", "currency"), Decimal("10"), 2, 0),),
    )


@pytest.mark.parametrize(
    "endpoint",
    [
        "https://example.com/api/generate",
        "http://192.168.1.10:11434/api/generate",
        "file:///tmp/socket",
        "http://user:password@localhost:11434/api/generate",
    ],
)
def test_ollama_provider_rejects_nonlocal_or_credentialed_endpoints(endpoint):
    with pytest.raises(ValueError):
        OllamaProvider(endpoint=endpoint)


def test_ollama_sends_only_computed_evidence(monkeypatch):
    captured = {}

    class Response:
        def __enter__(self):
            return self

        def __exit__(self, *args):
            return None

        def read(self):
            return json.dumps({"response": "- Revenue totals $10.00."}).encode()

    def fake_urlopen(request, timeout):
        captured["body"] = json.loads(request.data)
        captured["timeout"] = timeout
        return Response()

    monkeypatch.setattr("d2t_agent.providers.urlopen", fake_urlopen)
    report = OllamaProvider().render(facts(), "Brief")
    assert "Local model narrative" in report
    assert "Auditable evidence" in report
    assert '"row_count": 2' in captured["body"]["prompt"]
    assert "raw rows" not in captured["body"]["prompt"]

