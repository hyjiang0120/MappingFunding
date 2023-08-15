import pandas as pd

# 读取之前生成的结果文件
result_file = "../results/fine_scale/split_mallet_models/2022-2024/50-topic-files/amount.csv"
df = pd.read_csv(result_file)

sum = df.sum()

# 将结果保存到新文件
sums_file = "../results/fine_scale/split_mallet_models/2022-2024/50-topic-files/column_sum.csv"
sum.to_csv(sums_file)
