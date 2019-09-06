# This is the main file for PyBank
# Part of Python Challenge

# --------------------------------------------------------------------------------------------------
#Your task is to create a Python script that analyzes the records to calculate each of the following:


# - The total number of months included in the dataset
# - The net total amount of "Profit/Losses" over the entire period
# - The average of the changes in "Profit/Losses" over the entire period
# - The greatest increase in profits (date and amount) over the entire period
# - The greatest decrease in losses (date and amount) over the entire period
#------------------------------------------------------------------------------------------


# Import Dependencies
import os
import csv

# Set path for file
csvpath = os.path.join("..", "PyBank\Resources", "budget_data.csv")

# Create empty lists to iterate through specific rows for the following variables
total_mont = []
total_prof = []
mont_profit_var = []
 
# Open csv in default read mode with context manager
with open(csvpath,newline="") as budget:

     # read budget_data.csv in the variable csvreader
    csvreader = csv.reader(budget,delimiter=",") 

    # Skip the header labels
    header = next(csvreader)  

    # Iterate through the rows in the stored file contents
    for row in csvreader: 

        # Append the total months and profit to their lists
        total_mont.append(row[0])
        total_prof.append(int(row[1]))

    # Iterate through the profits in order to get the monthly change in profits
    for i in range(len(total_prof)-1):
        
        # Take the difference between two months and append to monthly profit change
        mont_profit_var.append(total_prof[i+1]-total_prof[i])
        
# Obtain the max and min of the the montly profit change list
max_inc_val = max(mont_profit_var)
max_dec_val = min(mont_profit_var)

# Correlate max and min to the proper month using month list and index from max and min
#We use the plus 1 at the end since month associated with change is the + 1 month or next month
max_inc_month = mont_profit_var.index(max(mont_profit_var)) + 1
max_dec_month = mont_profit_var.index(min(mont_profit_var)) + 1 

# Print Statements

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(total_mont)}")
print(f"Total: ${sum(total_prof)}")
print(f"Average Change: {round(sum(mont_profit_var)/len(mont_profit_var),2)}")
print(f"Greatest Increase in Profits: {total_mont[max_inc_month]} (${(str(max_inc_val))})")
print(f"Greatest Decrease in Profits: {total_mont[max_dec_month]} (${(str(max_dec_val))})")

# Output files
#output_file = Path("python-challenge", "PyBank", "Financial_Analysis_Summary.txt")

# Output files location
output_file = os.path.join("..", "PyBank", "Financial_Analysis_Summary.txt")

with open(output_file,"w") as file:
    
# Write methods to print to Financial_Analysis_Summary 
    file.write("Financial Analysis")
    file.write("\n")
    file.write("----------------------------")

    file.write("\n")
    file.write(f"Total Months: {len(total_mont)}")
    
    file.write("\n")
    file.write(f"Total: ${sum(total_prof)}")
    file.write("\n")
    
    file.write(f"Average Change: {round(sum(mont_profit_var)/len(mont_profit_var),2)}")
    file.write("\n")
    
    file.write(f"Greatest Increase in Profits: {total_mont[max_inc_month]} (${(str(max_inc_val))})")
    
    file.write("\n")
    file.write(f"Greatest Decrease in Profits: {total_mont[max_dec_month]} (${(str(max_dec_val))})")

