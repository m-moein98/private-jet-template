from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter

from configurations.base_router import BaseRouter
from configurations.dependency_injection import inject

from .controler.controler import TheAppControler


router = InferringRouter()


@cbv(router)
@inject(controller=TheAppControler)
class TheAppRouter(BaseRouter):

    def __init__(self, *args, **kwargs) -> None:
        self.controller: TheAppControler
        super().__init__(*args, **kwargs)

    @router.get("/")
    async def root(self) -> None:
        return await self.controller.save_data({"test": "test"})
