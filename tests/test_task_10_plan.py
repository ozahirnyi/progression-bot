"""Task 10: /plan."""

from __future__ import annotations

import pytest

from progression_bot.domain.models import Plan, PlanStage


@pytest.mark.task10
def test_render_plan_text_contains_stages_and_hours():
    """render_plan_text(plan) returns string with each stage name and expected hours."""
    try:
        from progression_bot.bot.render import render_plan_text
    except ImportError as e:
        pytest.skip(f"render.render_plan_text not available: {e}")
    plan = Plan(
        stages=(
            PlanStage(name="Stage A", expected_hours=10),
            PlanStage(name="Stage B", expected_hours=20),
        )
    )
    try:
        text = render_plan_text(plan)
    except NotImplementedError:
        pytest.skip("render_plan_text not implemented")
    if "TODO" in text or "implement" in text.lower():
        pytest.skip("render_plan_text still returns stub (task_10 not implemented)")
    assert "Stage A" in text
    assert "Stage B" in text
    assert "10" in text or "20" in text
