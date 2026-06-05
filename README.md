# AI &amp; ML Mastery — a self-paced course site

A complete, beginner-to-pro learning site for Applied Artificial Intelligence &amp; Machine Learning,
rebuilt from the IITM Pravartak Advanced Certificate curriculum (40 weeks) as **40 crystal-clear
lessons + 5 hands-on capstone projects**. Every concept is explained simply enough for a curious
10-year-old, yet technically complete — building strictly from *"how data becomes a vector"* all the
way to *"how an LLM like ChatGPT works."*

## How to use it

It's a **static site — no build step, no install — and it works 100% offline.** Just open `index.html` in any browser.

- For the best experience (lessons load shared scripts), run a tiny local server:
  ```bash
  cd iitmcourse
  python3 -m http.server 8000
  # then visit http://localhost:8000
  ```
  Opening `index.html` directly via `file://` also works.
- **Fully offline:** math (MathJax SVG build), code highlighting (highlight.js) and the dark theme are all
  vendored locally under `assets/vendor/` — no CDN, no network needed to read, render, or run the course.
  The only things that need internet are the optional **▶️ Watch & Read** links (YouTube/articles), which
  are content you click — not page dependencies.
- Your **progress is saved automatically** in the browser (localStorage). Dark mode toggle in the top-right.

## What's inside

| Path | What it is |
|------|------------|
| `index.html` | Landing page, the learning arc, the full course map + projects (generated from the manifest) |
| `assets/css/styles.css` | The whole design system (light/dark, all teaching components) |
| `assets/js/curriculum.js` | **Single source of truth** — every part, lesson and project. Edit this to add content. |
| `assets/js/app.js` | Sidebar, search, progress tracking, prev/next pager, quizzes, theme |
| `assets/vendor/` | Locally bundled MathJax (SVG) + highlight.js — this is what makes it work offline |
| `lessons/w01.html … w40.html` | The 40 weekly lessons |
| `projects/p1.html … p5.html` | The 5 capstone projects |
| `BUILD_SPEC.md` | The authoring spec every lesson follows (use it to add or edit lessons consistently) |

## The learning arc

1. **Start Here** (W1) — the one mental model behind everything.
2. **Mathematical Foundations** (W2–4) — linear algebra, calculus, probability.
3. **Data &amp; Python** (W5–8) — SQL, Python, NumPy, EDA.
4. **The Worlds of AI** (W9–10) — NLP, vision &amp; audio.
5. **Classical ML** (W11–23) — regression, classification, SVMs, PCA, trees, ensembles, clustering.
6. **Deep Learning** (W24–31) — neural nets, backprop, CNNs, RNNs, embeddings.
7. **Transformers &amp; Generative AI** (W32–37) — attention, LLMs, RAG, GANs, diffusion.
8. **Production &amp; RL** (W38–40) — MLOps, cloud deployment, reinforcement learning.

**Projects:** Tabular ML pipeline → Text classifier → CNN image classifier → **Mini-GPT from scratch** → Deploy a RAG chatbot.

## Adding or editing a lesson

1. Add/adjust the entry in `assets/js/curriculum.js`.
2. Create `lessons/wNN.html` following `BUILD_SPEC.md` (copy `lessons/w02.html` as the template).
3. The sidebar, course map, progress bar and prev/next pager update automatically.

Visual intuition throughout is credited to [3Blue1Brown](https://www.youtube.com/c/3blue1brown),
with additional references to StatQuest, distill.pub, official docs and the original papers.
