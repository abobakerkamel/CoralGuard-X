from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

required = [
    ROOT / "README.md",
    ROOT / "ARCHITECTURE.md",
    ROOT / "PROJECT_STATUS.md",
    ROOT / "MODEL_METRICS.md",
    ROOT / "notebooks" / "06_final_accuracy_first" / "CoralGuard_X_ACCURACY_FIRST_YOLO_CoralSCOP_DualView_SAM2_LOCAL.ipynb",
    ROOT / "docs" / "MASTER_PROJECT_KNOWLEDGE_BASE.pdf",
]

missing = [p for p in required if not p.exists()]

print("Repository:", ROOT)
print("Required files checked:", len(required))

if missing:
    print("MISSING:")
    for p in missing:
        print(" -", p.relative_to(ROOT))
    raise SystemExit(1)

print("STATUS: REPOSITORY_HEALTH_OK")
