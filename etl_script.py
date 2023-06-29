import csv

# Step 1: Extract data from a CSV file
def extract_data(file_path):
    data = []
    with open(file_path, 'r') as csv_file:
        reader = csv.reader(csv_file)
        header = next(reader)  # Skip the header row
        for row in reader:
            data.append(row)
    return data

# Step 2: Transform the extracted data
def transform_data(data):
    transformed_data = []
    for row in data:
        # Perform transformations on each row as needed
        transformed_row = []
        for value in row:
            transformed_value = value.upper()  # Example transformation: convert to uppercase
            transformed_row.append(transformed_value)
        transformed_data.append(transformed_row)
    return transformed_data

# Step 3: Load the transformed data to a new CSV file
def load_data(data, output_file):
    with open(output_file, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(data)

# Step 4: Define the main function to orchestrate the ETL process
def main():
    # Specify the file paths
    input_file = 'input.csv'
    output_file = 'output.csv'

    # Step 1: Extract data from the input file
    data = extract_data(input_file)

    # Step 2: Transform the extracted data
    transformed_data = transform_data(data)

    # Step 3: Load the transformed data to the output file
    load_data(transformed_data, output_file)

    print('ETL process completed successfully.')

# Step 5: Run the main function
if __name__ == '__main__':
    main()
