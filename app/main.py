from fastapi import APIRouter, Path, Query
from typing import Optional

from .routers.analytics import analytics_router

router = APIRouter()


@router.get('/', tags=['Welcome page'])
async def index():
    """Welcome page"""
    return {
        "User bahavior": "Analysis"
    }

# include routers
router.include_router(analytics_router)