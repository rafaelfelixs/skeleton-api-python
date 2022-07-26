from fastapi import APIRouter


def builder_router():
    router = APIRouter()

    @router.get("/is-alive")
    async def read_root():
        return {"message": "ok"}

    return router
