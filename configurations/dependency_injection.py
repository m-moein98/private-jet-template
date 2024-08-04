import inspect


def inject(**kwargs) -> any:
    def decorator(cls: type) -> type:
        for key in kwargs:

            def closure(key: str, attr: any) -> any:
                def getAttr(self) -> any:
                    value = kwargs[key]
                    return value() if inspect.isclass(value) else value

                def setAttr(self, value: any) -> None:
                    setattr(self, key, value() if inspect.isclass(value) else value)

                prop = property(getAttr, setAttr)
                setattr(cls, key, prop)

            closure(key, kwargs[key])
        return cls

    return decorator
