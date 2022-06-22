import configurations.base_db as base_db
from configurations.base_db import DatabaseConfiguration, start_db


class Database(DatabaseConfiguration):
    @start_db()
    async def save_data(self, data):
        await base_db.client.MY_COLLECTION.insert_one(data)
