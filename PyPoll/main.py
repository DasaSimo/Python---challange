#The total number of months
import os
import csv

votes_count  = 0
candidates = []
cand_votes = []

# Set path for file
csvpath = os.path.join("Resources", "election_data.csv")

# Read the csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

 #Skip the header
    next(csvreader, None)


    for row in csvreader:
         # The total number of votes cast
        votes_count += 1
        name = row[2]
        # Finding candidates with corresponding numbers of votes (in two lists):
        if name in candidates:
            position = candidates.index(name)
            cand_votes[position] += 1
        else:
            candidates.append(name)
            cand_votes.append(1) 
   

#  finding the winner of the election based on popular vote - maximum count of votes
max_count = max(cand_votes)
position = cand_votes.index(max_count)



# printing final statement 
print("Election Results")
print("-------------------------")
print(f"Total Votes:  {votes_count}")   
print("-------------------------")

print(f"Complete list of candidates:")
# The percentage of votes each candidate won
for i in range(len(candidates)):
        print(f"{candidates[i]}: {round(cand_votes[i]/votes_count *100 ,2)}%    ({cand_votes[i]} votes)")

#The winner of the election
print("-------------------------")
print(f"Winner: {candidates[position]}") 
print("-------------------------")

# Opening the new file and writing text
with open("Election Results.txt", 'w' ) as textfile:
        print("Election Results", file = textfile)
        print("----------------------------", file = textfile)
        print(f"Total Votes:  {votes_count}", file = textfile)   
        print("-------------------------", file = textfile)

        print(f"Complete list of candidates:", file = textfile)
    # The percentage of votes each candidate won
        for i in range(len(candidates)):
            print(f"{candidates[i]}: {round(cand_votes[i]/votes_count *100 ,2)}%    ({cand_votes[i]} votes)", file = textfile)

    #The winner of the election
        print("-------------------------", file = textfile)
        print(f"Winner: {candidates[position]}", file = textfile) 
        print("-------------------------", file = textfile)