import pandas as pd

# Read the two CSV files
topic_file_path = "../results/fine_scale/split_mallet_models/2022-2024/topic.csv"
project_count_file_path = "../results/fine_scale/split_mallet_models/2022-2024/50-topic-files/project_count_per_topic.csv"

try:
    topic_df = pd.read_csv(topic_file_path)
    project_count_df = pd.read_csv(project_count_file_path)

    # Merge the two DataFrames
    merged_df = pd.concat([topic_df, project_count_df], axis=1)

    # Generate the new file name
    new_file_name = "../results/fine_scale/split_mallet_models/2022-2024/50-topic-files/topic_project_num.txt"

    # Save the merged data as a new file
    merged_df.to_csv(new_file_name, index=False, sep='\t')
    print("文件合并成功！")
except pd.errors.EmptyDataError:
    print("文件为空或文件格式错误，请检查文件内容和格式。")
except FileNotFoundError:
    print("文件不存在，请检查文件路径是否正确。")
except Exception as e:
    print("???? NO IDEA WHATS WRONG", e)
