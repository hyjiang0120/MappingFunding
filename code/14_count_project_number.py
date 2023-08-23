
result_list = [0] * 50
file_path = "../results/fine_scale/split_mallet_models/2022-2024/50-topic-files/1-50-topics-doc.txt"


with open(file_path, 'r') as file:
    next(file)  
    for line in file:

        try:
            data_row = [float(val) for val in line.strip().split('\t')[2:]]  
        except ValueError:
       
            continue
        
        max_value = max(data_row)
        max_index = data_row.index(max_value) + 1 
        

        result_list[max_index - 2] += 1  



output_file_path = "../results/fine_scale/split_mallet_models/2022-2024/50-topic-files/project_count_per_topic.csv"

with open(output_file_path, 'w') as output_file:
    for count in result_list:
        output_file.write(f"{count}\n")
