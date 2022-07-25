from fastapi import APIRouter


def builder_router():
    router = APIRouter()

    @router.get("/")
    async def read_root():
        return {"Hello": "World"}

    return router
