import csv

def analyze_election(file_path):
    total_votes = 0
    candidate_votes = {}

    # Read the CSV file
    with open(file_path, mode='r', newline='') as csvfile:
        csvreader = csv.DictReader(csvfile)

        # Process each row in election_data.csv
        for row in csvreader:
            total_votes += 1
            candidate_var = row['Candidate']

            if candidate_var in candidate_votes:
                candidate_votes[candidate_var] += 1
            else:
                candidate_votes[candidate_var] = 1

    # Calculate percentages and determine the winner
    winner = None
    max_votes = 0
    candidate_percentages = {}

    for candidate_var, votes in candidate_votes.items():
        percentage = (votes / total_votes) * 100
        candidate_percentages[candidate_var] = percentage
        if votes > max_votes:
            max_votes = votes
            winner = candidate_var

    # Prepare the results
    output = (
        "Election Results\n"
        "-------------------------\n"
        f"Total Votes: {total_votes}\n"
        "-------------------------\n"
    )
    for candidate_var in candidate_votes:
        output += f"{candidate_var}: {candidate_percentages[candidate_var]:.3f}% ({candidate_votes[candidate_var]})\n"
    output += (
        "-------------------------\n"
        f"Winner: {winner}\n"
        "-------------------------\n"
    )

    # Print the results to the terminal
    print(output)

    # Write the results to a text file
    output_file_path = 'election_results.txt'
    with open(output_file_path, mode='w') as output_file:
        output_file.write(output)


# Path to your election_data.csv file
file_path = "C:\\Users\\HP\\OneDrive\\Documents\\Data bootcamp\\Homework\\Python-challenge_Assignment3\\Starter_Code (2)\\Starter_Code\\PyPoll\\Resources\\election_data.csv"

# Analyze the election data
analyze_election(file_path)
