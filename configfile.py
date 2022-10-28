import os.path
import sys
from dataclasses import dataclass, fields as _fields
import json

confirmation_env = "CONFIRM_FLAG"


@dataclass
class Config:
    left_dir: str = os.getcwd()
    right_dir: str = os.getcwd()
    confirmation: bool = True
    auto_scan: bool = False

    __filename = ".filemanager.config"

    @classmethod
    def load(cls) -> "Config":
        cls._unhide_config()
        config = None

        try:
            with open(cls.__filename, "r") as file:
                data: dict = json.load(file)
                fields = [f.name for f in _fields(cls)]
                saved_fields = [*data.keys()]
                for field in saved_fields:
                    if field not in fields:
                        del data[field]
                config = cls(**data)
        except (FileNotFoundError, json.decoder.JSONDecodeError, TypeError):
            config = cls()
        finally:
            os.environ.setdefault(confirmation_env, str(int(config.confirmation)))
            config.save()
            return config

    def save(self):
        config_json = {field.name: getattr(self, field.name) for field in _fields(self)}
        try:
            with open(self.__filename, "w") as file:
                json.dump(config_json, file, indent=2, ensure_ascii=False)
        except PermissionError:
            self._unhide_config()
        finally:
            self._hide_config()

    def _hide_config(self):
        if sys.platform == "win32":
            import subprocess
            subprocess.check_call(["attrib", "+h", self.__filename])

    @classmethod
    def _unhide_config(cls):
        if sys.platform == "win32":
            import subprocess
            subprocess.check_call(["attrib", "-h", cls.__filename])
