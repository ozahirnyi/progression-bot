from __future__ import annotations

from datetime import date

import pytest

from progression_bot.bot.parse import parse_duration_to_minutes, parse_log_command


@pytest.mark.task02
@pytest.mark.parametrize(
    ("raw", "minutes"),
    [
        ("32m", 32),
        ("90m", 90),
        ("2h", 120),
        ("2.5h", 150),
        ("1h30m", 90),
        ("2h 15m", 135),
    ],
)
def test_parse_duration_to_minutes(raw: str, minutes: int):
    assert parse_duration_to_minutes(raw) == minutes


@pytest.mark.task02
def test_parse_log_today(fixed_today: date):
    cmd = parse_log_command("/log 2h", today=fixed_today)
    assert cmd.day == fixed_today
    assert cmd.minutes == 120


@pytest.mark.task02
def test_parse_log_yesterday(fixed_today: date):
    cmd = parse_log_command("/log yesterday 45m", today=fixed_today)
    assert cmd.day == date(2026, 1, 23)
    assert cmd.minutes == 45


@pytest.mark.task02
def test_parse_logy_alias(fixed_today: date):
    cmd = parse_log_command("/logy 1h", today=fixed_today)
    assert cmd.day == date(2026, 1, 23)
    assert cmd.minutes == 60


@pytest.mark.task02
def test_parse_log_explicit_date(fixed_today: date):
    cmd = parse_log_command("/log 2026-01-20 2.5h", today=fixed_today)
    assert cmd.day == date(2026, 1, 20)
    assert cmd.minutes == 150


@pytest.mark.task02
@pytest.mark.parametrize("text", ["/log 0m", "/log 1m30", "/log yesterday", "/log 2026-01-99 1h"])
def test_parse_log_invalid_inputs_raise_value_error(text: str, fixed_today: date):
    with pytest.raises(ValueError):
        parse_log_command(text, today=fixed_today)

