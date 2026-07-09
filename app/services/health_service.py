from app.schemas import HealthResponse
from app.config import *

def get_health() -> HealthResponse:
    """
    Retrieve the current application health status.
    """

    return HealthResponse(
        status="healthy",
        version=APP_VERSION,
        database="connected",
    )