# Test page to use in lambda lab.

def lambda_handler(event, context):
    print("In lambda handler")

    resp = {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": "*",
        },
        "body": "--- Hello world... It works ---"
    }

    return resp