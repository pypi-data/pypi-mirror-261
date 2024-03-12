from typing import Dict, Optional

from pydantic import BaseModel


class Message(BaseModel):
    """ """

    metadata: Optional[Dict[str, str]] = None
    payload: bytes
