# BUILD SPEC — how to author a lesson page

Every lesson is a **standalone HTML file** in `/lessons` (projects in `/projects`).
They share `assets/css/styles.css` and `assets/js/app.js`. **No build step.**
Use `lessons/w02.html` as the reference implementation — copy its skeleton exactly.

## Required HTML skeleton (lessons)

```html
<!DOCTYPE html>
<html lang="en" data-theme="light">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Lesson N · TITLE — AI &amp; ML Mastery</title>
<link rel="stylesheet" href="../assets/css/styles.css">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/styles/atom-one-dark.min.css">
<script>window.MathJax={tex:{inlineMath:[['\\(','\\)']],displayMath:[['\\[','\\]']]},svg:{fontCache:'global'}};</script>
<script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js" async></script>
</head>
<body data-lesson="wNN">   <!-- MUST match the id in curriculum.js, e.g. w03 -->
  <!-- topbar (copy from w02) -->
  <div class="layout">
    <aside class="sidebar" id="sidebar"></aside>
    <div class="content"><main class="page">
       <!-- lesson content here -->
       <button class="mark-done" id="markDone"><span data-check>○</span> <span data-label>Mark this lesson complete</span></button>
       <nav class="pager" id="pager"></nav>
    </main></div>
  </div>
  <script src="../assets/js/curriculum.js"></script>
  <script src="../assets/js/app.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/highlight.min.js"></script>
  <script>hljs.highlightAll();</script>
</body></html>
```

Projects use the **same** skeleton but `<body data-project="pN">`, paths still `../assets/...`,
and instead of `#pager` they end with two manual links (← back to relevant lesson, → next project or Home).
Projects do NOT need `#markDone`.

## Required teaching structure, in order

1. `<header class="lesson-head">` — crumbs, `<span class="eyebrow">EMOJI Part name</span>`, `<h1>`, `.lesson-meta` (duration / focus / week).
2. `<div class="objectives">` — "By the end you'll be able to…" 4–5 bullets.
3. `<div class="bigq">` — one motivating "Big Question".
4. `<div class="prose">` … `</div>` wrapping the main teaching body (this gives nicer serif reading type). Inside it use `<h2>` numbered sections.
5. End-of-body sections (OUTSIDE prose): `<h2>🎥 Watch &amp; Read</h2>` then `<h2>✅ Check Yourself</h2>`.

## Reusable components (classes already styled — use them, don't invent CSS)

- **ELI5:** `<div class="callout eli5"><div class="c-title"><span class="c-emoji">🧒</span> Explain Like I'm 10</div><p>…</p></div>` — REQUIRED at least once per lesson. A 10-year-old must understand it. Use everyday analogies.
- **Analogy:** `callout analogy` (emoji of your choice) — a vivid real-world comparison. REQUIRED at least once.
- **Key idea:** `callout key` — the one thing to remember.
- **Warning/pitfall:** `callout warn`.
- **Connect the Dots:** `callout connect` — REQUIRED near the end: explicitly say how this builds on a previous week and what future week it powers (use the real week numbers/topics from curriculum.js). This is what makes the course "build on each concept."
- **Figure / illustration:** `<figure class="figure"><svg viewBox="0 0 W H">…</svg><figcaption>…</figcaption></figure>` — REQUIRED at least one hand-drawn inline SVG diagram per lesson (simple, clear, labelled; use brand colors #4f46e5 indigo, #14b8a6 teal, #f59e0b amber, #f43f5e rose, #767c93 grey, #e3e6f0 gridlines). Keep SVGs simple and correct.
- **Math:** use MathJax — inline `\( … \)`, display `\[ … \]`. Use real, correct formulas.
- **Code block:** precede with
  `<div class="code-head"><span class="dot" style="background:#f43f5e"></span><span class="dot" style="background:#f59e0b"></span><span class="dot" style="background:#14b8a6"></span><span class="code-label">LABEL</span></div>`
  then `<pre><code class="language-python">…</code></pre>`. REQUIRED: at least one runnable, well-commented Python snippet (use numpy / scikit-learn / pytorch as appropriate to the topic). Code must be correct and idiomatic; comment what each block does and what it prints.
- **References:** `<ul class="refs"><li><span class="r-ic">▶️</span><div><a href="URL" target="_blank" rel="noopener">Title</a> <span class="badge-3b1b">3Blue1Brown</span><span class="r-src">why it helps</span></div></li>…</ul>` — REQUIRED 2–4 references. Include a relevant **3Blue1Brown** video where one exists (linear algebra, calculus, neural nets, backprop, attention/GPT, gradient descent all have famous 3b1b videos — use the badge only for genuine 3b1b links). Otherwise use StatQuest, distill.pub, official docs, classic papers, etc. Use real, correct URLs.
- **Quiz:** `<div class="quiz" data-answer="INDEX"> <div class="q">question</div> <button class="opt">…</button>×4 <div class="explain">why</div></div>` — `data-answer` is the 0-based index of the correct `.opt`. REQUIRED: 2–3 quizzes per lesson, with a teaching explanation.

## Tone & quality bar
- World-class teacher. Warm, vivid, plain English first, then the precise math, then code.
- Build STRICTLY on earlier weeks; name them. Foreshadow later weeks.
- Every concept must be crystal-clear to a beginner yet technically correct for a pro.
- Aim ~1200–2200 words of teaching per lesson. Don't pad; be clear.
- Escape `&` as `&amp;` in HTML text. Keep SVGs valid.
```
