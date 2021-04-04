# First import the os module & csv reader
import os
import csv

# Then the function to read the csv file
pyPoll_csv = os.path.join('..', 'Resources', 'election_data.csv')

# Declare all the variables with their initial value
total_votes = 0
candidates_list = []
votes = {}

# Read the using CSV module
with open(pyPoll_csv, newline='', encoding='utf-8') as pyPoll_file:

    # CSV reader specifies delimiter "," and variable that holds contents
    pyPoll_reader = csv.reader(pyPoll_file, delimiter=',')

    # Read the header row and skip.
    pyPoll_header = next(pyPoll_reader)

    # Iteration for each row to make the calculations
    for row in pyPoll_reader:
        total_votes += 1                        # This is the abreviation of (total = total + 1)
        candidate = row[2]                      # I declare the variable candidate in column 2 (0,1,2) for each iteration

        if candidate not in candidates_list:
            candidates_list.append(candidate)   # This append is to save a list of the candidates, the iteration loop finds them each by each line. Result = ['Khan', 'Correy', 'Li', "O'Tooley"]
            votes[candidate] = 0                # Setting the first iteration with value 0, before start the counting iteration and saving in a dictionary. Result = {'Khan': 0, 'Correy': 0, 'Li': 0, "O'Tooley": 0}
                                                # The value '0' corresponds to the votes of the second column of the dictionary. We set the variable before counting.
        else:
            votes[candidate] += 1               # The iteration starts counting row by row and adding the value in the second column of the dictionary. Resutl = {'Khan': 1676, 'Correy': 534, 'Li': 369, "O'Tooley": 78} 
            
