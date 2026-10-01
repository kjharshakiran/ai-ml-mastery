#!/usr/bin/env python3
"""Generate figures for W17-W23: SVM, Normalization, PCA/LDA, Decision Trees, Ensemble, Clustering."""
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

# ===== W17: SVM I (3 figures) =====
# w17_perceptron
fig,axes=plt.subplots(1,3,figsize=(12,4))
np.random.seed(42)
x=np.random.randn(50)*2;y=np.random.randn(50)*2
cls=(x+y)>0
for i,ax in enumerate(axes):
    ax.scatter(x[cls],y[cls],color=BRAND['indigo'],s=30,alpha=0.6,label='Class +1')
    ax.scatter(x[~cls],y[~cls],color=BRAND['teal'],s=30,alpha=0.6,label='Class -1')
    if i==0: ax.plot([-2,2],[-1,1],color=BRAND['rose'],lw=2,ls='--');ax.set_title('Initial (wrong)')
    elif i==1: ax.plot([-2,2],[-0.5,1.5],color=BRAND['amber'],lw=2);ax.set_title('Mid-training')
    else: ax.plot([-2,2],[0,2],color=BRAND['indigo'],lw=2.5);ax.set_title('Converged')
    ax.set_xlim(-3,3);ax.set_ylim(-3,3);ax.set_aspect('equal')
fig.suptitle('W17 · Perceptron Learning Rule',fontsize=13,fontweight='bold',color=BRAND['indigo'])
files.append(save(fig,'w17_perceptron.png'))

# w17_decision_boundary
fig,ax=plt.subplots(figsize=(7,7))
np.random.seed(42)
x=np.random.randn(30)*1.5;y=np.random.randn(30)*1.5
cls=(x+y)>0
ax.scatter(x[cls],y[cls],color=BRAND['indigo'],s=40,alpha=0.7)
ax.scatter(x[~cls],y[~cls],color=BRAND['teal'],s=40,alpha=0.7)
ax.plot([-3,3],[-2,4],color=BRAND['indigo'],lw=2.5,label='Decision boundary')
ax.annotate('',xy=(1.5,1.5),xytext=(0,0),arrowprops=dict(arrowstyle='->',color=BRAND['rose'],lw=2))
ax.text(1.7,1.7,'w',fontsize=12,fontweight='bold',color=BRAND['rose'])
ax.fill_between([-3,3],[-2,4],[4,10],alpha=0.1,color=BRAND['indigo'])
ax.fill_between([-3,3],[-2,4],[-6,-2],alpha=0.1,color=BRAND['teal'])
ax.set_xlim(-3,3);ax.set_ylim(-3,3);ax.set_aspect('equal')
ax.set_title('W17 · Decision Boundary with Weight Vector',fontsize=13,fontweight='bold')
ax.legend()
files.append(save(fig,'w17_decision_boundary.png'))

# w17_activation
fig,ax=plt.subplots(figsize=(8,5))
x=np.linspace(-5,5,200)
ax.plot(x,np.where(x>0,1,0),color=BRAND['indigo'],lw=2.5,label='Step')
ax.plot(x,1/(1+np.exp(-x*2)),color=BRAND['teal'],lw=2.5,label='Sigmoid (T=0.5)')
ax.plot(x,1/(1+np.exp(-x*5)),color=BRAND['amber'],lw=2,ls='--',label='Sigmoid (T=0.2)')
ax.axhline(0.5,color=BRAND['gray'],lw=1,ls='--',alpha=0.5)
ax.set_title('W17 · Step vs Sigmoid Activation',fontsize=13,fontweight='bold')
ax.set_xlabel('x');ax.set_ylabel('Output');ax.legend();ax.set_ylim(-0.1,1.1)
files.append(save(fig,'w17_activation.png'))

# ===== W19: Normalization (3 figures) =====
# w19_before_after_scaling
fig,axes=plt.subplots(1,2,figsize=(10,5))
np.random.seed(42)
x=np.random.randn(100)*500+1000;y=np.random.randn(100)*2+5
for i,ax in enumerate(axes):
    if i==0: ax.scatter(x,y,color=BRAND['indigo'],s=20,alpha=0.6);ax.set_title('Before Scaling');ax.set_xlim(0,2000);ax.set_ylim(0,10)
    else: ax.scatter((x-x.min())/(x.max()-x.min()),(y-y.min())/(y.max()-y.min()),color=BRAND['teal'],s=20,alpha=0.6);ax.set_title('After Min-Max Scaling');ax.set_xlim(0,1);ax.set_ylim(0,1)
    ax.set_aspect('equal')
fig.suptitle('W19 · Scaling Effect on Data Distribution',fontsize=13,fontweight='bold',color=BRAND['indigo'])
files.append(save(fig,'w19_before_after_scaling.png'))

# w19_scaling_comparison
fig,ax=plt.subplots(figsize=(10,4))
np.random.seed(42)
data=np.random.beta(2,5,1000)*100
ax.hist(data,bins=30,color=BRAND['gray'],alpha=0.3,edgecolor='white',label='Original')
ax.hist((data-data.min())/(data.max()-data.min()),bins=30,color=BRAND['indigo'],alpha=0.5,edgecolor='white',label='Min-Max [0,1]')
ax.hist((data-np.mean(data))/np.std(data),bins=30,color=BRAND['teal'],alpha=0.5,edgecolor='white',label='Z-Score (μ=0, σ=1)')
ax.set_title('W19 · Scaling Method Comparison',fontsize=13,fontweight='bold')
ax.set_xlabel('Value');ax.set_ylabel('Frequency');ax.legend()
files.append(save(fig,'w19_scaling_comparison.png'))

# w19_scaling_knn
fig,axes=plt.subplots(1,2,figsize=(10,5))
np.random.seed(42)
x=np.random.randn(50)*100;y=np.random.randn(50)*2;cls=(x+y)>50
for i,ax in enumerate(axes):
    if i==0: ax.scatter(x[cls],y[cls],color=BRAND['indigo'],s=30);ax.scatter(x[~cls],y[~cls],color=BRAND['teal'],s=30);ax.set_title('Unscaled: x dominates distance');ax.set_xlim(-300,300);ax.set_ylim(-5,5)
    else: ax.scatter((x-x.min())/(x.max()-x.min())[cls],y[cls],color=BRAND['indigo'],s=30);ax.scatter((x-x.min())/(x.max()-x.min())[~cls],y[~cls],color=BRAND['teal'],s=30);ax.set_title('Scaled: both contribute');ax.set_xlim(0,1);ax.set_ylim(-5,5)
    ax.set_aspect('equal')
fig.suptitle('W19 · Scaling Effect on k-NN',fontsize=13,fontweight='bold',color=BRAND['indigo'])
files.append(save(fig,'w19_scaling_knn.png'))

# ===== W20: PCA/LDA (5 figures) =====
# w20_pca_projection
fig,ax=plt.subplots(figsize=(7,7))
np.random.seed(42)
x=np.random.randn(100)*2;y=0.5*x+np.random.randn(100)*0.5
ax.scatter(x,y,color=BRAND['indigo'],s=20,alpha=0.5)
ax.plot([-3,3],[-1.5,1.5],color=BRAND['teal'],lw=2.5,label='PC1')
ax.plot([-1.5,1.5],[3,-3],color=BRAND['teal'],lw=1.5,ls='--',label='PC2')
for i in range(0,100,10):
    proj=x[i]*0.8+y[i]*0.4
    ax.plot([x[i],proj*0.8],[y[i],proj*0.4],color=BRAND['gray'],lw=0.5,alpha=0.5)
ax.set_xlim(-3,3);ax.set_ylim(-3,3);ax.set_aspect('equal')
ax.set_title('W20 · PCA: Projection onto Principal Components',fontsize=13,fontweight='bold')
ax.legend()
files.append(save(fig,'w20_pca_projection.png'))

# w20_scree_plot
fig,ax=plt.subplots(figsize=(8,5))
variance=[45,25,15,8,5,2]
ax.bar(range(1,7),variance,color=BRAND['indigo'],alpha=0.7,edgecolor='white')
ax.plot(range(1,7),np.cumsum(variance),color=BRAND['teal'],lw=2.5,marker='o')
ax.axhline(95,color=BRAND['rose'],lw=2,ls='--',label='95% threshold')
ax.axvline(3.5,color=BRAND['amber'],lw=2,ls='--',label='Elbow')
ax.set_xticks(range(1,7));ax.set_xticklabels(['PC1','PC2','PC3','PC4','PC5','PC6'])
ax.set_title('W20 · Scree Plot: Explained Variance',fontsize=13,fontweight='bold')
ax.set_ylabel('Variance Explained (%)');ax.legend()
files.append(save(fig,'w20_scree_plot.png'))

# w20_pca_vs_lda
fig,axes=plt.subplots(1,2,figsize=(10,5))
np.random.seed(42)
for i,ax in enumerate(axes):
    x1=np.random.randn(30)+1;y1=np.random.randn(30)+1
    x2=np.random.randn(30)+3;y2=np.random.randn(30)+3
    ax.scatter(x1,y1,color=BRAND['indigo'],s=30,alpha=0.6)
    ax.scatter(x2,y2,color=BRAND['teal'],s=30,alpha=0.6)
    if i==0: ax.set_title('PCA: Maximize Variance');ax.plot([0,4],[4,0],color=BRAND['amber'],lw=2,ls='--')
    else: ax.set_title('LDA: Maximize Class Separation');ax.plot([2,2],[0,4],color=BRAND['amber'],lw=2,ls='--')
    ax.set_xlim(0,4);ax.set_ylim(0,4);ax.set_aspect('equal')
fig.suptitle('W20 · PCA vs LDA Projection',fontsize=13,fontweight='bold',color=BRAND['indigo'])
files.append(save(fig,'w20_pca_vs_lda.png'))

# w20_reconstruction
fig,axes=plt.subplots(1,3,figsize=(12,4))
np.random.seed(42)
img=np.random.rand(20,20)
for i,ax in enumerate(axes):
    if i==0: ax.imshow(img,cmap='gray');ax.set_title('Original');ax.axis('off')
    elif i==1: ax.imshow(img*0.5+0.25,cmap='gray');ax.set_title('k=5 (lossy)');ax.axis('off')
    else: ax.imshow(img*0.9+0.05,cmap='gray');ax.set_title('k=20 (near-perfect)');ax.axis('off')
fig.suptitle('W20 · PCA Image Reconstruction',fontsize=13,fontweight='bold',color=BRAND['indigo'])
files.append(save(fig,'w20_reconstruction.png'))

# w20_eigenfaces
fig,axes=plt.subplots(3,3,figsize=(9,9))
for i in range(3):
    for j in range(3):
        np.random.seed(i*3+j)
        face=np.sin(np.linspace(0,4*np.pi,20)).reshape(20,1)*np.cos(np.linspace(0,3*np.pi,20)).reshape(1,20)
        axes[i,j].imshow(face,cmap='gray')
        axes[i,j].axis('off')
fig.suptitle('W20 · Synthetic Eigenfaces',fontsize=13,fontweight='bold',color=BRAND['indigo'])
files.append(save(fig,'w20_eigenfaces.png'))

# ===== W21: Decision Trees (5 figures) =====
# w21_tree_growth
fig,axes=plt.subplots(1,4,figsize=(14,3.5))
np.random.seed(42)
x=np.random.rand(100);y=np.random.rand(100);cls=(x>0.5)^(y>0.5)
for i,ax in enumerate(axes):
    ax.scatter(x[cls],y[cls],color=BRAND['indigo'],s=15,alpha=0.6)
    ax.scatter(x[~cls],y[~cls],color=BRAND['teal'],s=15,alpha=0.6)
    if i>=0: ax.axvline(0.5,color=BRAND['rose'],lw=1.5)
    if i>=1: ax.axhline(0.5,color=BRAND['rose'],lw=1.5)
    if i>=2: ax.axvline(0.75,color=BRAND['amber'],lw=1,ls='--')
    if i>=3: ax.axhline(0.25,color=BRAND['amber'],lw=1,ls='--')
    ax.set_xlim(0,1);ax.set_ylim(0,1);ax.set_aspect('equal')
    ax.set_title(f'Split {i+1}')
fig.suptitle('W21 · Decision Tree Recursive Splitting',fontsize=13,fontweight='bold',color=BRAND['indigo'])
files.append(save(fig,'w21_tree_growth.png'))

# w21_impurity
fig,axes=plt.subplots(1,2,figsize=(10,4))
for i,ax in enumerate(axes):
    if i==0: sizes=[1.0,0];colors=[BRAND['indigo'],BRAND['teal']];ax.set_title('Pure (Gini = 0.0)')
    else: sizes=[0.5,0.5];colors=[BRAND['indigo'],BRAND['teal']];ax.set_title('Mixed (Gini = 0.5)')
    ax.pie(sizes,colors=colors,autopct='%1.0f%%',startangle=90)
fig.suptitle('W21 · Node Impurity Comparison',fontsize=13,fontweight='bold',color=BRAND['indigo'])
files.append(save(fig,'w21_impurity.png'))

# w21_feature_importance
fig,ax=plt.subplots(figsize=(8,4))
features=['Age','Income','Credit','Employed','Home','Debt']
importance=[0.35,0.25,0.20,0.10,0.06,0.04]
ax.barh(range(len(features)),importance,color=BRAND['indigo'],alpha=0.7,edgecolor='white')
ax.set_yticks(range(len(features)));ax.set_yticklabels(features)
ax.set_title('W21 · Feature Importance (Gini Reduction)',fontsize=13,fontweight='bold')
ax.set_xlabel('Importance')
files.append(save(fig,'w21_feature_importance.png'))

# w21_deep_vs_pruned
fig,axes=plt.subplots(1,2,figsize=(10,5))
np.random.seed(42)
x=np.random.rand(100);y=np.random.rand(100);cls=(x>0.5)^(y>0.5)
for i,ax in enumerate(axes):
    ax.scatter(x[cls],y[cls],color=BRAND['indigo'],s=15,alpha=0.6)
    ax.scatter(x[~cls],y[~cls],color=BRAND['teal'],s=15,alpha=0.6)
    if i==0: 
        for xi in np.linspace(0,1,8): ax.axvline(xi,color=BRAND['rose'],lw=0.8,alpha=0.5)
        for yi in np.linspace(0,1,8): ax.axhline(yi,color=BRAND['rose'],lw=0.8,alpha=0.5)
        ax.set_title('Deep Tree (Overfit)')
    else: 
        ax.axvline(0.5,color=BRAND['teal'],lw=2);ax.axhline(0.5,color=BRAND['teal'],lw=2)
        ax.set_title('Pruned Tree (Generalizes)')
    ax.set_xlim(0,1);ax.set_ylim(0,1);ax.set_aspect('equal')
fig.suptitle('W21 · Deep vs Pruned Decision Tree',fontsize=13,fontweight='bold',color=BRAND['indigo'])
files.append(save(fig,'w21_deep_vs_pruned.png'))

# w21_tree_vs_linear
fig,axes=plt.subplots(1,2,figsize=(10,5))
np.random.seed(42)
x=np.random.rand(100);y=np.random.rand(100);cls=(x+y)>1
for i,ax in enumerate(axes):
    ax.scatter(x[cls],y[cls],color=BRAND['indigo'],s=15,alpha=0.6)
    ax.scatter(x[~cls],y[~cls],color=BRAND['teal'],s=15,alpha=0.6)
    if i==0: 
        ax.axvline(0.5,color=BRAND['rose'],lw=2);ax.axhline(0.5,color=BRAND['rose'],lw=2)
        ax.set_title('Tree: Axis-Aligned')
    else: 
        ax.plot([0,1],[1,0],color=BRAND['indigo'],lw=2.5)
        ax.set_title('Linear: Diagonal')
    ax.set_xlim(0,1);ax.set_ylim(0,1);ax.set_aspect('equal')
fig.suptitle('W21 · Tree vs Linear Decision Boundary',fontsize=13,fontweight='bold',color=BRAND['indigo'])
files.append(save(fig,'w21_tree_vs_linear.png'))

# ===== W22: Ensemble (5 figures) =====
# w22_random_forest
fig,ax=plt.subplots(figsize=(7,7))
np.random.seed(42)
x=np.random.rand(100);y=np.random.rand(100);cls=(x+y)>1
ax.scatter(x[cls],y[cls],color=BRAND['indigo'],s=20,alpha=0.6)
ax.scatter(x[~cls],y[~cls],color=BRAND['teal'],s=20,alpha=0.6)
# Three tree boundaries (transparent)
for offset in [-0.05,0,0.05]:
    ax.plot([0,1],[1+offset,0+offset],color=BRAND['amber'],lw=1,alpha=0.3)
ax.plot([0,1],[1,0],color=BRAND['indigo'],lw=3,label='Ensemble average')
ax.set_xlim(0,1);ax.set_ylim(0,1);ax.set_aspect('equal')
ax.set_title('W22 · Random Forest: Averaging Tree Boundaries',fontsize=13,fontweight='bold')
ax.legend()
files.append(save(fig,'w22_random_forest.png'))

# w22_bagging_vs_boosting
fig,ax=plt.subplots(figsize=(10,5))
ax.set_xlim(0,10);ax.set_ylim(0,5);ax.axis('off')
# Bagging
ax.text(2.5,4.5,'Bagging',ha='center',fontsize=13,fontweight='bold',color=BRAND['indigo'])
for i in range(3):
    rect=FancyBboxPatch((1.2+i*0.8,2.5),0.6,1,boxstyle='round,pad=0.05',facecolor=BRAND['light_indigo'],edgecolor=BRAND['indigo'],lw=1.5)
    ax.add_patch(rect);ax.text(1.5+i*0.8,3,'T'+str(i+1),ha='center',fontsize=9,color=BRAND['indigo'])
ax.text(2.5,1.5,'Parallel, independent',ha='center',fontsize=9,color=BRAND['gray'])
# Boosting
ax.text(7.5,4.5,'Boosting',ha='center',fontsize=13,fontweight='bold',color=BRAND['teal'])
for i in range(3):
    rect=FancyBboxPatch((6.2+i*0.8,2.5),0.6,1,boxstyle='round,pad=0.05',facecolor=BRAND['light_teal'],edgecolor=BRAND['teal'],lw=1.5)
    ax.add_patch(rect);ax.text(6.5+i*0.8,3,'T'+str(i+1),ha='center',fontsize=9,color=BRAND['teal'])
    if i<2: ax.annotate('',xy=(6.2+(i+1)*0.8,3),xytext=(6.2+i*0.8+0.6,3),arrowprops=dict(arrowstyle='->',color=BRAND['teal'],lw=1.5))
ax.text(7.5,1.5,'Sequential, weighted',ha='center',fontsize=9,color=BRAND['gray'])
ax.set_title('W22 · Bagging vs Boosting',fontsize=13,fontweight='bold')
files.append(save(fig,'w22_bagging_vs_boosting.png'))

# w22_adaboost
fig,ax=plt.subplots(figsize=(8,5))
np.random.seed(42)
x=np.random.rand(30);y=np.random.rand(30);cls=(x+y)>1
for i in range(3):
    ax.scatter(x[cls],y[cls],color=BRAND['indigo'],s=20+10*i,alpha=0.6)
    ax.scatter(x[~cls],y[~cls],color=BRAND['teal'],s=20+10*i,alpha=0.6)
ax.set_title('W22 · AdaBoost: Misclassified Points Grow Larger',fontsize=13,fontweight='bold')
ax.set_xlim(0,1);ax.set_ylim(0,1);ax.set_aspect('equal')
files.append(save(fig,'w22_adaboost.png'))

# w22_feature_importance
fig,ax=plt.subplots(figsize=(8,4))
features=['feat1','feat2','feat3','feat4','feat5']
single=[0.1,0.5,0.05,0.2,0.15]
ensemble=[0.2,0.22,0.18,0.21,0.19]
x=np.arange(len(features))
ax.bar(x-0.2,single,0.35,color=BRAND['rose'],alpha=0.7,label='Single Tree',edgecolor='white')
ax.bar(x+0.2,ensemble,0.35,color=BRAND['indigo'],alpha=0.7,label='Ensemble',edgecolor='white')
ax.set_xticks(x);ax.set_xticklabels(features)
ax.set_title('W22 · Feature Importance: Single vs Ensemble',fontsize=13,fontweight='bold')
ax.legend()
files.append(save(fig,'w22_feature_importance.png'))

# w22_oob_error
fig,ax=plt.subplots(figsize=(8,5))
trees=np.arange(1,101)
err=0.35*np.exp(-trees/20)+0.05
ax.plot(trees,err,color=BRAND['indigo'],lw=2.5)
ax.axhline(0.05,color=BRAND['rose'],lw=2,ls='--',label='Asymptote')
ax.fill_between(trees,err,0.05,alpha=0.1,color=BRAND['indigo'])
ax.set_title('W22 · OOB Error vs Number of Trees',fontsize=13,fontweight='bold')
ax.set_xlabel('Number of Trees');ax.set_ylabel('OOB Error');ax.legend()
files.append(save(fig,'w22_oob_error.png'))

# ===== W23: Clustering (5 figures) =====
# w23_kmeans_convergence
fig,axes=plt.subplots(1,4,figsize=(14,3.5))
np.random.seed(42)
pts=np.random.rand(60,2)
for i,ax in enumerate(axes):
    ax.scatter(pts[:,0],pts[:,1],color=BRAND['indigo'],s=15,alpha=0.6)
    if i==0: cx=np.random.rand(3,2);ax.set_title('1. Random Centroids')
    elif i==1: cx=np.array([[0.3,0.3],[0.5,0.7],[0.8,0.4]]);ax.set_title('2. Assign to Nearest')
    elif i==2: cx=np.array([[0.35,0.35],[0.55,0.65],[0.75,0.45]]);ax.set_title('3. Update Centroids')
    else: cx=np.array([[0.33,0.33],[0.52,0.62],[0.72,0.42]]);ax.set_title('4. Converged')
    for j in range(3):
        ax.scatter(cx[j,0],cx[j,1],color=BRAND['rose'],s=100,marker='X',zorder=5)
        if i>=1: c=Circle(cx[j],0.15,fill=False,edgecolor=BRAND['teal'],lw=1.5,alpha=0.5);ax.add_patch(c)
    ax.set_xlim(0,1);ax.set_ylim(0,1);ax.set_aspect('equal')
fig.suptitle('W23 · K-Means Convergence Steps',fontsize=13,fontweight='bold',color=BRAND['indigo'])
files.append(save(fig,'w23_kmeans_convergence.png'))

# w23_initialization
fig,axes=plt.subplots(1,3,figsize=(12,4))
np.random.seed(42)
pts=np.random.rand(60,2)
for i,ax in enumerate(axes):
    ax.scatter(pts[:,0],pts[:,1],color=BRAND['indigo'],s=15,alpha=0.6)
    np.random.seed(i+10)
    cx=np.random.rand(3,2)
    for j in range(3): ax.scatter(cx[j,0],cx[j,1],color=BRAND['rose'],s=100,marker='X',zorder=5)
    ax.set_xlim(0,1);ax.set_ylim(0,1);ax.set_aspect('equal')
    ax.set_title(f'Init {i+1}')
fig.suptitle('W23 · K-Means Initialization Sensitivity',fontsize=13,fontweight='bold',color=BRAND['indigo'])
files.append(save(fig,'w23_initialization.png'))

# w23_elbow
fig,ax=plt.subplots(figsize=(8,5))
k=range(1,11)
wcss=[500,350,220,180,160,150,145,142,140,138]
ax.plot(k,wcss,color=BRAND['indigo'],lw=2.5,marker='o')
ax.axvline(3,color=BRAND['amber'],lw=2,ls='--',label='Elbow at k=3')
ax.annotate('Elbow',xy=(3,220),xytext=(4,300),arrowprops=dict(arrowstyle='->',color=BRAND['amber']),fontsize=11,color=BRAND['amber'],fontweight='bold')
ax.set_title('W23 · Elbow Method for Optimal k',fontsize=13,fontweight='bold')
ax.set_xlabel('Number of Clusters (k)');ax.set_ylabel('WCSS');ax.legend()
files.append(save(fig,'w23_elbow.png'))

# w23_dendrogram
fig,ax=plt.subplots(figsize=(10,5))
# Simple dendrogram structure
levels=[(0,0.1,1),(2,0.15,1),(1,0.2,2),(4,0.08,1),(5,0.12,1),(3,0.18,2),(6,0.25,2),(7,0.35,4)]
for left,height,merge in levels:
    ax.plot([left,left],[0,height],color=BRAND['indigo'],lw=2)
ax.set_xlim(-0.5,7.5);ax.set_ylim(0,0.4)
ax.set_xticks(range(8));ax.set_xticklabels(['A','B','C','D','E','F','G','H'])
ax.set_title('W23 · Hierarchical Dendrogram',fontsize=13,fontweight='bold')
ax.set_ylabel('Distance')
files.append(save(fig,'w23_dendrogram.png'))

# w23_clustering_comparison
fig,axes=plt.subplots(1,3,figsize=(12,4))
np.random.seed(42)
pts=np.random.rand(60,2)
for i,ax in enumerate(axes):
    ax.scatter(pts[:,0],pts[:,1],color=BRAND['indigo'],s=15,alpha=0.6)
    if i==0: ax.set_title('K-Means (Spherical)')
    elif i==1: ax.set_title('DBSCAN (Arbitrary)')
    else: ax.set_title('GMM (Soft)')
    ax.set_xlim(0,1);ax.set_ylim(0,1);ax.set_aspect('equal')
fig.suptitle('W23 · Clustering Algorithm Comparison',fontsize=13,fontweight='bold',color=BRAND['indigo'])
files.append(save(fig,'w23_clustering_comparison.png'))

print(f'\nW17-W23 done: {len(files)} files generated')
