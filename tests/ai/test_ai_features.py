from ai.failure_analyzer import build_failure_summary
from ai.test_generator import generate_test_ideas


def test_generate_test_ideas():
    test_ideas = generate_test_ideas("Login")

    assert "Positive test for Login" in test_ideas


def test_build_failure_summary():
    summary = build_failure_summary(
        "test_valid_login",
        "TimeoutException"
    )

    assert summary["test_name"] == "test_valid_login"
    assert "suggested_action" in summary
