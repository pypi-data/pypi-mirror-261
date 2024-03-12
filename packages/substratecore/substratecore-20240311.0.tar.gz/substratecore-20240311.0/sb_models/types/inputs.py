from typing import Dict, List, Optional

from pydantic import BaseModel


class StoreInfo(BaseModel):
    collection: str
    full_metadata: Optional[List[Dict]] = None
