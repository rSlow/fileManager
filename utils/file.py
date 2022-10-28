import os.path
from datetime import datetime, timedelta


class File:
    NEW = "[NEW]"

    def __init__(self, base_dir: str, path: str):

        if not os.path.isfile(path):
            raise TypeError(f"{path} is not file")
        if not path.startswith(base_dir):
            raise SyntaxError(f"{base_dir} is not parent directory for file {path}")

        self.base_dir = base_dir
        self.path = path
        self._edit_date = None

    @property
    def filename(self):
        return self.path.split("/")[-1]

    @property
    def relative_root(self):
        return "/".join(self.relative_path.split("/")[:-1])

    @property
    def relative_path(self):
        return self.path[len(self.base_dir) + 1:]

    def is_real(self):
        if not self.filename.startswith("~"):
            return True
        return False

    @property
    def as_center_old(self):
        return self.as_side

    @property
    def as_center_new(self):
        return f"{self.NEW} " + self.as_side

    @property
    def as_side(self):
        return f"{self.filename} ||| {self.relative_root}"
        # split = 50
        # if len(self.relative_path) > split:
        #     paths = self.relative_path.split("/")
        #     first = paths.pop(0)
        #     file = paths.pop(len(paths) - 1)
        #     while len(path := f"{first}/...{'/' * (len(paths) > 0)}{'/'.join(paths)}/{file}") > split:
        #         if len(paths) == 0:
        #             break
        #         paths.pop(0)
        #     return path
        # else:
        #     return self.relative_path

    @property
    def edit_date(self) -> datetime:
        if self._edit_date is None:
            ts = os.path.getmtime(self.path)
            edit_date = FileDatetime.fromtimestamp(ts)
            offset = timedelta(microseconds=edit_date.microsecond)
            self._edit_date = edit_date - offset
        return self._edit_date

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            raise TypeError(f"{other} type {self.__class__} required")

        if other.relative_path == self.relative_path:
            return True
        return False


class FileDatetime(datetime):
    def __eq__(self, other):
        if isinstance(other, type(self)):
            result = super(FileDatetime, self).__eq__(other)
            if not result and abs(self.second - other.second) <= 1:
                return True
            return result

    def __ne__(self, other):
        return not self == other
