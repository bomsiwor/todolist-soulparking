from fastapi import APIRouter
from app.todo.todo_route import todo_router

# Create global api prefix using "api"
api_router = APIRouter(prefix="/api")

# Include all sub router
api_router.include_router(todo_router)
