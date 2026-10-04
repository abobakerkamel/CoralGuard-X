# Model Metrics Registry

Only verified metrics from project runs are listed here. Different rows may use different evaluation protocols; do not compare values blindly.

## Detection

| Model / Stage | Evaluation | mAP50:95 | mAP50 | Precision | Recall | F1 |
|---|---|---:|---:|---:|---:|---:|
| RF-DETR Medium (10 ep) | validation | 0.5231 final; best ~0.5377 EMA | 0.8271 | 0.8030 | 0.7599 | 0.7808 |
| YOLO11n baseline | validation | 0.436 | 0.697 | 0.719 | 0.593 | — |
| YOLO11n Stage 2 | validation | 0.4439 | 0.7727 | 0.7576 | 0.6864 | — |
| YOLO11n Stage 3 | original validation audit | ~0.473 | ~0.793 | 0.7937 | 0.7175 | 0.7537 |
| YOLO26m | validation | **0.5071** | **0.8069** | **0.8363** | **0.7147** | — |
| YOLO26m-SEG Student | original GT operating point @ conf 0.40 | — | — | 0.7857 | 0.6836 | 0.7311 |

## YOLO26m-SEG pseudo-mask validation

| Metric | Value |
|---|---:|
| Box mAP50:95 | 0.641117 |
| Box mAP50 | 0.811005 |
| Box mAP75 | 0.687784 |
| Mask mAP50:95 | 0.590519 |
| Mask mAP50 | 0.787498 |
| Mask mAP75 | 0.630761 |

> These segmentation metrics are against CoralSCOP pseudo masks, not independent human mask annotations.

## Classification

### MobileNetV4 V3

| Split | Accuracy | Macro-F1 |
|---|---:|---:|
| Validation | 0.9011 | 0.9170 |
| Historical test | 0.8980 | 0.8961 |

Sarcophyton test F1: 0.8539.

### EfficientNetV2-S before dual-view retraining

- Accuracy: **0.8898305**
- Macro Precision: **0.8817367**
- Macro Recall: **0.8885519**
- Macro F1: **0.8838171**
- Weighted F1: **0.8903670**

### Dual-view classifier

An observed early epoch showed:

- Epoch 1 validation Accuracy: **0.8921**
- Epoch 1 validation Macro-F1: **0.8699**

This is **not a final model result**.

## End-to-end

### YOLO11n Stage 3 + MobileNetV4 V3 validation baseline

- Validation images: 100
- GT objects: 354
- Predictions: 320
- Matched detections: 254
- Correct detection + species: 239
- Detector Precision: 79.37%
- Detector Recall: 71.75%
- Detector F1: 75.37%
- Classifier accuracy on matched detections: 94.09%
- Classifier Macro-F1 on matched detections: 94.42%
- End-to-End Species Precision: 74.69%
- End-to-End Species Recall: 67.51%
- **End-to-End Species F1: 70.92%**

Failure attribution:

- 68 pure detector misses
- 32 localization errors
- 15 classification errors

### YOLO26m + EfficientNetV2-S validation integration

- Predictions: 292
- Matched detections: 248
- Correct detection + species: 229
- Best detector confidence: 0.375
- Detector Precision: 0.8493
- Detector Recall: 0.7006
- Classifier accuracy on matched: 0.9234
- End-to-End Species Precision: 0.7842
- End-to-End Species Recall: 0.6469
- **End-to-End Species F1: 0.7090**

Do not equate detector F1, classifier F1, mask mAP, and end-to-end species F1; they measure different layers of the system.
