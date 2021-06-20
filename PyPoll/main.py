#The total number of months
import os
import csv

votes_count  = 0

# Set path for file
csvpath = os.path.join("Resources", "election_data.csv")

# Read the csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

 #Skip the header
    next(csvreader, None)

    for row in csvreader:
        #The total number of votes
        votes_count += 1



# printing final statement 
print("Election Results")
print("-------------------------")
print(f"Total Votes:  {votes_count}")   
print("-------------------------")


#* The total number of votes cast

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

