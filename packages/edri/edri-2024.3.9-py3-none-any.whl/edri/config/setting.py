from os import getenv
from typing import Optional

HEALTH_CHECK_TIMEOUT = 10
DEFAULT_TOKEN_LENGTH = 64
REST_RESPONSE_TIMEOUT = 60

SWITCH_KEY_LENGTH = 8

SWITCH_HOST = getenv("EDRI_SWITCH_HOST")
SWITCH_PORT = getenv("EDRI_SWITCH_POST")
UPLOAD_FILES_PREFIX = "edri_"
UPLOAD_FILES_KEEP_DAYS = getenv("FILES_KEEP_DAYS") or 0
UPLOAD_FILES_PATH = getenv("FILES_PATH") or "/tmp/edri"

CACHE_TIMEOUT = 30
CACHE_INFO_MESSAGE = 60

HOST = getenv("EDRI_HOST") or "localhost"
ws_port_temp = getenv("EDRI_WS_PORT")
WS_PORT: Optional[int] = None
if ws_port_temp:
    WS_PORT = int(ws_port_temp)
