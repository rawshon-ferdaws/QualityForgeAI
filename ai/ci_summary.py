from ai.llm_client import LLMClient


class CISummary:

    def __init__(self):
        self.llm_client = LLMClient()

    def generate_summary(self, test_results):

        prompt = f"""
You are a Software QA Automation Engineer analyzing CI/CD test results.

Analyze the following automated test execution results:

{test_results}

Provide a concise QA summary containing:

1. Overall test status
2. Passed and failed tests
3. Important failures
4. Probable causes
5. Release risks
6. Recommended actions

Keep the summary concise, technical, and suitable for a CI/CD report.
"""

        return self.llm_client.generate_response(prompt)
