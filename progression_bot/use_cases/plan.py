"""Plan use-cases (student-owned)."""

from __future__ import annotations

from dataclasses import dataclass

from progression_bot.domain.models import Plan, PlanStage, State


@dataclass(frozen=True)
class PlanUpdate:
    stages: tuple[PlanStage, ...]


def get_plan(state: State) -> Plan:
    """Return the plan from state."""

    return state.plan


def update_plan(state: State, update: PlanUpdate) -> State:
    """Update plan stages.

    TODO(student): Implement.
    """

    raise NotImplementedError

