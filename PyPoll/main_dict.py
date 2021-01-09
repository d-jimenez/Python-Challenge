#The script below uses a list, set and for loop approach to evaluate the
#number of votes per candidate, the percentage of votes earnes by each
#candidate and the winner of the election.
#-----------------------------------------------------------------------------
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



with open(election_data_path) as csvfile:
    
    csvreader=csv.reader(csvfile, delimiter=",")
    #use csv module to read csv file and store data as list of lists
    # print(csvreader)

    header=next(csvreader)
    #next method iterates to next list in list, 
    #first being the header and stores list as variable
    # print(header)
    # row1=next(csvreader)
    # print(row1)

    for row in csvreader:
        #iterates through csv reader lists of lists
        # print(row)
        if row[2] not in poll_dict:
            poll_dict[row[2]]=1
        if row[2] in poll_dict:
            poll_dict[row[2]]+=1

    print(poll_dict)
    
    # print('Election Results')
    # print('-------------------------------------------------------------------')
    
    # print(f'Total Votes: {total_votes}')
    # percent_candidate=[count_candidate_0/total_votes, count_candidate_1/total_votes, count_candidate_2/total_votes, count_candidate_3/total_votes]
    # # print(len(voter_id_unique))
    # # print(county_unique)
    # # print(candidate_unique)

    # print('-------------------------------------------------------------------')
    # for x in range(0,len(candidate_unique)):
    #     print(f'{candidate_unique[x]}: {count_candidate[x]} total votes at {round(percent_candidate[x]*100,3)}%')
    
    # winning_votes=max(count_candidate)
    # # print(winning_votes)
    # winning_index=count_candidate.index(winning_votes)
    # # print(winning_index)
    # winner=candidate_unique[winning_index]
    # print('-------------------------------------------------------------------')
    # print(f'Winner: {winner}')
    # print('-------------------------------------------------------------------')

    # with open(election_output_path,"w") as text:
    #     text.write("Election Results\n")
    #     text.write('-------------------------------------------------------------------\n')
    #     text.write(f'Total Votes: {total_votes}\n')
    #     text.write('-------------------------------------------------------------------\n')
    #     for x in range(0,len(candidate_unique)):
    #         text.write(f'{candidate_unique[x]}: {count_candidate[x]} total votes at {round(percent_candidate[x]*100,3)}%\n')
    #     text.write('-------------------------------------------------------------------\n')
    #     text.write(f'Winner: {winner}\n')
    #     text.write('-------------------------------------------------------------------\n')