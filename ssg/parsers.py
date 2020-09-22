from shutil import copy2
from typing import List
from pathlib import Path


class Parser:
    extensions: List[str] = []

    def valid_extension(self, extension):
        return extension in self.extensions

    def parse(self, path: Path, source: Path, dest: Path):
        raise NotImplementedError()

    @staticmethod
    def read(path: Path):
        with open(path) as file:
            return file.read()

    @staticmethod
    def write(path: Path, dest: Path, content, ext='.html'):
        full_path = dest / path.with_suffix(ext).name
        with open(full_path, 'w') as file:
            file.write(content)

    @staticmethod
    def copy(path, source, dest):
        copy2(path, dest / path.relative_to(source))


class ResourceParser(Parser):
    extensions = ['.jpg', '.png', '.gif', '.css', '.html']

    def parse(self, path, source, dest):
        self.copy(path, source, dest)
