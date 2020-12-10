import os
import csv

# putting the resources
pypoll_csv = os.path.join("..", "Resources", "election_data.csv")

# putting the variables
election_candidates = []
votes_received = {}
total_votes = 0

# read the csv file
with open(pypoll_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # skipping the header
    csv_header = next(csvreader)

    # pulling the value from csv
    for row in csvreader:
        total_votes = total_votes + 1
        candidate = row[2]

        if candidate not in election_candidates:
            # if not already in the list, add the candidate name to the list
            election_candidates.append(candidate)

            # next, we want to start counting the number of votes for each candidate
            votes_received[candidate] = 0

        # add a vote for the candidate
        votes_received[candidate] += 1

print("Election Results")
print("-------------------------")
print("Total Votes: " + str(total_votes))
print("-------------------------")

# finding votes for Khan
votes = votes_received.get("Khan")
percent = ((votes / total_votes) * 100)
print(f"Khan: {percent:.3f}% ({votes})")

# finding votes for Correy
votes = votes_received.get("Correy")
percent = round((votes / total_votes) * 100, 3)
print(f"Correy: {percent:.3f}% ({votes})")

# finding votes for Li
votes = votes_received.get("Li")
percent = round((votes / total_votes) * 100, 3)
print(f"Li: {percent:.3f}% ({votes})")

# finding cotes for O'Tooley
votes = votes_received.get("O'Tooley")
percent = round((votes / total_votes) * 100, 3)
print(f"O'Tooley: {percent:.3f}% ({votes})")

# finding the maximum number of vote
max_votes = max(votes_received.values())
# print(max_votes)

# finding the person who have the max votes & store in a list
lst = [i for i in votes_received.keys() if votes_received[i] == max_votes]

print("-------------------------")
print(f"Winner: {sorted(lst)[0]}")
print("-------------------------")

# specify the file to write to
pollcount_path = os.path.join("..", "analysis", "pypoll.txt")

# open the text file and start writting
with open(pollcount_path, 'w') as txtfile:
    txtfile.write("Election Results\n")
    txtfile.write("-------------------------\n")
    txtfile.write("Total Votes: " + str(total_votes) + "\n")
    txtfile.write("-------------------------\n")
    txtfile.write("Khan: " + str(round((((votes_received.get("Khan")) / total_votes) * 100), 3)) +
                  "% " + str(votes_received.get("Khan")) + "\n")
    txtfile.write("Correy: " + str(round((((votes_received.get("Correy")) / total_votes) * 100), 3)) +
                  "% " + (str(votes_received.get("Correy"))) + "\n")
    txtfile.write("Li: " + str(round((((votes_received.get("Li")) / total_votes) * 100), 3)) +
                  "% " + str(votes_received.get("Li")) + "\n")
    txtfile.write("O'Tooley: " + str(round((((votes_received.get("O'Tooley")) / total_votes) * 100), 3)) +
                  "% " + (str(votes_received.get("O'Tooley"))) + "\n")
    txtfile.write("-------------------------\n")
    txtfile.write("Winner: " + (str(sorted(lst)[0])) + "\n")
    txtfile.write("-------------------------\n")
