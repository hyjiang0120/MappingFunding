import csv
import os

def generate_yearly_abstracts(input_metadata_file, input_abstracts_file, output_directory):
    # 读取 UKRI-raw-metadata.csv 文件
    with open(input_metadata_file, 'r') as metadata_file:
        metadata_reader = csv.reader(metadata_file)
        next(metadata_reader)  # 跳过表头行

        # 查找 UKRI-raw-metadata.csv 文件中列的索引
        metadata_project_id_index = 21  # ProjectId 的索引
        metadata_date_index = 14  # StartDate 的索引

        # 创建一个字典，用于存储每个年份的摘要列表
        yearly_abstracts = {}

        for metadata_row in metadata_reader:
            metadata_project_id = metadata_row[metadata_project_id_index]
            metadata_date = metadata_row[metadata_date_index]

            # 解析日期
            try:
                day, month, year = map(int, metadata_date.split('/'))
            except ValueError:
                print(f"UKRI-raw-metadata.csv 文件中的日期格式无效: {metadata_date}")
                continue

            # 获取年份
            year_str = str(year)

            # 如果字典中不存在该年份，则创建一个新列表
            if year_str not in yearly_abstracts:
                yearly_abstracts[year_str] = []

            # 将对应的摘要项目添加到相应年份的列表中
            yearly_abstracts[year_str].append(metadata_project_id)

    # 读取 titles-abstracts.csv 文件
    with open(input_abstracts_file, 'r') as abstracts_file:
        abstracts_reader = csv.reader(abstracts_file)
        header_row = next(abstracts_reader)  # 读取表头行

        # 创建输出目录
        os.makedirs(output_directory, exist_ok=True)

        # 创建年份_abstracts.csv 文件并写入对应的摘要
        for year, project_ids in yearly_abstracts.items():
            output_file = os.path.join(output_directory, f"{year}_abstracts.csv")

            with open(output_file, 'w', newline='') as output_file:
                writer = csv.writer(output_file)
                writer.writerow(header_row)  # 写入表头行

                for abstracts_row in abstracts_reader:
                    abstracts_project_id = abstracts_row[1]  # titles-abstracts.csv 的 ProjectId 索引为 1

                    if abstracts_project_id in project_ids:
                        writer.writerow(abstracts_row)

            # 重新打开 titles-abstracts.csv 文件以进行下一年份的读取
            abstracts_file.seek(0)
            next(abstracts_reader)  # 跳过表头行

    print("年度摘要文件生成成功")

# 示例用法
input_metadata_file = '../data/raw_data/UK/UKRI/UKRI-raw-metadata.csv'
input_abstracts_file = '../data/raw_data/UK/UKRI/titles-abstracts.csv'
output_directory = '../data/clean_data/UK/splitdata'
generate_yearly_abstracts(input_metadata_file, input_abstracts_file, output_directory)
