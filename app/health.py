from fastapi import APIRouter
from app.registry import registry_store
import httpx

health_router = APIRouter()

@health_router.get("/health")
async def global_healthcheck():
    results = {}
    async with httpx.AsyncClient() as client:
        for name, plugin in registry_store.items():
            try:
                r = await client.get(f"{plugin.url}/.well-known/mcp.yaml", timeout=3)
                results[name] = r.status_code == 200
            except Exception:
                results[name] = False
    return results
