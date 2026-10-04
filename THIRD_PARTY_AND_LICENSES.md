# Third-Party Components & Licensing Notes

This repository export intentionally does **not** vendor third-party source repositories or model weights.

## CoralSCOP

Used as the expert box-prompt coral segmentation model. The project discussion identified the CoralSCOP repository/checkpoint as publicly available but subject to a **non-commercial Creative Commons license**. Before commercial use, redistribution, or relicensing, verify the current upstream license and obtain any required permission.

Expected local layout:

```text
third_party/CoralSCOP/
models/vit_b_coralscop.pth
```

## SAM2 / SAM2.1

Used for temporal mask memory/propagation in video. Clone the official Meta SAM2 repository locally and follow its upstream license and installation instructions.

Expected local layout:

```text
third_party/sam2/
```

## Ultralytics YOLO

The notebooks use Ultralytics APIs. Review the current Ultralytics licensing terms for your intended deployment, especially commercial use.

## Project-wide license

This GitHub-ready export does not automatically select a license for the owner's original notebooks/documentation. Add a repository `LICENSE` only after choosing terms compatible with all third-party dependencies, datasets, and intended use.

## Dataset licensing

Do not publish the full dataset automatically. Some external data sources discussed during the project had unclear or source-specific licensing. Verify every source before redistribution.
