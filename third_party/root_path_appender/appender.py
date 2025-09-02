import os
from typing import AnyStr
import sys

def get_current_path_parent(path: AnyStr, depth=1):
    if depth == 0:
        return path
    else:
        path = os.path.dirname(path)
        return get_current_path_parent(path=path, depth=depth - 1)

sys.path.append(get_current_path_parent(path=os.path.abspath(__file__), depth=4))
