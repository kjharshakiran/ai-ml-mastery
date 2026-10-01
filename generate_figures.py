import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.patches as mpatches
from mpl_toolkits.mplot3d import Axes3D
import seaborn as sns
import numpy as np
import os

# Brand colors
INDIGO = '#4f46e5'
TEAL = '#14b8a6'
AMBER = '#f59e0b'
ROSE = '#f43f5e'
GRAY = '#767c93'
BG = '#f7f7fb'

# Set rcParams
plt.rcParams['figure.facecolor'] = BG
plt.rcParams['axes.facecolor'] = BG
plt.rcParams['font.size'] = 11
plt.rcParams['savefig.dpi'] = 120

OUT_DIR = '/Users/harshakiran/Coding/iitmcourse/assets/figures/phase1_static'
os.makedirs(OUT_DIR, exist_ok=True)

# ============== W03 CALCULUS ==============

# 1. w03_gradient_descent.png
fig, axes = plt.subplots(1, 3, figsize=(12, 4))
x = np.linspace(-3, 3, 200)
y = x**2

# Too small LR
ax = axes[0]
ax.plot(x, y, color=INDIGO, lw=2)
xs = [2.5]
for _ in range(15):
    xs.append(xs[-1] - 0.05 * 2 * xs[-1])
ys = [xi**2 for xi in xs]
ax.plot(xs, ys, 'o-', color=ROSE, markersize=4, lw=1)
ax.set_title('LR too small → crawls', fontsize=12, fontweight='bold')
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.set_xlim(-3, 3)
ax.set_ylim(0, 9)

# Too big LR
ax = axes[1]
ax.plot(x, y, color=INDIGO, lw=2)
xs = [2.5]
for _ in range(15):
    xs.append(xs[-1] - 1.1 * 2 * xs[-1])
ys = [xi**2 for xi in xs]
ax.plot(xs, ys, 'o-', color=AMBER, markersize=4, lw=1)
ax.set_title('LR too big → oscillates', fontsize=12, fontweight='bold')
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.set_xlim(-3, 3)
ax.set_ylim(0, 9)

# Just right
ax = axes[2]
ax.plot(x, y, color=INDIGO, lw=2)
xs = [2.5]
for _ in range(15):
    xs.append(xs[-1] - 0.2 * 2 * xs[-1])
ys = [xi**2 for xi in xs]
ax.plot(xs, ys, 'o-', color=TEAL, markersize=4, lw=1)
ax.set_title('LR just right → converges', fontsize=12, fontweight='bold')
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.set_xlim(-3, 3)
ax.set_ylim(0, 9)

fig.suptitle('Gradient Descent: Learning Rate Effects', fontsize=14, fontweight='bold', y=1.02)
plt.tight_layout()
fig.savefig(os.path.join(OUT_DIR, 'w03_gradient_descent.png'), bbox_inches='tight')
plt.close(fig)
print("Saved w03_gradient_descent.png")

# 2. w03_3d_loss_landscape.png
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')
X = np.linspace(-3, 3, 50)
Y = np.linspace(-3, 3, 50)
X, Y = np.meshgrid(X, Y)
Z = X**2 + Y**2

ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.6, edgecolor='none')
# Gradient descent path
path_x = np.array([2.5, 2.0, 1.5, 1.0, 0.6, 0.3, 0.1, 0.0])
path_y = np.array([2.0, 1.6, 1.2, 0.8, 0.5, 0.2, 0.05, 0.0])
path_z = path_x**2 + path_y**2
ax.plot(path_x, path_y, path_z, 'o-', color=ROSE, markersize=5, lw=2, label='Gradient path')
ax.scatter([0], [0], [0], color=ROSE, s=100, depthshade=False)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_title('3D Loss Landscape: z = x² + y²', fontsize=12, fontweight='bold')
ax.view_init(elev=30, azim=45)
fig.savefig(os.path.join(OUT_DIR, 'w03_3d_loss_landscape.png'), bbox_inches='tight')
plt.close(fig)
print("Saved w03_3d_loss_landscape.png")

# 3. w03_chain_rule.png
fig, ax = plt.subplots(figsize=(8, 6))
ax.set_xlim(0, 10)
ax.set_ylim(0, 6)
ax.axis('off')

# Boxes
box_x = patches.FancyBboxPatch((0.5, 2.5), 1.5, 1, boxstyle="round,pad=0.1", facecolor=TEAL, edgecolor='black', lw=2)
box_g = patches.FancyBboxPatch((3.5, 2.5), 1.5, 1, boxstyle="round,pad=0.1", facecolor=AMBER, edgecolor='black', lw=2)
box_f = patches.FancyBboxPatch((6.5, 2.5), 1.5, 1, boxstyle="round,pad=0.1", facecolor=INDIGO, edgecolor='black', lw=2)
ax.add_patch(box_x)
ax.add_patch(box_g)
ax.add_patch(box_f)

ax.text(1.25, 3.0, 'x', ha='center', va='center', fontsize=14, fontweight='bold', color='white')
ax.text(4.25, 3.0, 'g(x)', ha='center', va='center', fontsize=14, fontweight='bold', color='white')
ax.text(7.25, 3.0, 'f(g(x))', ha='center', va='center', fontsize=14, fontweight='bold', color='white')

# Arrows
ax.annotate('', xy=(3.5, 3.0), xytext=(2.0, 3.0), arrowprops=dict(arrowstyle='->', color=ROSE, lw=2))
ax.annotate('', xy=(6.5, 3.0), xytext=(5.0, 3.0), arrowprops=dict(arrowstyle='->', color=ROSE, lw=2))
ax.annotate('', xy=(8.5, 3.0), xytext=(8.0, 3.0), arrowprops=dict(arrowstyle='->', color=ROSE, lw=2))
ax.text(8.8, 3.0, 'y', fontsize=14, fontweight='bold', color=GRAY)

# Ripple labels
ax.annotate('∂g/∂x', xy=(2.75, 3.3), fontsize=11, color=ROSE, fontweight='bold')
ax.annotate('∂f/∂g', xy=(5.75, 3.3), fontsize=11, color=ROSE, fontweight='bold')

# Chain rule equation
ax.text(5, 1.5, r'$\frac{dy}{dx} = \frac{df}{dg} \cdot \frac{dg}{dx}$', fontsize=18, ha='center', color=INDIGO, fontweight='bold')
ax.text(5, 0.8, 'Ripple effect: change in x propagates through g to f', fontsize=11, ha='center', color=GRAY, style='italic')

ax.set_title('Chain Rule: f(g(x))', fontsize=14, fontweight='bold')
fig.savefig(os.path.join(OUT_DIR, 'w03_chain_rule.png'), bbox_inches='tight')
plt.close(fig)
print("Saved w03_chain_rule.png")

# 4. w03_lagrange_multiplier.png
fig, ax = plt.subplots(figsize=(8, 6))
x = np.linspace(-3, 3, 100)
y = np.linspace(-3, 3, 100)
X, Y = np.meshgrid(x, y)
Z = X**2 + Y**2  # f(x,y) = x^2 + y^2

contours = ax.contour(X, Y, Z, levels=8, colors=INDIGO, linewidths=1.5, alpha=0.7)
ax.clabel(contours, inline=True, fontsize=9)

# Constraint g(x,y) = x + y = 1
xc = np.linspace(-3, 4, 100)
yc = 1 - xc
ax.plot(xc, yc, color=ROSE, lw=2.5, label=r'Constraint: $g(x,y)=c$')

# Tangent point (approximate: on x+y=1, min of x^2+y^2 is at (0.5, 0.5))
tx, ty = 0.5, 0.5
ax.plot(tx, ty, 'o', color=AMBER, markersize=10, zorder=5)

# Gradient vectors
ax.annotate('', xy=(tx+1.0, ty+1.0), xytext=(tx, ty), arrowprops=dict(arrowstyle='->', color=TEAL, lw=2))
ax.text(tx+0.6, ty+0.8, r'$\nabla f$', fontsize=12, color=TEAL, fontweight='bold')
ax.annotate('', xy=(tx+0.7, ty-0.7), xytext=(tx, ty), arrowprops=dict(arrowstyle='->', color=ROSE, lw=2))
ax.text(tx+0.5, ty-0.6, r'$\nabla g$', fontsize=12, color=ROSE, fontweight='bold')

ax.annotate(r'$\nabla f = \lambda \nabla g$', xy=(2.2, 2.2), fontsize=12, color=AMBER, fontweight='bold',
            bbox=dict(boxstyle='round', facecolor='white', edgecolor=AMBER, alpha=0.9))

ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)
ax.set_aspect('equal')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Lagrange Multipliers', fontsize=14, fontweight='bold')
ax.legend(loc='upper left')
fig.savefig(os.path.join(OUT_DIR, 'w03_lagrange_multiplier.png'), bbox_inches='tight')
plt.close(fig)
print("Saved w03_lagrange_multiplier.png")

# 5. w03_jacobian_grid.png
fig, axes = plt.subplots(1, 2, figsize=(10, 5))

# Original grid
ax = axes[0]
grid_x, grid_y = np.meshgrid(np.arange(-2, 3), np.arange(-2, 3))
ax.scatter(grid_x, grid_y, color=INDIGO, s=50, zorder=3)
for i in range(grid_x.shape[0]):
    ax.plot(grid_x[i, :], grid_y[i, :], color=GRAY, lw=0.8, alpha=0.5)
    ax.plot(grid_x[:, i], grid_y[:, i], color=GRAY, lw=0.8, alpha=0.5)
ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)
ax.set_aspect('equal')
ax.set_title('Original Grid', fontsize=12, fontweight='bold')
ax.set_xlabel('x')
ax.set_ylabel('y')

# Transformed grid by matrix [[2, 1], [0.5, 1.5]]
ax = axes[1]
A = np.array([[2, 1], [0.5, 1.5]])
grid_flat = np.vstack([grid_x.ravel(), grid_y.ravel()])
grid_trans = A @ grid_flat
gt_x = grid_trans[0, :].reshape(grid_x.shape)
gt_y = grid_trans[1, :].reshape(grid_y.shape)
ax.scatter(gt_x, gt_y, color=ROSE, s=50, zorder=3)
for i in range(gt_x.shape[0]):
    ax.plot(gt_x[i, :], gt_y[i, :], color=GRAY, lw=0.8, alpha=0.5)
    ax.plot(gt_x[:, i], gt_y[:, i], color=GRAY, lw=0.8, alpha=0.5)
ax.set_xlim(-6, 6)
ax.set_ylim(-6, 6)
ax.set_aspect('equal')
ax.set_title("Transformed by A = [[2, 1], [0.5, 1.5]]", fontsize=12, fontweight='bold')
ax.set_xlabel("x'")
ax.set_ylabel("y'")

# Add matrix annotation
ax.annotate(r'Jacobian: $J = \frac{\partial f}{\partial x}$', xy=(0.5, 0.05), xycoords='figure fraction',
            fontsize=12, ha='center', color=INDIGO, fontweight='bold')

fig.suptitle('Jacobian: Local Linearization', fontsize=14, fontweight='bold', y=1.02)
plt.tight_layout()
fig.savefig(os.path.join(OUT_DIR, 'w03_jacobian_grid.png'), bbox_inches='tight')
plt.close(fig)
print("Saved w03_jacobian_grid.png")

# ============== W04 PROBABILITY ==============

# 1. w04_clt.png
fig, axes = plt.subplots(2, 2, figsize=(10, 8))

n_samples = 10000

# Uniform
ax = axes[0, 0]
data = np.random.uniform(0, 1, n_samples)
ax.hist(data, bins=30, color=INDIGO, edgecolor='white', alpha=0.8)
ax.set_title('Uniform Distribution', fontsize=12, fontweight='bold')
ax.set_xlabel('Value')
ax.set_ylabel('Frequency')

# Sum of 2
ax = axes[0, 1]
data = np.random.uniform(0, 1, (n_samples, 2)).sum(axis=1)
ax.hist(data, bins=30, color=TEAL, edgecolor='white', alpha=0.8)
ax.set_title('Sum of 2 Uniforms', fontsize=12, fontweight='bold')
ax.set_xlabel('Value')
ax.set_ylabel('Frequency')

# Sum of 5
ax = axes[1, 0]
data = np.random.uniform(0, 1, (n_samples, 5)).sum(axis=1)
ax.hist(data, bins=30, color=AMBER, edgecolor='white', alpha=0.8)
ax.set_title('Sum of 5 Uniforms', fontsize=12, fontweight='bold')
ax.set_xlabel('Value')
ax.set_ylabel('Frequency')

# Sum of 30
ax = axes[1, 1]
data = np.random.uniform(0, 1, (n_samples, 30)).sum(axis=1)
ax.hist(data, bins=30, color=ROSE, edgecolor='white', alpha=0.8, density=True)
mu, sigma = data.mean(), data.std()
xx = np.linspace(data.min(), data.max(), 200)
ax.plot(xx, (1/(sigma*np.sqrt(2*np.pi))) * np.exp(-0.5*((xx-mu)/sigma)**2), color=INDIGO, lw=2.5, label='Gaussian fit')
ax.set_title('Sum of 30 Uniforms → Gaussian', fontsize=12, fontweight='bold')
ax.set_xlabel('Value')
ax.set_ylabel('Density')
ax.legend()

fig.suptitle('Central Limit Theorem', fontsize=14, fontweight='bold', y=1.02)
plt.tight_layout()
fig.savefig(os.path.join(OUT_DIR, 'w04_clt.png'), bbox_inches='tight')
plt.close(fig)
print("Saved w04_clt.png")

# 2. w04_pdf_area.png
fig, ax = plt.subplots(figsize=(8, 6))
xx = np.linspace(-4, 4, 500)
yy = (1/np.sqrt(2*np.pi)) * np.exp(-0.5 * xx**2)
ax.plot(xx, yy, color=INDIGO, lw=2.5)

# Shade -1 to 1
xx_fill = np.linspace(-1, 1, 200)
yy_fill = (1/np.sqrt(2*np.pi)) * np.exp(-0.5 * xx_fill**2)
ax.fill_between(xx_fill, yy_fill, alpha=0.4, color=TEAL)

ax.axvline(-1, color=GRAY, linestyle='--', lw=1)
ax.axvline(1, color=GRAY, linestyle='--', lw=1)
ax.annotate('68.3%', xy=(0, 0.25), fontsize=16, ha='center', color=TEAL, fontweight='bold')
ax.annotate(r'$\mu - \sigma$', xy=(-1, 0.05), fontsize=11, ha='center', color=GRAY)
ax.annotate(r'$\mu + \sigma$', xy=(1, 0.05), fontsize=11, ha='center', color=GRAY)

ax.set_xlim(-4, 4)
ax.set_ylim(0, 0.45)
ax.set_xlabel('x')
ax.set_ylabel('Probability Density')
ax.set_title('Gaussian PDF: Area = Probability', fontsize=14, fontweight='bold')
fig.savefig(os.path.join(OUT_DIR, 'w04_pdf_area.png'), bbox_inches='tight')
plt.close(fig)
print("Saved w04_pdf_area.png")

# 3. w04_variance_target.png
fig, ax = plt.subplots(figsize=(8, 6))

# Generate concentric scatter
theta = np.random.uniform(0, 2*np.pi, 500)
r1 = np.random.normal(1, 0.1, 150)
r2 = np.random.normal(2, 0.15, 150)
r3 = np.random.normal(3, 0.2, 150)
r_combined = np.concatenate([r1, r2, r3])
theta_combined = np.random.uniform(0, 2*np.pi, len(r_combined))

x = r_combined * np.cos(theta_combined)
y = r_combined * np.sin(theta_combined)

# Color by ring
colors = [TEAL if r <= 1.5 else (AMBER if r <= 2.5 else ROSE) for r in r_combined]
ax.scatter(x, y, c=colors, s=30, alpha=0.7, edgecolors='none')

# Concentric circles
circle1 = plt.Circle((0, 0), 1, color=TEAL, fill=False, lw=2, linestyle='--')
circle2 = plt.Circle((0, 0), 2, color=AMBER, fill=False, lw=2, linestyle='--')
circle3 = plt.Circle((0, 0), 3, color=ROSE, fill=False, lw=2, linestyle='--')
ax.add_patch(circle1)
ax.add_patch(circle2)
ax.add_patch(circle3)

ax.plot(0, 0, 'o', color=INDIGO, markersize=8, label='Target')
ax.annotate(r'$1\sigma$', xy=(0.7, 0.7), fontsize=12, color=TEAL, fontweight='bold')
ax.annotate(r'$2\sigma$', xy=(1.4, 1.4), fontsize=12, color=AMBER, fontweight='bold')
ax.annotate(r'$3\sigma$', xy=(2.1, 2.1), fontsize=12, color=ROSE, fontweight='bold')

ax.set_xlim(-4, 4)
ax.set_ylim(-4, 4)
ax.set_aspect('equal')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Variance as Target Spread', fontsize=14, fontweight='bold')
ax.legend(loc='upper right')
fig.savefig(os.path.join(OUT_DIR, 'w04_variance_target.png'), bbox_inches='tight')
plt.close(fig)
print("Saved w04_variance_target.png")

# 4. w04_joint_distribution.png
fig, axes = plt.subplots(1, 2, figsize=(10, 5))

# Correlated (ellipse)
ax = axes[0]
mean = [0, 0]
cov = [[1, 0.8], [0.8, 1]]
x, y = np.random.multivariate_normal(mean, cov, 2000).T
ax.scatter(x, y, c=INDIGO, s=15, alpha=0.5, edgecolors='none')
ax.set_xlim(-4, 4)
ax.set_ylim(-4, 4)
ax.set_aspect('equal')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Correlated: ρ = 0.8', fontsize=12, fontweight='bold')
ax.axhline(0, color=GRAY, lw=0.5)
ax.axvline(0, color=GRAY, lw=0.5)

# Uncorrelated (circle)
ax = axes[1]
cov = [[1, 0], [0, 1]]
x, y = np.random.multivariate_normal(mean, cov, 2000).T
ax.scatter(x, y, c=TEAL, s=15, alpha=0.5, edgecolors='none')
ax.set_xlim(-4, 4)
ax.set_ylim(-4, 4)
ax.set_aspect('equal')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Uncorrelated: ρ = 0', fontsize=12, fontweight='bold')
ax.axhline(0, color=GRAY, lw=0.5)
ax.axvline(0, color=GRAY, lw=0.5)

fig.suptitle('Joint Distributions', fontsize=14, fontweight='bold', y=1.02)
plt.tight_layout()
fig.savefig(os.path.join(OUT_DIR, 'w04_joint_distribution.png'), bbox_inches='tight')
plt.close(fig)
print("Saved w04_joint_distribution.png")

# 5. w04_bayes_venn.png
fig, ax = plt.subplots(figsize=(8, 6))
ax.set_xlim(0, 10)
ax.set_ylim(0, 8)
ax.axis('off')

# Circle A
circle_a = plt.Circle((3.5, 4.5), 2, color=INDIGO, alpha=0.3, lw=2, ec=INDIGO)
ax.add_patch(circle_a)
# Circle B
circle_b = plt.Circle((5.5, 4.5), 2, color=TEAL, alpha=0.3, lw=2, ec=TEAL)
ax.add_patch(circle_b)

ax.text(1.5, 6.5, 'A', fontsize=16, fontweight='bold', color=INDIGO)
ax.text(7.5, 6.5, 'B', fontsize=16, fontweight='bold', color=TEAL)
ax.text(2.0, 4.5, r'$P(A)$', fontsize=12, color=INDIGO, fontweight='bold')
ax.text(6.5, 4.5, r'$P(B)$', fontsize=12, color=TEAL, fontweight='bold')
ax.text(4.5, 4.5, r'$P(A \cap B)$', fontsize=11, color=ROSE, fontweight='bold', ha='center')

ax.text(5, 2.0, r'$P(A|B) = \frac{P(A \cap B)}{P(B)}$', fontsize=14, ha='center', color=ROSE, fontweight='bold')
ax.text(5, 1.2, 'Bayes Theorem updates belief given evidence', fontsize=11, ha='center', color=GRAY, style='italic')

ax.set_title('Bayes Theorem: Venn Diagram', fontsize=14, fontweight='bold')
fig.savefig(os.path.join(OUT_DIR, 'w04_bayes_venn.png'), bbox_inches='tight')
plt.close(fig)
print("Saved w04_bayes_venn.png")

# ============== W05 SQL ==============

# 1. w05_joins.png
fig, axes = plt.subplots(1, 3, figsize=(12, 5))

def draw_table(ax, x0, y0, rows, cols, data, color, title, highlight=None):
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')
    ax.text(5, 9.5, title, fontsize=12, fontweight='bold', ha='center', color=color)
    w = 8 / cols
    h = 7 / rows
    for i in range(rows):
        for j in range(cols):
            rect = patches.Rectangle((x0 + j*w, y0 - i*h), w, h, fill=False, edgecolor=color, lw=1.5)
            ax.add_patch(rect)
            val = data[i][j] if i < len(data) and j < len(data[0]) else ''
            if highlight and (i, j) in highlight:
                inner = patches.Rectangle((x0 + j*w, y0 - i*h), w, h, facecolor=TEAL, alpha=0.3)
                ax.add_patch(inner)
            ax.text(x0 + j*w + w/2, y0 - i*h + h/2, str(val), ha='center', va='center', fontsize=9)

# INNER JOIN
ax = axes[0]
draw_table(ax, 0.5, 8, 4, 2, [['ID','Name'],[1,'Alice'],[2,'Bob'],[3,'Carol']], INDIGO, 'Table A', highlight={(1,0),(1,1),(2,0),(2,1)})
draw_table(ax, 0.5, 2, 4, 2, [['ID','Score'],[1,85],[2,92],[4,78]], TEAL, 'Table B', highlight={(1,0),(1,1),(2,0),(2,1)})
ax.text(5, 5.5, 'INNER JOIN', fontsize=13, ha='center', color=ROSE, fontweight='bold')
ax.text(5, 4.8, 'Only matching rows', fontsize=10, ha='center', color=GRAY)

# LEFT JOIN
ax = axes[1]
draw_table(ax, 0.5, 8, 4, 2, [['ID','Name'],[1,'Alice'],[2,'Bob'],[3,'Carol']], INDIGO, 'Table A', highlight={(1,0),(1,1),(2,0),(2,1),(3,0),(3,1)})
draw_table(ax, 0.5, 2, 4, 2, [['ID','Score'],[1,85],[2,92],[4,78]], TEAL, 'Table B', highlight={(1,0),(1,1),(2,0),(2,1)})
ax.text(5, 5.5, 'LEFT JOIN', fontsize=13, ha='center', color=ROSE, fontweight='bold')
ax.text(5, 4.8, 'All left + matched right', fontsize=10, ha='center', color=GRAY)
ax.text(5, 3.2, 'NULL →', fontsize=10, ha='center', color=AMBER)

# FULL OUTER
ax = axes[2]
draw_table(ax, 0.5, 8, 4, 2, [['ID','Name'],[1,'Alice'],[2,'Bob'],[3,'Carol']], INDIGO, 'Table A', highlight={(1,0),(1,1),(2,0),(2,1),(3,0),(3,1)})
draw_table(ax, 0.5, 2, 4, 2, [['ID','Score'],[1,85],[2,92],[4,78]], TEAL, 'Table B', highlight={(1,0),(1,1),(2,0),(2,1),(3,0),(3,1)})
ax.text(5, 5.5, 'FULL OUTER', fontsize=13, ha='center', color=ROSE, fontweight='bold')
ax.text(5, 4.8, 'All rows from both', fontsize=10, ha='center', color=GRAY)
ax.text(5, 3.2, 'NULL ←', fontsize=10, ha='center', color=AMBER)
ax.text(5, 9.2, 'NULL →', fontsize=10, ha='center', color=AMBER)

fig.suptitle('SQL Joins', fontsize=14, fontweight='bold', y=1.02)
plt.tight_layout()
fig.savefig(os.path.join(OUT_DIR, 'w05_joins.png'), bbox_inches='tight')
plt.close(fig)
print("Saved w05_joins.png")

# 2. w05_query_flow.png
fig, ax = plt.subplots(figsize=(8, 6))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis('off')

boxes = [
    ('SELECT', 5, 8.5, INDIGO),
    ('FROM', 5, 6.8, TEAL),
    ('WHERE', 5, 5.1, AMBER),
    ('GROUP BY', 5, 3.4, ROSE),
    ('ORDER BY', 5, 1.7, GRAY),
]

for name, x, y, color in boxes:
    rect = patches.FancyBboxPatch((x-1.5, y-0.5), 3, 1, boxstyle="round,pad=0.1", facecolor=color, edgecolor='black', lw=2)
    ax.add_patch(rect)
    ax.text(x, y, name, ha='center', va='center', fontsize=12, fontweight='bold', color='white')

for i in range(len(boxes)-1):
    ax.annotate('', xy=(boxes[i+1][1], boxes[i+1][2]+0.5), xytext=(boxes[i][1], boxes[i][2]-0.5),
                arrowprops=dict(arrowstyle='->', color=INDIGO, lw=2.5))

ax.text(5, 0.3, 'Logical Execution Order', fontsize=12, ha='center', color=GRAY, style='italic')
ax.set_title('SQL Query Flow', fontsize=14, fontweight='bold')
fig.savefig(os.path.join(OUT_DIR, 'w05_query_flow.png'), bbox_inches='tight')
plt.close(fig)
print("Saved w05_query_flow.png")

# 3. w05_acid.png
fig, ax = plt.subplots(figsize=(8, 6))
ax.set_xlim(0, 10)
ax.set_ylim(0, 8)
ax.axis('off')

steps = [
    ('BEGIN', 1.5, 5, INDIGO, True),
    ('UPDATE', 3.5, 5, TEAL, True),
    ('UPDATE', 5.5, 5, TEAL, True),
    ('COMMIT', 7.5, 5, ROSE, True),
]

for name, x, y, color, good in steps:
    rect = patches.FancyBboxPatch((x-0.8, y-0.4), 1.6, 0.8, boxstyle="round,pad=0.05", facecolor=color, edgecolor='black', lw=2)
    ax.add_patch(rect)
    ax.text(x, y, name, ha='center', va='center', fontsize=10, fontweight='bold', color='white')

for i in range(len(steps)-1):
    ax.annotate('', xy=(steps[i+1][1]-0.8, steps[i+1][2]), xytext=(steps[i][1]+0.8, steps[i][2]),
                arrowprops=dict(arrowstyle='->', color=INDIGO, lw=2))

# Failure path
ax.plot([3.5, 3.5, 2.5], [4.6, 3.0, 3.0], color=AMBER, lw=2, linestyle='--')
ax.annotate('', xy=(2.5, 3.0), xytext=(3.5, 3.0),
            arrowprops=dict(arrowstyle='->', color=AMBER, lw=2))
ax.text(4.5, 3.0, 'Failure → ROLLBACK', fontsize=11, color=AMBER, fontweight='bold')

ax.text(5, 1.0, 'ACID: Atomicity, Consistency, Isolation, Durability', fontsize=12, ha='center', color=GRAY, style='italic')
ax.set_title('ACID Transaction Timeline', fontsize=14, fontweight='bold')
fig.savefig(os.path.join(OUT_DIR, 'w05_acid.png'), bbox_inches='tight')
plt.close(fig)
print("Saved w05_acid.png")

# ============== W06 PYTHON ==============

# 1. w06_memory_model.png
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(0, 10)
ax.set_ylim(0, 8)
ax.axis('off')

# Stack
stack = patches.FancyBboxPatch((0.5, 1), 3, 6, boxstyle="round,pad=0.1", facecolor='#e0e7ff', edgecolor=INDIGO, lw=2)
ax.add_patch(stack)
ax.text(2, 7.5, 'Stack', fontsize=14, fontweight='bold', color=INDIGO, ha='center')
ax.text(2, 6.5, 'a →', fontsize=12, color=INDIGO, ha='right')
ax.text(2, 5.5, 'b →', fontsize=12, color=INDIGO, ha='right')
ax.text(2, 4.5, 'c →', fontsize=12, color=INDIGO, ha='right')
ax.text(2, 3.5, 'd →', fontsize=12, color=INDIGO, ha='right')
ax.text(2, 2.5, 'e →', fontsize=12, color=INDIGO, ha='right')

# Heap
heap = patches.FancyBboxPatch((5.5, 1), 4, 6, boxstyle="round,pad=0.1", facecolor='#f0fdf4', edgecolor=TEAL, lw=2)
ax.add_patch(heap)
ax.text(7.5, 7.5, 'Heap', fontsize=14, fontweight='bold', color=TEAL, ha='center')

# Objects
objs = [
    (7.5, 6.5, 'int: 42', TEAL, False),
    (7.5, 5.5, 'str: "hi"', TEAL, False),
    (7.5, 4.5, 'tuple: (1,2)', TEAL, False),
    (7.5, 3.5, 'list: [1,2,3]', ROSE, True),
    (7.5, 2.5, 'dict: {k:v}', ROSE, True),
]
for x, y, text, color, mutable in objs:
    rect = patches.FancyBboxPatch((x-1.2, y-0.3), 2.4, 0.6, boxstyle="round,pad=0.05", facecolor=color, edgecolor='black', lw=1.5, alpha=0.7)
    ax.add_patch(rect)
    ax.text(x, y, text, ha='center', va='center', fontsize=10, fontweight='bold', color='white')

# Arrows
ax.annotate('', xy=(6.3, 6.5), xytext=(2.2, 6.5), arrowprops=dict(arrowstyle='->', color=INDIGO, lw=1.5))
ax.annotate('', xy=(6.3, 5.5), xytext=(2.2, 5.5), arrowprops=dict(arrowstyle='->', color=INDIGO, lw=1.5))
ax.annotate('', xy=(6.3, 4.5), xytext=(2.2, 4.5), arrowprops=dict(arrowstyle='->', color=INDIGO, lw=1.5))
ax.annotate('', xy=(6.3, 3.5), xytext=(2.2, 3.5), arrowprops=dict(arrowstyle='->', color=INDIGO, lw=1.5))
ax.annotate('', xy=(6.3, 2.5), xytext=(2.2, 2.5), arrowprops=dict(arrowstyle='->', color=INDIGO, lw=1.5))

ax.text(5, 0.3, 'Immutable: copied on assignment  |  Mutable: shared reference', fontsize=11, ha='center', color=GRAY)
ax.set_title('Python Memory Model: Stack vs Heap', fontsize=14, fontweight='bold')
fig.savefig(os.path.join(OUT_DIR, 'w06_memory_model.png'), bbox_inches='tight')
plt.close(fig)
print("Saved w06_memory_model.png")

# 2. w06_list_dict.png
fig, axes = plt.subplots(1, 2, figsize=(10, 5))

# Array-backed list
ax = axes[0]
ax.set_xlim(0, 10)
ax.set_ylim(0, 6)
ax.axis('off')
ax.text(5, 5.5, 'List: Dynamic Array', fontsize=12, fontweight='bold', color=INDIGO, ha='center')
for i in range(6):
    rect = patches.Rectangle((1 + i*1.3, 3), 1.2, 1.2, facecolor=TEAL, edgecolor='black', lw=1.5)
    ax.add_patch(rect)
    ax.text(1.6 + i*1.3, 3.6, str(i), ha='center', va='center', fontsize=10, fontweight='bold', color='white')
    ax.text(1.6 + i*1.3, 2.5, f'idx {i}', ha='center', va='center', fontsize=8, color=GRAY)
ax.annotate('O(1) access by index', xy=(5, 1.5), fontsize=10, ha='center', color=GRAY, style='italic')

# Hash table
ax = axes[1]
ax.set_xlim(0, 10)
ax.set_ylim(0, 6)
ax.axis('off')
ax.text(5, 5.5, 'Dict: Hash Table', fontsize=12, fontweight='bold', color=INDIGO, ha='center')

buckets = [0, 3, 1, 4, 2, 5]
for i in range(6):
    bx = 1 + i*1.3
    rect = patches.Rectangle((bx, 3), 1.2, 1.2, facecolor=AMBER, edgecolor='black', lw=1.5)
    ax.add_patch(rect)
    ax.text(bx+0.6, 3.6, str(buckets[i]), ha='center', va='center', fontsize=10, fontweight='bold', color='white')
    ax.text(bx+0.6, 2.5, f'bkt {i}', ha='center', va='center', fontsize=8, color=GRAY)

# Collision chains
collision_x = 1 + 3*1.3 + 0.6
ax.plot([collision_x, collision_x+1.5], [3, 3], color=ROSE, lw=2)
ax.plot([collision_x+1.5, collision_x+1.5], [3, 2.2], color=ROSE, lw=2)
rect2 = patches.Rectangle((collision_x+0.9, 1.5), 1.2, 0.7, facecolor=ROSE, edgecolor='black', lw=1.5)
ax.add_patch(rect2)
ax.text(collision_x+1.5, 1.85, 'chain', ha='center', va='center', fontsize=9, color='white', fontweight='bold')
ax.annotate('collision', xy=(collision_x+1.2, 2.8), fontsize=9, color=ROSE, fontweight='bold')

ax.annotate('O(1) average lookup', xy=(5, 1.5), fontsize=10, ha='center', color=GRAY, style='italic')

fig.suptitle('Python Data Structures', fontsize=14, fontweight='bold', y=1.02)
plt.tight_layout()
fig.savefig(os.path.join(OUT_DIR, 'w06_list_dict.png'), bbox_inches='tight')
plt.close(fig)
print("Saved w06_list_dict.png")

# ============== W07 PYTHON ADVANCED ==============

# 1. w07_broadcasting.png
fig, ax = plt.subplots(figsize=(8, 6))
ax.set_xlim(0, 10)
ax.set_ylim(0, 8)
ax.axis('off')

# Array A (3,1)
ax.text(1.5, 7, 'A (3,1)', fontsize=12, fontweight='bold', color=INDIGO)
for i in range(3):
    for j in range(1):
        rect = patches.Rectangle((1 + j, 6.2 - i*0.6), 0.6, 0.5, facecolor=INDIGO, edgecolor='black', lw=1.5)
        ax.add_patch(rect)
        ax.text(1.3, 6.45 - i*0.6, str(i+1), ha='center', va='center', fontsize=9, color='white', fontweight='bold')

# Array B (1,4)
ax.text(6.5, 7, 'B (1,4)', fontsize=12, fontweight='bold', color=TEAL)
for i in range(1):
    for j in range(4):
        rect = patches.Rectangle((5.5 + j*0.6, 6.2 - i*0.6), 0.6, 0.5, facecolor=TEAL, edgecolor='black', lw=1.5)
        ax.add_patch(rect)
        ax.text(5.8 + j*0.6, 6.45, str(j+1), ha='center', va='center', fontsize=9, color='white', fontweight='bold')

# Arrows showing stretch
ax.annotate('', xy=(3, 5.0), xytext=(2, 6.0), arrowprops=dict(arrowstyle='->', color=AMBER, lw=2))
ax.text(3.5, 5.5, 'Stretch', fontsize=10, color=AMBER, fontweight='bold')
ax.annotate('', xy=(5.5, 5.0), xytext=(6.5, 6.0), arrowprops=dict(arrowstyle='->', color=AMBER, lw=2))
ax.text(5.5, 5.5, 'Stretch', fontsize=10, color=AMBER, fontweight='bold')

# Result (3,4)
ax.text(5, 3.5, 'Result (3,4)', fontsize=12, fontweight='bold', color=ROSE, ha='center')
for i in range(3):
    for j in range(4):
        val = (i+1) + (j+1)
        rect = patches.Rectangle((3 + j*0.6, 3.0 - i*0.6), 0.6, 0.5, facecolor=ROSE, edgecolor='black', lw=1.5)
        ax.add_patch(rect)
        ax.text(3.3 + j*0.6, 3.25 - i*0.6, str(val), ha='center', va='center', fontsize=8, color='white', fontweight='bold')

ax.text(5, 0.8, 'Dimensions match from the right: (3,1) + (1,4) → (3,4)', fontsize=11, ha='center', color=GRAY)
ax.set_title('NumPy Broadcasting', fontsize=14, fontweight='bold')
fig.savefig(os.path.join(OUT_DIR, 'w07_broadcasting.png'), bbox_inches='tight')
plt.close(fig)
print("Saved w07_broadcasting.png")

# 2. w07_generator.png
fig, ax = plt.subplots(figsize=(8, 6))
ax.set_xlim(0, 10)
ax.set_ylim(0, 8)
ax.axis('off')

# Generator pipeline
boxes_gen = [
    ('Data\nSource', 1.5, 5, INDIGO),
    ('Generator\n(lazy)', 5, 5, TEAL),
    ('Consumer', 8.5, 5, AMBER),
]
for name, x, y, color in boxes_gen:
    rect = patches.FancyBboxPatch((x-1.2, y-0.6), 2.4, 1.2, boxstyle="round,pad=0.1", facecolor=color, edgecolor='black', lw=2)
    ax.add_patch(rect)
    ax.text(x, y, name, ha='center', va='center', fontsize=10, fontweight='bold', color='white')

ax.annotate('', xy=(3.8, 5), xytext=(2.7, 5), arrowprops=dict(arrowstyle='->', color=INDIGO, lw=2))
ax.annotate('', xy=(7.3, 5), xytext=(6.2, 5), arrowprops=dict(arrowstyle='->', color=INDIGO, lw=2))
ax.text(5, 6.5, 'One item at a time', fontsize=11, ha='center', color=TEAL, fontweight='bold')

# List (all at once)
rect = patches.FancyBboxPatch((2.5, 1.5), 5, 1.2, boxstyle="round,pad=0.1", facecolor=ROSE, edgecolor='black', lw=2)
ax.add_patch(rect)
ax.text(5, 2.1, 'List: [1, 2, 3, 4, 5, ...] → all in memory at once', ha='center', va='center', fontsize=10, fontweight='bold', color='white')
ax.text(5, 0.8, 'Generator: memory efficient, lazy evaluation', fontsize=11, ha='center', color=GRAY, style='italic')

ax.set_title('Generators: Lazy Evaluation', fontsize=14, fontweight='bold')
fig.savefig(os.path.join(OUT_DIR, 'w07_generator.png'), bbox_inches='tight')
plt.close(fig)
print("Saved w07_generator.png")

# 3. w07_decorator.png
fig, ax = plt.subplots(figsize=(8, 6))
ax.set_xlim(0, 10)
ax.set_ylim(0, 8)
ax.axis('off')

# Onion layers (from outside to inside)
layers = [
    ('@timing', 5, 6.5, INDIGO, 3.8),
    ('@log', 5, 5.5, TEAL, 3.0),
    ('@cache', 5, 4.5, AMBER, 2.2),
    ('func()', 5, 3.5, ROSE, 1.4),
]

for name, x, y, color, w in layers:
    rect = patches.FancyBboxPatch((x-w/2, y-0.4), w, 0.8, boxstyle="round,pad=0.1", facecolor=color, edgecolor='black', lw=2, alpha=0.8)
    ax.add_patch(rect)
    ax.text(x, y, name, ha='center', va='center', fontsize=10, fontweight='bold', color='white')

# Execution arrows
ax.annotate('', xy=(5, 5.1), xytext=(5, 5.9), arrowprops=dict(arrowstyle='->', color='black', lw=1.5))
ax.annotate('', xy=(5, 4.1), xytext=(5, 4.9), arrowprops=dict(arrowstyle='->', color='black', lw=1.5))
ax.annotate('', xy=(5, 3.1), xytext=(5, 3.9), arrowprops=dict(arrowstyle='->', color='black', lw=1.5))
ax.annotate('', xy=(5, 2.5), xytext=(5, 3.1), arrowprops=dict(arrowstyle='->', color='black', lw=1.5))

ax.annotate('', xy=(5, 3.9), xytext=(5, 4.1), arrowprops=dict(arrowstyle='->', color='black', lw=1.5))
ax.annotate('', xy=(5, 4.9), xytext=(5, 5.1), arrowprops=dict(arrowstyle='->', color='black', lw=1.5))
ax.annotate('', xy=(5, 5.9), xytext=(5, 6.1), arrowprops=dict(arrowstyle='->', color='black', lw=1.5))

ax.text(5, 1.5, 'Execution: outer → inner → func → inner → outer', fontsize=11, ha='center', color=GRAY, style='italic')
ax.set_title('Decorators: Function Wrapping', fontsize=14, fontweight='bold')
fig.savefig(os.path.join(OUT_DIR, 'w07_decorator.png'), bbox_inches='tight')
plt.close(fig)
print("Saved w07_decorator.png")

# ============== W08 EDA ==============

# 1. w08_histogram_kde.png
fig, ax = plt.subplots(figsize=(8, 6))

np.random.seed(42)
data = np.random.gamma(2, 2, 2000)

# Histogram
n, bins, patches_hist = ax.hist(data, bins=40, density=True, color=INDIGO, alpha=0.6, edgecolor='white', label='Histogram')

# KDE (numpy-only, no scipy)
def simple_kde(data, num_points=500):
    n = len(data)
    bandwidth = 1.06 * np.std(data) * n ** (-1/5)
    xx = np.linspace(data.min(), data.max(), num_points)
    # Gaussian kernel
    kernel = np.exp(-0.5 * ((xx[:, None] - data) / bandwidth) ** 2) / (bandwidth * np.sqrt(2 * np.pi))
    yy = kernel.sum(axis=1) / n
    return xx, yy

xx, yy = simple_kde(data)
ax.plot(xx, yy, color=TEAL, lw=2.5, label='KDE')

mean = data.mean()
median = np.median(data)
ax.axvline(mean, color=AMBER, linestyle='-', lw=2, label=f'Mean = {mean:.2f}')
ax.axvline(median, color=ROSE, linestyle='--', lw=2, label=f'Median = {median:.2f}')

ax.annotate(f'Mean\n{mean:.2f}', xy=(mean, ax.get_ylim()[1]*0.8), fontsize=10, color=AMBER, fontweight='bold')
ax.annotate(f'Median\n{median:.2f}', xy=(median, ax.get_ylim()[1]*0.6), fontsize=10, color=ROSE, fontweight='bold')

ax.set_xlabel('Value')
ax.set_ylabel('Density')
ax.set_title('Histogram with KDE Overlay', fontsize=14, fontweight='bold')
ax.legend(loc='upper right')
fig.savefig(os.path.join(OUT_DIR, 'w08_histogram_kde.png'), bbox_inches='tight')
plt.close(fig)
print("Saved w08_histogram_kde.png")

# 2. w08_boxplot.png
fig, ax = plt.subplots(figsize=(8, 6))

np.random.seed(42)
data = np.random.normal(50, 10, 200)
# Add outliers
data = np.concatenate([data, [80, 82, 85, 20, 18]])

bp = ax.boxplot(data, vert=False, patch_artist=True, widths=0.5)
bp['boxes'][0].set_facecolor(INDIGO)
bp['boxes'][0].set_alpha(0.7)
bp['medians'][0].set_color(ROSE)
bp['medians'][0].set_linewidth(2.5)

for whisker in bp['whiskers']:
    whisker.set(color=TEAL, linewidth=2)
for cap in bp['caps']:
    cap.set(color=TEAL, linewidth=2)
for flier in bp['fliers']:
    flier.set(marker='o', color=AMBER, markersize=8, alpha=0.8)

# Labels
q1 = np.percentile(data, 25)
q2 = np.median(data)
q3 = np.percentile(data, 75)
iqr = q3 - q1
lower = q1 - 1.5 * iqr
upper = q3 + 1.5 * iqr

ax.annotate(f'Q3 = {q3:.1f}', xy=(q3, 1.15), fontsize=10, color=INDIGO, fontweight='bold')
ax.annotate(f'Q2 = {q2:.1f}', xy=(q2, 1.15), fontsize=10, color=ROSE, fontweight='bold')
ax.annotate(f'Q1 = {q1:.1f}', xy=(q1, 1.15), fontsize=10, color=INDIGO, fontweight='bold')
ax.annotate(f'Whisker\n{upper:.1f}', xy=(upper, 0.7), fontsize=9, color=TEAL, fontweight='bold')
ax.annotate(f'Whisker\n{lower:.1f}', xy=(lower, 0.7), fontsize=9, color=TEAL, fontweight='bold')
ax.annotate('Outliers', xy=(82, 0.75), fontsize=10, color=AMBER, fontweight='bold')

ax.set_yticks([])
ax.set_xlabel('Value')
ax.set_title('Box Plot Anatomy', fontsize=14, fontweight='bold')
fig.savefig(os.path.join(OUT_DIR, 'w08_boxplot.png'), bbox_inches='tight')
plt.close(fig)
print("Saved w08_boxplot.png")

# 3. w08_correlation_heatmap.png
fig, ax = plt.subplots(figsize=(8, 6))

np.random.seed(42)
# Create 8 correlated features
data = np.random.randn(500, 8)
data[:, 1] += 0.7 * data[:, 0]  # corr
data[:, 2] -= 0.5 * data[:, 0]  # anti-corr
data[:, 3] += 0.3 * data[:, 1]
data[:, 4] += 0.8 * data[:, 5]

corr = np.corrcoef(data.T)
labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

sns.heatmap(corr, annot=True, fmt='.2f', cmap='RdBu_r', vmin=-1, vmax=1,
            square=True, linewidths=0.5, ax=ax, xticklabels=labels, yticklabels=labels,
            cbar_kws={'label': 'Correlation'})
ax.set_title('Correlation Heatmap', fontsize=14, fontweight='bold')
fig.savefig(os.path.join(OUT_DIR, 'w08_correlation_heatmap.png'), bbox_inches='tight')
plt.close(fig)
print("Saved w08_correlation_heatmap.png")

# 4. w08_missing_data.png
fig, ax = plt.subplots(figsize=(8, 6))

np.random.seed(42)
# Create data with NaN patterns
n_rows, n_cols = 30, 12
data = np.random.randn(n_rows, n_cols)
# Introduce missing patterns
for i in range(5, 15):
    data[i, 3:7] = np.nan
for i in range(20, 28):
    data[i, 8:11] = np.nan
for i in range(0, 8):
    data[i, 0] = np.nan

data = np.where(np.isnan(data), 0, 1)
ax.imshow(data, cmap='Greys', aspect='auto', interpolation='nearest')
ax.set_xlabel('Features')
ax.set_ylabel('Samples')
ax.set_title('Missing Data Pattern (White = NaN)', fontsize=14, fontweight='bold')
ax.set_xticks(range(n_cols))
ax.set_yticks(range(0, n_rows, 5))
fig.savefig(os.path.join(OUT_DIR, 'w08_missing_data.png'), bbox_inches='tight')
plt.close(fig)
print("Saved w08_missing_data.png")

# 5. w08_before_after.png
fig, axes = plt.subplots(2, 2, figsize=(10, 8))

# Raw messy data
np.random.seed(42)

# Before: outliers, missing, skewed
ax = axes[0, 0]
raw_x = np.random.exponential(2, 200)
raw_x = np.concatenate([raw_x, [15, 18, 20]])  # outliers
ax.hist(raw_x, bins=30, color=AMBER, edgecolor='white', alpha=0.8)
ax.set_title('Before: Skewed with Outliers', fontsize=12, fontweight='bold')
ax.set_xlabel('Value')
ax.set_ylabel('Frequency')

ax = axes[0, 1]
raw_y = np.random.normal(50, 15, 200)
raw_y[20:30] = np.nan  # missing block
ax.scatter(range(len(raw_y)), raw_y, c=ROSE, s=20, alpha=0.6)
ax.set_title('Before: Missing Values', fontsize=12, fontweight='bold')
ax.set_xlabel('Index')
ax.set_ylabel('Value')

# After: clean
ax = axes[1, 0]
clean_x = np.random.normal(5, 1.5, 200)
ax.hist(clean_x, bins=30, color=TEAL, edgecolor='white', alpha=0.8)
ax.set_title('After: Normalized', fontsize=12, fontweight='bold')
ax.set_xlabel('Value')
ax.set_ylabel('Frequency')

ax = axes[1, 1]
clean_y = np.random.normal(50, 10, 200)
ax.scatter(range(len(clean_y)), clean_y, c=INDIGO, s=20, alpha=0.6)
ax.set_title('After: Complete & Smooth', fontsize=12, fontweight='bold')
ax.set_xlabel('Index')
ax.set_ylabel('Value')

fig.suptitle('Before vs After Data Cleaning', fontsize=14, fontweight='bold', y=1.02)
plt.tight_layout()
fig.savefig(os.path.join(OUT_DIR, 'w08_before_after.png'), bbox_inches='tight')
plt.close(fig)
print("Saved w08_before_after.png")

# ============== SUMMARY ==============
files = os.listdir(OUT_DIR)
print(f"\n=== Total files created: {len(files)} ===")
total_size = 0
for f in sorted(files):
    fpath = os.path.join(OUT_DIR, f)
    size = os.path.getsize(fpath)
    total_size += size
    print(f"  {f}: {size/1024:.1f} KB")
print(f"Total size: {total_size/1024:.1f} KB")
