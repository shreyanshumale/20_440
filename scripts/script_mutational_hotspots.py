import pandas as pd
import re 
import seaborn as sns
import matplotlib.pyplot as plt

f=pd.read_csv('../data/mutation-summary.tsv',sep='\t')
k=[]
for i in f['S']:
    k.append(re.findall(r'\d+', str(i)))


freq_desired_array = [int(item) for sublist in k for item in sublist]
fig=plt.figure(dpi=800)
ax=sns.distplot(freq_desired_array,hist=True)
ax.set(xlabel='Spike protein sequence',ylabel='Frequency of mutaitons',)

plt.savefig('../figures/spike_protein_mutational_hotspots.png')
