import os

import csv

csvpath=os.path.join("Resources","budget_data.csv")

date_count=0
net_gain_loss=float(0)

with open(csvpath) as csvfile:

    csvreader=csv.reader(csvfile, delimiter=",")

    # print(csvreader)

    csv_header=next(csvreader)

    # print(f"CSV Header: {csv_header}")
    print(csv_header)

    for row in csvreader:
        date_count+=1
        net_gain_loss+=float(row[1])
    
    average_gain_loss=net_gain_loss/date_count

    print(f"There are a total of {date_count} months in the budget data set.")
    print(f"The net gain/loss for the budget data is {net_gain_loss} dollars.")
    print(f"The average gain/loss for the budget data is {average_gain_loss} dollars.")

