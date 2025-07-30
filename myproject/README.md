


# myproject

A Python-C++ hybrid project integrating PyTorch machine learning models with native C++ extensions. The system supports both `ctypes` and `pybind11` interfaces, and includes a LaunchAgent-based macOS background service installer.

## Features

- PyTorch model training and inference
- C++ shared library with Python bridge
- `ctypes` and optional `pybind11` bindings
- macOS `.pkg` installer with LaunchAgent support

## Requirements

- Python 3.8+
- PyTorch
- CMake
- A C++17 compatible compiler
- macOS (for full system integration features)

## Usage

### Train the model

```bash
python3 python/myproject/train.py
```

### Run inference

```bash
python3 python/myproject/infer.py
```

### Call native C++ function

```python
from myproject import cbridge
print(cbridge.add_numbers(3, 4))  # Output: 7
```

## Build Native Library

```bash
mkdir build && cd build
cmake ..
make
```

## License

MIT