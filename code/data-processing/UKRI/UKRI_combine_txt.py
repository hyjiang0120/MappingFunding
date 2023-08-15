import os
import re
import pandas as pd

directory = '/Users/jianghanyi/Documents/Project/data/raw_data/UK/UKRI'

os.chdir(directory)

data = {"ProjectId": [], "TitleAbstract": []}

files = os.listdir()
for x in files:
    if not x.startswith('.'):
        file_path = os.path.join(directory, x)  # Absolute path to the file
        # Open file
        with open(file_path, 'r') as text:
            id = str('UKRI-') + os.path.splitext(x)[0]
            content = "".join(text.readlines())

            data["ProjectId"].append(id)
            data["TitleAbstract"].append(content)

df = pd.DataFrame.from_dict(data)
output_file = os.path.join(directory, 'UKRI-raw-text.csv')  # Absolute path to the output file
df.to_csv(output_file, index=False)
