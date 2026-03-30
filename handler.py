import runpod

def handler(job):
    job_input = job.get("input", {}) or {}
    name = job_input.get("name", "world")
    return {"message": f"Hello, {name}!"}

runpod.serverless.start({"handler": handler})
