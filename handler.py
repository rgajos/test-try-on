import runpod

def handler(event):
    input_data = event["input"]

    # testowy output (na start!)
    return {
        "message": "Serverless działa 🚀",
        "input": input_data
    }

runpod.serverless.start({"handler": handler})
