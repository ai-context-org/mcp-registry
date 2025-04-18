from pydantic import BaseModel
from typing import List, Dict

class PluginRegistration(BaseModel):
    name: str
    url: str
    description: str
    scopes: List[str]

class ContextRequest(BaseModel):
    request_id: str
    parameters: Dict
    user_id: str
    time: str

class ContextResponse(BaseModel):
    request_id: str
    documents: List[Dict]
