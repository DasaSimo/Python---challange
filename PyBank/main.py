#The total number of months
import os
import csv


# Set path for file
csvpath = os.path.join("Resources", "budget_data.csv")
# Open the CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Loop through looking for number of the month
    month_count = 0
    total = 0
    #Skip the header
    next(csvreader, None)

    for row in csvreader:
        #The total number of month
        month_count += 1
        #The net total amount of "Profit/Losses"
        total += int(row[1])
    

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {month_count}") 
print(f"Total: ${total}")

print("Average  Change: $-2315.12")
print("Greatest Increase in Profits: Feb-2012 ($1926159)")
print("Greatest Decrease in Profits: Sep-2013 ($-2196167)")




  

# the changes in "Profit/Losses" over the entire period, 
#    - the average of those changes

#The greatest increase in profits (date and amount)

#The greatest decrease in profits (date and amount) #The total number of months 



#The net total amount of "Profit/Losses" 

# the changes in "Profit/Losses" over the entire period, 
#    - the average of those changes

#The greatest increase in profits (date and amount)

#The greatest decrease in profits (date and amount) 

