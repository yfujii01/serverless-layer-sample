# from layers import say
import say


def hello(event, context):
    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event
    }

    mes = say.say()
    print(mes)
    response = {
        "statusCode": 200,
        "body": mes
    }
    print(response)
    return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """


if __name__ == "__main__":
    hello(None, None)
