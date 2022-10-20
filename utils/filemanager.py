from .file import File


class SideFileSection(list[File]):
    pass


class CentralFileSection:
    def __init__(self):
        self._left_side = CentralFileSectionSide()
        self._right_side = CentralFileSectionSide()

    def append_to_left(self, file: File):
        self._left_side.append(file)

    def append_to_right(self, file: File):
        self._right_side.append(file)

    def add_pair(self, left_file: File, right_file: File):
        self.append_to_left(left_file)
        self.append_to_right(right_file)

    def __str__(self):
        return f"{[self._left_side, self._right_side]}"


class CentralFileSectionSide(list[File]):
    pass


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
        self.left_section_files = SideFileSection()
        self.right_section_files = SideFileSection()
        self.central_section_files = CentralFileSection()

        self._left_section_file_table = self.app.left_section.get_file_table()
        self._right_section_file_table = self.app.right_section.get_file_table()

        self.init_left_side()
        self.init_right_side()

        print(self.left_section_files)
        print(self.central_section_files)
        print(self.right_section_files)

    def init_right_side(self):
        for path, left_file in self._left_section_file_table.items():
            right_file = self._right_section_file_table.get(path, None)
            if not right_file:
                self.right_section_files.append(left_file)

            # check to add in central side
            elif left_file.edit_date != right_file.edit_date:
                self.central_section_files.add_pair(left_file, right_file)

    def init_left_side(self):
        for path, right_file in self._right_section_file_table.items():
            left_file = self._left_section_file_table.get(path, None)
            if not left_file:
                self.left_section_files.append(right_file)

    # def get_file_table(self):
    #     files = {}
    #     directory = self.file_string.get_directory()
    #     if os.path.isdir(directory):
    #         directory_pattern = os.path.join(directory, "**")
    #         for path in glob.glob(directory_pattern, recursive=True):
    #             if os.path.isfile(path):
    #                 file = File(base_dir=directory, path=path)
    #                 files[file.relative_path] = file
    #     return files
