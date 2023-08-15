import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 指定合适的字体
plt.rcParams["font.family"] = "Arial"

file_path = '../results/fine_scale/split_mallet_models/2022-2024/50-topic-files/result.csv'

# 读取数据文件
df = pd.read_csv(file_path, delimiter='\t', header=None, names=['category', 'topic', 'count'])

# 合并重复数据
df = df.groupby(['category', 'topic']).sum().reset_index()

# 将数据转换为透视表格形式
pivot_table = df.pivot('category', 'topic', 'count')

# 绘制热力图
plt.figure(figsize=(12, 20))
sns.heatmap(pivot_table, cmap='YlGnBu', annot=True, fmt='.0f', linewidths=0.5, cbar=True, annot_kws={'rotation': 90})
plt.title('Heatmap of Topic Counts', fontsize=18)  # 调整标题字体大小
plt.xlabel('Topic')
plt.ylabel('Category')

# 保存热力图到指定路径
output_file_path = '../results/fine_scale/split_mallet_models/2022-2024/50-topic-files/heatmap.png'
plt.savefig(output_file_path)
