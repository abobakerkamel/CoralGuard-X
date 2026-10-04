# Model Checkpoints

Model checkpoints are not bundled in the GitHub-ready package.

Typical local checkpoint names used by the notebooks include:

```text
models/
├── vit_b_coralscop.pth
├── best_yolo26m_plus150.pt                 # if completed/promoted
├── best_yolo26m_seg_student.pt
├── best_efficientnetv2s_plus150.pth        # if completed/promoted
└── best_dualview_effnetv2s_macro_f1.pth    # after final dual-view training
```

Historical YOLO26m detector checkpoint path used in the local project:

```text
outputs/YOLO26m_EfficientNetV2S_FullPipeline/01_YOLO26m/Detection_YOLO26m/weights/best.pt
```

Do not rename or publish a checkpoint as “final” unless the corresponding validation/test run actually completed and its metrics are recorded.
