# Run Order

## Recommended current path

### 1. Prepare local data/checkpoints

Follow `SETUP_WINDOWS.md` and `data/README.md`.

### 2. Run the final accuracy-first notebook

```text
notebooks/06_final_accuracy_first/
CoralGuard_X_ACCURACY_FIRST_YOLO_CoralSCOP_DualView_SAM2_LOCAL.ipynb
```

Core flow:

1. environment/config,
2. path/checkpoint discovery,
3. CoralSCOP/SAM2 setup,
4. teacher-mask reuse/generation,
5. dual-view dataset build,
6. Dual-View EfficientNetV2-S train/reuse,
7. validation + OOD calibration,
8. YOLO26m + CoralSCOP image smoke test,
9. video extraction and seed pass,
10. SAM2.1 propagation,
11. final video export.

## Quick demo mode

If the goal is to produce one demonstration video quickly:

- process only `video_paths[:1]`,
- reuse existing first-video seed metadata,
- keep the top stable tracks only (around 25 is a practical demo setting used during troubleshooting),
- set classification stride around 5,
- use FFmpeg `veryfast` + CRF 16 for presentation output.

## Scientific/final mode

For final reporting:

- restore quality-focused encoding,
- retain all justified objects rather than arbitrary demo pruning,
- report measured FPS/latency/flicker,
- keep the held-out detector test untouched until the architecture and operating thresholds are frozen.
