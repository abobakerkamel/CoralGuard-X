# Architecture

## Current production candidate: Accuracy-First

```text
RAW FRAME
    ↓
YOLO26m OLD DETECTOR
    ↓
Strong Candidate Boxes
    ↓
CoralSCOP on each candidate box
    ↓
Precise Instance Masks
    ↓
Overlap / Duplicate Resolver
    ↓
Masked Coral + 10% Context
    ↓
Dual-View EfficientNetV2-S
    ↓
Known Species / Other-Unknown Coral / Non-Coral
    ↓
SAM2.1 Temporal Mask Memory
    ↓
Stable ID + Mask + Species
    ↓
Annotated Video + Diagnostics
```

## Component responsibilities

| Component | Role | Input | Output |
|---|---|---|---|
| YOLO26m detector | High-recall coral candidate localization | RGB frame | bounding boxes + confidence |
| CoralSCOP | Prompted coral segmentation | frame + YOLO box | precise coral mask + mask score |
| Duplicate resolver | Remove redundant/overlapping instance hypotheses | masks + boxes | filtered instances |
| Dual-View EfficientNetV2-S | Species/validity classification | masked foreground + context crop | 6 known labels + NON_CORAL probabilities + embedding |
| OOD/validity gate | Avoid forced labels | class probabilities + margin + embedding similarity | known / Other-Unknown Coral / Non-Coral |
| SAM2.1 | Temporal mask propagation and memory | seed masks + video | propagated masks by object ID |
| FFmpeg | High-quality final export | annotated raw frames | H.264 MP4 |

## Teacher → Student branch

A separate experiment generated CoralSCOP pseudo masks from existing ground-truth boxes and trained a YOLO26m-SEG student.

```text
Existing GT Boxes
      ↓
CoralSCOP Teacher
      ↓
Pseudo Instance Masks
      ↓
Quality Filter
      ↓
YOLO26m-SEG Student
```

This branch succeeded at learning useful masks, but the student was weaker than the existing YOLO26m detector on original-GT detection operating-point metrics. Therefore it is currently a **fast/backup segmentation path**, not the main accuracy-first detector.

## Historical architecture evolution

1. YOLO11n detector + MobileNetV4 classifier.
2. Stage 2/3 YOLO11n localization improvements.
3. P2 small-object experiment.
4. YOLO26m + EfficientNetV2-S stronger-model experiment.
5. Hybrid detector + CoralSCOP inference refinement.
6. CoralSCOP Teacher → YOLO26m-SEG Student.
7. Final current accuracy-first: YOLO26m detector + direct CoralSCOP + dual-view classifier + SAM2.1.
