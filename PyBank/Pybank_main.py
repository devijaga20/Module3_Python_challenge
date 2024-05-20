import csv

#The total number of months included in the dataset
def count_months(csv_filepath):
    file = open(csv_filepath, 'r') 
    csvreader = csv.reader(file) 
    # Skip the header
    next(csvreader)
    # Initialize a counter
    month_count = 0
    print(file)
    # Loop through each row and count the months
    for row in csvreader:
        month_count += 1
    return month_count

# Path to the CSV file
csv_filepath = "C:\\Users\HP\OneDrive\Documents\Data bootcamp\Homework\Python Homework\Module3_Python_challenge\PyBank\Resources\\budget_data.csv"
total_months = count_months(csv_filepath)
print(f"Total number of months: {total_months}")


#The net total amount of "Profit/Losses" over the entire period

def calculate_net_total(csv_filepath):
    file = open(csv_filepath, 'r')
    csvreaderobj = csv.reader(file)
        # Skip the header
    next(csvreaderobj)
        # Initialize a variable called sum
    sum = 0
        # Loop through each row and add the Profit/Losses to sum
    for row in csvreaderobj:
            profit_losses = int(row[1]) 
            sum = sum + profit_losses 
    return sum

# Path to the CSV file
csv_filepath = "C:\\Users\HP\OneDrive\Documents\Data bootcamp\Homework\Python Homework\Module3_Python_challenge\PyBank\Resources\\budget_data.csv"
final_sum= calculate_net_total(csv_filepath)
print(f"Net total amount of Profit/Losses: {final_sum}")


#The changes in "Profit/Losses" over the entire period, and then the average of those changes
#The greatest increase and decrease in profits (date and amount) over the entire period


def analyze_budget_data(file_path):
    with open(file_path, mode='r') as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)  # Skip the header

        previous_profit_losses = None
        changes = []
        dates = []
        greatest_increase = {"date": None, "amount": float('-inf')}
        greatest_decrease = {"date": None, "amount": float('inf')}

        for row in csv_reader:
            date = row[0]
            current_profit_losses = int(row[1])

            if previous_profit_losses is not None:
                change = current_profit_losses - previous_profit_losses
                changes.append(change)
                dates.append(date)

                if change > greatest_increase["amount"]:
                    greatest_increase["amount"] = change
                    greatest_increase["date"] = date

                if change < greatest_decrease["amount"]:
                    greatest_decrease["amount"] = change
                    greatest_decrease["date"] = date

            previous_profit_losses = current_profit_losses

    if changes:
        average_change = sum(changes) / len(changes)
    else:
        average_change = 0

    return {
        "changes": changes,
        "average_change": average_change,
        "greatest_increase": greatest_increase,
        "greatest_decrease": greatest_decrease
    }

# path to CSV file
file_path = "C:\\Users\HP\OneDrive\Documents\Data bootcamp\Homework\Python Homework\Module3_Python_challenge\PyBank\Resources\\budget_data.csv"
# Get results
total_months = count_months(csv_filepath)
final_sum = calculate_net_total(csv_filepath)
results = analyze_budget_data(csv_filepath)

# Prepare the output
output = (
    "Financial Analysis\n"
    "----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${final_sum}\n"
    f"Average Change: ${results['average_change']:.2f}\n"
    f"Greatest Increase in Profits: {results['greatest_increase']['date']} (${results['greatest_increase']['amount']})\n"
    f"Greatest Decrease in Profits: {results['greatest_decrease']['date']} (${results['greatest_decrease']['amount']})\n"
)

# Print the analysis to the terminal
print(output)

# Export the analysis to a text file
output_file_path = "./PyPoll/analysis/financial_analysis.txt"
with open(output_file_path, mode='w') as output_file:
    output_file.write(output)
