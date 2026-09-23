from ai.llm_client import LLMClient


def test_llm_generates_response():

    client = LLMClient()

    response = client.generate_response(
        "Give me three test scenarios for a login page."
    )

    assert response is not None
    assert isinstance(response, str)
    assert len(response) > 0

    print("\nLLM Response:")
    print(response)
