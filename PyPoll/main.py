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
         #* The total number of votes cast
        votes_count += 1
        name = row[2]
        if name in candidates:
            position = candidates.index(name)
            cand_votes[position] += 1
        else:
            candidates.append(name)
            cand_votes.append(1) 







# * A complete list of candidates who received votes

#* The percentage of votes each candidate won

#  * The total number of votes each candidate won

#  * The winner of the election based on popular vote.

#* As an example, your analysis should look similar to the one below:

#  Election Results
#  -------------------------
#  Total Votes: 3521001
#  -------------------------
#  Khan: 63.000% (2218231)
#  Correy: 20.000% (704200)
#  Li: 14.000% (492940)
#  O'Tooley: 3.000% (105630)
#  -------------------------
#  Winner: Khan
#  -------------------------

#* In addition, your final script should both print the analysis to the terminal and export a text file with the results.

# printing final statement 
print("Election Results")
print("-------------------------")
print(f"Total Votes:  {votes_count}")   
print("-------------------------")
print(candidates)
print(cand_votes)
