
---

### ✅ `README.md`

```markdown
# myproject

A hybrid macOS app that combines PyTorch-based machine learning with native C++ libraries. Built for deployment via signed `.pkg` installers, with LaunchAgent integration for background execution.

## 🚀 Features

- ✅ PyTorch model training & inference
- ✅ C++ shared library accessed via `ctypes` or `pybind11`
- ✅ macOS `.pkg` installer with LaunchAgent
- ✅ Auto-start on login
- ✅ Signed installer package
- ✅ Uninstaller script

---

## 🔧 Requirements

- macOS 12+
- Python 3.8+
- [Homebrew](https://brew.sh/)
- CMake (`brew install cmake`)
- PyTorch & NumPy

Install Python dependencies:

```bash
pip install -r requirements.txt
```

---

## 🛠 Build & Package App

```bash
chmod +x scripts/build_all.sh
./scripts/build_all.sh
```

This creates:

- `/usr/local/myproject/` with `libmylib.dylib`, model, and Python
- `myproject-0.1.0.pkg` — the unsigned installer
- `myproject-0.1.0-signed.pkg` — the signed installer

---

## 📦 Install via .pkg

```bash
sudo installer -pkg myproject-0.1.0-signed.pkg -target /
```

---

## 🔁 Train the Model

```bash
python3 python/myproject/train.py
```

---

## 🔎 Run Inference

```bash
python3 python/myproject/infer.py
```

---

## 🧪 Call Native C++ Function

```python
from myproject import cbridge
print(cbridge.add_numbers(3, 4))  # Output: 7
```

---

## 🧼 Uninstall

```bash
sudo bash scripts/uninstall.sh
```

---

## 🛡 Code Signing & Notarization (Optional)

Edit `scripts/build_all.sh` and replace:

```bash
SIGNING_IDENTITY="Developer ID Installer: Your Name (TEAMID)"
```

Then the script will run:

```bash
productsign --sign "$SIGNING_IDENTITY" ...
```

---

## 📁 Directory Structure

```
myproject/
├── python/              # PyTorch model, training, inference
├── src/                 # C++ sources
├── include/             # C++ headers
├── launchd/             # LaunchAgent plist
├── scripts/             # Build + uninstall scripts
├── models/              # model.pt
├── pkg/                 # Distribution.xml
└── build/               # .pkg output + compiled dylib
```

---
---

