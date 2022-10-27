import os.path
from dataclasses import dataclass, fields as _fields
import json


@dataclass
class Config:
    left_dir: str = os.getcwd()
    right_dir: str = os.getcwd()

    __filename = ".filemanager.config"

    @classmethod
    def load(cls):
        if os.path.isfile(cls.__filename):
            with open(cls.__filename, "r") as file:
                try:
                    data: dict = json.load(file)
                except json.decoder.JSONDecodeError:
                    return cls()

            fields = cls.__annotations__.keys()
            saved_fields = [*data.keys()]
            for key in saved_fields:
                if key not in fields:
                    del data[key]

            try:
                return cls(**data)
            except TypeError:
                return cls()
        else:
            config = cls()
            config.save()
            return config

    def save(self):
        config_json = {field.name: getattr(self, field.name) for field in _fields(self)}
        with open(self.__filename, "w") as file:
            json.dump(config_json, file, indent=2, ensure_ascii=False)
