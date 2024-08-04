from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from configurations.base_controller import BaseControler


class BaseRouter:
    def __init__(self, *args, **kwargs):
        self.controller: BaseControler
        super().__init__(*args, **kwargs)
