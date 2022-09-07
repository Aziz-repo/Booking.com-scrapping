from asyncio.windows_events import NULL
from enum import Enum

class HealthSafetyFilter(Enum):
    TRUE = "health_and_hygiene=1"
    FALSE = NULL