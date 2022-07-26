from fastapi import FastAPI

from api.routes import builder_router
from api.routes_user import builder_router_user

router_skeleton = builder_router()
router_user = builder_router_user()

app = FastAPI(docs_url="/api/docs")
app.include_router(router_skeleton, prefix='/api/v1', tags=['skeleton'])
app.include_router(router_user, prefix='/api/v1', tags=['user'])
