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
    change = 0 
    prev_PL = 0
    tot_change = 0

    #Skip the header
    next(csvreader, None)

    for row in csvreader:
        #The total number of month
        month_count += 1
        #The net total amount of "Profit/Losses"
        total += int(row[1])
        if month_count ==1:
            prev_PL = int(row[1])      
        else:
            change = int(row[1]) - prev_PL
            tot_change += change
            prev_PL = int(row[1])
    average_change = round(tot_change / (month_count - 1), 2)

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {month_count}") 
print(f"Total: ${total}")
print(f"Average  Change: ${average_change}")

#print (f"Total change: {tot_change}")

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

