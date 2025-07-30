

import ctypes
import os
from pathlib import Path

# Load the shared library (adjust path as needed)
lib_path = Path(__file__).resolve().parent.parent.parent / "src" / "mylib" / "libmylib.dylib"
mylib = ctypes.CDLL(str(lib_path))

# Define argument and return types for the exposed C++ functions
mylib.add.argtypes = [ctypes.c_int, ctypes.c_int]
mylib.add.restype = ctypes.c_int

def add_numbers(a: int, b: int) -> int:
    """Bridge function to call C++ add from Python."""
    return mylib.add(a, b)