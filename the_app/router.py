from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter

from configurations.base_router import BaseRouter
from .controler.controler import TheAppControler

router = InferringRouter()


@cbv(router)
class TheAppRouter(BaseRouter, TheAppControler):

    @router.get("/")
    async def root(self):
        self.save_data({"test": "test"})
