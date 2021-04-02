# First import the os module & csv reader
import os
import csv

# Then the function to read the csv file
pyBank_csv = os.path.join('..', 'Resources', 'budget_data.csv')

# Declare all the variables with their initial value
total_month = 0
total_pl = 0
change = 0
change_list = []
previous = 0
max_num = 0
max_dt = ""
min_num = 0
min_dt = ""

# Read the using CSV module
with open(pyBank_csv, newline='', encoding='utf-8') as pyBank_file:

    # CSV reader specifies delimiter "," and variable that holds contents
    pyBank_reader = csv.reader(pyBank_file, delimiter=',')

    #Read the header row and skip.
    pyBank_header = next(pyBank_reader)

    #Iteration for each row to make the calculations
    for row in pyBank_reader:

        total_month = total_month + 1
        total_pl = total_pl + int(row[1])
        change = int(row[1]) - previous
        change_list.append(change)
        previous = int(row[1])

        if change > max_num:
            max_num = change 
            max_dt = row[0]

        if change < min_num:
            min_num = change 
            min_dt = row[0]

    average = sum(change_list[1:])/len(change_list[1:]) 

# Print the results
print("\n")
print("Financial Analysis")
print("------------------")
print(f'Total Month {total_month}')
print(f'Total P&L ${total_pl}')
print(f'Change ${round(average,2)}')
print(f'Greatest Increase in Profits: {max_dt} (${max_num})')
print(f'Greatest Decrease in Profits: {min_dt} (${min_num})')