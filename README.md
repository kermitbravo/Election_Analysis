# Election_Analysis

## Project Overview
A Colorado Board of Elections employee has given you the following tasks to complete the election audit of a recent local congressional election. 

1. Calculate the total number of votes cast. 
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.
6. Calculate the total number of votes received per county
7. Calculate the percentage of votes per county
8. Determine the county with the largest turnout

## Challenge Overview

The purpose of this analysis was to provide further data on top of the candidate analysis that we performed. The main objective was to accurately calculate the turnout & vote counts per County and display them along the candidate information.

## Resources
- Data Source: election_results.csv
- Software: Python 3.9.4

## Summary
The analysis of the election shows that:
- There were "369,711" votes cast in the election.
### Candidate Analysis
- The candidates were: 
  - Charles Casper Stockham 
  - Diana DeGette
  - Raymon Anthony Doane
- The Candidate results were: 
  - Charles Casper Stockham received "23.0%" of the vote and "85,213" number of votes. 
  - Diana DeGette received "73.8%" of the vote and "272,892" number of votes. 
  - Raymon Anthony Doane received "3.1%" of the vote and "11,606" number of votes. 
- The winner of the election was: 
  - Diana DeGette received "73.8%" of the vote and "272,892" number of votes. 
### County Analysis
- The Counties were: 
  - Jefferson
  - Denver
  - Arapahoe
- The County voting results were: 
  - Jefferson received "10.5%" of the vote and "38.855" number of votes. 
  - Denver received "82.8%" of the vote and "306,055" number of votes. 
  - Arapahoe received "6.7%" of the vote and "24,801" number of votes. 
- The County with the largest turnout was: 
  - Denver received "82.8%" of the vote and "306,055" number of votes. 

We can observe the output of this exercise in the image below in the terminal & the [election_results.txt](https://github.com/kermitbravo/Election_Analysis/blob/main/analysis/election_results.txt) file 

![County & Candidate.](/Resources/Terminal_Output_Challenge.png " Results of our candidate & county analysis.")

## Challenge Summary

It is clear that Denver was the county with the largest turnaround. This was all calculated by a python script using the resources provided by UT in the election_results.csv file. We were able to consume this information by using the CSV module in Python. 

By refactoring our code we were able to quickly add a county analysis by using similar logic to what we wrote for the candidate analysis. 

In the code below we can observe the similarities between the two, in this example we see how we obtained a unique list of Counties by using a similar logic to the candidate name list by leveraging the same reader object "reader". 

```python
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read the header
    header = next(reader)

    # For each row in the CSV file.
    for row in reader:

        # Add to the total vote count
        total_votes = total_votes + 1

        # Get the candidate name from each row.
        candidate_name = row[2]

        # 3: Extract the county name from each row.

        county_name = row[1]
        
        # If the candidate does not match any existing candidate add it to
        # the candidate list
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

        # 4a: Write an if statement that checks that the
        # county does not match any existing county in the county list.
        if county_name not in county_list:
            # 4b: Add the existing county to the list of counties.
            county_list.append(county_name)
            # 4c: Begin tracking the county's vote count.
            county_votes[county_name] = 0
        # 5: Add a vote to that county's vote count.
        county_votes[county_name] += 1
```
This could be leveraged to calculate the results of ANY election. We could make the code more generic to obtain the name of the "County", "State" or "Country" from the name of the file or from the header row of the file instead of "hard-coding" it into our print statements to make this more reusable as long as the file structure remains the same. 




Similarly, we were able to reuse the logic to write to a file using the same file_save path with a "write / w" option just by including the write function in two separate occasions: 

```python
# Save the results to our text file.
with open(file_to_save, "w") as txt_file:

    # Print the final vote count (to terminal)
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n"
    )
    print(election_results, end="")

    txt_file.write(election_results)

    # 6a: Write a for loop to get the county from the county dictionary.
    for county_name in county_votes:
        # 6b: Retrieve the county vote count.
        votes = county_votes.get(county_name)
        # 6c: Calculate the percentage of votes for the county.
        vote_percentage = float(votes) / float(total_votes) * 100
        # 6d: Print the county results to the terminal.
        county_results = f"{county_name}: {vote_percentage:.1f}% ({votes:,})\n"
        print(county_results)
        # 6e: Save the county votes to a text file.
        txt_file.write(county_results)
        # 6f: Write an if statement to determine the winning county and get its vote count.
        if (votes > county_largest_turnout) and (vote_percentage > winning_percentage):
            county_largest_turnout = votes
            winning_county = county_name
    # 7: Print the county with the largest turnout to the terminal.
    winning_county_summary = (
        f"-------------------------\n"
        f"Largest County Turnout: {winning_county}\n"
        f"-------------------------\n"
    )
    print(winning_county_summary)
    # 8: Save the county with the largest turnout to a text file.
    txt_file.write(winning_county_summary)

    # Save the final candidate vote count to the text file.
    for candidate_name in candidate_votes:

        # Retrieve vote count and percentage
        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n"

        # Print each candidate's voter count and percentage to the
        # terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

        # Determine winning vote count, winning percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

    # Print the winning candidate (to terminal)
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n"
    )
    print(winning_candidate_summary)

    # Save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)
```
