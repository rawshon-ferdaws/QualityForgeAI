from ai.ci_summary import CISummary


def test_generate_ci_summary():

    ci_summary = CISummary()

    test_results = """
    35 tests executed
    33 passed
    2 failed

    Failed tests:
    test_valid_login - TimeoutException: login button not clickable
    test_create_post - Expected status 201 but received 500
    """

    result = ci_summary.generate_summary(test_results)

    assert result is not None
    assert isinstance(result, str)
    assert len(result) > 0

    print("\nAI CI Summary:")
    print(result)
