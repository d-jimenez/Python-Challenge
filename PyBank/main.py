import os

import csv

csvpath=os.path.join("Resources","budget_data.csv")
#path of budget profit/loss data

text_output_path=os.path.join("Analysis","budget_analysis_output.txt")

dates_list=[]

# net_gain_loss2=float(0)
profit_loss_list=[]

monthly_change=[]

with open(csvpath) as csvfile:

    csvreader=csv.reader(csvfile, delimiter=",")

    # print(csvreader)

    csv_header=next(csvreader)

    # print(f"CSV Header: {csv_header}")
    # print(csv_header)

    for row in csvreader:
        # print(row)
        # date_count+=1
        dates_list.append(row[0])
        profit_loss_list.append(float(row[1]))
        # net_gain_loss2+=float(row[1])
    
    date_count=(len(dates_list))
    # print(date_count)
    
    net_gain_loss=sum(profit_loss_list)
    # print(net_gain_loss)
    # print(net_gain_loss2)

    for n in range(1, len(profit_loss_list)):
        monthly_change.append(profit_loss_list[n]-profit_loss_list[n-1])

    # print(monthly_change)

    average_monthly_change=sum(monthly_change)/len(monthly_change)

    # print(round(average_monthly_change,2))

    max_change=max(monthly_change)
    # print(max(monthly_change))
    max_index=monthly_change.index(max_change)
    # print(max_index)
    max_date=dates_list[max_index+1]
    #need to add 1 to the index because the monthly_change list starts at index 1 and not 0
    # print(max_date)

    min_change=min(monthly_change)
    # print(min(monthly_change))
    min_index=monthly_change.index(min_change)
    # print(min_index)
    min_date=dates_list[min_index+1]
    #need to add 1 to the index because the monthly_change list starts at index 1 and not 0
    # print(min_date)

    with open(text_output_path,"w") as text:
        text.write("Financial Analysis\n")
        text.write('----------------------------------------------------\n')
        text.write(f'Total Months: {date_count}\n')
        text.write(f'Total: ${round(net_gain_loss,2)}\n')
        text.write(f"Average Change: ${round(average_monthly_change,2)}\n")
        text.write(f'Greatest Increase in Profits: ${max_change} on {max_date}\n')
        text.write(f'Greatest Decrease in Profits: ${min_change} on {min_date}\n')


    print("Financial Analysis")
    print('----------------------------------------------------')
    print(f'Total Months: {date_count}')
    print(f'Total: ${round(net_gain_loss,2)}')
    print(f"Average Change: ${round(average_monthly_change,2)}")
    print(f'Greatest Increase in Profits: ${max_change} on {max_date}')
    print(f'Greatest Decrease in Profits: ${min_change} on {min_date}')

