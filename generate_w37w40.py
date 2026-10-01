#!/usr/bin/env python3
"""Generate figures for W37-W40: GenAI Applications, MLOps, Cloud, RL."""
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

# ===== W37: GenAI Applications (3 figures) =====
# w37_diffusion_process
fig,axes=plt.subplots(2,4,figsize=(12,6))
for i in range(4):
    np.random.seed(i)
    img=np.random.rand(10,10)*0.1+0.5
    axes[0,i].imshow(img,cmap='gray');axes[0,i].set_title(f'Step {i*3}');axes[0,i].axis('off')
    axes[1,3-i].imshow(img,cmap='gray');axes[1,3-i].set_title(f'Step {i*3}');axes[1,3-i].axis('off')
axes[0,0].set_ylabel('Forward: Add Noise',fontsize=11,fontweight='bold')
axes[1,0].set_ylabel('Reverse: Denoise',fontsize=11,fontweight='bold')
fig.suptitle('W37 · Diffusion Forward/Reverse Process',fontsize=13,fontweight='bold',color=BRAND['indigo'])
files.append(save(fig,'w37_diffusion_process.png'))

# w37_text_to_image_attention
fig,axes=plt.subplots(1,2,figsize=(10,4))
img=np.random.rand(20,20)
axes[0].imshow(img,cmap='gray');axes[0].set_title('Generated Image');axes[0].axis('off')
heatmap=np.random.rand(20,20)*0.3
heatmap[8:14,5:12]=0.8
axes[1].imshow(img,cmap='gray');axes[1].imshow(heatmap,cmap='YlOrRd',alpha=0.4);axes[1].set_title('Attention Heatmap');axes[1].axis('off')
fig.suptitle('W37 · Text-to-Image Attention Overlay',fontsize=13,fontweight='bold',color=BRAND['indigo'])
files.append(save(fig,'w37_text_to_image_attention.png'))

# w37_genai_map
fig,ax=plt.subplots(figsize=(9,9))
ax.set_xlim(0,10);ax.set_ylim(0,10);ax.axis('off')
nodes=[('Art',(5,8.5)),('Music',(2,7)),('Code',(8,7)),('Drug\nDiscovery',(2,4)),('Protein\nDesign',(5,4)),('Materials',(8,4))]
for label,pos in nodes:
    c=Circle(pos,0.8,facecolor=BRAND['light_indigo'],edgecolor=BRAND['indigo'],lw=2)
    ax.add_patch(c);ax.text(pos[0],pos[1],label,ha='center',va='center',fontsize=10,fontweight='bold',color=BRAND['indigo'])
ax.plot([5,2,5,8],[7.7,7,7,7],color=BRAND['teal'],lw=1.5,alpha=0.5)
ax.plot([5,2,5,8],[5.7,4,4,4],color=BRAND['teal'],lw=1.5,alpha=0.5)
ax.text(5,9.5,'Generative AI Applications',ha='center',fontsize=14,fontweight='bold',color=BRAND['indigo'])
ax.set_title('W37 · GenAI Application Landscape',fontsize=13,fontweight='bold')
files.append(save(fig,'w37_genai_map.png'))

# ===== W38: MLOps (4 figures) =====
# w38_ml_pipeline
fig,ax=plt.subplots(figsize=(12,3))
ax.set_xlim(0,12);ax.set_ylim(0,3);ax.axis('off')
stages=[('Data\nIngestion',BRAND['indigo']),('Preprocess',BRAND['teal']),('Training',BRAND['amber']),('Validation',BRAND['rose']),('Deployment',BRAND['gray']),('Monitoring',BRAND['indigo'])]
for i,(stage,color) in enumerate(stages):
    rect=FancyBboxPatch((i*1.9+0.1,1),1.6,1,boxstyle='round,pad=0.1',facecolor=color,alpha=0.2,edgecolor=color,lw=2)
    ax.add_patch(rect);ax.text(i*1.9+0.9,1.5,stage,ha='center',va='center',fontsize=9,fontweight='bold',color=color)
    if i<5: ax.annotate('',xy=((i+1)*1.9+0.05,1.5),xytext=(i*1.9+1.7,1.5),arrowprops=dict(arrowstyle='->',color=BRAND['gray'],lw=2))
ax.annotate('',xy=(0.9,1.0),xytext=(11.5,1.0),arrowprops=dict(arrowstyle='->',color=BRAND['teal'],lw=1.5,connectionstyle='arc3,rad=-0.3'))
ax.text(6,0.3,'Feedback Loop',ha='center',fontsize=9,color=BRAND['teal'])
ax.set_title('W38 · ML Pipeline DAG',fontsize=13,fontweight='bold')
files.append(save(fig,'w38_ml_pipeline.png'))

# w38_model_drift
fig,ax=plt.subplots(figsize=(10,5))
months=np.arange(12)
ks=0.02+0.08*np.sin(months/3)+0.03*np.random.rand(12)
ax.plot(months,ks,color=BRAND['indigo'],lw=2.5,marker='o',label='Input Drift (KS)')
ax.axhline(0.1,color=BRAND['rose'],lw=2,ls='--',label='Retraining Threshold')
ax.fill_between(months,ks,0.1,where=(ks>0.1),color=BRAND['rose'],alpha=0.2)
ax.set_title('W38 · Model Drift Over Time',fontsize=13,fontweight='bold')
ax.set_xlabel('Month');ax.set_ylabel('KS Statistic');ax.legend()
files.append(save(fig,'w38_model_drift.png'))

# w38_ab_testing
fig,ax=plt.subplots(figsize=(8,5))
x=np.arange(2)
conv=[0.12,0.15]
err=[0.02,0.02]
ax.bar(x,conv,color=[BRAND['indigo'],BRAND['teal']],alpha=0.7,edgecolor='white',width=0.5)
ax.errorbar(x,conv,yerr=err,fmt='none',color=BRAND['gray'],lw=2)
ax.set_xticks(x);ax.set_xticklabels(['Model A','Model B'])
ax.set_title('W38 · A/B Testing: Conversion Comparison',fontsize=13,fontweight='bold')
ax.set_ylabel('Conversion Rate');ax.axhline(0.12,color=BRAND['gray'],lw=1,ls='--')
ax.text(0.5,0.155,'p < 0.05 *',ha='center',fontsize=11,color=BRAND['teal'],fontweight='bold')
files.append(save(fig,'w38_ab_testing.png'))

# w38_responsible_ai
fig,ax=plt.subplots(figsize=(10,3))
ax.set_xlim(0,10);ax.set_ylim(0,2);ax.axis('off')
items=['Bias\nAudit','Fairness','Explainability','Privacy','Security']
for i,item in enumerate(items):
    rect=FancyBboxPatch((i*1.9+0.2,0.5),1.6,1,boxstyle='round,pad=0.1',facecolor=BRAND['light_teal'],edgecolor=BRAND['teal'],lw=2)
    ax.add_patch(rect);ax.text(i*1.9+1.0,1.0,item,ha='center',va='center',fontsize=9,fontweight='bold',color=BRAND['teal'])
    if i<4: ax.annotate('',xy=((i+1)*1.9+0.15,1.0),xytext=(i*1.9+1.8,1.0),arrowprops=dict(arrowstyle='->',color=BRAND['teal'],lw=2))
ax.set_title('W38 · Responsible AI Checklist',fontsize=13,fontweight='bold')
files.append(save(fig,'w38_responsible_ai.png'))

# ===== W39: Cloud Deployment (4 figures) =====
# w39_container_vm
fig,axes=plt.subplots(1,2,figsize=(10,5))
for i,ax in enumerate(axes):
    ax.set_xlim(0,5);ax.set_ylim(0,5);ax.axis('off')
    if i==0:
        for j in range(3):
            rect=Rectangle((0.5+j*1.5,1),1.2,3,facecolor='#e3e6f0',edgecolor=BRAND['gray'],lw=2)
            ax.add_patch(rect);ax.text(1.1+j*1.5,2.5,'OS\nApp',ha='center',fontsize=8,color=BRAND['gray'])
        ax.set_title('VM: Full OS per app',fontweight='bold')
    else:
        rect=Rectangle((0.5,1),4,3,facecolor=BRAND['light_indigo'],edgecolor=BRAND['indigo'],lw=2)
        ax.add_patch(rect);ax.text(2.5,2.5,'Shared Kernel',ha='center',fontsize=10,color=BRAND['indigo'])
        for j in range(3):
            rect=Rectangle((0.7+j*1.3,1.2),1.0,2.6,facecolor='#fff',edgecolor=BRAND['teal'],lw=1.5)
            ax.add_patch(rect);ax.text(1.2+j*1.3,2.5,'App',ha='center',fontsize=8,color=BRAND['teal'])
        ax.set_title('Container: Shared kernel',fontweight='bold')
fig.suptitle('W39 · VM vs Container',fontsize=13,fontweight='bold',color=BRAND['indigo'])
files.append(save(fig,'w39_container_vm.png'))

# w39_serverless
fig,ax=plt.subplots(figsize=(10,4))
ax.set_xlim(0,10);ax.set_ylim(0,3);ax.axis('off')
ax.plot([0,2,4,6,8,10],[0.5,0.5,1.5,0.5,0.5,1.5],color=BRAND['indigo'],lw=2.5)
ax.fill_between([0,2,4,6,8,10],[0.5,0.5,1.5,0.5,0.5,1.5],0.5,alpha=0.2,color=BRAND['indigo'])
ax.scatter([2],[0.5],color=BRAND['rose'],s=50,zorder=5)
ax.text(2,0.2,'Cold Start',ha='center',fontsize=9,color=BRAND['rose'])
ax.text(4,1.8,'Warm Instance',ha='center',fontsize=9,color=BRAND['indigo'])
ax.text(8,0.2,'Scale to Zero',ha='center',fontsize=9,color=BRAND['gray'])
ax.set_title('W39 · Serverless Scaling Timeline',fontsize=13,fontweight='bold')
files.append(save(fig,'w39_serverless.png'))

# w39_edge
fig,ax=plt.subplots(figsize=(10,3))
ax.set_xlim(0,10);ax.set_ylim(0,2);ax.axis('off')
stages=[('Cloud\nTraining',BRAND['indigo']),('Compress\nQuantize',BRAND['teal']),('Deploy\nEdge',BRAND['amber'])]
for i,(stage,color) in enumerate(stages):
    rect=FancyBboxPatch((i*3.0+0.5,0.5),2.0,1,boxstyle='round,pad=0.1',facecolor=color,alpha=0.2,edgecolor=color,lw=2)
    ax.add_patch(rect);ax.text(i*3.0+1.5,1.0,stage,ha='center',va='center',fontsize=10,fontweight='bold',color=color)
    if i<2: ax.annotate('',xy=((i+1)*3.0+0.4,1.0),xytext=(i*3.0+2.5,1.0),arrowprops=dict(arrowstyle='->',color=BRAND['gray'],lw=2))
ax.set_title('W39 · Edge Deployment Pipeline',fontsize=13,fontweight='bold')
files.append(save(fig,'w39_edge.png'))

# w39_load_balancing
fig,ax=plt.subplots(figsize=(10,4))
ax.set_xlim(0,10);ax.set_ylim(0,3);ax.axis('off')
ax.plot([0,2,3,5,7,8,10],[0.5,0.5,1.2,2.5,2.5,0.5,0.5],color=BRAND['indigo'],lw=2.5,label='CPU Usage')
ax.plot([0,2,3,5,7,8,10],[1,1,1,2,2,1,1],color=BRAND['teal'],lw=2,ls='--',label='Pod Count')
ax.axhline(2.0,color=BRAND['rose'],lw=2,ls='--',alpha=0.5,label='Scale-up Threshold')
ax.set_title('W39 · Load Balancing: Auto-Scaling',fontsize=13,fontweight='bold')
ax.legend()
files.append(save(fig,'w39_load_balancing.png'))

# ===== W40: RL (5 figures) =====
# w40_value_iteration
fig,axes=plt.subplots(1,4,figsize=(14,3.5))
grid=np.zeros((4,4))
grid[3,3]=1.0
for i,ax in enumerate(axes):
    if i==0: vals=grid;ax.set_title('Initial: All Zero')
    elif i==1: vals=np.array([[0,0,0,0],[0,0,0,0.5],[0,0,0,0.75],[0,0,0,1.0]]);ax.set_title('Iteration 1')
    elif i==2: vals=np.array([[0,0,0,0.25],[0,0,0.25,0.5],[0,0.25,0.5,0.75],[0.25,0.5,0.75,1.0]]);ax.set_title('Iteration 5')
    else: vals=np.array([[0.06,0.09,0.14,0.2],[0.09,0.14,0.2,0.3],[0.14,0.2,0.3,0.5],[0.2,0.3,0.5,1.0]]);ax.set_title('Converged')
    ax.imshow(vals,cmap='YlOrRd',vmin=0,vmax=1)
    for r in range(4):
        for c in range(4):
            ax.text(c,r,f'{vals[r,c]:.2f}',ha='center',va='center',fontsize=8,color='white' if vals[r,c]>0.5 else 'black')
    ax.set_xticks([]);ax.set_yticks([])
fig.suptitle('W40 · Value Iteration: Grid World',fontsize=13,fontweight='bold',color=BRAND['indigo'])
files.append(save(fig,'w40_value_iteration.png'))

# w40_policy_vs_value
fig,axes=plt.subplots(1,2,figsize=(10,4))
for i,ax in enumerate(axes):
    ax.set_xlim(0,10);ax.set_ylim(0,6);ax.axis('off')
    if i==0: title='Value Iteration';color=BRAND['indigo']
    else: title='Policy Iteration';color=BRAND['teal']
    for j in range(3):
        rect=FancyBboxPatch((0.5+j*3,3.5),2.5,1,boxstyle='round,pad=0.1',facecolor=color,alpha=0.2,edgecolor=color,lw=2)
        ax.add_patch(rect);ax.text(1.75+j*3,4.0,['Evaluate','Improve','Repeat'][j],ha='center',va='center',fontsize=9,color=color)
        if j<2: ax.annotate('',xy=(0.5+(j+1)*3,4.0),xytext=(0.5+j*3+2.5,4.0),arrowprops=dict(arrowstyle='->',color=color,lw=1.5))
    ax.set_title(title,fontweight='bold')
fig.suptitle('W40 · Value Iteration vs Policy Iteration',fontsize=13,fontweight='bold',color=BRAND['indigo'])
files.append(save(fig,'w40_policy_vs_value.png'))

# w40_qlearning
fig,ax=plt.subplots(figsize=(7,7))
ax.set_xlim(0,10);ax.set_ylim(0,10);ax.axis('off')
# Maze
for wall in [(2,0),(2,1),(2,2),(5,5),(5,6),(5,7),(7,3),(7,4)]:
    rect=Rectangle((wall[0],wall[1]),1,1,facecolor='#e3e6f0',edgecolor=BRAND['gray'],lw=1)
    ax.add_patch(rect)
# Goal
c=Circle((8.5,8.5),0.4,facecolor=BRAND['amber'],edgecolor=BRAND['amber'],lw=2)
ax.add_patch(c);ax.text(8.5,8.5,'G',ha='center',va='center',fontsize=10,fontweight='bold',color='white')
# Agent
c=Circle((0.5,0.5),0.3,facecolor=BRAND['indigo'],edgecolor=BRAND['indigo'],lw=2)
ax.add_patch(c);ax.text(0.5,0.5,'A',ha='center',va='center',fontsize=9,fontweight='bold',color='white')
ax.set_title('W40 · Q-Learning: Maze Exploration',fontsize=13,fontweight='bold')
files.append(save(fig,'w40_qlearning.png'))

# w40_exploration_exploitation
fig,ax=plt.subplots(figsize=(8,5))
eps=np.linspace(0,1,50)
reward=0.8*(1-eps)+0.3*eps+0.1*np.random.rand(50)
ax.plot(eps,reward,color=BRAND['indigo'],lw=2.5)
ax.axvline(0.1,color=BRAND['teal'],lw=2,ls='--',label='ε=0.1 (optimal)')
ax.fill_between(eps,reward,0,alpha=0.1,color=BRAND['indigo'])
ax.set_title('W40 · Exploration-Exploitation Tradeoff',fontsize=13,fontweight='bold')
ax.set_xlabel('Exploration Rate (ε)');ax.set_ylabel('Cumulative Reward');ax.legend()
files.append(save(fig,'w40_exploration_exploitation.png'))

# w40_rlhf_llm
fig,ax=plt.subplots(figsize=(10,3))
ax.set_xlim(0,10);ax.set_ylim(0,2);ax.axis('off')
stages=[('Human\nRanks',BRAND['indigo']),('Reward\nModel',BRAND['teal']),('PPO',BRAND['amber']),('Policy\nUpdate',BRAND['rose'])]
for i,(stage,color) in enumerate(stages):
    rect=FancyBboxPatch((i*2.3+0.3,0.5),1.8,1,boxstyle='round,pad=0.1',facecolor=color,alpha=0.2,edgecolor=color,lw=2)
    ax.add_patch(rect);ax.text(i*2.3+1.2,1.0,stage,ha='center',va='center',fontsize=10,fontweight='bold',color=color)
    if i<3: ax.annotate('',xy=((i+1)*2.3+0.25,1.0),xytext=(i*2.3+2.1,1.0),arrowprops=dict(arrowstyle='->',color=BRAND['gray'],lw=2))
ax.set_title('W40 · RLHF for LLM Alignment',fontsize=13,fontweight='bold')
files.append(save(fig,'w40_rlhf_llm.png'))

print(f'\nW37-W40 done: {len(files)} files generated')
