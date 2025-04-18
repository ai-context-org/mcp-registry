from fastapi import FastAPI
from app.registry import registry_router
from app.dispatcher import dispatcher_router
from app.health import health_router

app = FastAPI(title="MCP Registry")

app.include_router(registry_router)
app.include_router(dispatcher_router)
app.include_router(health_router)
