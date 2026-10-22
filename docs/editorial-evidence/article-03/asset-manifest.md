# Article 3 evidence assets

Issue: [#43](https://github.com/andrew199799/trust-bounded-collaboration/issues/43).

Source snapshot: canonical `main` at `3e7a5d574ef9fb44554b528bfd5862c3739f8a7d`.

Asset folder: [editorial Drive folder](https://drive.google.com/drive/folders/1yhhbLGqYaQkOuuZO78wPR2BmQoTY1Qh-)

Images are stored only in the specified Drive folder. These links do not imply public-anyone access; editor access depends on existing Drive permissions. All three are genuine browser captures. No image is committed to GitHub.

| Asset | Source / provenance | Capture UTC; viewport | SHA-256 | Verification / redaction |
| --- | --- | --- | --- | --- |
| [repo-home.jpg](https://drive.google.com/file/d/184BcpiDxMvTA296tS6JWCdzA3e-_XvQg/view) | [Public repository landing page](https://github.com/andrew199799/trust-bounded-collaboration), showing `main`, public status, repository tree, and MIT license | 2026-10-22 13:11:42Z; 874 × 940 | `f9b6195be86940485975b6c8fd77f379b645f2718d894e25ef8e0a22e3246a41` | Genuine in-app-browser capture; no private project or account settings; no edits/redaction |
| [readme-zh.jpg](https://drive.google.com/file/d/1Wt6kdAXZQtF3a_sgakgTgd36bamiD_Gn/view) | [Chinese README permalink at source SHA](https://github.com/andrew199799/trust-bounded-collaboration/blob/3e7a5d574ef9fb44554b528bfd5862c3739f8a7d/README.zh-CN.md) | 2026-10-22 13:13:25Z; 874 × 940 | `cd553917cd33d32af6fbeab165880b6ddea826767ec69693dba06476fad10496` | Genuine GitHub preview capture; no edits/redaction |
| [demo-output.jpg](https://drive.google.com/file/d/1w4EPMYx15Rz7caCI0bMgWoH3NvOR37FD/view) | Local browser rendering of the **exact saved JSON** from `PYTHONPATH=src python -m tbc demo repository --json`, run at the source SHA; table displays every case's original decision, reasons, and `executed` value | 2026-10-22 13:15:41Z; 1280 × 720 | `63d76ce268eeda3a8de07e50c6ca81daf8e4bd0ea8ac5492d1d32198d712b6d4` | Genuine screenshot of a locally rendered execution transcript, **not a terminal screenshot**. Rendering only selected output fields; full stdout is in `demo-reproduction.md`. No edits to values/redaction |

No diagram was needed. All image files are JPEG, with matching `.jpg` names and MIME type. The local browser rendering was used only for capture; no server or executable asset is placed in the repository.
