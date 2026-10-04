# Upload to GitHub

## Option A — Git command line

Create a new empty repository on GitHub, then from this folder:

```bash
git init
git add .
git commit -m "Initial CoralGuard-X project release"
git branch -M main
git remote add origin https://github.com/<YOUR_USERNAME>/<YOUR_REPOSITORY>.git
git push -u origin main
```

## Option B — GitHub Desktop

1. Add this local folder as a repository.
2. Publish repository.
3. Review the file list before pushing.

## Large files

GitHub rejects normal Git files above 100 MB. This package intentionally excludes the full `coral_video.zip` (~212 MB), datasets, and model weights.

If you later decide to publish large checkpoints/videos, use Git LFS only after confirming licensing:

```bash
git lfs install
git lfs track "*.pt"
git lfs track "*.pth"
git lfs track "*.mp4"
git lfs track "*.zip"
git add .gitattributes
```

## Before making the repository public

- verify dataset redistribution rights,
- verify CoralSCOP and Ultralytics licensing for your intended use,
- scan notebooks for credentials/tokens,
- remove local absolute paths if you want a portable public demo,
- ensure no patient/private/personal data exists in screenshots or samples,
- decide whether to add a project-wide license.
