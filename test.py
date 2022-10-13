from pathlib import Path

# print(*Path.cwd().glob("../*.*"))
import os
from pprint import pprint

for p in os.walk("../", topdown=False):
    pprint(p)
