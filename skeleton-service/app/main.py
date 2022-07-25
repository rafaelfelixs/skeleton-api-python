from fastapi import FastAPI
from api.routes import builder_router

router = builder_router()
fastApp = FastAPI(openapi_url="/api/v1/skeleton/openapi.json", docs_url="/api/v1/skeleton/docs")

fastApp.include_router(router, prefix='/api/v1/skeleton', tags=['skeleton'])
