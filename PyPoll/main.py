import os
#import os module, allowing computer to read file path on various operating systems

import csv
#import CSV helps python read in csv data

election_data_path=os.path.join("Resources","election_data.csv")
#election data CSV file patch

election_output_path=os.path.join("Analysis","election_analysis.txt")
#output text file for election data analysis

poll_dict={}
#empty dictionary to store candidates and the number of votes for each candidate

voter_ID=[]
#Empty list to store all voter IDs 

with open(election_data_path) as csvfile:
    
    csvreader=csv.reader(csvfile, delimiter=",")
    #use csv module to read csv file and store data as list of lists

    header=next(csvreader)
    #next method iterates to next list in list, 
    #first being the header and stores list as variable

    for row in csvreader:
        #iterates through csv reader lists of lists

        voter_ID.append(row[0])
        #appends each voter ID to list
        
        if row[2] not in poll_dict:
        #if the name of the candidate is not a key in the dictionary, then add it to dictionary as key with a value of 1
            poll_dict[row[2]]=1
         
        elif row[2] in poll_dict:
        #if the name of the candidate is  a key in the dictionary, then add 1 to the existing value with respect to the key
            poll_dict[row[2]]+=1
    
    total_votes=len(voter_ID)
    #assignes the length of the voter_ID list to variable

    #The code below runs the analysis on the dictionary and prints to terminal:
    print('Election Results')
    print('-------------------------------------------------------------------')
    
    print(f'Total Votes: {total_votes}')
    
    print('-------------------------------------------------------------------')

    winning_votes=0

    for name,votes in poll_dict.items():
    #itterate through dictionary items with name bein key and the votes being the values
        if votes>=winning_votes:
        #if the votes value is greater than the winnign votes, then store votes as winnig votes and the name of the candidate as the winner
            winning_votes=votes
            winner=name
        print(f'{name},: {round((int(votes)/total_votes)*100,3)}% ({votes})')
    
    print('-------------------------------------------------------------------')

    print(f"Winner: {winner}")

    print('-------------------------------------------------------------------')

    #The code below prints to text file:
    with open(election_output_path,"w") as text:
        text.write("Election Results\n")
        text.write('-------------------------------------------------------------------\n')
        text.write(f'Total Votes: {total_votes}\n')
        text.write('-------------------------------------------------------------------\n')
        
        for name,votes in poll_dict.items():
        #itterate through dictionary items with name bein key and the votes being the values
            text.write(f'{name},: {round((int(votes)/total_votes)*100,3)}% ({votes})\n')
        text.write('-------------------------------------------------------------------\n')
        text.write(f'Winner: {winner}\n')
        text.write('-------------------------------------------------------------------\n')