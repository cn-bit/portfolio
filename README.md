# Carl Navè | Selected Work

Portfolio website for Carl Navè: client leadership, commercial development and customer experience.

A plain static site (HTML and CSS, no build step), published with GitHub Pages.

## What's where

```
index.html                 Home: introduction and the six projects
about.html                 About and contact
work/                      One page per case study
  casper-magazine.html
  byron-bay-bone-broth.html
  elly-sofocli.html
  rt-edgar.html
  femme-connection.html
  cnit.html
assets/css/main.css        All styling (colours and type are set at the top)
assets/img/<project>/      Web-ready images, each in a large and an 800px version
_originals/                Original uploads, kept for reprocessing (not linked from the site)
tools/process_images.py    Crops and compresses originals into assets/img
```

## Publishing with GitHub Pages

1. On GitHub, open the repository and go to **Settings**, then **Pages**.
2. Under **Build and deployment**, set **Source** to **Deploy from a branch**.
3. Choose the **main** branch and the **/ (root)** folder, then click **Save**.
4. After a minute or two the site is live at `https://cn-bit.github.io/portfolio/`.

To use your own domain (for example `work.carlnave.com.au`), enter it under **Custom domain** on the same page, then add the DNS record GitHub shows you at your domain registrar.

## Making updates

**Change some words.** Open the page on GitHub, click the pencil icon, edit the text between the tags, then click **Commit changes**. The live site updates within a couple of minutes.

**Add or replace an image.**

1. Upload the original into `_originals/`.
2. Add a line for it in the `JOBS` list in `tools/process_images.py`, choosing a shape: `tall` (4:5), `wide` (3:2), `square`, `pano` (2:1) or `tile` (2:3).
3. Run `python3 tools/process_images.py` (needs Python with Pillow installed).
4. Reference the new file in the page.

Images shown side by side must use the same shape so they display at the same size.

**Before going public.** Remove each `<p class="draft-note">` line and resolve every `[figure to confirm]` and "To confirm" in the pages.

## Writing style

Australian English. No em dashes or en dashes. Plain, understated language.
