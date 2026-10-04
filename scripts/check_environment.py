from __future__ import annotations

import sys


def safe_version(name: str) -> str:
    try:
        mod = __import__(name)
        return str(getattr(mod, "__version__", "unknown"))
    except Exception as exc:
        return f"NOT AVAILABLE ({exc})"


print("Python      :", sys.version.split()[0])
print("Executable  :", sys.executable)
print("numpy       :", safe_version("numpy"))
print("pandas      :", safe_version("pandas"))
print("cv2         :", safe_version("cv2"))
print("timm        :", safe_version("timm"))
print("ultralytics :", safe_version("ultralytics"))

try:
    import torch

    print("torch       :", torch.__version__)
    print("CUDA runtime:", torch.version.cuda)
    print("CUDA avail. :", torch.cuda.is_available())
    if torch.cuda.is_available():
        print("GPU         :", torch.cuda.get_device_name(0))
        gb = torch.cuda.get_device_properties(0).total_memory / (1024**3)
        print(f"VRAM        : {gb:.2f} GB")
except Exception as exc:
    print("torch       : NOT AVAILABLE", exc)
