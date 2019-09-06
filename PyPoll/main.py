#This is the main file for PyPoll
# Part I of the Python Challenge

# -----------------------------------------------------------------------------------------
#The dataset is composed of three columns: Voter ID, County, and Candidate. 
#Your task is to create a Python script that analyzes the votes and calculates each of the following:

#The total number of votes cast
# - A complete list of candidates who received votes
# - The percentage of votes each candidate won
# - The total number of votes each candidate won
# - The winner of the election based on popular vote.

# -----------------------------------------------------------------------------------------

# Import dependencies
import os
import csv

# Assign file location with the pathlib library
#csv_file_path = Path("python-challenge", "PyPoll", "election_data.csv")

csvpath = os.path.join("..", "PyPoll\Resources", "election_data.csv")

# Declare candidates/Total votes variables 
total_votes = 0 
khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0

# Openning csv file in default read mode with context manager
with open(csvpath,newline="", encoding="utf-8") as elections:

    # Storing data in csvreader variable
    csvreader = csv.reader(elections,delimiter=",") 

    # Skiping the header to make sure it iterates through the actual values
    header = next(csvreader)     

    # Iterate through each row in the csv
    for row in csvreader: 

        # Counting the unique voter ID and store in total_votes
        total_votes +=1

        # There are four candidates.
        # We have to count the times a name appears and store in a list
        # Use this values in vote % calculation in the print statements later

        if row[2] == "Khan": 
            khan_votes +=1
        elif row[2] == "Correy":
            correy_votes +=1
        elif row[2] == "Li": 
            li_votes +=1
        elif row[2] == "O'Tooley":
            otooley_votes +=1

 # To find the winner candidate:
 # make a dictionary out of the two lists we previously created

candidates = ["Khan", "Correy", "Li","O'Tooley"]
votes = [khan_votes, correy_votes,li_votes,otooley_votes]

# We zip them together the list of candidate(key) and the total votes(value)
# Return the winner using a max function of the dictionary 

dict_candidates_and_votes = dict(zip(candidates,votes))
key = max(dict_candidates_and_votes, key=dict_candidates_and_votes.get)

# Summary of the analysis
khan_pc = (khan_votes/total_votes) *100
correy_pc = (correy_votes/total_votes) * 100
li_pc = (li_votes/total_votes)* 100
otooley_pc = (otooley_votes/total_votes) * 100

# Print the summary table
print(f"Election Results")
print(f"----------------------------")

print(f"Total Votes: {total_votes}")
print(f"----------------------------")

print(f"Khan: {khan_pc:.3f}% ({khan_votes})")
print(f"Correy: {correy_pc:.3f}% ({correy_votes})")
print(f"Li: {li_pc:.3f}% ({li_votes})")
print(f"O'Tooley: {otooley_pc:.3f}% ({otooley_votes})")

print(f"----------------------------")
print(f"Winner: {key}")
print(f"----------------------------")

# Output files location
output_file = os.path.join("..", "PyPoll", "Election_Results_Summary.txt")


with open(output_file,"w") as file:

# Write methods to print to Elections_Results_Summary 
    file.write(f"Election Results")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Total Votes: {total_votes}")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Khan: {khan_pc:.3f}% ({khan_votes})")
    file.write("\n")
    file.write(f"Correy: {correy_pc:.3f}% ({correy_votes})")
    file.write("\n")
    file.write(f"Li: {li_pc:.3f}% ({li_votes})")
    file.write("\n")
    file.write(f"O'Tooley: {otooley_pc:.3f}% ({otooley_votes})")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Winner: {key}")
    file.write("\n")
    file.write(f"----------------------------")

