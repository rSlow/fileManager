import os.path


class File:
    def __init__(self, base_dir: str, path: str):

        if not os.path.isfile(path):
            raise TypeError(f"{path} is not file")
        if not path.startswith(base_dir):
            raise SyntaxError(f"{base_dir} is not parent directory for file {path}")

        self.base_dir = base_dir
        self.path = path
        self.relative_path = self._get_relative_path()

    def _get_relative_path(self):
        return self.path[len(self.base_dir) + 1:]

    def __str__(self):
        split = 80
        if len(self.relative_path) > split:
            paths = self.relative_path.split("/")
            first = paths.pop(0)
            file = paths.pop(len(paths) - 1)
            while len(path := f"{first}/.../{'/'.join(paths)}/{file}") > split:
                paths.pop(0)
                if len(paths) == 0:
                    break
            return path
        else:
            return self.relative_path

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            raise TypeError(f"{other} type {self.__class__} required")

        if other.relative_path == self.relative_path:
            return True
        return False
