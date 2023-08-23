import pandas as pd


df_metadata = pd.read_csv("../data/clean_data/UK/splitdata/filter_metadata/2022_2024_metadata.csv")
df_topics = pd.read_csv("../data/clean_data/UK/splitdata/filter/2022_2024_titles-abstracts-tokenized.csv", header=None)


df_topics.columns = ["Topic"]
df_merged = pd.merge(df_metadata, df_topics, left_index=True, right_index=True)



df_merged["FundingAmount"] = df_merged["FundingAmount"].astype(str)
df_merged["FundingAmount"] = df_merged["FundingAmount"].str.replace("[^\d.]", "", regex=True)
df_merged["FundingAmount"] = pd.to_numeric(df_merged["FundingAmount"], errors="coerce")


df_topic_funding = df_merged.groupby("Topic")["FundingAmount"].sum().reset_index()
df_topic_funding.to_csv("../results/fine_scale/split_mallet_models/2022-2024/50-topic-files/topic_amount.csv", index=False, header=False)
