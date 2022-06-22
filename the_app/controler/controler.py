from .db import Database


class TheAppControler:
    def __init__(self):
        self.db = Database()

    async def save_data(self, data):
        await self.db.save_data(data)
