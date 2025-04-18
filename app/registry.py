from fastapi import APIRouter, HTTPException
from app.models import PluginRegistration

registry_router = APIRouter()
registry_store = {}

@registry_router.post("/register")
def register_plugin(plugin: PluginRegistration):
    if plugin.name in registry_store:
        raise HTTPException(status_code=400, detail="Plugin already registered")
    registry_store[plugin.name] = plugin
    return {"message": f"Plugin {plugin.name} registered"}

@registry_router.get("/registry")
def get_registry():
    return {"plugins": list(registry_store.values())}
