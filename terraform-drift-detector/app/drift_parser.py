from models import DriftChange


class DriftParser:

    @staticmethod
    def parse(plan_json):

        results = []

        for rc in plan_json.get(
            "resource_changes",
            []
        ):

            results.append(
                DriftChange(
                    resource=rc["address"],
                    action=rc["change"]["actions"],
                    before=rc["change"].get(
                        "before",
                        {}
                    ),
                    after=rc["change"].get(
                        "after",
                        {}
                    ),
                )
            )

        return results
