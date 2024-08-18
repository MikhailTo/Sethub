from enum import Enum
from typing import Final, List, Dict, Any
from app.version import __version__

# Application params
APP_TITLE: Final[str] = "Sethub"
APP_DESCRIPTION: Final[str] = "Sethub is an information portal designed for creating, managing, and sharing various types of lists."

app_params:   Final[Dict[str, Any]] = {
    "title": APP_TITLE, 
    "description": APP_DESCRIPTION,
    "version": __version__,
    "swagger_ui_parameters": {"defaultModelsExpandDepth": -1},
    }

# Uvicorn params
HOST: Final = "0.0.0.0"
PORT: Final = 8000

uvicorn_params:   Final[Dict[str, Any]] = {
    "host": HOST, 
    "port": PORT
    }

# Authentication service constants
AUTH_TAGS: Final[List[str | Enum] | None] = ["Authentication"]
AUTH_URL: Final = "token"

auth_params:   Final[Dict[str, Any]] = {
    "prefix": "/" + AUTH_URL, 
    "tags": AUTH_TAGS
    }

# Posts service constants
POST_TAGS: Final[List[str | Enum] | None] = ["Posts"]
POST_URL: Final = "posts"

post_params:   Final[Dict[str, Any]] = {
    "prefix": "/" + POST_URL, 
    "tags": POST_TAGS
    }


# Token constants
TOKEN_TYPE: Final = "bearer"
TOKEN_ALGORITHM: Final = "HS256"
TOKEN_EXPIRE_MINUTES: Final = 60
