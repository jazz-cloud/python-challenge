import os
import csv

# putting the resources
pybank_csv = os.path.join("..", "Resources", "budget_data.csv")

# read the csv file
with open(pybank_csv, 'r') as csvfile:
    # split the commas
    csv.reader = csv.reader(csvfile, delimiter=',')
    # identify and store the header row
    header = next(csvfile, None)

    # create some empty list
    month = []
    profit_loss = []
    profit_loss_change = []

    # pulling the values from the csv file
    for row in csv.reader:
        month.append(row[0])
        profit_loss.append(float(row[1]))

        print("Financial Analysis")
        print("----------------------------")
        print(f"Total months: {len(month)}")
        print(f"Total: ${round(sum(profit_loss),0)}")

    # finding the difference in the profit/loss which can b use for later as well
    profit_loss_change = [profit_loss[i] - profit_loss[i-1]
                          for i in range(1, len(profit_loss))]

    # now to find the average changes
    average_change = sum(profit_loss_change)/len(profit_loss_change)
    print(f"Average Change: ${round(average_change,2)}")

    # finding the greatest increase in profit
    greatinc = max(profit_loss_change)
    greatincdate = str(month[profit_loss_change.index(greatinc)+1])
    print(f"Greatest Increase in Profits: {greatincdate} (${greatinc})")

    # finding the greatest decrease in losses
    greatdec = min(profit_loss_change)
    greatdecdate = str(month[profit_loss_change.index(greatdec)+1])
    print(f"Greatest Decrease in Profits: {greatdecdate} (${greatdec})")

# exporting into a text file with the result
finanalysis_path = os.path.join("..", "analysis", "pybank.txt")

# open the text file and start writting
with open(finanalysis_path, 'w') as txtfile:
    txtfile.write("Financial Analysis" + "\n")
    txtfile.write("-----------------------------" + "\n")
    txtfile.write("Total Months: " + str(len(month)) + "\n")
    txtfile.write("Total: $" + str(round(sum(profit_loss), 0)) + "\n")
    txtfile.write("Average Change: $" + str(round(average_change, 2)) + "\n")
    txtfile.write("Greatest Increase in Profits: " +
                  str(greatincdate) + "($" + str(greatinc) + ")" + "\n")
    txtfile.write("Greatest Decrease in Profits: " +
                  str(greatdecdate) + "($" + str(greatdec) + ")" + "\n")
