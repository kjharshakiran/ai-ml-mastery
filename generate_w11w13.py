#!/usr/bin/env python3
"""Generate figures for W09-W15: NLP, Image/Audio, ML Paradigms, Regression, Classification."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Rectangle, Circle, Ellipse, Polygon
import numpy as np
import os

OUTPUT_DIR = '/Users/harshakiran/Coding/iitmcourse/assets/figures/phase1_static'
os.makedirs(OUTPUT_DIR, exist_ok=True)

BRAND = {'indigo':'#4f46e5','teal':'#14b8a6','amber':'#f59e0b','rose':'#f43f5e','gray':'#767c93','bg':'#f7f7fb'}
plt.rcParams.update({'figure.facecolor':BRAND['bg'],'axes.facecolor':BRAND['bg'],'axes.edgecolor':BRAND['gray'],'axes.labelcolor':'#2e3047','text.color':'#2e3047','xtick.color':BRAND['gray'],'ytick.color':BRAND['gray'],'font.size':11,'figure.dpi':120,'savefig.dpi':120,'savefig.facecolor':BRAND['bg']})

def save(fig,name):
    fig.tight_layout()
    fig.savefig(os.path.join(OUTPUT_DIR,name),bbox_inches='tight',pad_inches=0.15)
    plt.close(fig)
    print(f'  {name}')

files=[]

# ===== W09: NLP (4 figures) =====
# w09_tokenization, w09_word_embedding, w09_ngram_tree, w09_tfidf already generated

# ===== W10: Image/Audio (5 figures) =====
# w10_rgb_channels, w10_convolution, w10_spectrogram, w10_vision_tasks, w10_normalization already generated

# ===== W11: ML Paradigms I (3 figures) =====
# w11_paradigm_venn
fig,ax=plt.subplots(figsize=(8,6))
ax.set_xlim(0,10);ax.set_ylim(0,8);ax.axis('off')
# Circles
c1=Circle((3.5,4.5),2.2,fill=False,edgecolor=BRAND['indigo'],lw=2.5)
c2=Circle((5.5,4.5),2.2,fill=False,edgecolor=BRAND['teal'],lw=2.5)
c3=Circle((4.5,3.2),2.0,fill=False,edgecolor=BRAND['amber'],lw=2.5)
for c in [c1,c2,c3]: ax.add_patch(c)
ax.text(3.5,5.5,'Supervised',ha='center',fontsize=11,fontweight='bold',color=BRAND['indigo'])
ax.text(5.5,5.5,'Unsupervised',ha='center',fontsize=11,fontweight='bold',color=BRAND['teal'])
ax.text(4.5,2.5,'Semi-\nsupervised',ha='center',fontsize=10,fontweight='bold',color=BRAND['amber'])
ax.text(4.5,4.5,'Both',ha='center',fontsize=9,color='#555')
ax.text(4.5,1.0,'Reinforcement Learning',ha='center',fontsize=11,fontweight='bold',color=BRAND['rose'],
        bbox=dict(boxstyle='round,pad=0.5',facecolor=BRAND['light_rose'],edgecolor=BRAND['rose']))
ax.annotate('',xy=(4.5,1.5),xytext=(4.5,2.0),arrowprops=dict(arrowstyle='->',color=BRAND['rose'],lw=2))
ax.set_title('W11 · ML Paradigm Venn Diagram',fontsize=13,fontweight='bold')
files.append(save(fig,'w11_paradigm_venn.png'))

# w11_pipeline
fig,ax=plt.subplots(figsize=(12,3))
ax.set_xlim(0,12);ax.set_ylim(0,3);ax.axis('off')
stages=[('Raw Data',BRAND['indigo']),('Preprocessing',BRAND['teal']),('Model',BRAND['amber']),('Predictions',BRAND['rose']),('Evaluation',BRAND['gray'])]
for i,(stage,color) in enumerate(stages):
    rect=FancyBboxPatch((i*2.2+0.2,1),1.8,1,boxstyle='round,pad=0.1',facecolor=color,alpha=0.2,edgecolor=color,lw=2)
    ax.add_patch(rect);ax.text(i*2.2+1.1,1.5,stage,ha='center',va='center',fontsize=10,fontweight='bold',color=color)
    if i<4: ax.annotate('',xy=((i+1)*2.2+0.15,1.5),xytext=(i*2.2+2.0,1.5),arrowprops=dict(arrowstyle='->',color=BRAND['gray'],lw=2))
ax.set_title('W11 · ML Learning Pipeline',fontsize=13,fontweight='bold')
files.append(save(fig,'w11_pipeline.png'))

# w11_labeled_unlabeled
fig,axes=plt.subplots(1,2,figsize=(10,4))
np.random.seed(42)
for i,ax in enumerate(axes):
    x=np.random.randn(50);y=np.random.randn(50)
    if i==0:
        colors=[BRAND['indigo'] if xi+yi>0 else BRAND['teal'] for xi,yi in zip(x,y)]
        ax.scatter(x,y,c=colors,s=30,alpha=0.7);ax.set_title('Labeled Data',fontweight='bold')
    else:
        ax.scatter(x,y,c=BRAND['gray'],s=30,alpha=0.5);ax.set_title('Unlabeled Data',fontweight='bold')
    ax.set_xlim(-3,3);ax.set_ylim(-3,3);ax.set_aspect('equal')
fig.suptitle('W11 · Labeled vs Unlabeled Data',fontsize=13,fontweight='bold',color=BRAND['indigo'])
files.append(save(fig,'w11_labeled_unlabeled.png'))

# ===== W12: ML Paradigms II (2 figures) =====
# w12_meta_learning
fig,ax=plt.subplots(figsize=(8,6))
ax.set_xlim(0,10);ax.set_ylim(0,8);ax.axis('off')
# Outer loop
rect=FancyBboxPatch((1,5),3,2,boxstyle='round,pad=0.2',facecolor=BRAND['light_indigo'],edgecolor=BRAND['indigo'],lw=2)
ax.add_patch(rect);ax.text(2.5,6,'Meta-Optimizer',ha='center',fontsize=11,fontweight='bold',color=BRAND['indigo'])
# Inner loop
rect=FancyBboxPatch((5.5,5),3,2,boxstyle='round,pad=0.2',facecolor=BRAND['light_teal'],edgecolor=BRAND['teal'],lw=2)
ax.add_patch(rect);ax.text(7,6,'Task Learner',ha='center',fontsize=11,fontweight='bold',color=BRAND['teal'])
ax.annotate('',xy=(5.3,6),xytext=(4.1,6),arrowprops=dict(arrowstyle='->',color=BRAND['gray'],lw=2))
ax.annotate('',xy=(4.1,5.5),xytext=(5.3,5.5),arrowprops=dict(arrowstyle='->',color=BRAND['gray'],lw=2))
ax.text(4.7,6.5,'θ (meta)',ha='center',fontsize=9,color=BRAND['indigo'])
ax.text(4.7,5.0,'∇L',ha='center',fontsize=9,color=BRAND['teal'])
ax.set_title('W12 · Meta-Learning: Nested Optimization',fontsize=13,fontweight='bold')
files.append(save(fig,'w12_meta_learning.png'))

# w12_rl_loop
fig,ax=plt.subplots(figsize=(7,7))
ax.set_xlim(0,10);ax.set_ylim(0,10);ax.axis('off')
# Nodes as circles
for pos,label,color in [((5,8.5),'Agent',BRAND['indigo']),((8,5),'Environment',BRAND['teal']),((2,5),'State\nReward',BRAND['amber'])]:
    c=Circle(pos,1.2,facecolor=color,alpha=0.2,edgecolor=color,lw=2)
    ax.add_patch(c);ax.text(pos[0],pos[1],label,ha='center',va='center',fontsize=11,fontweight='bold',color=color)
ax.annotate('Action',xy=(7.2,6.5),xytext=(5.8,7.5),arrowprops=dict(arrowstyle='->',color=BRAND['gray'],lw=2,connectionstyle='arc3,rad=-0.3'))
ax.annotate('Observation\n+ Reward',xy=(3.2,5.8),xytext=(6.8,5.2),arrowprops=dict(arrowstyle='->',color=BRAND['gray'],lw=2,connectionstyle='arc3,rad=-0.3'))
ax.annotate('',xy=(5,7.2),xytext=(2.8,5.8),arrowprops=dict(arrowstyle='->',color=BRAND['gray'],lw=2,connectionstyle='arc3,rad=0.3'))
ax.set_title('W12 · RL Feedback Loop',fontsize=13,fontweight='bold')
files.append(save(fig,'w12_rl_loop.png'))

# ===== W13: Regression I (5 figures) =====
# w13_regression_line
fig,ax=plt.subplots(figsize=(8,5))
np.random.seed(42)
x=np.linspace(0,10,50)
y=2+0.8*x+np.random.randn(50)*1.5
ax.scatter(x,y,color=BRAND['indigo'],s=30,alpha=0.6,label='Data')
ax.plot(x,2+0.8*x,color=BRAND['teal'],lw=2.5,label='Regression line')
for xi,yi in zip(x[::5],y[::5]):
    ax.plot([xi,xi],[yi,2+0.8*xi],color=BRAND['rose'],lw=1,alpha=0.5)
ax.set_title('W13 · Regression Line with Residuals',fontsize=13,fontweight='bold')
ax.set_xlabel('x');ax.set_ylabel('y');ax.legend()
files.append(save(fig,'w13_regression_line.png'))

# w13_residual_dist
fig,ax=plt.subplots(figsize=(7,4))
residuals=np.random.randn(500)*0.5
ax.hist(residuals,bins=25,color=BRAND['indigo'],alpha=0.7,edgecolor='white')
ax.axvline(0,color=BRAND['rose'],lw=2,ls='--',label='Mean = 0')
ax.set_title('W13 · Residual Distribution (Should be Gaussian)',fontsize=13,fontweight='bold')
ax.set_xlabel('Residual');ax.set_ylabel('Frequency');ax.legend()
files.append(save(fig,'w13_residual_dist.png'))

# w13_3d_plane
fig=plt.figure(figsize=(9,7))
ax=fig.add_subplot(111,projection='3d')
np.random.seed(42)
x=np.random.rand(30)*10;y=np.random.rand(30)*10;z=2+0.5*x+0.3*y+np.random.randn(30)*0.5
ax.scatter(x,y,z,color=BRAND['indigo'],s=30,alpha=0.6)
xx,yy=np.meshgrid(np.linspace(0,10,10),np.linspace(0,10,10))
zz=2+0.5*xx+0.3*yy
ax.plot_surface(xx,yy,zz,alpha=0.2,color=BRAND['teal'])
ax.set_title('W13 · 3D Regression Plane',fontsize=13,fontweight='bold')
ax.set_xlabel('x');ax.set_ylabel('y');ax.set_zlabel('z')
files.append(save(fig,'w13_3d_plane.png'))

# w13_coefficients
fig,ax=plt.subplots(figsize=(8,4))
features=['sqft','bedrooms','age','distance','crime','school']
coeffs=[150,-2000,-500,-8000,-12000,18000]
errors=[20,300,80,500,1200,900]
ax.barh(range(len(features)),coeffs,color=[BRAND['indigo'] if c>0 else BRAND['rose'] for c in coeffs],alpha=0.7,edgecolor='white')
ax.errorbar(coeffs,range(len(features)),xerr=errors,fmt='none',color=BRAND['gray'],lw=1.5)
ax.set_yticks(range(len(features)));ax.set_yticklabels(features)
ax.set_title('W13 · Feature Coefficients with Confidence Intervals',fontsize=13,fontweight='bold')
ax.set_xlabel('Coefficient Value');ax.axvline(0,color=BRAND['gray'],lw=1,ls='--')
files.append(save(fig,'w13_coefficients.png'))

# w13_normal_equation
fig,ax=plt.subplots(figsize=(7,7))
ax.set_xlim(0,10);ax.set_ylim(0,10);ax.axis('off')
# Column space
rect=Rectangle((1,1),5,6,facecolor=BRAND['light_indigo'],edgecolor=BRAND['indigo'],lw=2,alpha=0.3)
ax.add_patch(rect);ax.text(3.5,7.2,'Col(X)',ha='center',fontsize=12,fontweight='bold',color=BRAND['indigo'])
# y vector
ax.annotate('',xy=(8,8),xytext=(3,5),arrowprops=dict(arrowstyle='->',color=BRAND['rose'],lw=3))
ax.text(8.2,8.2,'y',fontsize=14,fontweight='bold',color=BRAND['rose'])
# Projection
ax.annotate('',xy=(4.5,6.5),xytext=(3,5),arrowprops=dict(arrowstyle='->',color=BRAND['teal'],lw=3))
ax.text(4.7,6.7,'Xβ̂',fontsize=12,fontweight='bold',color=BRAND['teal'])
# Residual
ax.plot([4.5,8],[6.5,8],color=BRAND['amber'],lw=2,ls='--')
ax.text(6.5,7.8,'⊥ (residual)',fontsize=10,color=BRAND['amber'],fontweight='bold')
ax.set_title('W13 · Normal Equation: Projection Geometry',fontsize=13,fontweight='bold')
files.append(save(fig,'w13_normal_equation.png'))

print(f'\nW09-W13 done: {len(files)} files generated')
