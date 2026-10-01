/* code-runner.js — in-browser Python execution for lesson code blocks.
 *
 * Adds a toolbar (Run / Copy) under every <pre><code class="language-python"> block.
 * Python runs entirely in the browser via Pyodide (WebAssembly) — no server.
 * Pyodide and its packages are lazy-loaded on the first Run click, so pages
 * stay fast until a learner actually wants to execute something.
 *
 * Blocks that import torch / tensorflow cannot run in the browser; those get a
 * "Copy + Open in Colab" affordance instead of a Run button.
 */
(function () {
  "use strict";

  var PYODIDE_VERSION = "v0.26.4";
  var PYODIDE_BASE = "https://cdn.jsdelivr.net/pyodide/" + PYODIDE_VERSION + "/full/";

  // Map an import to the Pyodide package that provides it.
  var PKG_RULES = [
    [/(^|\n)\s*(import\s+numpy|from\s+numpy\b)/, "numpy"],
    [/(^|\n)\s*(import\s+pandas|from\s+pandas\b)/, "pandas"],
    [/(^|\n)\s*(import\s+sklearn|from\s+sklearn\b)/, "scikit-learn"],
    [/(^|\n)\s*(import\s+scipy|from\s+scipy\b)/, "scipy"],
    [/(^|\n)\s*(import\s+matplotlib|from\s+matplotlib\b)/, "matplotlib"]
  ];

  // Imports we cannot satisfy in-browser: deep-learning backends and
  // server/infra libraries that need a real runtime (a GPU, a web server, a
  // tracking backend, cloud SDKs). These route to "Copy + Open in Colab".
  var UNSUPPORTED = /(^|\n)\s*(import|from)\s+(torch|tensorflow|fastapi|uvicorn|flask|django|gunicorn|mlflow|boto3|google\.cloud)\b/;

  var pyodide = null;
  var pyodideReady = null; // promise, created on first use

  function loadScript(src) {
    return new Promise(function (resolve, reject) {
      var s = document.createElement("script");
      s.src = src;
      s.onload = resolve;
      s.onerror = function () { reject(new Error("Could not load " + src)); };
      document.head.appendChild(s);
    });
  }

  function initPyodide(onStatus) {
    if (pyodideReady) return pyodideReady;
    pyodideReady = (async function () {
      onStatus("Loading the Python runtime (~10 MB, one-time download)…");
      await loadScript(PYODIDE_BASE + "pyodide.js");
      pyodide = await window.loadPyodide({ indexURL: PYODIDE_BASE });
      return pyodide;
    })();
    return pyodideReady;
  }

  function neededPackages(code) {
    var pkgs = [];
    for (var i = 0; i < PKG_RULES.length; i++) {
      if (PKG_RULES[i][0].test(code) && pkgs.indexOf(PKG_RULES[i][1]) === -1) {
        pkgs.push(PKG_RULES[i][1]);
      }
    }
    return pkgs;
  }

  function colabUrl() {
    // A blank Colab notebook; learner pastes the copied code.
    return "https://colab.research.google.com/#create=true";
  }

  // Build the toolbar + output panel for one code block.
  function enhance(codeEl) {
    var pre = codeEl.closest("pre");
    if (!pre || pre.dataset.runnerAttached) return;
    pre.dataset.runnerAttached = "1";

    var code = codeEl.textContent;
    var runnable = !UNSUPPORTED.test(code);

    var bar = document.createElement("div");
    bar.className = "pyrun-bar";

    var output = document.createElement("div");
    output.className = "pyrun-output";
    output.hidden = true;

    function setStatus(msg) {
      output.hidden = false;
      output.className = "pyrun-output pyrun-status";
      output.textContent = msg;
    }

    // Copy button (always present).
    var copyBtn = document.createElement("button");
    copyBtn.className = "pyrun-btn pyrun-copy";
    copyBtn.type = "button";
    copyBtn.innerHTML = "⧉ Copy";
    copyBtn.addEventListener("click", function () {
      navigator.clipboard.writeText(codeEl.textContent).then(function () {
        copyBtn.innerHTML = "✓ Copied";
        setTimeout(function () { copyBtn.innerHTML = "⧉ Copy"; }, 1500);
      });
    });

    if (runnable) {
      var runBtn = document.createElement("button");
      runBtn.className = "pyrun-btn pyrun-run";
      runBtn.type = "button";
      runBtn.innerHTML = "▶ Run";

      runBtn.addEventListener("click", async function () {
        runBtn.disabled = true;
        var original = runBtn.innerHTML;
        runBtn.innerHTML = "● Running…";
        var buffer = "";
        function append(text) {
          buffer += text;
          output.hidden = false;
          output.className = "pyrun-output";
          output.textContent = buffer;
        }
        try {
          await initPyodide(setStatus);
          var pkgs = neededPackages(code);
          if (pkgs.length) {
            setStatus("Loading packages: " + pkgs.join(", ") + "…");
            await pyodide.loadPackage(pkgs);
          }
          buffer = "";
          output.className = "pyrun-output";
          output.textContent = "";
          pyodide.setStdout({ batched: function (s) { append(s + "\n"); } });
          pyodide.setStderr({ batched: function (s) { append(s + "\n"); } });
          await pyodide.runPythonAsync(codeEl.textContent);
          if (buffer.trim() === "") {
            output.className = "pyrun-output pyrun-status";
            output.textContent = "✓ Ran with no printed output. Add a print(...) to see values.";
          }
        } catch (err) {
          output.hidden = false;
          output.className = "pyrun-output pyrun-error";
          output.textContent = String((err && err.message) || err);
        } finally {
          runBtn.disabled = false;
          runBtn.innerHTML = original;
        }
      });

      bar.appendChild(runBtn);
      bar.appendChild(copyBtn);
    } else {
      var note = document.createElement("span");
      note.className = "pyrun-note";
      note.textContent = "Needs a backend not available in the browser — run it in Colab:";

      var colab = document.createElement("a");
      colab.className = "pyrun-btn pyrun-colab";
      colab.href = colabUrl();
      colab.target = "_blank";
      colab.rel = "noopener";
      colab.innerHTML = "↗ Open Colab";

      bar.appendChild(note);
      bar.appendChild(copyBtn);
      bar.appendChild(colab);
    }

    pre.parentNode.insertBefore(bar, pre.nextSibling);
    pre.parentNode.insertBefore(output, bar.nextSibling);
  }

  function init() {
    var blocks = document.querySelectorAll("pre code.language-python");
    for (var i = 0; i < blocks.length; i++) enhance(blocks[i]);
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
