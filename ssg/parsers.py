from os import read
from typing import List
from pathlib import Path

class Parser:
    extensions = List[str]

    def valid_extension(self,extension):
        if extension in self.extensions:
            return True
        else:
            return False
    
    def parse(path, source, dest):
        raise NotImplementedError
    
    def read(path):
        with open(path) as file:
            return read(file)
    
    def write(path, dest, content, ext='html'):
        full_path = self.dest / path.with_suffix(ext)

