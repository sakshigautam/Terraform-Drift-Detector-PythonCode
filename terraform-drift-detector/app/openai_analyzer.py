import json
from openai import OpenAI


class OpenAIAnalyzer:

    def __init__(self):
        self.client = OpenAI()

    def analyze(self, drift):

        prompt = f"""
You are a Senior AWS Terraform Engineer.

Analyze the following drift.

Return JSON ONLY.

Determine:

1. Severity
2. Intent
3. Risk
4. Explanation
5. Terraform remediation script

Drift:

{json.dumps(drift, indent=2)}
"""

        response = self.client.responses.create(
            model="gpt-5",
            input=prompt
        )

        return response.output_text
