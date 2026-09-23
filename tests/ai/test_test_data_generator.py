from ai.test_data_generator import TestDataGenerator as AITestDataGenerator


def test_generate_test_data():

    generator = AITestDataGenerator()

    requirement = (
        "Username is required and password must contain "
        "at least 8 characters."
    )

    result = generator.generate_test_data(requirement)

    assert result is not None
    assert isinstance(result, str)
    assert len(result) > 0

    print("\nAI Generated Test Data:")
    print(result)
