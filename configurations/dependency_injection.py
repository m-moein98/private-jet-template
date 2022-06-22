import inspect


def inject(**kwargs):
    def decorator(cls):
        for key in kwargs:
            def closure(key, attr):
                def getAttr(self):
                    value = kwargs[key]
                    return value() if inspect.isclass(value) else value

                def setAttr(self, value):
                    setattr(self, key, value() if inspect.isclass(value) else value)

                prop = property(getAttr, setAttr)
                setattr(cls, key, prop)

            closure(key, kwargs[key])
        return cls

    return decorator