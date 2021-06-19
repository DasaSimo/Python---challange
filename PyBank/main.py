#The total number of months
import os
import csv


# Set path for file
csvpath = os.path.join("Resources", "budget_data.csv")
# Open the CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    month_count = 0
    total = 0
    change = 0 
    prev_PL = 0
    tot_change = 0
    max_inc_value = 0
    max_dec_value = 0

    #Skip the header
    next(csvreader, None)

    for row in csvreader:
        #The total number of month
        month_count += 1
        #The net total amount of "Profit/Losses"
        total += int(row[1])
        # calculation for the first row and the rest 
        if month_count ==1:
            prev_PL = int(row[1])      
        else:
            change = int(row[1]) - prev_PL
            tot_change += change
            prev_PL = int(row[1])
           # looking for maximum values in change and taking the date for the maximum found 
            if change  > max_inc_value:
                max_inc_value = change
                max_inc_date = row[0]
            if change < max_dec_value:
                max_dec_value= change
                max_dec_date = row[0]

    # calculation for average change, round up to 2 decimal places
    average_change = round(tot_change / (month_count - 1), 2)
    


# printing final statement 
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {month_count}") 
print(f"Total: ${total}")
print(f"Average  Change: ${average_change}")
print(f"Greatest Increase in Profits: {max_inc_date}  $({max_inc_value})")
print(f"Greatest Decrease in Profits: {max_dec_date}  $({max_dec_value})")


# Open the file and write text
with open("Financial_analysis.txt", 'w' ) as textfile:
    print("Financial Analysis", file = textfile)
    print("----------------------------", file = textfile)
    print(f"Total Months: {month_count}", file = textfile) 
    print(f"Total: ${total}", file = textfile)
    print(f"Average  Change: ${average_change}", file = textfile)
    print(f"Greatest Increase in Profits: {max_inc_date}  $({max_inc_value})", file = textfile)
    print(f"Greatest Decrease in Profits: {max_dec_date}  $({max_dec_value})", file = textfile)
   
