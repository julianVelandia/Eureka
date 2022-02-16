import os


class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Scope(metaclass=SingletonMeta):
    __PROD_SCOPE: str
    __DEV_SCOPE: str
    __TEST_SCOPE: str

    def __init__(self):
        self.__PROD_SCOPE = "prod"
        self.__DEV_SCOPE = "dev"
        self.__TEST_SCOPE = "test"

        os.getenv(self.__DEV_SCOPE, default=self.__DEV_SCOPE)

    def set_scope(self, new_scope):
        if new_scope == self.__DEV_SCOPE:
            os.getenv(self.__DEV_SCOPE)
        elif new_scope == self.__PROD_SCOPE:
            os.getenv(self.__PROD_SCOPE)
        elif new_scope == self.__TEST_SCOPE:
            os.getenv(self.__TEST_SCOPE)
        else:
            #TODO manage error
            pass
