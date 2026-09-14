# Research Data Release Template

Template repository for publishing small research datasets and the scripts
needed to reproduce the associated publication results.

## Use this template

1. Create a repository from this template.
2. Put release data under `data/` and reproducibility scripts under `scripts/`.
3. Add a `CITATION.cff`, publication metadata, and a project-specific README.
4. Run `uv sync --group dev` and `uv run pytest` locally.

The release archive is deterministic and contains the files tracked by Git at
the release commit. Build it with:

```console
uv run python scripts/build_release_archive.py --output-dir dist
```

## Scheduled releases

The scheduled release workflow is deliberately disabled by default. In the
template repository, set the repository variable `ENABLE_SCHEDULED_RELEASE` to
the exact string `true` to enable it. The workflow then checks for commits since
the latest release, runs CI with fresh development dependencies, and publishes a
versioned GitHub release containing the archive and SHA-256 checksum.

Leave this variable unset in repositories created from the template when the
data release must remain frozen. A manual dispatch is also gated by the same
variable, so it cannot accidentally bypass the freeze.

## Layout

```text
data/       Small release data and metadata
scripts/    Analysis and reproduction scripts
tests/      Tests for the scripts
docs/       Optional supplementary documentation
```
