from .OrmManager import OrmManager


class Model(object):
    objects = OrmManager()
    def __init__(self, **kwargs) -> None:
        self.__dict__.update(kwargs)
    
