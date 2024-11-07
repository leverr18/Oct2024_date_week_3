# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = "PyPoll/Resources/election_data.csv"  # Input file path
file_to_output = "Pypoll/analysis/election_analysis.txt"  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast

# Define lists and dictionaries to track candidate names and vote counts
vote_dict = {}

# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:
        total_votes += 1
        # Track votes
        candidate = row[2]
        if candidate in vote_dict.keys():
            vote_dict[candidate] += 1
        else:
            vote_dict[candidate] = 1
# generate the output summary
print(vote_dict)
output = f"""
Election Results
-------------------------
Total Votes: {total_votes}
-------------------------
"""

winner = ""
greatest_vote = 0

#Loop through candidates
for candidate in vote_dict:
    votes = vote_dict[candidate]
    vote_percentage = round(votes / total_votes * 100, 3) # calculate the percent

    #update the winning candidate
    if votes > greatest_vote:
        winner = candidate
        greatest_vote = votes

    # Add the candidate's results to the output
    output += f"{candidate}: {vote_percentage}% ({votes})\n"

    # Add the winning candidate summary
output += f"""
-------------------------
Winner: {winner}
-------------------------
"""
print(output)

# Write the output to the text file
with open (file_to_output, "w") as txt_file:
    txt_file.write(output)