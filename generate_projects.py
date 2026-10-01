#!/usr/bin/env python3
"""Generate figures for Projects P1-P5."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Rectangle, Circle
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

# P1: Pipeline Flowchart
fig,ax=plt.subplots(figsize=(12,3))
ax.set_xlim(0,12);ax.set_ylim(0,3);ax.axis('off')
stages=[('Data',BRAND['indigo']),('EDA',BRAND['teal']),('Preprocess',BRAND['amber']),('Model',BRAND['rose']),('Evaluate',BRAND['gray']),('Feature\nImportance',BRAND['indigo']),('Deploy',BRAND['teal'])]
for i,(stage,color) in enumerate(stages):
    rect=FancyBboxPatch((i*1.6+0.2,1),1.4,1,boxstyle='round,pad=0.1',facecolor=color,alpha=0.2,edgecolor=color,lw=2)
    ax.add_patch(rect);ax.text(i*1.6+0.9,1.5,stage,ha='center',va='center',fontsize=9,fontweight='bold',color=color)
    if i<6: ax.annotate('',xy=((i+1)*1.6+0.15,1.5),xytext=(i*1.6+1.6,1.5),arrowprops=dict(arrowstyle='->',color=BRAND['gray'],lw=2))
ax.set_title('P1 · End-to-End ML Pipeline',fontsize=13,fontweight='bold')
files.append(save(fig,'p1_pipeline.png'))

# P2: Word Cloud (spam vs ham)
fig,axes=plt.subplots(1,2,figsize=(12,5))
spam_words=['FREE','WIN','URGENT','CLICK','MONEY','NOW','LIMITED','OFFER']
ham_words=['Meeting','Project','Team','Review','Update','Deadline','Schedule','Report']
for i,(words,title,color) in enumerate([(spam_words,'Spam Words',BRAND['rose']),(ham_words,'Ham Words',BRAND['teal'])]):
    ax=axes[i];ax.set_xlim(0,10);ax.set_ylim(0,10);ax.axis('off')
    for j,word in enumerate(words):
        size=18-j if i==0 else 16-j
        x,y=(j%4)*2.2+1.5,(j//4)*4+2.5
        ax.text(x,y,word,ha='center',va='center',fontsize=size,fontweight='bold',color=color,alpha=0.7+j*0.04)
    ax.set_title(title,fontweight='bold')
fig.suptitle('P2 · Spam vs Ham Word Cloud',fontsize=13,fontweight='bold',color=BRAND['indigo'])
files.append(save(fig,'p2_word_cloud.png'))

# P2: Confusion Matrix
fig,ax=plt.subplots(figsize=(6,5))
cm=[[85,10],[5,120]]
im=ax.imshow(cm,cmap='YlGnBu',vmin=0,vmax=130)
ax.set_xticks([0,1]);ax.set_yticks([0,1])
ax.set_xticklabels(['Predicted Spam','Predicted Ham']);ax.set_yticklabels(['Actual Spam','Actual Ham'])
for i in range(2):
    for j in range(2):
        ax.text(j,i,cm[i][j],ha='center',va='center',fontsize=16,fontweight='bold',color='white' if cm[i][j]>65 else 'black')
ax.text(0.5,-0.4,'TP',ha='center',fontsize=11,fontweight='bold',color=BRAND['teal'])
ax.text(1.5,-0.4,'FP',ha='center',fontsize=11,fontweight='bold',color=BRAND['rose'])
ax.text(-0.5,0,'FN',ha='center',fontsize=11,fontweight='bold',color=BRAND['rose'])
ax.text(-0.5,1,'TN',ha='center',fontsize=11,fontweight='bold',color=BRAND['teal'])
plt.colorbar(im,ax=ax,label='Count')
ax.set_title('P2 · Confusion Matrix',fontsize=13,fontweight='bold')
files.append(save(fig,'p2_confusion_matrix.png'))

# P2: ROC
fig,ax=plt.subplots(figsize=(7,7))
fpr=np.linspace(0,1,100)
tpr=1-(1-fpr)**2
ax.plot(fpr,tpr,color=BRAND['indigo'],lw=2.5,label='ROC Curve (AUC = 0.92)')
ax.fill_between(fpr,tpr,alpha=0.2,color=BRAND['indigo'])
ax.plot([0,1],[0,1],color=BRAND['gray'],lw=2,ls='--',label='Random')
ax.set_xlim(0,1);ax.set_ylim(0,1);ax.set_aspect('equal')
ax.set_title('P2 · ROC Curve for Text Classifier',fontsize=13,fontweight='bold')
ax.set_xlabel('False Positive Rate');ax.set_ylabel('True Positive Rate');ax.legend()
files.append(save(fig,'p2_roc.png'))

# P3: CNN Filters
fig,axes=plt.subplots(3,3,figsize=(9,9))
for i in range(3):
    for j in range(3):
        np.random.seed(i*3+j)
        filt=np.random.randn(5,5)*0.5
        filt=np.sin(np.linspace(0,2*np.pi,5)).reshape(5,1)*np.cos(np.linspace(0,2*np.pi,5)).reshape(1,5)
        axes[i,j].imshow(filt,cmap='RdBu_r',vmin=-1,vmax=1,interpolation='nearest')
        axes[i,j].axis('off')
fig.suptitle('P3 · CNN Filter Visualizations',fontsize=13,fontweight='bold',color=BRAND['indigo'])
files.append(save(fig,'p3_filters.png'))

# P3: Feature Maps
fig,axes=plt.subplots(1,4,figsize=(12,3))
for i,title in enumerate(['Input','Layer 1 (Edges)','Layer 2 (Textures)','Layer 3 (Shapes)']):
    np.random.seed(i)
    img=np.random.rand(10,10)*0.1+0.5 if i==0 else np.random.rand(10,10)*0.2+0.3
    if i==1: img[4:7,:]=0.8;img[:,4:7]=0.8
    if i==2: img[3:8,3:8]=0.9
    if i==3: img[2:9,2:9]=0.7;img[4:7,4:7]=0.9
    axes[i].imshow(img,cmap='gray' if i==0 else 'viridis')
    axes[i].set_title(title,fontsize=10,fontweight='bold')
    axes[i].axis('off')
fig.suptitle('P3 · Feature Maps at Each Layer',fontsize=13,fontweight='bold',color=BRAND['indigo'])
files.append(save(fig,'p3_feature_maps.png'))

# P3: Grad-CAM
fig,axes=plt.subplots(1,2,figsize=(10,4))
np.random.seed(42)
img=np.random.rand(20,20)*0.2+0.5
axes[0].imshow(img,cmap='gray');axes[0].set_title('Original Image');axes[0].axis('off')
heatmap=np.zeros((20,20))
heatmap[8:14,5:12]=0.8
axes[1].imshow(img,cmap='gray');axes[1].imshow(heatmap,cmap='YlOrRd',alpha=0.5)
axes[1].set_title('Grad-CAM Heatmap');axes[1].axis('off')
fig.suptitle('P3 · Grad-CAM Class Activation',fontsize=13,fontweight='bold',color=BRAND['indigo'])
files.append(save(fig,'p3_gradcam.png'))

# P3: Training Curves
fig,ax=plt.subplots(figsize=(8,5))
epochs=np.arange(50)
train_loss=2*np.exp(-epochs/10)+0.1
val_loss=2*np.exp(-epochs/12)+0.15+0.05*np.sin(epochs/3)
ax.plot(epochs,train_loss,color=BRAND['indigo'],lw=2.5,label='Training Loss')
ax.plot(epochs,val_loss,color=BRAND['teal'],lw=2.5,label='Validation Loss')
ax.fill_between(epochs,train_loss,val_loss,alpha=0.1,color=BRAND['rose'])
ax.set_title('P3 · Training/Validation Loss Curves',fontsize=13,fontweight='bold')
ax.set_xlabel('Epoch');ax.set_ylabel('Loss');ax.legend()
files.append(save(fig,'p3_training_curves.png'))

# P4: Attention Heatmaps
fig,axes=plt.subplots(2,3,figsize=(9,6))
for i in range(2):
    for j in range(3):
        np.random.seed(i*3+j)
        attn=np.random.rand(6,6)*0.2
        if i==0: attn+=np.eye(6)*0.6
        else: attn+=np.tril(np.ones((6,6)))*0.4
        axes[i,j].imshow(attn,cmap='YlOrRd',vmin=0,vmax=1)
        axes[i,j].axis('off')
fig.suptitle('P4 · Attention Patterns for Generated Text',fontsize=13,fontweight='bold',color=BRAND['indigo'])
files.append(save(fig,'p4_attention_heatmaps.png'))

# P4: Loss Curve
fig,ax=plt.subplots(figsize=(8,5))
epochs=np.arange(100)
loss=3*np.exp(-epochs/20)+0.1
smooth=np.convolve(loss,np.ones(5)/5,mode='same')
ax.plot(epochs,loss,color=BRAND['indigo'],alpha=0.3,lw=1)
ax.plot(epochs,smooth,color=BRAND['indigo'],lw=2.5,label='Smoothed Loss')
ax.set_title('P4 · Training Loss Over Epochs',fontsize=13,fontweight='bold')
ax.set_xlabel('Epoch');ax.set_ylabel('Loss');ax.legend()
files.append(save(fig,'p4_loss_curve.png'))

# P5: RAG Pipeline
fig,ax=plt.subplots(figsize=(12,3))
ax.set_xlim(0,12);ax.set_ylim(0,3);ax.axis('off')
stages=[('Query',BRAND['indigo']),('Embed',BRAND['teal']),('Vector\nSearch',BRAND['amber']),('Top-k\nChunks',BRAND['rose']),('Context\nWindow',BRAND['gray']),('Response',BRAND['indigo'])]
for i,(stage,color) in enumerate(stages):
    rect=FancyBboxPatch((i*1.9+0.2,1),1.6,1,boxstyle='round,pad=0.1',facecolor=color,alpha=0.2,edgecolor=color,lw=2)
    ax.add_patch(rect);ax.text(i*1.9+1.0,1.5,stage,ha='center',va='center',fontsize=9,fontweight='bold',color=color)
    if i<5: ax.annotate('',xy=((i+1)*1.9+0.15,1.5),xytext=(i*1.9+1.8,1.5),arrowprops=dict(arrowstyle='->',color=BRAND['gray'],lw=2))
ax.set_title('P5 · RAG Pipeline Architecture',fontsize=13,fontweight='bold')
files.append(save(fig,'p5_rag_pipeline.png'))

print(f'\nProjects P1-P5 done: {len(files)} files generated')
