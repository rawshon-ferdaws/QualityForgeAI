def build_failure_summary(test_name, error_message):
    return {
        "test_name": test_name,
        "error_message": error_message,
        "suggested_action": "Review logs, screenshots, test data, and recent code changes"
    }
