from fastapi import FastAPI, Request
import uvicorn

app = FastAPI()

@app.post("/mcp/context")
async def handle_context(request: Request):
    data = await request.json()
    return {
        "request_id": data["request_id"],
        "documents": [
            {"text": "This is a test response from dummy plugin"}
        ]
    }

if __name__ == "__main__":
    uvicorn.run(app, port=8100)

@app.get("/.well-known/mcp.yaml")
async def mcp_spec():
    return {"name": "dummy", "scopes": ["test"]}