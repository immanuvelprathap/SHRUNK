# SHRUNK · Flow v9 Pitch Deck

Sovereign clinical-intelligence pitch deck with embedded 60-second story, dashboard scene, and interactive demo.

## Live URLs

- **Pitch deck:** https://immanuvelprathap.github.io/SHRUNK/
- **Interactive dashboard demo:** https://immanuvelprathap.github.io/SHRUNK/dashboard/
- **Story prompts:** https://immanuvelprathap.github.io/SHRUNK/story-prompts/

## Repository layout

| Path | What it is |
|---|---|
| `index.html` | Flow v9 pitch deck |
| `assets/` | Story video, poster, dashboard screenshot |
| `dashboard/` | Self-contained interactive clinical-intelligence dashboard demo |
| `story-prompts/` | Higgsfield AI and Gemini Nano Banana Pro video-generation prompts |

## Custom domain (GoDaddy / DNS)

To point `https://immanuvelprathap.com` to this GitHub Pages site:

1. In this repo, go to **Settings → Pages → Custom domain** and enter `immanuvelprathap.com`.
   - This creates a `CNAME` file at the repo root.
2. In your GoDaddy DNS for the domain, add one of the following:
   - **Apex (`@`):** A records pointing to GitHub Pages IPs:
     - `185.199.108.153`
     - `185.199.109.153`
     - `185.199.110.153`
     - `185.199.111.153`
   - **WWW (`www`):** CNAME record pointing to `immanuvelprathap.github.io`.
3. Wait for DNS propagation and GitHub’s HTTPS certificate. The dashboard will then be available at:
   - `https://immanuvelprathap.com/dashboard/`

## Dashboard demo notes

- The `dashboard/index.html` is a fully client-side, synthetic-data demo.
- It demonstrates the Clinical Intelligence Document (10 sections), longitudinal patient chat tracking, XAI, CEAI, and federation controls.
- No PHI or backend is used; it is safe for public hosting.
