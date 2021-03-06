# First import the os module & csv reader
import os
import csv

# Then the function to read the csv file
pyBank_csv = os.path.join('..', 'Resources', 'budget_data.csv')

# Declare all the variables with their initial value
total_month = 0     # Declares in 0 because it's the value of the first iteration
total_pl = 0
change = 0
change_list = []    # I declare a list for saving all the changes (value i+1 - value 1)
previous = 0
max_num = 0
max_dt = ""         # As the value of dates is string, I declare as ""
min_num = 0
min_dt = ""

# Read the using CSV module
with open(pyBank_csv, newline='', encoding='utf-8') as pyBank_file:

    # CSV reader specifies delimiter "," and variable that holds contents
    pyBank_reader = csv.reader(pyBank_file, delimiter=',')

    # Read the header row and skip.
    pyBank_header = next(pyBank_reader)

    # Iteration for each row to make the calculations
    for row in pyBank_reader:

        total_month = total_month + 1           # Sum of total months, iteration will sum 1 by 1
        total_pl = total_pl + int(row[1])       # Same as up but convertig the row[1] as integer value to be able to sum
        change = int(row[1]) - previous         # Formula = Initial Value - Previous Value
        change_list.append(change)              # Save all the changes in a list
        previous = int(row[1])                  # Re-adjust the previous value for the next iteration

        if change > max_num:                    # The max_num is a variable wich finds the maximum value
            max_num = change 
            max_dt = row[0]

        if change < min_num:                    # The min_num is a variable wich finds the minimum value
            min_num = change 
            min_dt = row[0]

    average = sum(change_list[1:])/len(change_list[1:])     # Average will sum all values/total ítems
                                                            # The function [1:] helps to initiate the calculation in the value that I declare before the :

# Output results - remember ()
output = (
    f'\nFinancial Analysis\n'
    f'------------------\n'
    f'Total Month {total_month}\n'
    f'Total P&L ${total_pl}\n'
    f'Change ${round(average,2)}\n'
    f'Greatest Increase in Profits: {max_dt} (${max_num})\n'
    f'Greatest Decrease in Profits: {min_dt} (${min_num})\n'
)

# Print Output
print(output)

# Export the reuslts to a text file
output_file = os.path.join('Analysis','analysis_pybank.txt')

with open(output_file,'w') as txt_file:
    txt_file.write(output)