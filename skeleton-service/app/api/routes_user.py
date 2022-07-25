from fastapi import APIRouter


def builder_router_user():
    router = APIRouter()

    @router.get("/{id}")
    async def find_by_id(id: str):
        return {"id": id, "name": "Rafael"}

    return router
