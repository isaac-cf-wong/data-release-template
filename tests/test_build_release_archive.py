"""Tests for deterministic release archive helpers."""

from build_release_archive import archive_name


def test_archive_name_normalizes_unsafe_characters() -> None:
    """Archive names are safe for common filesystems."""
    assert archive_name("data release/v1") == "data-release-v1"


def test_archive_name_rejects_empty_values() -> None:
    """Names made only of punctuation are rejected."""
    try:
        archive_name("...")
    except ValueError:
        pass
    else:
        raise AssertionError("expected ValueError")
