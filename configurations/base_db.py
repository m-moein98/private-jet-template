import functools

import motor.motor_asyncio

from settings import get_settings


settings = get_settings()

client = None


class DatabaseConfiguration:
    client: motor.motor_asyncio.AsyncIOMotorClient = None
    MY_COLLECTION: motor.motor_asyncio.AsyncIOMotorCollection = None

    async def open(self) -> None:
        self.client = motor.motor_asyncio.AsyncIOMotorClient(settings.MONGO_DB_URL)
        self.MY_COLLECTION = self.client[settings.DB][settings.MY_COLLECTION]

    async def close(self) -> None:
        await self.client.close()


def start_db() -> DatabaseConfiguration:
    def wrapper(func: callable) -> callable:
        @functools.wraps(func)
        async def async_decorator(*args, **kwargs):
            db_client = DatabaseConfiguration()
            await db_client.open()
            global client
            client = db_client
            return await func(*args, **kwargs)

        return async_decorator

    return wrapper
