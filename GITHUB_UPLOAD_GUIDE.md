# GitHub Upload Guide

## Upload steps

1. Open terminal.
2. Go to the project folder:

```bat
cd /d E:\spatial-ai-modeling-system
```

3. Initialize git:

```bash
git init
```

4. Add files:

```bash
git add .
```

5. Commit:

```bash
git commit -m "Initial release: Spatial AI Modeling System v0.1"
```

6. Create a new repository on GitHub.
7. Recommended repository name:

```text
spatial-ai-modeling-system
```

8. Add the remote:

```bash
git remote add origin https://github.com/YOUR_USERNAME/spatial-ai-modeling-system.git
```

9. Set main branch:

```bash
git branch -M main
```

10. Push:

```bash
git push -u origin main
```

## Before uploading

- Do not upload `E:\urban-design`.
- Do not upload DWG, DXF, 3DM, GH, GHX, PDF, DOCX, ZIP, RAR, 7Z, backup, or temporary files.
- Check `.gitignore`.
- Check that there is no personal information.
- Check that there is no API key.
- Check that raw project files are not inside this repository.
- If real screenshots are not ready yet, it is still okay to publish v0.1 as a system release.

## Release positioning

v0.1 is a system release: skills, workflow, schemas, templates, validators, prompts, examples, and case study structure. It is not yet a full visual portfolio release.

