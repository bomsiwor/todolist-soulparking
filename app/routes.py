from fastapi import APIRouter
from app.todo.todo_route import todo_router
from core.helper.responses import SuccessResponse

# Create global api prefix using "api"
api_router = APIRouter(prefix="/api")


# Check health api
@api_router.get("/", include_in_schema=False)
def api_root():
    return SuccessResponse(
        message="This API has good health and ready to use.", data=None
    ).result()


# Include all sub router
api_router.include_router(todo_router)
