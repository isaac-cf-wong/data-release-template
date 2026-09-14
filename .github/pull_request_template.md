## Summary

Describe the changes and mention any related issues (for example,
`Closes #123`).

## Type of change

- [ ] New or revised release data
- [ ] Analysis or reproduction script
- [ ] Bug fix
- [ ] Documentation or metadata
- [ ] Build or workflow maintenance

## Release impact

- [ ] This changes the contents of a future release archive.
- [ ] This changes an already published release and requires an explicit
      decision.
- [ ] This is maintenance only and does not change released data.

If data changed, describe its provenance, format, license, and any relevant size
or privacy considerations.

## Validation

Describe the checks performed and include their commands or outputs.

- [ ] `uv run pytest`
- [ ] `uv run python scripts/build_release_archive.py --output-dir dist`
- [ ] Reproduction or analysis scripts were run where applicable.
- [ ] The README, citation metadata, and data documentation are up to date.

## Checklist

- [ ] I performed a self-review.
- [ ] I added or updated tests for changed scripts.
- [ ] I checked that no secrets, credentials, or unintended large files are
      included.
- [ ] I confirmed whether the scheduled-release setting should remain disabled.
