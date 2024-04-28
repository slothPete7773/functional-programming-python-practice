import csv
from toolz import curry


# Function to handle file reading
def read_csv_file(file_path):
    try:
        with open(file_path, "r") as csvfile:
            reader = csv.reader(csvfile)
            data = [row for row in reader]
            return data
    except FileNotFoundError as e:
        print(e)
        return None


@curry
def extract_column_currying_std_python(column_index, data):
    try:
        score_column_values = [row[column_index] for row in data]
        return score_column_values
    except (ValueError, IndexError):
        return None


@curry
def offset_data_from_row(row_index: int, data):
    try:
        return data[row_index:]
    except IndexError as e:
        return None


@curry
def convert_to(converter, data):
    try:
        converted_values = [converter(row) for row in data]
        return converted_values
    except Exception as e:
        print(e)
        return None


# Function to calculate average
def calculate_average(column_values):
    if column_values is None or not column_values:
        return None, "Cannot calculate average due to empty or missing column"
    try:
        average = sum(column_values) / len(column_values)
        return average
    except ZeroDivisionError as e:
        return None


# Data pipeline
csv_file_path = "example.csv"
column_index = 1  # Assuming the second column (index 1) needs to be processed

# Step 1: Read CSV file
data = read_csv_file(csv_file_path)

if data == None:
    print("Error reading CSV file")
else:
    # Step 2: Extract column
    to_extract_column_from = extract_column_currying_std_python(column_index)(data=data)
    score_column_values = offset_data_from_row(1)(to_extract_column_from)
    float_score_values = convert_to(float)(score_column_values)

    if float_score_values == None:
        print("Error extracting column")
    else:
        # Step 3: Calculate average
        result = calculate_average(float_score_values)

        if result == None:
            print("Error calculating average")
        else:
            print(f"The average is: {result}")
