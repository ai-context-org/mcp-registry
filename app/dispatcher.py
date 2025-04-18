from fastapi import APIRouter, HTTPException, Request
from app.models import ContextRequest
from app.registry import registry_store
import httpx, logging
from app.config import MCP_TIMEOUT

dispatcher_router = APIRouter()

@dispatcher_router.post("/dispatch/{plugin_name}")
async def dispatch(plugin_name: str, req: ContextRequest):
    if plugin_name not in registry_store:
        raise HTTPException(status_code=404, detail="Plugin not found")

    plugin_url = registry_store[plugin_name].url
    try:
        async with httpx.AsyncClient(timeout=MCP_TIMEOUT) as client:
            response = await client.post(f"{plugin_url}/mcp/context", json=req.dict())
            return response.json()
    except httpx.RequestError as e:
        logging.error(f"Plugin call failed: {e}")
        raise HTTPException(status_code=502, detail="Plugin error")
