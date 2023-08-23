import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 指定合适的字体
plt.rcParams["font.family"] = "Arial"

file_path = '../results/fine_scale/split_mallet_models/2019-2021/50-topic-files/result.csv'

# 读取数据文件
df = pd.read_csv(file_path, delimiter='\t', header=None, names=['category', 'topic', 'count'])

# 合并重复数据
df = df.groupby(['category', 'topic']).sum().reset_index()

# 过滤出只包含 'Applied Science' 和 'Natural Science' 的数据
filtered_df = df[df['category'].isin(['Applied Science', 'Natural Science'])]

# 将过滤后的数据转换为透视表格形式
pivot_table = filtered_df.pivot('category', 'topic', 'count')

# 绘制热力图
plt.figure(figsize=(30, 40))
sns.heatmap(pivot_table, cmap='YlGnBu', annot=True, fmt='.0f', linewidths=0.5, cbar=True,
            annot_kws={'fontsize': 16, 'rotation': 90})  # 调整小方块上数字的字体大小和旋转角度

plt.xticks(rotation=90, fontsize=40)  # 调整x轴刻度标签旋转角度和字体大小
plt.yticks(fontsize=25)  # 调整y轴刻度标签字体大小
plt.xticks(fontsize=25)  # 调整x轴刻度标签字体大小

# 调整布局以减少周围空白
plt.tight_layout()

# 隐藏x轴和y轴的标签
plt.xlabel('')
plt.ylabel('')

# 保存热力图到指定路径
output_file_path = '../results/fine_scale/split_mallet_models/2019-2021/50-topic-files/heatmap.png'
plt.savefig(output_file_path)
