from fastapi import FastAPI
app = FastAPI()

@app.get("/")

@app.get("/welcome")
def root():
    return {"status": "🔥 FastAPI is alive"}
