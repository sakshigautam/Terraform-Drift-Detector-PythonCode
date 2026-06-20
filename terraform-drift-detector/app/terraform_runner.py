import subprocess
import json
from pathlib import Path


class TerraformRunner:

    def __init__(self, working_dir):
        self.working_dir = working_dir

    def generate_plan(self):

        subprocess.run(
            [
                "terraform",
                "plan",
                "-refresh-only",
                "-out=tfplan"
            ],
            cwd=self.working_dir,
            check=True
        )

        subprocess.run(
            [
                "terraform",
                "show",
                "-json",
                "tfplan"
            ],
            cwd=self.working_dir,
            stdout=open(
                f"{self.working_dir}/drift.json",
                "w"
            ),
            check=True
        )

        with open(
            Path(self.working_dir) / "drift.json"
        ) as f:
            return json.load(f)
