import csv
from toolz import curry, pipe


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
def extract_column_currying(column_index, data):
    try:
        score_column_values = [row[column_index] for row in data]
        return score_column_values
    except IndexError:
        raise IndexError(f"Error extracting column: {e}")


@curry
def offset_data_from_row(row_index: int, data):
    try:
        return data[row_index:]
    except IndexError as e:
        raise IndexError(f"Error removing header: {e}")


@curry
def convert_to(converter, data):
    try:
        converted_values = [converter(row) for row in data]
        return converted_values
    except ValueError as e:
        raise ValueError(f"Error converting to float: {e}")


# Function to calculate average
def calculate_average(column_values):
    if column_values is None or not column_values:
        return None, "Cannot calculate average due to empty or missing column"
    try:
        average = sum(column_values) / len(column_values)
        return average
    except ZeroDivisionError as e:
        raise ValueError(f"Error zero division: {e}")


# Data pipeline
csv_file_path = "example.csv"
column_index = 1  # Assuming the second column (index 1) needs to be processed
content_row_index_offset = 1

extract_column = extract_column_currying(column_index)
offsetting_data = offset_data_from_row(1)
convert_to_float = convert_to(float)

try:
    avg_result = pipe(
        read_csv_file(csv_file_path),
        extract_column,
        offsetting_data,
        convert_to_float,
        calculate_average,
    )

    if avg_result is None:
        print("Error calculating average")
    print(f"The average is: {avg_result}")
except (FileNotFoundError, ValueError, IndexError, ZeroDivisionError) as e:
    (f"Exception caught: {e}")
