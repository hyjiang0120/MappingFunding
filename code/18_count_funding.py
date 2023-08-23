import pandas as pd
from tqdm import tqdm


file_path = "../results/fine_scale/split_mallet_models/2022-2024/50-topic-files/1-50-topics-doc.txt"
data = []
with open(file_path, 'r') as file:
    for line in file:
        data.append(line.strip().split())


columns = ['Topic_' + str(i) for i in range(1, 51)]
df = pd.DataFrame(0, index=range(len(data)), columns=columns)

# 处理数据并添加进度条
for i, row in tqdm(enumerate(data), total=len(data), desc="Processing"):
    project_number = row[1] 

    metadata_file = "../data/clean_data/UK/fine_scale/project-metadata.csv"
    metadata_df = pd.read_csv(metadata_file)
    matching_row = metadata_df[metadata_df['ProjectId'] == 'UKRI-' + project_number]
    
    if not matching_row.empty:
        funding_amount = matching_row.iloc[0, -2]  

        max_value_index = max(enumerate(row[2:], start=2), key=lambda x: float(x[1]))[0]
       
        df.at[i, columns[max_value_index - 2]] += funding_amount



result_file = "../results/fine_scale/split_mallet_models/2022-2024/50-topic-files/amount.csv"
df.to_csv(result_file, index=False)
