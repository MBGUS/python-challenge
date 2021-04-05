# First import the os module & csv reader
import os
import csv

# Dictionary for states
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

# Then the function to read the csv file
pyBoss_csv = os.path.join('..', 'Resources', 'employee_data.csv')

# Declare all the variables with their initial value. I will work with list.
emp_id = []
emp_first_name = []
emp_last_name = []
emp_dob = []
emp_ssn = []
emp_state = []

# Read the using CSV module
with open(pyBoss_csv, newline='', encoding='utf-8') as pyBoss_file:

    # CSV reader specifies delimiter "," and variable that holds contents
    pyBoss_reader = csv.reader(pyBoss_file, delimiter=',')

    # Read the header row and skip.
    pyBoss_header = next(pyBoss_reader)

    for row in pyBoss_reader:
        emp_id += [row[0]]           # The objective is to save all the Employee ID in a list called emp_id
       
        name = row[1].split(' ')     # It separates the name and save as a list. We use funciton split and ' ' (space).Result example = ['John', 'Mathews']
        emp_first_name += [name[0]]  # It takes from name list the column 0 (firs name) and we save as new list. Restul = ['John', 'Nathan', 'Amanda',...]
        emp_last_name += [name[1]]   # It takes from name list the column 1 (last name) and we save as new list. Result = ['Mathews', 'Moore', 'Douglas',...]
       
        ssn = row[3].split('-')      # It separates the SNN and save in a list. We use funciton split and '-' (hyphen).Result example = ['465', '80', '8629'] for each line
        emp_ssn += [ssn[2]]          # It takes from snn list the column 2 (last 4 digits) and we save as new list. Result = ['9165', '7469', '6961',...]
       
        date = row[2].split('-')    # It separates the date and save in a list. We use funciton split and '-' (hyphen).Result example = [['1991', '02', '24'] for each line
        emp_dob.append(f'{date[1]}/{date[2]}/{date[0]}') # It takes from date list the columns and readjust in the other MM/DD/YYYY and we save as new list. Result = ['02/24/1991', '11/19/1978', '01/08/1990',...]

        state = us_state_abbrev[row[4]]  # It takes the states from list and replaces for the names of the dictionary. Result = ND (for each line)
        emp_state += [state]             # It takes each by each line and make a list of the states with the dictionary abbreviation. That's why define [state] - as dict. Result = ['ND', 'ME', 'ID',...]

# Generate a ZIP to save the new data adjusted
data_adjusted = zip(emp_id, emp_first_name, emp_last_name, emp_dob, emp_ssn, emp_state)

