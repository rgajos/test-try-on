import runpod

print("🚀 Loading model...")

# TODO: tutaj później załadujemy OOTDiffusion
model = "fake-model"

print("✅ Model loaded")

def handler(job):
    job_input = job.get("input", {})

    return {
        "status": "ok",
        "input": job_input,
        "message": "model działa (jeszcze fake)"
    }

runpod.serverless.start({"handler": handler})
