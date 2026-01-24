from __future__ import annotations

from pathlib import Path

import pytest


@pytest.mark.task00
def test_repo_has_required_student_files():
    # Basic guardrails so PRs from task_00 branch have a passing CI target.
    assert Path("tasks/task_00.md").exists()
    assert Path("tasks/progress.json").exists()
    assert Path("fixtures/mock_state.json").exists()
    assert Path(".github/workflows/ci.yml").exists()
    assert Path(".github/pull_request_template.md").exists()

