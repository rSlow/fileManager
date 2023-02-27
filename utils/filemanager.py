import glob
import os
import shutil
from tkinter import constants as c

from .file import File


class SideFileSection(list[File]):
    def __init__(self, root_dir):
        super(SideFileSection, self).__init__()
        self.root_dir = root_dir

    def copy_selected(self, index_tuple: tuple[int]):
        for index in index_tuple:
            file = self[index]
            new_path = os.path.join(self.root_dir, file.relative_root)
            os.makedirs(new_path, exist_ok=True)
            shutil.copy2(
                src=file.path,
                dst=os.path.join(self.root_dir, file.relative_root, file.filename)
            )

    def delete_selected(self, index_tuple: tuple[int]):
        for index in index_tuple:
            file = self[index]
            os.remove(path=file.path)


class CentralFileSideSection(list[File]):
    pass


class CentralFileSection:
    def __init__(self):
        self.left_side = CentralFileSideSection()
        self.right_side = CentralFileSideSection()

    def append_to_left(self, file: File):
        self.left_side.append(file)

    def append_to_right(self, file: File):
        self.right_side.append(file)

    def add_pair(self, left_file: File, right_file: File):
        self.append_to_left(left_file)
        self.append_to_right(right_file)

    def __str__(self):
        return f"[{self.left_side}, {self.right_side}]"

    def copy_selected_to_side(self, indexes: list[int] | tuple[int], to_side: str):
        """to_side - copy in this side from another side"""
        match to_side:
            case c.LEFT:
                dst_section = self.left_side
                src_section = self.right_side
            case c.RIGHT:
                dst_section = self.right_side
                src_section = self.left_side
            case _:
                raise AttributeError(f"section type is not {c.LEFT} or {c.RIGHT}")

        for index in indexes:
            src_file = src_section[index]
            dst_file = dst_section[index]
            shutil.copy2(
                src=src_file.path,
                dst=dst_file.path
            )

    def __bool__(self):
        if self.left_side and self.right_side:
            return True
        return False


class FileManager:
    def __init__(self, app):
        try:
            from app import App
        except ImportError as ex:
            raise ex

        self.app: "App" = app

        self.left_section_files: SideFileSection | None = None
        self.right_section_files: SideFileSection | None = None
        self.central_section_files: CentralFileSection | None = None

        self._left_section_file_table: dict[str, File] | None = None
        self._right_section_file_table: dict[str, File] | None = None

    def scan_files(self):
        left_dir = self.app.left_section.get_dir()
        right_dir = self.app.right_section.get_dir()

        self.left_section_files = SideFileSection(left_dir)
        self.central_section_files = CentralFileSection()
        self.right_section_files = SideFileSection(right_dir)

        self._left_section_file_table = self.get_file_table(self.left_section_files.root_dir)
        self._right_section_file_table = self.get_file_table(self.right_section_files.root_dir)

        self.init_left_side()
        self.init_right_side()

    def init_right_side(self):
        for path, left_file in self._left_section_file_table.items():
            right_file = self._right_section_file_table.get(path, None)
            if right_file is None and left_file.is_real():
                self.right_section_files.append(left_file)

    def init_left_side(self):
        for path, right_file in self._right_section_file_table.items():
            left_file = self._left_section_file_table.get(path, None)
            if left_file is None and right_file.is_real():
                self.left_section_files.append(right_file)
            # auto init central section
            elif left_file and left_file.edit_date != right_file.edit_date:
                self.central_section_files.add_pair(left_file, right_file)

    @staticmethod
    def get_file_table(directory: str):
        files = {}
        if os.path.isdir(directory):
            directory_pattern = os.path.join(directory, "**")
            for path in glob.glob(directory_pattern, recursive=True):
                if os.path.isfile(path):
                    file = File(base_dir=directory, path=path)
                    files[file.relative_path] = file
        return files

    @property
    def empty(self):
        if all((
                not self.left_section_files,
                not self.right_section_files,
                not self.central_section_files
        )):
            return True
        return False

    def get_side(self, side):
        match side:
            case c.LEFT:
                section_files = self.left_section_files
            case c.RIGHT:
                section_files = self.right_section_files
            case _:
                raise AttributeError(f"section type is not {c.LEFT} or {c.RIGHT}")
        return section_files
