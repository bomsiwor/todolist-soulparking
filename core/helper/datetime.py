from typing import Optional
from datetime import datetime


def formatDateTime(dt: Optional[datetime]) -> Optional[str]:
    if dt:
        return dt.strftime("%d-%m-%Y %H:%M:%S")

    return None
