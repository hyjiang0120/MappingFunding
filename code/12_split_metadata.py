import pandas as pd

# 读取项目元数据文件
df_metadata = pd.read_csv("../data/clean_data/UK/fine_scale/project-metadata.csv")

# 将 StartDate 列转换为日期类型
df_metadata['StartDate'] = pd.to_datetime(df_metadata['StartDate'], format='%d/%m/%Y')

# 按照年份将数据分割成不同的数据框
years = [2010, 2013, 2016, 2019, 2022]
file_paths = []
for i in range(len(years)):
    
    if i < len(years) - 1:
        start_year = years[i]
        end_year = years[i+1] - 1
    else:
        start_year = 2022
        end_year = 2024
    
    filtered_df = df_metadata[(df_metadata['StartDate'].dt.year >= start_year) & (df_metadata['StartDate'].dt.year <= end_year)]
    file_path = f"../data/clean_data/UK/splitdata/filter_metadata/{start_year}_{end_year}_metadata.csv"
    filtered_df.to_csv(file_path, index=False)
    file_paths.append(file_path)

