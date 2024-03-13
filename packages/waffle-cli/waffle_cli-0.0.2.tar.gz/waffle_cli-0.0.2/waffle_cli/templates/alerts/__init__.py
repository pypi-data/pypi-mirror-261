from troposphere import Template  # pyright: ignore[reportMissingTypeStubs]
from .parameters import Parameters
from .alerts_sns import AlertsSns


def generate_alerts_stack_json() -> str:
    t = Template()
    parameters = Parameters(t)
    AlertsSns(t, parameters)

    return t.to_json()

def generate_alerts_parameter_list(
    deployment_id: str,
    email_notification_list: str,
) -> list[dict[str, str]]:
    return [
        {
            "ParameterKey": "DeploymentId",
            "ParameterValue": deployment_id,
        },
        {
            "ParameterKey": "EmailNotificationList",
            "ParameterValue": email_notification_list,
        },
    ]
