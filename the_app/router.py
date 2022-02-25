from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter

from configurations.base_router import BaseRouter
from .db import Database

db_client = Database()
router = InferringRouter()


@cbv(router)
class TheAppRouter(BaseRouter):

    @router.get("/")
    async def root(self):
        return await db_client.save_data({'test': 'test'})
