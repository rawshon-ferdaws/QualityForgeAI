from ai.llm_client import LLMClient


class TestGenerator:

    def __init__(self):
        self.llm_client = LLMClient()

    def generate_tests(self, requirement):

        prompt = f"""
You are a Software QA Automation Engineer.

Analyze the following requirement:

{requirement}

Generate concise test scenarios covering:

1. Positive tests
2. Negative tests
3. Boundary tests
4. Edge cases

For each scenario provide:
- Test scenario
- Test steps
- Expected result

Do not generate automation code.
"""

        return self.llm_client.generate_response(prompt)
