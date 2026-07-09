from fastapi import APIRouter, status

from app.schemas import HealthResponse
from app.services import get_health

router = APIRouter(
    prefix="/health",
    tags=["Health"],
)


@router.get(
    "/",
    response_model=HealthResponse,
    status_code=status.HTTP_200_OK,
    summary="Health Check",
    description="Retrieve the current health status of the API.",
)
def health():
    """
    Check whether the API is running.
    """

    return get_health()