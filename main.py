from fastapi import FastAPI

from Request import RequestModel

app = FastAPI()

@app.get("/")
def root():
    return "Hello world"

@app.post("/api/v1/request")
async def request(re: RequestModel):
    print(re.json)
    return {"open": "OK"}