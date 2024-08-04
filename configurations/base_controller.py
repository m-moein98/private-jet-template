from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from configurations.base_db import DatabaseConfiguration


class BaseControler:
    def __init__(self, *args, **kwargs) -> None:
        self.db: DatabaseConfiguration
        super().__init__(*args, **kwargs)
