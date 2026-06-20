import json
from pathlib import Path


class RemediationGenerator:

    @staticmethod
    def save(result_text):

        data = json.loads(result_text)

        Path("reports").mkdir(
            exist_ok=True
        )

        with open(
            "reports/remediation.sh",
            "w"
        ) as f:
            f.write(
                data["remediation_script"]
            )

        with open(
            "reports/analysis.json",
            "w"
        ) as f:
            json.dump(
                data,
                f,
                indent=2
            )
