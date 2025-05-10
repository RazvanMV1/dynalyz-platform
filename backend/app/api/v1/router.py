from fastapi import APIRouter
from app.api.v1.endpoints import health, db_check

router = APIRouter()

# Include endpoint-urile
router.include_router(health.router)
router.include_router(db_check.router)

