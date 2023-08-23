import csv
import os

def generate_yearly_abstracts(input_metadata_file, input_abstracts_file, output_directory):
    with open(input_metadata_file, 'r') as metadata_file:
        metadata_reader = csv.reader(metadata_file)
        next(metadata_reader)  # 跳过表头行


        metadata_project_id_index = 21  # ProjectId 
        metadata_date_index = 14  # StartDate 


        yearly_abstracts = {}

        for metadata_row in metadata_reader:
            metadata_project_id = metadata_row[metadata_project_id_index]
            metadata_date = metadata_row[metadata_date_index]

            try:
                day, month, year = map(int, metadata_date.split('/'))
            except ValueError:
                print(f"UKRI-raw-metadata.csv 文件中的日期格式无效: {metadata_date}")
                continue
            year_str = str(year)

        
            if year_str not in yearly_abstracts:
                yearly_abstracts[year_str] = []


            yearly_abstracts[year_str].append(metadata_project_id)


    with open(input_abstracts_file, 'r') as abstracts_file:
        abstracts_reader = csv.reader(abstracts_file)
        header_row = next(abstracts_reader)  


        os.makedirs(output_directory, exist_ok=True)

 
        for year, project_ids in yearly_abstracts.items():
            output_file = os.path.join(output_directory, f"{year}_abstracts.csv")

            with open(output_file, 'w', newline='') as output_file:
                writer = csv.writer(output_file)
                writer.writerow(header_row) 

                for abstracts_row in abstracts_reader:
                    abstracts_project_id = abstracts_row[1] 

                    if abstracts_project_id in project_ids:
                        writer.writerow(abstracts_row)


            abstracts_file.seek(0)
            next(abstracts_reader) 

    print("success!!!!!!!!")


input_metadata_file = '../data/raw_data/UK/UKRI/UKRI-raw-metadata.csv'
input_abstracts_file = '../data/raw_data/UK/UKRI/titles-abstracts.csv'
output_directory = '../data/clean_data/UK/splitdata'
generate_yearly_abstracts(input_metadata_file, input_abstracts_file, output_directory)
