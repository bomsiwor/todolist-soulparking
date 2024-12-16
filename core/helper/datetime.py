from typing import Optional
from datetime import datetime


def formatDateTime(dt: Optional[datetime]) -> Optional[str]:
    if dt:
        return dt.strftime("%Y-%m-%d %H:%M:%S")

    return None
