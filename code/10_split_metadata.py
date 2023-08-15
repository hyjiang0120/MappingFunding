import csv
import os

def generate_yearly_csv_files(input_file, output_directory):
    # Read the input CSV file
    with open(input_file, 'r') as file:
        reader = csv.reader(file)
        header = next(reader)  # Skip the header row

        start_date_index = 14  # Index of the "StartDate" column is 14

        # Create a dictionary to store file objects for each year
        yearly_files = {}

        for row in reader:
            start_date = row[start_date_index]

            # Parse the date
            try:
                day, month, year = map(int, start_date.split('/'))
            except ValueError:
                print(f"Invalid date format: {start_date}")
                continue

            # Get the year
            year_str = str(year)

            # If the file for the year doesn't exist, create a new file
            if year_str not in yearly_files:
                output_file = os.path.join(output_directory, f"{year_str}_metadata.csv")
                yearly_files[year_str] = open(output_file, 'w', newline='')
                writer = csv.writer(yearly_files[year_str])
                writer.writerow(header)  # Write the header row

            # Write the current row to the corresponding year file
            writer = csv.writer(yearly_files[year_str])
            writer.writerow(row)

        # Close all the yearly files
        for file in yearly_files.values():
            file.close()

        print("Yearly files generated successfully")

# Usage example
input_file = '../data/raw_data/UK/UKRI/UKRI-raw-metadata.csv'
output_directory = '../data/clean_data/UK/splitdata'
generate_yearly_csv_files(input_file, output_directory)
