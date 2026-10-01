/* ============================================================
   AI & ML Mastery — Interactive Widgets
   ============================================================ */

(function() {
  'use strict';

  // Helper: create SVG element
  function svg(tag, attrs) {
    const el = document.createElementNS('http://www.w3.org/2000/svg', tag);
    for (const [k, v] of Object.entries(attrs || {})) el.setAttribute(k, v);
    return el;
  }

  // ---------- Polynomial Overfitting Widget (W14) ----------
  window.initPolynomialWidget = function(containerId) {
    const container = document.getElementById(containerId);
    if (!container) return;

    const slider = container.querySelector('.widget-slider');
    const canvas = container.querySelector('.widget-canvas');
    const valueDisplay = container.querySelector('.widget-value');
    const ctx = canvas.getContext('2d');

    // Set canvas size
    const w = canvas.width = canvas.offsetWidth || 600;
    const h = canvas.height = canvas.offsetHeight || 300;

    // Generate synthetic data
    const n = 15;
    const xData = Array.from({length: n}, (_, i) => -1 + 2 * i / (n - 1));
    const yTrue = xData.map(x => Math.sin(Math.PI * x));
    const yData = yTrue.map(y => y + (Math.random() - 0.5) * 0.3);

    function draw(degree) {
      ctx.clearRect(0, 0, w, h);
      const padding = 40;
      const plotW = w - 2 * padding;
      const plotH = h - 2 * padding;

      // Background
      ctx.fillStyle = '#fff';
      ctx.fillRect(0, 0, w, h);

      // Axes
      ctx.strokeStyle = '#e3e6f0';
      ctx.lineWidth = 1;
      ctx.beginPath();
      ctx.moveTo(padding, padding);
      ctx.lineTo(padding, h - padding);
      ctx.lineTo(w - padding, h - padding);
      ctx.stroke();

      // Grid
      ctx.strokeStyle = '#f0f0f5';
      for (let i = 0; i <= 5; i++) {
        const x = padding + plotW * i / 5;
        ctx.beginPath(); ctx.moveTo(x, padding); ctx.lineTo(x, h - padding); ctx.stroke();
      }
      for (let i = 0; i <= 5; i++) {
        const y = padding + plotH * i / 5;
        ctx.beginPath(); ctx.moveTo(padding, y); ctx.lineTo(w - padding, y); ctx.stroke();
      }

      // Scale functions
      const sx = x => padding + (x + 1) / 2 * plotW;
      const sy = y => h - padding - (y + 1.5) / 3 * plotH;

      // True curve
      ctx.strokeStyle = '#14b8a6';
      ctx.lineWidth = 2;
      ctx.setLineDash([4, 4]);
      ctx.beginPath();
      for (let i = 0; i <= 100; i++) {
        const x = -1 + 2 * i / 100;
        const y = Math.sin(Math.PI * x);
        if (i === 0) ctx.moveTo(sx(x), sy(y)); else ctx.lineTo(sx(x), sy(y));
      }
      ctx.stroke();
      ctx.setLineDash([]);

      // Polynomial fit
      const coeffs = fitPolynomial(xData, yData, degree);
      ctx.strokeStyle = degree <= 3 ? '#4f46e5' : degree <= 8 ? '#f59e0b' : '#f43f5e';
      ctx.lineWidth = 3;
      ctx.beginPath();
      for (let i = 0; i <= 100; i++) {
        const x = -1 + 2 * i / 100;
        const y = evaluatePoly(coeffs, x);
        if (i === 0) ctx.moveTo(sx(x), sy(y)); else ctx.lineTo(sx(x), sy(y));
      }
      ctx.stroke();

      // Data points
      ctx.fillStyle = '#767c93';
      for (let i = 0; i < n; i++) {
        ctx.beginPath();
        ctx.arc(sx(xData[i]), sy(yData[i]), 4, 0, 2 * Math.PI);
        ctx.fill();
      }

      // Labels
      ctx.fillStyle = '#767c93';
      ctx.font = '12px sans-serif';
      ctx.fillText('True curve (dashed)', padding + 10, padding + 15);
      ctx.fillStyle = degree <= 3 ? '#4f46e5' : degree <= 8 ? '#f59e0b' : '#f43f5e';
      ctx.fillText('Degree-' + degree + ' fit', padding + 10, padding + 30);
    }

    function fitPolynomial(x, y, d) {
      const A = x.map(xi => Array.from({length: d + 1}, (_, p) => Math.pow(xi, p)));
      const At = transpose(A);
      const AtA = matMul(At, A);
      const Atb = matMul(At, y.map(v => [v]));
      return solveLinear(AtA, Atb);
    }

    function evaluatePoly(coeffs, x) {
      return coeffs.reduce((sum, c, p) => sum + c * Math.pow(x, p), 0);
    }

    function transpose(m) {
      return m[0].map((_, j) => m.map(row => row[j]));
    }

    function matMul(a, b) {
      return a.map(row => b[0].map((_, j) => row.reduce((s, v, i) => s + v * b[i][j], 0)));
    }

    function solveLinear(A, b) {
      const n = A.length;
      const aug = A.map((row, i) => [...row, b[i][0]]);
      for (let i = 0; i < n; i++) {
        let max = i;
        for (let j = i + 1; j < n; j++) if (Math.abs(aug[j][i]) > Math.abs(aug[max][i])) max = j;
        [aug[i], aug[max]] = [aug[max], aug[i]];
        for (let j = i + 1; j < n; j++) {
          const factor = aug[j][i] / aug[i][i];
          for (let k = i; k <= n; k++) aug[j][k] -= factor * aug[i][k];
        }
      }
      const x = new Array(n).fill(0);
      for (let i = n - 1; i >= 0; i--) {
        x[i] = aug[i][n];
        for (let j = i + 1; j < n; j++) x[i] -= aug[i][j] * x[j];
        x[i] /= aug[i][i];
      }
      return x;
    }

    slider.addEventListener('input', function() {
      const degree = parseInt(this.value);
      valueDisplay.textContent = 'Polynomial degree: ' + degree;
      draw(degree);
    });

    draw(parseInt(slider.value));
  };

  // ---------- k-NN Decision Boundary Widget (W15) ----------
  window.initKNNWidget = function(containerId) {
    const container = document.getElementById(containerId);
    if (!container) return;

    const slider = container.querySelector('.widget-slider');
    const canvas = container.querySelector('.widget-canvas');
    const valueDisplay = container.querySelector('.widget-value');
    const ctx = canvas.getContext('2d');

    const w = canvas.width = canvas.offsetWidth || 600;
    const h = canvas.height = canvas.offsetHeight || 300;

    // Generate 2-class data
    const n = 40;
    const points = [];
    for (let i = 0; i < n; i++) {
      const cls = i < n / 2 ? 0 : 1;
      const cx = cls === 0 ? 0.3 : 0.7;
      const cy = cls === 0 ? 0.4 : 0.6;
      points.push({
        x: cx + (Math.random() - 0.5) * 0.5,
        y: cy + (Math.random() - 0.5) * 0.5,
        cls: cls
      });
    }

    function draw(k) {
      ctx.clearRect(0, 0, w, h);
      const padding = 30;
      const plotW = w - 2 * padding;
      const plotH = h - 2 * padding;

      const sx = x => padding + x * plotW;
      const sy = y => h - padding - y * plotH;

      // Background grid
      ctx.fillStyle = '#fff';
      ctx.fillRect(0, 0, w, h);
      ctx.strokeStyle = '#f0f0f5';
      for (let i = 0; i <= 10; i++) {
        ctx.beginPath(); ctx.moveTo(sx(i/10), padding); ctx.lineTo(sx(i/10), h - padding); ctx.stroke();
        ctx.beginPath(); ctx.moveTo(padding, sy(i/10)); ctx.lineTo(w - padding, sy(i/10)); ctx.stroke();
      }

      // Draw decision boundary regions
      const res = 40;
      for (let i = 0; i < res; i++) {
        for (let j = 0; j < res; j++) {
          const x = i / res;
          const y = j / res;
          const pred = knnClassify(points, x, y, k);
          ctx.fillStyle = pred === 0 ? 'rgba(79, 70, 229, 0.08)' : 'rgba(20, 184, 166, 0.08)';
          ctx.fillRect(sx(i/res), sy((j+1)/res), plotW/res + 1, plotH/res + 1);
        }
      }

      // Data points
      for (const p of points) {
        ctx.fillStyle = p.cls === 0 ? BRAND.indigo : BRAND.teal;
        ctx.beginPath();
        ctx.arc(sx(p.x), sy(p.y), 5, 0, 2 * Math.PI);
        ctx.fill();
        ctx.strokeStyle = '#fff';
        ctx.lineWidth = 2;
        ctx.stroke();
      }

      // Label
      ctx.fillStyle = '#767c93';
      ctx.font = '12px sans-serif';
      ctx.fillText('k = ' + k, padding + 10, padding + 15);
      ctx.fillStyle = BRAND.indigo;
      ctx.fillText('● Class 0', padding + 10, padding + 30);
      ctx.fillStyle = BRAND.teal;
      ctx.fillText('● Class 1', padding + 10, padding + 45);
    }

    function knnClassify(points, x, y, k) {
      const dists = points.map(p => ({
        cls: p.cls,
        dist: Math.hypot(p.x - x, p.y - y)
      })).sort((a, b) => a.dist - b.dist);
      const votes = [0, 0];
      for (let i = 0; i < k && i < dists.length; i++) votes[dists[i].cls]++;
      return votes[0] >= votes[1] ? 0 : 1;
    }

    slider.addEventListener('input', function() {
      const k = parseInt(this.value);
      valueDisplay.textContent = 'k = ' + k;
      draw(k);
    });

    draw(parseInt(slider.value));
  };

  // ---------- Learning Rate Explorer (W26) ----------
  window.initLRWidget = function(containerId) {
    const container = document.getElementById(containerId);
    if (!container) return;

    const slider = container.querySelector('.widget-slider');
    const canvas = container.querySelector('.widget-canvas');
    const valueDisplay = container.querySelector('.widget-value');
    const ctx = canvas.getContext('2d');

    const w = canvas.width = canvas.offsetWidth || 600;
    const h = canvas.height = canvas.offsetHeight || 300;

    function draw(lr) {
      ctx.clearRect(0, 0, w, h);
      const padding = 40;

      ctx.fillStyle = '#fff';
      ctx.fillRect(0, 0, w, h);

      // Axes
      ctx.strokeStyle = '#e3e6f0';
      ctx.lineWidth = 1;
      ctx.beginPath();
      ctx.moveTo(padding, padding);
      ctx.lineTo(padding, h - padding);
      ctx.lineTo(w - padding, h - padding);
      ctx.stroke();

      ctx.fillStyle = '#767c93';
      ctx.font = '11px sans-serif';
      ctx.fillText('Iterations →', w - 80, h - padding + 20);
      ctx.save();
      ctx.translate(15, h / 2);
      ctx.rotate(-Math.PI / 2);
      ctx.fillText('Loss →', 0, 0);
      ctx.restore();

      // Generate loss curve based on LR
      const steps = 100;
      const trueMin = 0.2;
      ctx.strokeStyle = lr < 0.05 ? '#f59e0b' : lr > 0.3 ? '#f43f5e' : '#4f46e5';
      ctx.lineWidth = 2.5;
      ctx.beginPath();
      for (let i = 0; i <= steps; i++) {
        const x = padding + (w - 2 * padding) * i / steps;
        let y;
        if (lr < 0.05) {
          y = trueMin + 0.8 * Math.exp(-lr * i * 3) + 0.02;
        } else if (lr > 0.3) {
          y = trueMin + 0.8 * Math.exp(-0.05 * i) * (1 + 0.3 * Math.sin(i * 0.5)) + (i > 30 ? 0.05 * (i - 30) : 0);
        } else {
          y = trueMin + 0.8 * Math.exp(-lr * i * 2) + 0.01;
        }
        const py = h - padding - (y / 1.2) * (h - 2 * padding);
        if (i === 0) ctx.moveTo(x, py); else ctx.lineTo(x, py);
      }
      ctx.stroke();

      // Label
      ctx.fillStyle = '#767c93';
      ctx.font = '13px sans-serif';
      if (lr < 0.05) {
        ctx.fillText('Too small: crawls slowly', padding + 10, padding + 20);
      } else if (lr > 0.3) {
        ctx.fillText('Too large: oscillates and diverges', padding + 10, padding + 20);
      } else {
        ctx.fillText('Just right: smooth convergence', padding + 10, padding + 20);
      }
    }

    slider.addEventListener('input', function() {
      const lr = parseFloat(this.value);
      valueDisplay.textContent = 'Learning rate: ' + lr.toFixed(2);
      draw(lr);
    });

    draw(parseFloat(slider.value));
  };

  // ---------- SVM Soft Margin Widget (W18) ----------
  window.initSVMWidget = function(containerId) {
    const container = document.getElementById(containerId);
    if (!container) return;

    const slider = container.querySelector('.widget-slider');
    const canvas = container.querySelector('.widget-canvas');
    const valueDisplay = container.querySelector('.widget-value');
    const ctx = canvas.getContext('2d');

    const w = canvas.width = canvas.offsetWidth || 600;
    const h = canvas.height = canvas.offsetHeight || 300;

    // Two-class data with overlap
    const points = [];
    for (let i = 0; i < 30; i++) {
      points.push({
        x: 0.3 + Math.random() * 0.4,
        y: 0.3 + Math.random() * 0.4,
        cls: 0
      });
    }
    for (let i = 0; i < 30; i++) {
      points.push({
        x: 0.5 + Math.random() * 0.4,
        y: 0.5 + Math.random() * 0.4,
        cls: 1
      });
    }

    function draw(C) {
      ctx.clearRect(0, 0, w, h);
      const padding = 30;
      const plotW = w - 2 * padding;
      const plotH = h - 2 * padding;
      const sx = x => padding + x * plotW;
      const sy = y => h - padding - y * plotH;

      ctx.fillStyle = '#fff';
      ctx.fillRect(0, 0, w, h);
      ctx.strokeStyle = '#f0f0f5';
      for (let i = 0; i <= 10; i++) {
        ctx.beginPath(); ctx.moveTo(sx(i/10), padding); ctx.lineTo(sx(i/10), h - padding); ctx.stroke();
        ctx.beginPath(); ctx.moveTo(padding, sy(i/10)); ctx.lineTo(w - padding, sy(i/10)); ctx.stroke();
      }

      // Decision boundary (diagonal)
      const margin = 0.15 / (1 + C * 2);
      ctx.strokeStyle = '#4f46e5';
      ctx.lineWidth = 2;
      ctx.beginPath();
      ctx.moveTo(sx(0.2), sy(0.8));
      ctx.lineTo(sx(0.8), sy(0.2));
      ctx.stroke();

      // Margins
      ctx.strokeStyle = '#14b8a6';
      ctx.lineWidth = 1.5;
      ctx.setLineDash([6, 3]);
      ctx.beginPath();
      ctx.moveTo(sx(0.2 - margin), sy(0.8 - margin));
      ctx.lineTo(sx(0.8 - margin), sy(0.2 - margin));
      ctx.stroke();
      ctx.beginPath();
      ctx.moveTo(sx(0.2 + margin), sy(0.8 + margin));
      ctx.lineTo(sx(0.8 + margin), sy(0.2 + margin));
      ctx.stroke();
      ctx.setLineDash([]);

      // Margin width label
      ctx.fillStyle = '#14b8a6';
      ctx.font = '11px sans-serif';
      ctx.fillText('Margin = ' + margin.toFixed(2), sx(0.5), sy(0.55));

      // Points
      for (const p of points) {
        ctx.fillStyle = p.cls === 0 ? '#4f46e5' : '#14b8a6';
        ctx.beginPath();
        ctx.arc(sx(p.x), sy(p.y), 5, 0, 2 * Math.PI);
        ctx.fill();
        ctx.strokeStyle = '#fff';
        ctx.lineWidth = 2;
        ctx.stroke();
      }

      // Misclassified count
      const misclassified = points.filter(p => {
        const side = p.x + p.y - 1;
        return (p.cls === 0 && side > 0) || (p.cls === 1 && side < 0);
      }).length;
      ctx.fillStyle = '#f43f5e';
      ctx.font = '12px sans-serif';
      ctx.fillText('Misclassified: ' + misclassified, padding + 10, padding + 15);
    }

    slider.addEventListener('input', function() {
      const C = parseFloat(this.value);
      valueDisplay.textContent = 'C = ' + C.toFixed(2);
      draw(C);
    });

    draw(parseFloat(slider.value));
  };

  // ---------- Temperature Sampling Widget (W34) ----------
  window.initTemperatureWidget = function(containerId) {
    const container = document.getElementById(containerId);
    if (!container) return;

    const slider = container.querySelector('.widget-slider');
    const canvas = container.querySelector('.widget-canvas');
    const valueDisplay = container.querySelector('.widget-value');
    const ctx = canvas.getContext('2d');

    const w = canvas.width = canvas.offsetWidth || 600;
    const h = canvas.height = canvas.offsetHeight || 300;

    const words = ['the', 'cat', 'sat', 'on', 'mat', 'and', 'looked', 'outside'];
    const logits = [2.0, 1.5, 0.8, 0.3, 0.1, -0.5, -1.0, -1.5];

    function softmax(logits, T) {
      const exp = logits.map(z => Math.exp(z / T));
      const sum = exp.reduce((a, b) => a + b, 0);
      return exp.map(e => e / sum);
    }

    function draw(T) {
      ctx.clearRect(0, 0, w, h);
      const padding = 40;
      const barW = (w - 2 * padding) / words.length - 4;
      const maxH = h - 2 * padding;

      ctx.fillStyle = '#fff';
      ctx.fillRect(0, 0, w, h);

      const probs = softmax(logits, T);

      for (let i = 0; i < words.length; i++) {
        const barH = probs[i] * maxH;
        const x = padding + i * (barW + 4);
        const y = h - padding - barH;

        ctx.fillStyle = probs[i] === Math.max(...probs) ? '#4f46e5' : '#14b8a6';
        ctx.fillRect(x, y, barW, barH);

        ctx.fillStyle = '#767c93';
        ctx.font = '11px sans-serif';
        ctx.save();
        ctx.translate(x + barW / 2, h - padding + 15);
        ctx.rotate(-Math.PI / 6);
        ctx.fillText(words[i], 0, 0);
        ctx.restore();

        ctx.fillStyle = '#2e3047';
        ctx.font = '10px sans-serif';
        ctx.fillText((probs[i] * 100).toFixed(1) + '%', x + 2, y - 5);
      }

      // Axes
      ctx.strokeStyle = '#e3e6f0';
      ctx.lineWidth = 1;
      ctx.beginPath();
      ctx.moveTo(padding, padding);
      ctx.lineTo(padding, h - padding);
      ctx.lineTo(w - padding, h - padding);
      ctx.stroke();

      ctx.fillStyle = '#767c93';
      ctx.font = '12px sans-serif';
      if (T < 0.5) {
        ctx.fillText('Peaky: deterministic', padding + 10, padding + 15);
      } else if (T > 1.5) {
        ctx.fillText('Uniform: random', padding + 10, padding + 15);
      } else {
        ctx.fillText('Balanced: diverse', padding + 10, padding + 15);
      }
    }

    slider.addEventListener('input', function() {
      const T = parseFloat(this.value);
      valueDisplay.textContent = 'Temperature: ' + T.toFixed(1);
      draw(T);
    });

    draw(parseFloat(slider.value));
  };

  // Auto-init widgets on page load
  document.addEventListener('DOMContentLoaded', function() {
    const widgets = document.querySelectorAll('[data-widget]');
    widgets.forEach(function(widget) {
      const type = widget.dataset.widget;
      const id = widget.id;
      if (type === 'polynomial' && window.initPolynomialWidget) initPolynomialWidget(id);
      if (type === 'knn' && window.initKNNWidget) initKNNWidget(id);
      if (type === 'lr' && window.initLRWidget) initLRWidget(id);
      if (type === 'svm' && window.initSVMWidget) initSVMWidget(id);
      if (type === 'temperature' && window.initTemperatureWidget) initTemperatureWidget(id);
    });
  });

})();
