import pandas as pd
import os
from tqdm import tqdm


def main():
    input_file = "02.1_abstract_path.txt"  # Input file path
    output_dir = "../data/clean_data/UK/fine_scale/splitdata/filter"  # Output directory path

    with open(input_file, "r") as file:
        file_paths = file.read().splitlines()  # Read file paths from the input file

    for file_path in tqdm(file_paths, desc="Processing Files"):  # Iterate over file paths with a progress bar
        file_name = os.path.splitext(os.path.basename(file_path))[0]  # Get the file name (without extension)
        output_file = os.path.join(output_dir, f"{file_name}_filter.csv")  # Output file path

        processed_text = pd.read_csv(file_path, delimiter=" ", header=None, names=["Num", "ProjectId", "Abstract", "Tokens"])
        # Read the file and specify column names as "Num", "ProjectId", "Abstract", "Tokens"

        processed_text = processed_text.drop(columns=["Num", "Tokens"])  # Drop columns "Num" and "Tokens"

        processed_text.to_csv(output_file, index=False, header=True, sep=" ")
        # Save the processed data as the output file, including the header row, separated by spaces

if __name__ == "__main__":
    main()
