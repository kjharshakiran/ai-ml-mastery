/* ============================================================
   app.js — shared runtime for every page.
   Responsibilities:
     • Theme (light/dark) with persistence
     • Progress tracking via localStorage
     • Build the sidebar nav from CURRICULUM
     • Search/filter lessons
     • Mobile nav toggle
     • Lesson page helpers: mark-done button, prev/next pager
     • Interactive quizzes
   ============================================================ */

(function () {
  "use strict";

  const STORE_DONE = "aiml.progress.v1";
  const STORE_THEME = "aiml.theme.v1";

  /* ---------- storage helpers ---------- */
  const getDone = () => {
    try { return new Set(JSON.parse(localStorage.getItem(STORE_DONE) || "[]")); }
    catch { return new Set(); }
  };
  const saveDone = (set) => localStorage.setItem(STORE_DONE, JSON.stringify([...set]));
  const isDone = (id) => getDone().has(id);
  const toggleDone = (id) => {
    const s = getDone();
    s.has(id) ? s.delete(id) : s.add(id);
    saveDone(s);
    return s.has(id);
  };

  /* ---------- theme ---------- */
  function applyTheme(t) {
    document.documentElement.setAttribute("data-theme", t);
    localStorage.setItem(STORE_THEME, t);
    document.querySelectorAll("[data-theme-icon]").forEach(el => el.textContent = t === "dark" ? "☀️" : "🌙");
  }
  function initTheme() {
    const saved = localStorage.getItem(STORE_THEME);
    const prefers = window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches;
    applyTheme(saved || (prefers ? "dark" : "light"));
  }
  window.toggleTheme = () =>
    applyTheme(document.documentElement.getAttribute("data-theme") === "dark" ? "light" : "dark");

  /* ---------- path helper (works from / and /lessons/ and /projects/) ---------- */
  function rootPrefix() {
    // Pages in /lessons or /projects need to go up one level.
    return /\/(lessons|projects)\//.test(location.pathname) ? "../" : "";
  }

  /* ---------- build sidebar ---------- */
  function buildSidebar() {
    const host = document.getElementById("sidebar");
    if (!host || typeof CURRICULUM === "undefined") return;
    const root = rootPrefix();
    const currentId = document.body.getAttribute("data-lesson");
    const done = getDone();

    const completed = ALL_LESSONS.filter(l => done.has(l.id)).length;
    const pct = Math.round((completed / TOTAL_LESSONS) * 100);

    let html = `
      <a class="brand" href="${root}index.html">
        <span class="logo">AI</span>
        <span class="brand-text"><strong>AI &amp; ML Mastery</strong><span>40 weeks · 0 → pro</span></span>
      </a>
      <div class="search-box">
        <span class="ic">🔎</span>
        <input id="navSearch" type="search" placeholder="Search lessons & topics…" autocomplete="off">
      </div>
      <div class="progress-pill">
        <div class="label"><span>Your progress</span><span id="navPct">${pct}%</span></div>
        <div class="bar"><i id="navBar" style="width:${pct}%"></i></div>
        <div class="label" style="margin-top:6px"><span id="navCount">${completed} of ${TOTAL_LESSONS} lessons</span></div>
      </div>
    `;

    CURRICULUM.parts.forEach(part => {
      const partActive = part.lessons.some(l => l.id === currentId);
      html += `<details class="nav-part" ${partActive ? "open" : ""} data-part="${part.id}">
        <summary>${part.emoji} ${part.title}<span class="chev">›</span></summary>`;
      part.lessons.forEach(l => {
        const cls = [l.id === currentId ? "active" : "", done.has(l.id) ? "done" : ""].join(" ").trim();
        html += `<a class="nav-link ${cls}" href="${root}${l.file}" data-search="${(l.title + " " + (l.tags||[]).join(" ")).toLowerCase()}">
          <span class="num">${done.has(l.id) ? "" : l.n}</span>
          <span>${l.title}</span></a>`;
      });
      html += `</details>`;
    });

    // Projects
    html += `<details class="nav-part" data-part="projects" ${document.body.dataset.project ? "open" : ""}>
      <summary>🏆 Capstone Projects<span class="chev">›</span></summary>`;
    CURRICULUM.projects.forEach(p => {
      const active = p.id === document.body.dataset.project ? "active" : "";
      html += `<a class="nav-link ${active}" href="${root}${p.file}" data-search="${(p.title+' '+p.uses.join(' ')).toLowerCase()}">
        <span class="num">P${p.n}</span><span>${p.title}</span></a>`;
    });
    html += `</details>`;

    host.innerHTML = html;

    // search wiring
    const search = document.getElementById("navSearch");
    if (search) {
      search.addEventListener("input", () => {
        const q = search.value.trim().toLowerCase();
        document.querySelectorAll(".nav-part").forEach(part => {
          let any = false;
          part.querySelectorAll(".nav-link").forEach(a => {
            const match = !q || (a.dataset.search || "").includes(q);
            a.style.display = match ? "" : "none";
            if (match) any = true;
          });
          part.style.display = any ? "" : "none";
          if (q && any) part.setAttribute("open", "");
        });
      });
    }
  }

  /* ---------- lesson page: mark-done + pager ---------- */
  function initLessonPage() {
    const id = document.body.getAttribute("data-lesson");
    if (!id) return;
    const root = rootPrefix();

    // mark-done button
    const btn = document.getElementById("markDone");
    if (btn) {
      const sync = () => {
        const d = isDone(id);
        btn.classList.toggle("done", d);
        btn.querySelector("[data-label]").textContent = d ? "Completed — nice work!" : "Mark this lesson complete";
        btn.querySelector("[data-check]").textContent = d ? "✓" : "○";
      };
      sync();
      btn.addEventListener("click", () => { toggleDone(id); sync(); buildSidebar(); });
    }

    // prev/next pager
    const idx = ALL_LESSONS.findIndex(l => l.id === id);
    const pager = document.getElementById("pager");
    if (pager && idx !== -1) {
      const prev = ALL_LESSONS[idx - 1], next = ALL_LESSONS[idx + 1];
      pager.innerHTML = `
        ${prev ? `<a class="prev" href="${root}${prev.file}"><div class="dir">← Previous</div><div class="ttl">${prev.title}</div></a>`
               : `<a class="prev disabled"><div class="dir">← Previous</div><div class="ttl">Start of course</div></a>`}
        ${next ? `<a class="next" href="${root}${next.file}"><div class="dir">Next →</div><div class="ttl">${next.title}</div></a>`
               : `<a class="next" href="${root}projects/p1.html"><div class="dir">Next →</div><div class="ttl">🏆 Capstone Projects</div></a>`}`;
    }
  }

  /* ---------- quizzes ---------- */
  // Usage: <div class="quiz" data-answer="2"> ... .opt buttons ... <div class="explain">…</div></div>
  window.initQuizzes = function () {
    document.querySelectorAll(".quiz").forEach(quiz => {
      const answer = parseInt(quiz.getAttribute("data-answer"), 10);
      const opts = [...quiz.querySelectorAll(".opt")];
      const explain = quiz.querySelector(".explain");
      opts.forEach((opt, i) => {
        opt.addEventListener("click", () => {
          if (quiz.dataset.answered) return;
          quiz.dataset.answered = "1";
          opts[answer]?.classList.add("correct");
          if (i !== answer) opt.classList.add("wrong");
          if (explain) explain.classList.add("show");
        });
      });
    });
  };

  /* ---------- mobile nav ---------- */
  window.toggleNav = () => document.body.classList.toggle("nav-open");

  /* ---------- boot ---------- */
  initTheme();
  document.addEventListener("DOMContentLoaded", () => {
    buildSidebar();
    initLessonPage();
    if (window.initQuizzes) window.initQuizzes();
    // close mobile nav on link click
    document.getElementById("sidebar")?.addEventListener("click", e => {
      if (e.target.closest(".nav-link")) document.body.classList.remove("nav-open");
    });
  });

  // expose a few helpers for the landing page
  window.AIML = { getDone, isDone, rootPrefix };
})();
