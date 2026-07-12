from .employee_routers import router as employee_router
from .health_routers import router as health_router
from .authentication_routers import router as authentication_router

__all__ = [
    "employee_router",
    "health_router",
    "authentication_router"
]