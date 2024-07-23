def check_types(cls):
    class Wrapper:
        def __init__(self, *args, **kwargs):
            for name, arg in kwargs.items():
                attr_type = cls.__annotations__.get(name, type(arg))
                if not isinstance(arg, attr_type):
                    raise TypeError(f"Argument '{name}' must be {attr_type}")
            self.__wrapped = cls(*args, **kwargs)

        def __getattr__(self, name):
            return getattr(self.__wrapped, name)
    return Wrapper

@check_types
class Data:
    name: str
    value: int

    def __init__(self, name, value):
        self.name = name
        self.value = value

data = Data(name="Count", value='aa')
