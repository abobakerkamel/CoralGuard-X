# Project Status

## Working / verified

- Detection dataset audit completed: 646 images, 2,198 final GT boxes after duplicate removal.
- Train/validation/test split created and preserved.
- YOLO11n Stage 3 baseline/improvement path completed.
- MobileNetV4 V3 classifier completed.
- Historical end-to-end detector + classifier evaluation completed.
- YOLO26m detector trained/evaluated on validation.
- EfficientNetV2-S classifier trained/evaluated on validation.
- CoralSCOP teacher mask generation working locally.
- YOLO26m-SEG Teacher→Student training completed for 150 epochs.
- YOLO26m-SEG validation completed, including original-GT confidence sweep.
- Dual-view dataset construction implemented with robust 2D mask normalization and resume-safe/Turbo variants.
- Accuracy-first notebook created for YOLO26m + CoralSCOP + Dual-View EfficientNetV2-S + SAM2.1.
- Local Windows environment verified on RTX A6000.

## Partially working / still being optimized

- Dual-View EfficientNetV2-S training: training pipeline exists and early validation was promising, but no final completed metric is recorded in this package as a verified final result.
- Video accuracy-first inference: CoralSCOP seed pass works, but runtime can be high when refresh stride is too frequent.
- SAM2 final propagation path exists in the notebook but still needs full final end-to-end runtime validation on the target videos.

## Known current issues

1. **CoralSCOP seed-pass runtime**
   - `REFRESH_STRIDE=1` is too expensive for long videos.
   - `REFRESH_STRIDE=5` gives roughly a 5× reduction in refresh count.
   - Recommended future improvement: adaptive CoralSCOP refresh only for new/uncertain/failed tracks.

2. **Track fragmentation**
   - Seed pass can create many track IDs (60+ observed in long videos).
   - This can increase SAM2 cost and destabilize identity continuity.
   - Needs stronger association/pruning before final production deployment.

3. **True open-set validation is missing**
   - Unknown rejection is pragmatic only.

4. **No human mask GT**
   - Segmentation student mask metrics are teacher agreement, not independent mask accuracy.

## Current recommended demo path

For a quick doctor/demo video:

- process only the first video,
- reuse already generated seed metadata,
- keep only the most stable ~25 tracks for the fast demo,
- classify every ~5 frames,
- export with FFmpeg `veryfast` + CRF 16 for presentation speed.

For final scientific reporting, restore higher-quality settings and measure runtime/stability explicitly.
