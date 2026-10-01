import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Rectangle, Ellipse, Circle
import numpy as np
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
    print(f'  {name}')

print('=== Generating W09-W15 figures ===')

# W09-1: Tokenization
fig, ax = plt.subplots(figsize=(10, 3))
ax.set_xlim(0, 10); ax.set_ylim(0, 3); ax.axis('off')
stages = ['Sentence', 'Words', 'Subwords', 'Token IDs']
colors = [BRAND['indigo'], BRAND['teal'], BRAND['amber'], BRAND['rose']]
for i, (stage, color) in enumerate(zip(stages, colors)):
    rect = FancyBboxPatch((i*2.2+0.3, 1), 1.8, 1, boxstyle="round,pad=0.1", facecolor=color, alpha=0.2, edgecolor=color, lw=2)
    ax.add_patch(rect)
    ax.text(i*2.2+1.2, 1.5, stage, ha='center', va='center', fontsize=11, fontweight='bold', color=color)
    if i < 3:
        ax.annotate('', xy=((i+1)*2.2+0.2, 1.5), xytext=(i*2.2+2.1, 1.5), arrowprops=dict(arrowstyle='->', color=BRAND['gray'], lw=2))
ax.text(1.2, 0.5, '"The cat sat"', ha='center', fontsize=9, color=BRAND['gray'])
ax.text(3.4, 0.5, '["The","cat","sat"]', ha='center', fontsize=9, color=BRAND['gray'])
ax.text(5.6, 0.5, '["The","c","at","sat"]', ha='center', fontsize=9, color=BRAND['gray'])
ax.text(7.8, 0.5, '[101, 202, 305, 412]', ha='center', fontsize=9, color=BRAND['gray'])
ax.set_title('W09 · Tokenization Pipeline', fontsize=13, fontweight='bold', color=BRAND['indigo'])
save(fig, 'w09_tokenization.png')

# W09-2: Word Embedding
fig, ax = plt.subplots(figsize=(8, 7))
np.random.seed(42)
words = {'king': [2, 3], 'queen': [2.5, 4], 'man': [4, 2], 'woman': [4.5, 3], 'prince': [1.5, 2.5], 'princess': [2, 3.5], 'boy': [3.5, 1.5], 'girl': [4, 2.5]}
for w, pos in words.items():
    ax.scatter(pos[0], pos[1], color=BRAND['indigo'], s=80, zorder=3)
    ax.text(pos[0]+0.1, pos[1]+0.1, w, fontsize=10, color=BRAND['gray'])
ax.annotate('', xy=words['queen'], xytext=words['king'], arrowprops=dict(arrowstyle='->', color=BRAND['teal'], lw=2))
ax.annotate('', xy=words['woman'], xytext=words['man'], arrowprops=dict(arrowstyle='->', color=BRAND['teal'], lw=2))
ax.annotate('', xy=(2.35, 3.5), xytext=(4.25, 2.5), arrowprops=dict(arrowstyle='->', color=BRAND['amber'], lw=2, ls='--'))
ax.text(3, 2.8, 'same\ndirection', fontsize=9, color=BRAND['amber'], ha='center')
ax.text(3, 1.5, 'king - man + woman ≈ queen', fontsize=11, color=BRAND['indigo'], fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.4', facecolor=BRAND['light_indigo'], edgecolor=BRAND['indigo']))
ax.set_xlim(0, 6); ax.set_ylim(0, 5); ax.set_aspect('equal')
ax.axhline(0, color=BRAND['gray'], lw=0.5); ax.axvline(0, color=BRAND['gray'], lw=0.5)
ax.set_title('W09 · Word Embedding Vector Arithmetic', fontsize=13, fontweight='bold')
save(fig, 'w09_word_embedding.png')

# W09-3: N-gram Tree
fig, ax = plt.subplots(figsize=(9, 6))
ax.set_xlim(0, 10); ax.set_ylim(0, 6); ax.axis('off')
ax.text(5, 5.5, 'The cat sat on the', ha='center', fontsize=12, fontweight='bold', color=BRAND['indigo'])
branches = {'mat': 0.45, 'chair': 0.30, 'floor': 0.15, 'table': 0.10}
x_pos = [2, 4.5, 7, 9]
for i, (word, prob) in enumerate(branches.items()):
    ax.plot([5, x_pos[i]], [5.2, 3.5], color=BRAND['teal'], lw=prob*8, alpha=0.6)
    ax.text(x_pos[i], 3.2, word, ha='center', fontsize=10, fontweight='bold', color=BRAND['teal'])
    ax.text(x_pos[i], 2.8, f'{prob:.0%}', ha='center', fontsize=9, color=BRAND['gray'])
ax.set_title('W09 · N-gram Next-Word Prediction', fontsize=13, fontweight='bold')
save(fig, 'w09_ngram_tree.png')

# W09-4: TF-IDF
fig, ax = plt.subplots(figsize=(8, 5))
np.random.seed(42)
docs = ['Doc1', 'Doc2', 'Doc3', 'Doc4', 'Doc5']
terms = ['machine', 'learning', 'data', 'model', 'neural', 'deep', 'algorithm', 'training']
tfidf = np.random.rand(5, 8) * 0.5
tfidf[0, 0] = 0.85; tfidf[0, 1] = 0.82; tfidf[2, 2] = 0.90; tfidf[4, 5] = 0.88
im = ax.imshow(tfidf, cmap='YlOrRd', aspect='auto', vmin=0, vmax=1)
ax.set_xticks(range(8)); ax.set_yticks(range(5))
ax.set_xticklabels(terms, rotation=45, ha='right'); ax.set_yticklabels(docs)
for i in range(5):
    for j in range(8):
        ax.text(j, i, f'{tfidf[i,j]:.2f}', ha='center', va='center', fontsize=8, color='white' if tfidf[i,j] > 0.5 else 'black')
plt.colorbar(im, ax=ax, label='TF-IDF Weight')
ax.set_title('W09 · TF-IDF Document-Term Matrix', fontsize=13, fontweight='bold')
save(fig, 'w09_tfidf.png')

# W10-1: RGB Channels
fig, axes = plt.subplots(1, 4, figsize=(12, 3))
np.random.seed(0)
img = np.random.rand(10, 10, 3)
img[:, :, 0] = np.linspace(0, 1, 10).reshape(10, 1) * np.ones((10, 10))
img[:, :, 1] = np.ones((10, 10)) * np.linspace(0, 1, 10)
img[:, :, 2] = np.linspace(0, 1, 10).reshape(10, 1) * np.linspace(0, 1, 10)
for i, title in enumerate(['R Channel', 'G Channel', 'B Channel']):
    channel = np.zeros((10, 10, 3))
    channel[:, :, i] = img[:, :, i]
    axes[i].imshow(channel, interpolation='nearest')
    axes[i].set_title(title, fontsize=10, fontweight='bold')
    axes[i].axis('off')
axes[3].imshow(img, interpolation='nearest')
axes[3].set_title('RGB Combined', fontsize=10, fontweight='bold')
axes[3].axis('off')
fig.suptitle('W10 · RGB Channel Separation', fontsize=13, fontweight='bold', color=BRAND['indigo'])
save(fig, 'w10_rgb_channels.png')

# W10-2: Convolution
fig, axes = plt.subplots(1, 3, figsize=(12, 4))
input_grid = np.array([[1,2,3,4,5],[2,3,4,5,6],[3,4,5,6,7],[4,5,6,7,8],[5,6,7,8,9]])
axes[0].imshow(input_grid, cmap='Blues', interpolation='nearest')
axes[0].set_title('Input (5×5)', fontsize=10, fontweight='bold')
for i in range(5):
    for j in range(5):
        axes[0].text(j, i, input_grid[i, j], ha='center', va='center', fontsize=8)
axes[0].set_xticks([]); axes[0].set_yticks([])
filter_grid = np.array([[0,1,0],[1,-4,1],[0,1,0]])
axes[1].imshow(filter_grid, cmap='RdYlBu_r', interpolation='nearest', vmin=-5, vmax=5)
axes[1].set_title('Laplacian Filter (3×3)', fontsize=10, fontweight='bold')
for i in range(3):
    for j in range(3):
        axes[1].text(j, i, filter_grid[i, j], ha='center', va='center', fontsize=9)
axes[1].set_xticks([]); axes[1].set_yticks([])
output = np.array([[0,0,0],[0,0,0],[0,0,0]])
axes[2].imshow(output, cmap='Greens', interpolation='nearest')
axes[2].set_title('Output Feature Map (3×3)', fontsize=10, fontweight='bold')
for i in range(3):
    for j in range(3):
        axes[2].text(j, i, output[i, j], ha='center', va='center', fontsize=8)
axes[2].set_xticks([]); axes[2].set_yticks([])
fig.suptitle('W10 · Convolution Operation', fontsize=13, fontweight='bold', color=BRAND['indigo'])
save(fig, 'w10_convolution.png')

# W10-3: Spectrogram
fig, axes = plt.subplots(1, 3, figsize=(12, 3.5))
t = np.linspace(0, 1, 1000)
waveform = np.sin(2*np.pi*5*t) + 0.5*np.sin(2*np.pi*15*t) + 0.3*np.sin(2*np.pi*30*t)
axes[0].plot(t, waveform, color=BRAND['indigo'], lw=1)
axes[0].set_title('Waveform', fontsize=10, fontweight='bold')
axes[0].set_xlabel('Time'); axes[0].set_ylabel('Amplitude')
axes[1].plot(t, waveform, color=BRAND['gray'], alpha=0.3, lw=1)
for start in [0, 200, 400, 600, 800]:
    axes[1].axvspan(t[start], t[start+200], alpha=0.3, color=BRAND['teal'])
axes[1].set_title('Sliding FFT Windows', fontsize=10, fontweight='bold')
axes[1].set_xlabel('Time')
spec = np.random.rand(50, 20) * 0.1
spec[5, :] = 0.8; spec[15, :] = 0.5; spec[30, :] = 0.3
axes[2].imshow(spec, aspect='auto', origin='lower', cmap='viridis', extent=[0, 1, 0, 50])
axes[2].set_title('Spectrogram', fontsize=10, fontweight='bold')
axes[2].set_xlabel('Time'); axes[2].set_ylabel('Frequency')
fig.suptitle('W10 · Spectrogram Generation', fontsize=13, fontweight='bold', color=BRAND['indigo'])
save(fig, 'w10_spectrogram.png')

# W10-4: Vision Tasks
fig, axes = plt.subplots(1, 3, figsize=(12, 4))
for i, title in enumerate(['Classification', 'Detection', 'Segmentation']):
    ax = axes[i]
    ax.set_xlim(0, 10); ax.set_ylim(0, 10); ax.set_aspect('equal')
    img = np.random.rand(10, 10) * 0.3 + 0.5
    ax.imshow(img, cmap='gray', interpolation='nearest')
    if i == 0:
        rect = Rectangle((3, 3), 4, 4, fill=False, edgecolor=BRAND['indigo'], lw=3)
        ax.add_patch(rect)
        ax.text(5, 5, 'CAT', ha='center', va='center', fontsize=14, color=BRAND['indigo'], fontweight='bold')
    elif i == 1:
        for pos, label in [((1, 2), 'DOG'), ((6, 5), 'CAT'), ((2, 7), 'BIRD')]:
            rect = Rectangle(pos, 2.5, 2.5, fill=False, edgecolor=BRAND['teal'], lw=2)
            ax.add_patch(rect)
            ax.text(pos[0]+1.25, pos[1]+1.25, label, ha='center', va='center', fontsize=9, color=BRAND['teal'], fontweight='bold')
    else:
        mask = np.zeros((10, 10, 4))
        mask[3:7, 3:7, 0] = 1; mask[3:7, 3:7, 3] = 0.5
        ax.imshow(mask, interpolation='nearest')
        ax.text(5, 5, 'CAT', ha='center', va='center', fontsize=14, color='white', fontweight='bold')
    ax.set_title(title, fontsize=11, fontweight='bold')
    ax.set_xticks([]); ax.set_yticks([])
fig.suptitle('W10 · Vision Task Difficulty Ladder', fontsize=13, fontweight='bold', color=BRAND['indigo'])
save(fig, 'w10_vision_tasks.png')

# W10-5: Normalization
fig, axes = plt.subplots(1, 2, figsize=(10, 4))
np.random.seed(42)
raw = np.random.beta(2, 5, 1000) * 255
axes[0].hist(raw, bins=30, color=BRAND['indigo'], alpha=0.7, edgecolor='white')
axes[0].axvline(np.mean(raw), color=BRAND['rose'], lw=2, ls='--', label=f'Mean={np.mean(raw):.1f}')
axes[0].set_title('Before: Raw (0-255)', fontsize=11, fontweight='bold')
axes[0].set_xlabel('Pixel Value'); axes[0].set_ylabel('Frequency')
axes[0].legend()
normalized = (raw - raw.min()) / (raw.max() - raw.min())
axes[1].hist(normalized, bins=30, color=BRAND['teal'], alpha=0.7, edgecolor='white')
axes[1].axvline(np.mean(normalized), color=BRAND['rose'], lw=2, ls='--', label=f'Mean={np.mean(normalized):.2f}')
axes[1].set_title('After: Normalized (0-1)', fontsize=11, fontweight='bold')
axes[1].set_xlabel('Pixel Value'); axes[1].set_ylabel('Frequency')
axes[1].legend()
fig.suptitle('W10 · Image Normalization', fontsize=13, fontweight='bold', color=BRAND['indigo'])
save(fig, 'w10_normalization.png')

print(f'\nW09-W10 done: 9 files generated')
