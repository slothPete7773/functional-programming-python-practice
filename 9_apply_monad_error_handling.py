import csv
from toolz import curry, pipe
import os
from pymonad.either import Right, Left


# Function to handle file reading
def read_csv_file(file_path):
    if os.path.isfile(file_path):
        with open(file_path, "r") as csvfile:
            return Right([row for row in csv.reader(csvfile)])
    else:
        return Left("Error: File not found")


@curry
def extract_column_currying(column_index, data):
    if len(data) > column_index:
        return Right([row[column_index] for row in data])
    else:
        return Left("Error: Unable to extract column")


@curry
def offset_data_from_row(row_index: int, data):
    if len(data) > 1:
        return Right(data[row_index:])
    else:
        return Left("Error: Unable to remove header")


@curry
def convert_to(converter, data):
    converted_data = [converter(item) if item.isdigit() else None for item in data]
    if all(x is not None for x in converted_data):
        return Right(converted_data)
    else:
        return Left("Error: Unable to convert to float")


# Function to calculate average
def calculate_average(column_values):
    if len(column_values) > 0:
        return Right(sum(column_values) / len(column_values))
    else:
        return Left("Error: Division by zero")


# Data pipeline
csv_file_path = "example.csv"
column_index = 1  # Assuming the second column (index 1) needs to be processed
content_row_index_offset = 1

extract_column = extract_column_currying(column_index)
offsetting_data = offset_data_from_row(1)
convert_to_float = convert_to(float)

avg_result = (
    read_csv_file(csv_file_path)
    .then(extract_column)
    .then(offsetting_data)
    .then(convert_to_float)
    .then(calculate_average)
)

if avg_result.is_left():
    print("Error calculating average")
print(f"The average is: {avg_result}")
