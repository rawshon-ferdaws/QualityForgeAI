from ai.failure_analyzer import FailureAnalyzer


def test_analyze_selenium_failure():

    analyzer = FailureAnalyzer()

    analysis = analyzer.analyze_failure(
        test_name="test_valid_login",
        error_message=(
            "selenium.common.exceptions.TimeoutException: "
            "Element not clickable"
        ),
        traceback=(
            "WebDriverWait(driver, 10).until("
            "EC.element_to_be_clickable((By.ID, 'login-button')))"
        )
    )

    assert analysis is not None
    assert isinstance(analysis, str)
    assert len(analysis) > 0

    print("\nAI Failure Analysis:")
    print(analysis)
