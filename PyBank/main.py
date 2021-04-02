# First import the os module & csv reader
import os
import csv

# Then the function to read the csv file
pyBank_csv = os.path.join('..', 'Resources', 'budget_data.csv')

# Declare all the variables with their initial value
total_month = 0
total_pl = 0

# Read the using CSV module
with open(pyBank_csv, newline='', encoding='utf-8') as pyBank_file:

    # CSV reader specifies delimiter "," and variable that holds contents
    pyBank_reader = csv.reader(pyBank_file, delimiter=',')

    #Read the header row and skip.
    pyBank_header = next(pyBank_reader)

    #Iteration for each row to make the calculations
    for row in pyBank_file:

        total_month = len(row[0])

# Hint 1: pie_purchases[choice_index] += 1
# Hint 2: percent = round(int(row[6]) / int(row[5]), 2)

# Print the results
print("\n")
print("Financial Analysis")
print("\n------------------")
print(f'Total Month {total_month}')
