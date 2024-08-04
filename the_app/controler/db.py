from configurations import base_db
from configurations.base_db import DatabaseConfiguration, start_db


class Database(DatabaseConfiguration):
    @start_db()
    async def save_data(self, data: dict) -> None:
        await base_db.client.MY_COLLECTION.insert_one(data)
