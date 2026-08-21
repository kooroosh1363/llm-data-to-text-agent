# Security model

## Supported input

The CLI reads local `.csv` and `.json` files only. Inputs are treated as data, never executed. Files are capped at 10 MiB and 100,000 records. Configuration is strict JSON with unknown fields rejected.

## Model boundary

The default deterministic provider makes no network request. The optional Ollama provider accepts only local HTTP endpoints (`localhost`, `127.0.0.1`, or `::1`) and sends computed facts—not raw source rows. This prevents the CLI option from becoming a general server-side request forgery primitive and reduces data exposure.

Local-model wording is explicitly marked as model-generated and is kept separate from the deterministic evidence tables. Model output should still be reviewed before external use.

## Reporting vulnerabilities

Please use GitHub's private vulnerability reporting if enabled for this repository. Do not include secrets, private datasets, or personal data in a public issue.

