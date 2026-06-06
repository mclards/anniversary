# ❤ Para Sa'yo, Baby

A private, single-link anniversary website for **Jezel** — from **Baba**.
One self-contained `index.html` (HTML + CSS + JS inline). No frameworks, no tracking.

Live target: `https://yourusername.github.io/anniversary`

---

## Open it right now

Double-click **`index.html`**. It works straight from your computer (`file://`) — no server
needed. Placeholder photos and graceful fallbacks mean it already looks finished. The live
counter is set to your anniversary, **June 8, 2025**, so it reads **365 araw** on June 8, 2026.

---

## ✦ The Editor — your private way to change everything

You don't have to touch any code to edit your story. There's a built-in editor:

1. **To open it:** tap the **tiny faint dot in the bottom-left corner** of the page (it's
   almost invisible — only you know it's there). Jezel will never notice it.
   *(Alternative: add **`#edit`** to the URL, e.g. `index.html#edit`.)*
2. Enter the passcode: **`admin123`**
3. For each **Moment** you can change the **photo** (upload — kept at **full original
   quality**), the **date**, the **title**, and the **story / message**. You can also edit
   the **letter** and the **signature**, and in the **Music** section choose the **song**
   (upload your MP3 + set its title/artist) — it plays when she opens the site.
4. Tap **Save & preview** to see it live on the page (saved on your device).

### Publish your edits (one tap, from any device)
The editor can commit straight to GitHub for you — **text and photos together, in one commit:**

1. Scroll to **Publish to GitHub** in the editor and fill in:
   - **GitHub username** (the repo owner)
   - **Repo name** (default `anniversary`) and **Branch** (default `main`)
   - **Access token** (see below), then tap **Save settings**.
2. Tap **Publish to GitHub**. The live site updates in about a minute. Works from your phone
   or any computer — no terminal, no GitHub Desktop needed.

Each Publish commits, in one go: `content.json` (your dates/titles/stories/letter) **plus any
new photos as full-quality `photos/moment#.jpg` files**. `content.json` stays tiny, and your
pictures keep their original quality.

> **Tip:** edit on the **live site** (`…github.io/anniversary/#edit`), not the local file —
> that way newly published photos load right back from the repo. A just-uploaded photo is a
> session preview until you **Publish** (publishing is what saves the image).

#### Make your access token (one time, ~2 min)
1. GitHub → **Settings → Developer settings → Personal access tokens → Fine-grained tokens →
   Generate new token**.
2. **Repository access:** *Only select repositories* → pick **`anniversary`**.
3. **Repository permissions → Contents: Read and write**.
4. Generate, copy the token, paste it into the editor's **Access token** field → **Save settings**.

> The token is stored **only in this browser** (never in the site's code). Keep it private;
> tap **Forget token** or revoke it on GitHub if you lose the device.

> **No token? Still works:** tap **Download (content.json)** — it also downloads any photos you
> just added. Commit `content.json` and drop those photos into `photos/` via the GitHub website
> or mobile app from anywhere.

> **Why only you can change the live site:** the editor is hidden + passcode-gated, the token
> lives only on your device, and GitHub only accepts the commit with your token. No visitor
> (including Jezel) can alter what's published.

### Change the passcode
Open the browser **console** (F12) and run:

```js
annivHash('your-new-secret')
```

Copy the number it prints into `CONFIG.adminCodeHash` near the bottom of `index.html`.

---

## Add your photos
Either **upload them in the editor** (easiest), or drop 4 images into `photos/`, named:

```
photos/moment1.jpg   photos/moment2.jpg   photos/moment3.jpg   photos/moment4.jpg
```

> Placeholder images are already there. If a photo is ever missing, the page shows a tasteful
> on-brand placeholder automatically — never a broken-image icon.

## The song (chosen in the editor)
Open the editor → **Music** section → upload your MP3 and set the **title / artist**, then
**Publish**. The song commits as `audio/song.mp3` and plays for her automatically.

**About autoplay:** browsers (especially iPhone Safari) block sound until the visitor
interacts, so the song **starts the instant she taps or scrolls** the page — which is right
away on a scroll-through site. It fades in gently, and the bottom-right button pauses/plays it.
If no song is set, the button just quietly disables itself.

---

## ⚙ Quick settings — `CONFIG` block (bottom of `index.html`)

```js
const CONFIG = {
  startDate: '2025-06-08T00:00:00', // your anniversary (drives the live counter)
  adminCodeHash: 4657503786230626   // hash of the passcode "admin123"
};
```
*(The song — file, title, artist — is chosen in the editor's **Music** section, not here.)*

---

## 🚀 Publish to GitHub Pages (≈5 minutes)

1. Free account at **github.com**.
2. New **public** repo named exactly **`anniversary`** (keep it private while you work; flip to
   Public the day you send it).
3. Upload everything — `index.html`, `content.json` (once you've exported it), `photos/`,
   `audio/`, `assets/` — to the repo root. (Easiest with **GitHub Desktop**.)
4. **Settings → Pages → Source: Deploy from branch → `main` → `/ (root)` → Save**.
5. Wait ~60 seconds for the link at the top of the Pages settings.

When the day comes: send her the link. Maybe just — *"buksan mo to."*

---

## What's in this folder

```
anniversary/
├── index.html      ← the whole site (HTML + CSS + JS inline) + built-in editor
├── content.json    ← (optional) your published edits — created via the editor's Download
├── README.md       ← this file
├── photos/         ← moment1–4.jpg (placeholders included)
├── audio/          ← song.mp3 (set it in the editor's Music section)
└── assets/         ← og-image.jpg (link preview) + the placeholder generators
```

Language is mostly **English + Tagalog with a little Bisaya** — written in your voice. Only
external loads: Google Fonts + canvas-confetti. No analytics, no ads, no third parties.

> The code took an evening. The letter took courage.
> Write it like nobody else is going to read it — because nobody else will. ❤
