from ai.llm_client import LLMClient


class FailureAnalyzer:

    def __init__(self):
        self.llm_client = LLMClient()

    def analyze_failure(
        self,
        test_name,
        error_message,
        traceback=""
    ):
        prompt = f"""
You are a Software QA Automation failure analyzer.

Analyze the following automated test failure.

Test Name:
{test_name}

Error Message:
{error_message}

Traceback:
{traceback}

Provide:
1. Probable root cause
2. Recommended fix
3. Failure category

Keep the analysis concise and technical.
"""

        return self.llm_client.generate_response(prompt)
