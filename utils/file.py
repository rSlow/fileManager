import os.path
from datetime import datetime


class File:
    def __init__(self, base_dir: str, path: str):

        if not os.path.isfile(path):
            raise TypeError(f"{path} is not file")
        if not path.startswith(base_dir):
            raise SyntaxError(f"{base_dir} is not parent directory for file {path}")

        self.base_dir = base_dir
        self.path = path
        self.relative_path = self._get_relative_path()
        self._edit_date = None

    @property
    def filename(self):
        return self.path.split("/")[-1]

    def _get_relative_path(self):
        return self.path[len(self.base_dir) + 1:]

    def get_visible_path(self):
        split = 100
        if len(self.relative_path) > split:
            paths = self.relative_path.split("/")
            first = paths.pop(0)
            file = paths.pop(len(paths) - 1)
            while len(path := f"{first}/...{'/' * (len(paths) > 0)}{'/'.join(paths)}/{file}") > split:
                if len(paths) == 0:
                    break
                paths.pop(0)
            return path
        else:
            return self.relative_path

    def is_real(self):
        if not self.filename.startswith("~"):
            return True
        return False

    def __str__(self):
        return self.get_visible_path()

    def __repr__(self):
        return self.__str__()

    @property
    def edit_date(self) -> datetime:
        if self._edit_date is None:
            ts = os.path.getmtime(self.path)
            edit_date = datetime.fromtimestamp(ts)
            self._edit_date = edit_date
        return self._edit_date

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            raise TypeError(f"{other} type {self.__class__} required")

        if other.relative_path == self.relative_path:
            return True
        return False
