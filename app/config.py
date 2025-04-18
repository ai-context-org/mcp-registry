from dotenv import load_dotenv
import os

load_dotenv()

REGISTRY_SECRET = os.getenv("REGISTRY_SECRET", "secret")
MCP_TIMEOUT = int(os.getenv("MCP_TIMEOUT", 10))
