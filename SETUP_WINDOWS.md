# Windows Setup — Verified Local Target

## Verified project machine

- Windows
- Python 3.12.0
- PyTorch 2.11.0 + CUDA 12.8 build
- CUDA runtime: 12.8
- GPU: NVIDIA RTX A6000
- VRAM: ~47.99 GB
- Ultralytics: 8.4.117
- timm: 1.0.22
- OpenCV (`cv2`): 5.0.0 in the verified environment
- scikit-learn: 1.9.0
- scipy: 1.18.0
- pandas: 3.0.5
- Pillow: 12.2.0

VS Code interpreter used during the project:

```text
D:\Coral_Local_Workspace\.venv\Scripts\python.exe
```

## Suggested workspace

```text
D:\Coral_Local_Workspace\
├── .venv\
├── data\
│   ├── Coral_Reef_AI_Project\
│   └── Coral_video\
├── models\
├── outputs\
├── cache\
└── third_party\
    ├── CoralSCOP\
    └── sam2\
```

## Setup outline

```powershell
cd D:\Coral_Local_Workspace
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Install the PyTorch build appropriate for your NVIDIA driver/CUDA environment separately, following the official PyTorch installation selector. The verified project environment used PyTorch 2.11.0 with a CUDA 12.8 build.

Clone third-party dependencies under `third_party/`:

```powershell
git clone https://github.com/zhengziqiang/CoralSCOP third_party\CoralSCOP
git clone https://github.com/facebookresearch/sam2.git third_party\sam2
pip install -e third_party\sam2
```

Place the CoralSCOP ViT-B checkpoint at:

```text
D:\Coral_Local_Workspace\models\vit_b_coralscop.pth
```

Place your trained project checkpoints under `models/` or update the auto-discovery paths inside the notebooks.

## FFmpeg

FFmpeg is required for high-quality H.264 final video export. Ensure `ffmpeg` is on `PATH`.

## Jupyter warning

If you see:

```text
TqdmWarning: IProgress not found
```

it is a UI/progress-bar warning, not a model/training failure. Installing/updating `ipywidgets` improves notebook progress rendering.
