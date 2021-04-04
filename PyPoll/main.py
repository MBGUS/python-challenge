# First import the os module & csv reader
import os
import csv

# Then the function to read the csv file
pyPoll_csv = os.path.join('..', 'Resources', 'election_data.csv')

# Declare all the variables with their initial value
total_votes = 0
candidates_list = []
votes = {}
votes_pct = {}
winner_votes = 0
winner = ""

# Read the using CSV module
with open(pyPoll_csv, newline='', encoding='utf-8') as pyPoll_file:

    # CSV reader specifies delimiter "," and variable that holds contents
    pyPoll_reader = csv.reader(pyPoll_file, delimiter=',')

    # Read the header row and skip.
    pyPoll_header = next(pyPoll_reader)

    # Iteration for each row to make the calculations of total votes, list of candidates and count of votes
    for row in pyPoll_reader:
        total_votes += 1                        # This is the abreviation of (total = total + 1)
        candidate = row[2]                      # I declare the variable candidate in column 2 (0,1,2) for each iteration

        if candidate not in candidates_list:
            candidates_list.append(candidate)   # This append is to save a list of the candidates, the iteration loop finds them each by each line. Result = ['Khan', 'Correy', 'Li', "O'Tooley"]
            votes[candidate] = 1                # Setting the first iteration with value 1, which is the first data found and then it saves in the dictionary. Result = {'Khan': 30, 'Correy': 13, 'Li': 3, "O'Tooley": 1}
                                                # The value '1' corresponds to the votes of the second column of the dictionary.
        else:
            votes[candidate] += 1               # The iteration starts counting row by row after finding the firs value (if) and adding the value in the second column of the dictionary. Resutl = {'Khan': 1676, 'Correy': 534, 'Li': 369, "O'Tooley": 78} 
            
    # Iteration for each row to make the calculations of percentage
    for candidate,votes_count in votes.items():       
        votes_pct[candidate] = '{0:.0%}'.format(votes_count / total_votes) # Takes from the dictionary the total of vote values from column 1 (0,1). Result = {'Khan': '63%', 'Correy': '20%', 'Li': '14%', "O'Tooley": '3%'}
         
        if votes_count > winner_votes:
            winner_votes = votes_count          # Goes row by row and gets the max number which compares line by line and go back with the biggest number of votes. Result = 2218230 
            winner = candidate                  # Returns the name of the candidate with more votes. Result = Khan

# Print results
print(f'\nElection Results\n')
print(f'-------------------------\n')
print(f'Total Votes: {total_votes}\n')
print(f'-------------------------\n')
for candidate,votes_count in votes.items():  
    print(f'{candidate}: {votes_pct[candidate]} ({votes_count})\n')
print(f'-------------------------\n')
print(f'Winner: {winner}\n')

# Export the reuslts to a text file
output_file = os.path.join('Analysis','analysis_pypoll.txt')

with open(output_file,'w') as txt_file:
    txt_file.write(f'\nElection Results\n')
    txt_file.write(f'-------------------------\n')
    txt_file.write(f'Total Votes: {total_votes}\n')
    txt_file.write(f'-------------------------\n')
    for candidate,votes_count in votes.items():
        txt_file.write(f'{candidate}: {votes_pct[candidate]} ({votes_count})\n')
    txt_file.write(f'-------------------------\n')
    txt_file.write(f'Winner: {winner}\n')
        

