# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources/election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Initialize a total vote counter.
total_votes = 0
# Candidate options and candidate votes.
candidate_options = []
candidate_votes = {}

# Counties dictionary - key: county, value: votes cast
# County votes dictionary
county_votes = {}

# County with the largest turnout
largest_turnout = ""

# Turnout count for the county with the largest turnout
largest_turnout_count = 0

# Track the winning candidate, vote count, and percentage.
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # Read the header row.
    headers = next(file_reader)
    
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1
        # Get the candidate name from each row.
        candidate_name = row[2]
        # If the candidate does not match any existing candidate, add the
        # the candidate list.
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

        # County Voter Count
        # Get the county name
        county_name = row[1]

        # if the county has not be encountered thus far
        if county_name not in county_votes.keys():
            # Initialize the vote count to 0 
            county_votes[county_name] = 0

        # Increment the vote count for the county in the current row
        county_votes[county_name] += 1

# Start the construction of election_results, the string to be outputted to the terminal and saved to the analysis file

# Put the title, Election Results, and the total votes in the election_results
election_results = (
    f"\nElection Results\n"
    f"-------------------------\n"
    f"Total Votes: {total_votes:,}\n"
    f"-------------------------\n\n")

# Add the subtitle, County Votes:, to election_results
election_results = election_results + "County Votes:\n"

# Add the county names, total votes, and vote percentages to election_results 
for name, votes in county_votes.items():
    percentVotes = votes / total_votes * 100
    election_results = election_results + f"{name}: {percentVotes:.1F}% ({votes:,})\n"

    # Find the county with the largest turnout, set largest_turnout to the county name and largest_turnout_count to the turnout
    if votes > largest_turnout_count:
        largest_turnout_count = votes
        largest_turnout = name

# Add the name of the county with the largest turnout to election_results
election_results = election_results + "\n-------------------------\n"
election_results = election_results + f"Largest County Turnout: {largest_turnout}\n"
election_results = election_results +   "-------------------------\n"

# Add the names of the candidates, their vote percentage, and their vote tally to election_results
for candidate in candidate_votes:
    # Retrieve vote count and percentage.
    votes = candidate_votes[candidate]
    vote_percentage = float(votes) / float(total_votes) * 100
    election_results = election_results + f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n"

    # Determine winning vote count, winning percentage, and winning candidate.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        winning_count = votes
        winning_candidate = candidate
        winning_percentage = vote_percentage

# Create entry for winning candidate's results.
winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")

#  Add the winning candidate results to election_results
election_results = election_results + winning_candidate_summary

# Print the election_results to the terminal
print(election_results)

# Save the election_results to a text file.
with open(file_to_save, "w") as txt_file:
    txt_file.write(election_results)

