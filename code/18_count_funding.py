import pandas as pd
from tqdm import tqdm

# 读取文本文件
file_path = "../results/fine_scale/split_mallet_models/2022-2024/50-topic-files/1-50-topics-doc.txt"
data = []
with open(file_path, 'r') as file:
    for line in file:
        data.append(line.strip().split())

# 创建初始DataFrame
columns = ['Topic_' + str(i) for i in range(1, 51)]
df = pd.DataFrame(0, index=range(len(data)), columns=columns)

# 处理数据并添加进度条
for i, row in tqdm(enumerate(data), total=len(data), desc="Processing"):
    project_number = row[1]  # 项目序号
    # 连接项目序号前缀和文件路径，读取metadata文件
    metadata_file = "../data/clean_data/UK/fine_scale/project-metadata.csv"
    metadata_df = pd.read_csv(metadata_file)
    matching_row = metadata_df[metadata_df['ProjectId'] == 'UKRI-' + project_number]
    
    if not matching_row.empty:
        funding_amount = matching_row.iloc[0, -2]  # 获取倒数第二列的值
        # 找到值最大的列（从第三列开始）
        max_value_index = max(enumerate(row[2:], start=2), key=lambda x: float(x[1]))[0]
        # 将funding_amount添加到DataFrame的相应列
        df.at[i, columns[max_value_index - 2]] += funding_amount


# 保存结果到指定文件夹
result_file = "../results/fine_scale/split_mallet_models/2022-2024/50-topic-files/amount.csv"
df.to_csv(result_file, index=False)
