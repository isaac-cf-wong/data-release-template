# Contributing

Thank you for improving this research data release template. Contributions that
make small-data publication, reproducibility, and long-term maintenance safer
are welcome.

## Before you start

Open an issue for substantial changes, or check that an existing issue covers
the proposed work. Keep pull requests focused and do not add real publication
data, credentials, or private information to this template repository.

## Development

```console
uv sync --group dev
uv run pre-commit install
uv run pytest
```

Put fixtures and small test data under `tests/`, release data under `data/`, and
reusable analysis or reproduction code under `scripts/`. Update the
documentation and `CITATION.cff` when the repository structure or purpose
changes.

The archive builder includes Git-tracked files only. Before changing it, check
that archive contents, file permissions, timestamps, and checksums remain
deterministic:

```console
uv run python scripts/build_release_archive.py --output-dir dist
```

## Pull requests

Use a Conventional Commit-style title, explain the release impact, and describe
the validation performed. The pull-request template includes checks for data
provenance, licensing, unintended files, and the scheduled-release setting.

The scheduled release and support-floor workflows are gated by the
`ENABLE_SCHEDULED_RELEASE` repository variable. Keep it unset for repositories
whose published data and dependencies must remain frozen.

By contributing, you agree that your contributions are made available under the
repository's BSD 3-Clause license.
