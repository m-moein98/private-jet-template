from configurations.base_controller import BaseControler
from configurations.dependency_injection import inject

from .db import Database


@inject(db=Database)
class TheAppControler(BaseControler):
    def __init__(self, *args, **kwargs) -> None:
        self.db: Database
        super().__init__(*args, **kwargs)

    async def save_data(self, data: dict) -> None:
        return await self.db.save_data(data)
