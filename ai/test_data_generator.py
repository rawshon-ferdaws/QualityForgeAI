from ai.llm_client import LLMClient


class TestDataGenerator:

    def __init__(self):
        self.llm_client = LLMClient()

    def generate_test_data(self, requirement):

        prompt = f"""
You are a Software QA Automation Engineer.

Analyze the following requirement:

{requirement}

Generate test data covering:

1. Valid data
2. Invalid data
3. Boundary data
4. Edge-case data

For each test data set provide:
- Input
- Test data
- Expected behavior

Keep the output concise and suitable for automation testing.
"""

        return self.llm_client.generate_response(prompt)
