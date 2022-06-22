from configurations.dependency_injection import inject
from .db import Database

@inject(db=Database)
class TheAppControler:
    async def save_data(self, data):
        return self.db.save_data(data)
