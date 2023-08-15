# 初始列表，长度为50，初始值都为0
result_list = [0] * 50

# 数据文件路径
file_path = "../results/fine_scale/split_mallet_models/2022-2024/50-topic-files/1-50-topics-doc.txt"

# 读取数据文件并跳过第一行标题
with open(file_path, 'r') as file:
    next(file)  # 跳过第一行标题
    for line in file:
        # 将一行数据拆分为多个数值，并转换为浮点数列表
        try:
            data_row = [float(val) for val in line.strip().split('\t')[2:]]  # 从第三列开始处理
        except ValueError:
            # 如果无法转换为浮点数，跳过当前行继续处理下一行
            continue
        
        # 找到该行数据中的最大值和对应的列索引
        max_value = max(data_row)
        max_index = data_row.index(max_value) + 1  # 对应的列索引加1，因为我们从第三列开始处理
        
        # 更新对应列的值加1
        result_list[max_index - 2] += 1  # 列索引减2，对应到result_list中的索引位置

# 将结果保存到文本文件
output_file_path = "../results/fine_scale/split_mallet_models/2022-2024/50-topic-files/project_count_per_topic.csv"

with open(output_file_path, 'w') as output_file:
    for count in result_list:
        output_file.write(f"{count}\n")
