import os.path
from dataclasses import dataclass, fields
import json


@dataclass
class Config:
    left_dir: str = os.getcwd()
    right_dir: str = os.getcwd()

    __file = "./.config"

    @classmethod
    def load(cls):
        if os.path.isfile(cls.__file):
            with open(cls.__file, "r") as file:
                try:
                    data: dict = json.load(file)
                except json.decoder.JSONDecodeError:
                    return cls()

            annotations = cls.__annotations__
            for key, value in data.items():
                if key in annotations and annotations[key] != type(value):
                    return cls()
            try:
                return cls(**data)
            except TypeError:
                return cls()
        else:
            config = cls()
            config.save()
            return config

    def save(self):
        config_json = {field.name: getattr(self, field.name) for field in fields(self)}
        with open(self.__file, "w") as file:
            json.dump(config_json, file, indent=2, ensure_ascii=False)
