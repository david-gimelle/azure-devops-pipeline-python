from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/ping")
async def pinging():
    return JSONResponse(content={"message": "pong"}, status_code=200)

@app.get("/demo")
async def get_demo():
    return JSONResponse(content={"message": "demo"}, status_code=200)

@app.get("/health")
async def health():
    return JSONResponse(content={"status": "healthy"}, status_code=200)