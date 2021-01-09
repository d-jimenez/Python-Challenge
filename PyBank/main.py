import os
#import os module, allowing computer to read file path on various operating systems

import csv
#import CSV helps python read in csv data

csvpath=os.path.join("Resources","budget_data.csv")
#path of budget data used in financial analysis

text_output_path=os.path.join("Analysis","budget_analysis_output.txt")
#path of text output file to be used to print analysis information

dates_list=[]
#blank list used to store dates in order to cound number of months

profit_loss_list=[]
#blank list to store monthly profit/loss number

monthly_change=[]
#blank list used to store the month over month change starting with profit_loss[1]-profit_loss[0]

with open(csvpath) as csvfile:
#acts as content manager to close file after all indented code is ran

    csvreader=csv.reader(csvfile, delimiter=",")
    #stores the content of csv data into a list of lists

    csv_header=next(csvreader)
    #itterates through next item within a list and stores the first itterated list as the header

    for row in csvreader:
        #itterate through the row of data within the csvfile, starting with row index 1 after the header

        dates_list.append(row[0])
        #Append the date to the empty dates_list

        profit_loss_list.append(float(row[1]))
        #append the profit/losst data into the empty profit_loss_list
    
    date_count=(len(dates_list))
    #finds length of the dates_list to determine number of months
    
    net_gain_loss=sum(profit_loss_list)
    #sum of every months profit/loss to fint net_gain_loss

    for n in range(1, len(profit_loss_list)):
    #itterates through the profit_loss_list to find the n-(n-1) 
    # month over month change, begining with index 1 of the list
        
        monthly_change.append(profit_loss_list[n]-profit_loss_list[n-1])
        #append the month over month change to the empty monthl_change list
    
    average_monthly_change=sum(monthly_change)/len(monthly_change)
    #calculates the average month over month change

    max_change=max(monthly_change)
    #calculates max change for month over month list

    max_index=monthly_change.index(max_change)
    #calculates index of max change for month over month list

    max_date=dates_list[max_index+1]
    #Finds where in the monthly_change list the maximum change occurs
    #need to add 1 to the index because the monthly_change list starts at index 1 and not 0

    min_change=min(monthly_change)
    #calculates min change for month over month list

    min_index=monthly_change.index(min_change)
    #calculates index of min change for month over month list

    min_date=dates_list[min_index+1]
    #Finds where in the monthly_change list the minimum change occurs
    #need to add 1 to the index because the monthly_change list starts at index 1 and not 0

    with open(text_output_path,"w") as text:
    #opens the text output file, if one does not exist, it will create one
        text.write("Financial Analysis\n")
        text.write('----------------------------------------------------\n')
        text.write(f'Total Months: {date_count}\n')
        text.write(f'Total: ${round(net_gain_loss,2)}\n')
        text.write(f"Average Change: ${round(average_monthly_change,2)}\n")
        text.write(f'Greatest Increase in Profits: ${max_change} on {max_date}\n')
        text.write(f'Greatest Decrease in Profits: ${min_change} on {min_date}\n')
        #All output information is written to the text file

    print("Financial Analysis")
    print('----------------------------------------------------')
    print(f'Total Months: {date_count}')
    print(f'Total: ${round(net_gain_loss,2)}')
    print(f"Average Change: ${round(average_monthly_change,2)}")
    print(f'Greatest Increase in Profits: ${max_change} on {max_date}')
    print(f'Greatest Decrease in Profits: ${min_change} on {min_date}')
    #all output information is also printed on the console's terminal

