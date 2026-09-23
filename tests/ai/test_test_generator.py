from ai.test_generator import TestGenerator as AITestGenerator


def test_generate_test_scenarios():

    generator = AITestGenerator()

    requirement = (
        "A user can log in using a valid username and password. "
        "Username is required and password must contain at least "
        "8 characters."
    )

    result = generator.generate_tests(requirement)

    assert result is not None
    assert isinstance(result, str)
    assert len(result) > 0

    print("\nAI Generated Test Scenarios:")
    print(result)
