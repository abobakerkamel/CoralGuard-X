# Notebook Index

## `01_baselines`
Initial detector/classifier baselines and an alternative RF-DETR pipeline.

## `02_yolo11_improvements`
YOLO11n error analysis, Stage 3 targeted fine-tuning, SAHI experiment, and P2 experiments.

- SAHI route: **deprecated** after poor project results.
- P2 Stage 4: **under-converged**, not a fair proof of failure.

## `03_integrated_v1`
Historical Stage 3 + MobileNetV4 end-to-end evaluation and video stabilization notebooks.

## `04_yolo26_effnetv2`
Stronger YOLO26m + EfficientNetV2-S branch, continuation/resume notebooks, and +150-each plan.

## `05_segmentation_teacher_student`
CoralSCOP hybrid and Teacher→Student segmentation work.

The final Teacher→Student student is useful, but its original-GT detection operating point was weaker than the old YOLO26m detector. It is therefore not the primary accuracy-first detector.

## `06_final_accuracy_first`
**Current recommended notebook**:

`CoralGuard_X_ACCURACY_FIRST_YOLO_CoralSCOP_DualView_SAM2_LOCAL.ipynb`
