import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


plt.rcParams["font.family"] = "Arial"

file_path = '../results/fine_scale/split_mallet_models/2019-2021/50-topic-files/result.csv'


df = pd.read_csv(file_path, delimiter='\t', header=None, names=['category', 'topic', 'count'])


df = df.groupby(['category', 'topic']).sum().reset_index()


filtered_df = df[df['category'].isin(['Applied Science', 'Natural Science'])]


pivot_table = filtered_df.pivot('category', 'topic', 'count')


plt.figure(figsize=(30, 40))
sns.heatmap(pivot_table, cmap='YlGnBu', annot=True, fmt='.0f', linewidths=0.5, cbar=True,
            annot_kws={'fontsize': 16, 'rotation': 90})  

plt.xticks(rotation=90, fontsize=40)  
plt.yticks(fontsize=25)
plt.xticks(fontsize=25)  


plt.tight_layout()


plt.xlabel('')
plt.ylabel('')


output_file_path = '../results/fine_scale/split_mallet_models/2019-2021/50-topic-files/heatmap.png'
plt.savefig(output_file_path)
