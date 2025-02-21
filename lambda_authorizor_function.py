def lambda_handler(event, context):
    # log event
    print(f"event data: {event}")
    # validate token
    authorization = "Deny"
    if event["authorizationToken"] != "123456":
        authorization = "Deny"
    else:
        authorization = "Allow"

    # generate IAM policy
    authorizationpolicy = {
        "principalId": "erikpohl",
        "policyDocument": {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Action": "execute-api:Invoke",
                    "Effect": authorization,
                    "Resource": [
                        "arn:aws:execute-api:us-east-1:669469292348:gbh68d8a53/dev/GET/students"
                    ]
                }
            ]
        }
    }
    return authorizationpolicy
