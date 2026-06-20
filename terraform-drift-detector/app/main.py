import yaml

from terraform_runner import TerraformRunner
from drift_parser import DriftParser
from openai_analyzer import OpenAIAnalyzer
from remediation_generator import (
    RemediationGenerator
)


def main():

    config = yaml.safe_load(
        open("config/config.yaml")
    )

    tf = TerraformRunner(
        config["terraform"]["working_dir"]
    )

    print("Running terraform scan")

    plan = tf.generate_plan()

    drift = DriftParser.parse(plan)

    if not drift:
        print("No drift detected")
        return

    analyzer = OpenAIAnalyzer()

    result = analyzer.analyze(
        [d.model_dump() for d in drift]
    )

    RemediationGenerator.save(result)

    print(
        "Analysis saved in reports/"
    )


if __name__ == "__main__":
    main()
