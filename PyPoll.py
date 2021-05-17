# Import dependencies
import os
import csv

# The data we need to retrieve.
file_to_load = os.path.join("Resources", "election_results.csv")
# election_data = open(file_to_load, "r")
with open(file_to_load) as election_data:
    # Read the file object with the reader function
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)
    print(headers)

    # for row in file_reader:
    #     print(row)

# Create a filename variable to a direct or indirect path to the file.
# file_to_save = os.path.join("analysis", "election_analysis.txt")
# # Using the open() function with the "w" mode we will write data to the file.
# with open(file_to_save, "w") as outfile:
#     outfile.write("Counties in the Election \n")
#     outfile.write("-------------------------\n")
#     outfile.write("Arapahoe\nDenver\nJefferson")
# outfile.write("Denver, ")
# outfile.write("Jefferson")
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote
# election_data.close()
