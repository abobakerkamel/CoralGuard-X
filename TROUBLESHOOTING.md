# Troubleshooting Knowledge Base

## 1. `coralscop_predictor` is undefined

**Cause:** CoralSCOP model/predictor initialization cell was not run after a kernel/device restart.

**Fix:** run the CoralSCOP loading cell before pseudo-mask generation or inference.

---

## 2. `mask_bbox`: `ValueError: too many values to unpack`

**Cause:** a stored/returned mask sometimes had an extra singleton/channel dimension instead of strict `H×W`.

**Final pattern:** normalize every mask before geometry operations.

```python
def normalize_mask_2d(mask):
    mask = np.asarray(mask)
    mask = np.squeeze(mask)
    if mask.ndim == 3:
        if mask.shape[0] in (1, 3, 4):
            mask = mask[0]
        elif mask.shape[-1] in (1, 3, 4):
            mask = mask[..., 0]
    if mask.ndim != 2:
        raise ValueError(f"Expected 2D mask, got {mask.shape}")
    return (mask > 0).astype(bool)
```

---

## 3. Cell 6 `KeyError: 'score'`

**Cause:** the empty-mask branch of `mask_quality()` did not return all keys expected later by the audit writer.

**Fix:** every branch must return a consistent dictionary schema including `score`, `area_ratio`, `bbox_iou`, `mask_pixels`, and `reason`.

---

## 4. Dual-view build: boolean index dimension mismatch

Error:

```text
IndexError: boolean index did not match indexed array along axis 2;
size of axis is 3 but size of corresponding boolean axis is 1
```

**Cause:** `context` was `H×W×3`, while `local_mask` was `H×W×1`.

**Fix:** use `np.squeeze`, normalize to a strict 2-D boolean mask, and resize with nearest-neighbor if spatial dimensions differ before:

```python
masked[~local_mask] = 0
```

---

## 5. Dual-view dataset generation is slow

**Cause:** repeated JPEG reads/decodes for multiple coral ROIs from the same source image.

**Fixes used:**

- group ROIs by source image,
- load the source image once,
- process all corals from that image in RAM,
- skip existing `context.jpg` + `masked.jpg` outputs,
- use `itertuples()` instead of heavy `iterrows()` in hot loops.

---

## 6. Dual-view EfficientNet training is slow

**Causes:**

- two images per sample,
- repeated disk JPEG decode,
- two separate backbone forwards,
- Windows notebook multiprocessing limitations.

**Fast version used:**

- pre-resize/cache context + masked images in system RAM,
- concatenate both views and perform one shared-backbone forward,
- FP16 AMP,
- channels-last format,
- cuDNN benchmark,
- TF32 where applicable,
- fused AdamW when available,
- batch 64 on RTX A6000,
- resume from existing checkpoint.

---

## 7. Video seed pass is too slow

Observed expensive setting:

```python
REFRESH_STRIDE = 1
```

This runs YOLO26m + CoralSCOP on every frame.

**Immediate fix:** increase refresh stride, e.g. `5` or `10`, depending on the desired speed/accuracy trade-off.

**Preferred future fix:** adaptive CoralSCOP — run CoralSCOP only for new, uncertain, overlapping, or failed tracks, plus periodic safety refreshes.

---

## 8. Track count grows too high

Observed long-video seed passes created 60+ track IDs.

**Likely issue:** track fragmentation / overly permissive creation of new IDs.

**Impact:** larger SAM2 state and potentially unstable identity continuity.

**Quick demo workaround:** keep only the most stable tracks ranked by repeated refresh hits.

**Production fix:** improve association and pruning using mask IoU, box IoU, centroid distance, track gap rules, and duplicate suppression.

---

## 9. SAHI performed poorly

The Stage 3 SAHI/sliced inference route degraded badly in this dataset and is not part of the current final system.

**Status:** deprecated.

---

## 10. P2 Stage 4 looked weak

P2 Stage 4 was heavily architecture-changed and transferred only part of the previous weights; 15 epochs were insufficient for a fair conclusion.

**Interpretation:** under-converged experiment, not proof that P2 is inherently bad.

---

## 11. Video MP4 quality was poor with OpenCV `mp4v`

**Fix:** use FFmpeg H.264 with CRF-based quality control. High-quality experiments used CRF around 10–12; quick demos can use CRF ~16 with a faster preset.
