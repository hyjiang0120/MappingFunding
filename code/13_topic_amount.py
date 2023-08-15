import pandas as pd

# 读取项目元数据文件
df_metadata = pd.read_csv("../data/clean_data/UK/splitdata/filter_metadata/2022_2024_metadata.csv")

# 读取主题数据文件（每一行是一个 topic，没有列名）
df_topics = pd.read_csv("../data/clean_data/UK/splitdata/filter/2022_2024_titles-abstracts-tokenized.csv", header=None)

# 添加列名为 "Topic"
df_topics.columns = ["Topic"]

# 合并项目元数据和主题数据
df_merged = pd.merge(df_metadata, df_topics, left_index=True, right_index=True)

# 清理 FundingAmount 列的数据格式
df_merged["FundingAmount"] = df_merged["FundingAmount"].astype(str)
df_merged["FundingAmount"] = df_merged["FundingAmount"].str.replace("[^\d.]", "", regex=True)
df_merged["FundingAmount"] = pd.to_numeric(df_merged["FundingAmount"], errors="coerce")

# 计算每个主题的总资金金额
df_topic_funding = df_merged.groupby("Topic")["FundingAmount"].sum().reset_index()

# 保存结果为单列的 CSV 文件
df_topic_funding.to_csv("../results/fine_scale/split_mallet_models/2022-2024/50-topic-files/topic_amount.csv", index=False, header=False)
