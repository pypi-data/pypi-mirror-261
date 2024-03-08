from __future__ import annotations

from typing import Any

def coalesce(*arguments: Any) -> Any:
    """Returns the first value in the argument list that is not null."""
    for argument in arguments:
        if argument is not None:
            return argument
        
    return None

class Dictionary(dict):
    """A dictionary built for a dynamic language which allows access to items either by attributes or items."""
    def __init__(self, *args, **kwargs):
        super(Dictionary, self).__init__(*args, **kwargs)
        for arg in args:
            if isinstance(arg, dict):
                for k, v in arg.items():
                    self[k] = v

        if kwargs:
            for k, v in kwargs.items():
                self[k] = v

    def __getattr__(self, attr):
        return self.get(attr)

    def __setattr__(self, key, value):
        self.__setitem__(key, value)

    def __setitem__(self, key, value):
        super(Dictionary, self).__setitem__(key, value)
        self.__dict__.update({key: value})

    def __delattr__(self, item):
        self.__delitem__(item)

    def __delitem__(self, key):
        super(Dictionary, self).__delitem__(key)
        del self.__dict__[key]