#!/usr/bin/env python3
"""
Comprehensive figure generator for AI & ML Mastery course visual enhancements.
Generates all Phase 1 (static) figures for lessons W02-W40 and projects P1-P5.
Run: python3 generate_all_figures.py
"""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Circle, FancyArrowPatch, Ellipse, Rectangle, Polygon
import matplotlib.patheffects as path_effects
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import seaborn as sns
import os

OUTPUT_DIR = '/Users/harshakiran/Coding/iitmcourse/assets/figures/phase1_static'
os.makedirs(OUTPUT_DIR, exist_ok=True)

BRAND = {
    'indigo': '#4f46e5', 'teal': '#14b8a6', 'amber': '#f59e0b',
    'rose': '#f43f5e', 'gray': '#767c93', 'bg': '#f7f7fb',
    'light_indigo': '#eef2ff', 'light_teal': '#e7faf7',
    'light_rose': '#ffe4e6', 'light_amber': '#fff7ed'
}

plt.rcParams.update({
    'figure.facecolor': BRAND['bg'], 'axes.facecolor': BRAND['bg'],
    'axes.edgecolor': BRAND['gray'], 'axes.labelcolor': '#2e3047',
    'text.color': '#2e3047', 'xtick.color': BRAND['gray'], 'ytick.color': BRAND['gray'],
    'font.size': 11, 'figure.dpi': 120, 'savefig.dpi': 120, 'savefig.facecolor': BRAND['bg']
})


def save(fig, name):
    fig.tight_layout()
    path = os.path.join(OUTPUT_DIR, name)
    fig.savefig(path, bbox_inches='tight', pad_inches=0.15)
    plt.close(fig)
    print(f'✓ {name}')


files = []


# ============================================================
# W02: Linear Algebra
# ============================================================

# W02-1: Matrix Transformation
fig, axes = plt.subplots(1, 2, figsize=(10, 5))
ax = axes[0]
ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)
ax.set_aspect('equal')
ax.axhline(0, color=BRAND['gray'], lw=0.5)
ax.axvline(0, color=BRAND['gray'], lw=0.5)
grid_x, grid_y = np.meshgrid(np.linspace(-2, 2, 6), np.linspace(-2, 2, 6))
ax.scatter(grid_x, grid_y, color=BRAND['gray'], s=15, alpha=0.5)
ax.annotate('', xy=(2.2, 0), xytext=(0, 0), arrowprops=dict(arrowstyle='->', color=BRAND['indigo'], lw=2))
ax.annotate('', xy=(0, 2.2), xytext=(0, 0), arrowprops=dict(arrowstyle='->', color=BRAND['indigo'], lw=2))
ax.text(2.3, 0.2, 'î', color=BRAND['indigo'], fontsize=13, fontweight='bold')
ax.text(0.2, 2.3, 'ĵ', color=BRAND['indigo'], fontsize=13, fontweight='bold')
ax.set_title('Before: Standard Basis', fontsize=12, fontweight='bold')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax = axes[1]
ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)
ax.set_aspect('equal')
ax.axhline(0, color=BRAND['gray'], lw=0.5)
ax.axvline(0, color=BRAND['gray'], lw=0.5)
A = np.array([[1.5, 0.5], [0.3, 1.2]])
pts = np.column_stack([grid_x.ravel(), grid_y.ravel()])
new_pts = pts @ A.T
ax.scatter(new_pts[:, 0], new_pts[:, 1], color=BRAND['teal'], s=15, alpha=0.5)
ax.annotate('', xy=(2.2, 0.3), xytext=(0, 0), arrowprops=dict(arrowstyle='->', color=BRAND['rose'], lw=2))
ax.annotate('', xy=(0.5, 2.2), xytext=(0, 0), arrowprops=dict(arrowstyle='->', color=BRAND['rose'], lw=2))
ax.text(2.3, 0.4, 'î′', color=BRAND['rose'], fontsize=13, fontweight='bold')
ax.text(0.6, 2.3, 'ĵ′', color=BRAND['rose'], fontsize=13, fontweight='bold')
ax.set_title('After: Matrix A', fontsize=12, fontweight='bold')
ax.set_xlabel('x')
ax.set_ylabel('y')
fig.suptitle('W02 · Matrix Transformation', fontsize=14, fontweight='bold', color=BRAND['indigo'])
files.append(save(fig, 'w02_matrix_transform.png'))

# W02-2: Dot Product Explorer
fig, ax = plt.subplots(figsize=(8, 6))
ax.set_xlim(-0.5, 5)
ax.set_ylim(-0.5, 4)
ax.set_aspect('equal')
ax.axhline(0, color=BRAND['gray'], lw=0.5)
ax.axvline(0, color=BRAND['gray'], lw=0.5)
v = np.array([4, 0])
w = np.array([3, 2])
ax.annotate('', xy=v, xytext=(0, 0), arrowprops=dict(arrowstyle='->', color=BRAND['indigo'], lw=3))
ax.annotate('', xy=w, xytext=(0, 0), arrowprops=dict(arrowstyle='->', color=BRAND['teal'], lw=3))
proj = (np.dot(v, w) / np.dot(v, v)) * v
ax.plot([w[0], proj[0]], [w[1], proj[1]], '--', color=BRAND['amber'], lw=2)
ax.plot([0, proj[0]], [0, proj[1]], color=BRAND['amber'], lw=2, alpha=0.6)
ax.fill_between([0, proj[0]], [0, proj[1]], alpha=0.15, color=BRAND['amber'])
ax.text(4.2, 0.2, 'v', fontsize=14, color=BRAND['indigo'], fontweight='bold')
ax.text(3.2, 2.2, 'w', fontsize=14, color=BRAND['teal'], fontweight='bold')
ax.text(1.5, 1.0, 'projᵥ(w)', fontsize=12, color=BRAND['amber'], fontweight='bold')
ax.text(0.5, 3.5, r'$v \cdot w = |v||w|\cos(\theta) = 12$', fontsize=12,
        bbox=dict(boxstyle='round,pad=0.5', facecolor=BRAND['light_indigo'], edgecolor=BRAND['indigo']))
ax.set_title('W02 · Dot Product = Projection Length × |v|', fontsize=13, fontweight='bold')
files.append(save(fig, 'w02_dot_product_explorer.png'))

# W02-3: SVD Decomposition
fig, axes = plt.subplots(1, 3, figsize=(12, 4))
np.random.seed(42)
cov = np.array([[1.5, 0.8], [0.8, 0.5]])
pts = np.random.multivariate_normal([0, 0], cov, 300)
axes[0].scatter(pts[:, 0], pts[:, 1], alpha=0.5, color=BRAND['indigo'], s=15)
axes[0].set_xlim(-3, 3)
axes[0].set_ylim(-3, 3)
axes[0].set_aspect('equal')
axes[0].set_title('1. Original Data', fontweight='bold')
axes[0].set_xlabel('x')
axes[0].set_ylabel('y')
U, s, Vh = np.linalg.svd(cov)
pts_rot = pts @ U
axes[1].scatter(pts_rot[:, 0], pts_rot[:, 1], alpha=0.5, color=BRAND['teal'], s=15)
axes[1].set_xlim(-3, 3)
axes[1].set_ylim(-3, 3)
axes[1].set_aspect('equal')
axes[1].set_title('2. Rotate (Uᵀ)', fontweight='bold')
axes[1].set_xlabel('x')
axes[1].set_ylabel('y')
pts_stretch = pts_rot @ np.diag(np.sqrt(s))
axes[2].scatter(pts_stretch[:, 0], pts_stretch[:, 1], alpha=0.5, color=BRAND['rose'], s=15)
axes[2].set_xlim(-3, 3)
axes[2].set_ylim(-3, 3)
axes[2].set_aspect('equal')
axes[2].set_title('3. Stretch (Σ)', fontweight='bold')
axes[2].set_xlabel('x')
axes[2].set_ylabel('y')
fig.suptitle('W02 · SVD: X = UΣVᵀ', fontsize=14, fontweight='bold', color=BRAND['indigo'])
files.append(save(fig, 'w02_svd_decomposition.png'))

# W02-4: Eigenvector Field
fig, ax = plt.subplots(figsize=(8, 8))
A = np.array([[2, 1], [1, 2]])
eigvals, eigvecs = np.linalg.eig(A)
angles = np.linspace(0, 2*np.pi, 100)
for i in range(100):
    theta = angles[i]
    v = np.array([np.cos(theta), np.sin(theta)])
    Av = A @ v
    Av = Av / (np.linalg.norm(Av) + 0.1) * 0.8
    is_eigen = False
    for j in range(2):
        ev = eigvecs[:, j]
        if abs(np.cross(v, ev)) < 0.15:
            is_eigen = True
    color = BRAND['indigo'] if is_eigen else BRAND['gray']
    ax.annotate('', xy=Av, xytext=(0, 0), arrowprops=dict(arrowstyle='->', color=color, lw=1.5, alpha=0.7))
for i in range(2):
    ev = eigvecs[:, i] * 1.5
    ax.annotate('', xy=ev, xytext=(0, 0), arrowprops=dict(arrowstyle='->', color=BRAND['rose'], lw=4))
    ax.annotate('', xy=-ev, xytext=(0, 0), arrowprops=dict(arrowstyle='->', color=BRAND['rose'], lw=4))
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_aspect('equal')
ax.axhline(0, color=BRAND['gray'], lw=0.5)
ax.axvline(0, color=BRAND['gray'], lw=0.5)
ax.set_title('W02 · Eigenvectors (red) stay on their line after transformation', fontsize=13, fontweight='bold')
ax.set_xlabel('x')
ax.set_ylabel('y')
files.append(save(fig, 'w02_eigenvector_field.png'))

# W02-5: Covariance Heatmap
fig, ax = plt.subplots(figsize=(7, 6))
features = ['Area', 'Bedrooms', 'Bathrooms', 'Age', 'Price']
np.random.seed(42)
base = np.random.randn(100, 3)
data = np.column_stack([
    base[:, 0] * 500 + 1500,
    base[:, 0] * 0.3 + base[:, 1] * 0.5 + 3,
    base[:, 0] * 0.2 + base[:, 2] * 0.6 + 2,
    np.random.randn(100) * 10 + 20,
    base[:, 0] * 300 + base[:, 1] * 50 + 200
])
corr = np.corrcoef(data.T)
sns.heatmap(corr, annot=True, fmt='.2f', cmap='RdYlBu_r', center=0,
            xticklabels=features, yticklabels=features, ax=ax,
            linewidths=0.5, vmin=-1, vmax=1, cbar_kws={'label': 'Correlation'})
ax.set_title('W02 · Covariance/Correlation Matrix', fontsize=13, fontweight='bold')
files.append(save(fig, 'w02_covariance_heatmap.png'))
