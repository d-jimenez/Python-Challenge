#The script below uses a list, set and for loop approach to evaluate the
#number of votes per candidate, the percentage of votes earnes by each
#candidate and the winner of the election.
#-----------------------------------------------------------------------------
import os

import csv

from collections import counter


election_data_path=os.path.join("Resources","election_data.csv")
#election data CSV file patch

election_output_path=os.path.join("Analysis","election_analysis.txt")
#output text file for election data analysis

voter_id=[]

county=[]

candidate=[]

with open(election_data_path) as csvfile:
    
    csvreader=csv.reader(csvfile, delimiter=",")
    # print(csvreader)

    header=next(csvreader)
    # print(header)
    # row1=next(csvreader)
    # print(row1)

    for row in csvreader:
        # print(row)

        voter_id.append(row[0])

        county.append(row[1])

        candidate.append(row[2])
    
    voter_id_unique= list(set(voter_id))

    county_unique= sorted(list(set(county)))

    candidate_unique=sorted(list(set(candidate)))

    count_candidate_0=0

    count_candidate_1=0

    count_candidate_2=0

    count_candidate_3=0
    

    # for person in candidate:
    #     if person == candidate_unique[0]:
    #         count_candidate_0+=1

    #     if person == candidate_unique[1]:
    #         count_candidate_1+=1

    #     if person == candidate_unique[2]:
    #         count_candidate_2+=1

    #     if person == candidate_unique[3]:
    #         count_candidate_3+=1

    count_candidate=[count_candidate_0, count_candidate_1, count_candidate_2, count_candidate_3]
    
    total_votes=len(voter_id)
    # print(len(csvreader))
    print('Election Results')
    print('-------------------------------------------------------------------')
    
    print(f'Total Votes: {total_votes}')
    percent_candidate=[count_candidate_0/total_votes, count_candidate_1/total_votes, count_candidate_2/total_votes, count_candidate_3/total_votes]
    # print(len(voter_id_unique))
    # print(county_unique)
    # print(candidate_unique)

    print('-------------------------------------------------------------------')
    for x in range(0,len(candidate_unique)):
        print(f'{candidate_unique[x]}: {count_candidate[x]} total votes at {round(percent_candidate[x]*100,3)}%')
    
    winning_votes=max(count_candidate)
    # print(winning_votes)
    winning_index=count_candidate.index(winning_votes)
    # print(winning_index)
    winner=candidate_unique[winning_index]
    print('-------------------------------------------------------------------')
    print(f'Winner: {winner}')
    print('-------------------------------------------------------------------')

    with open(election_output_path,"w") as text:
        text.write("Election Results\n")
        text.write('-------------------------------------------------------------------\n')
        text.write(f'Total Votes: {total_votes}\n')
        text.write('-------------------------------------------------------------------\n')
        for x in range(0,len(candidate_unique)):
            text.write(f'{candidate_unique[x]}: {count_candidate[x]} total votes at {round(percent_candidate[x]*100,3)}%\n')
        text.write('-------------------------------------------------------------------\n')
        text.write(f'Winner: {winner}\n')
        text.write('-------------------------------------------------------------------\n')
#=========================================================================================================================================================
# #The script below uses a counter and dictionary approach to determine the total number of votes,
# #the total number of votes for each candidate, the percventage of votes 
# #won by each candidate and the winner of the election.
# #-----------------------------------------------------------------------------
# import os

# import csv

# election_data_path=os.path.join("Resources","election_data.csv")
# #election data CSV file patch

# election_output_path=os.path.join("Analysis","election_analysis.txt")
# #output text file for election data analysis

# voter_id=[]

# county=[]

# candidate=[]

# poll_dict={}

# with open(election_data_path) as csvfile:
    
#     csvreader=csv.reader(csvfile, delimiter=",")
#     # print(csvreader)

#     header=next(csvreader)
#     # print(header)
#     # row1=next(csvreader)
#     # print(row1)

#     for row in csvreader:
#         # print(row)

#         voter_id.append(row[0])

#         county.append(row[1])

#         candidate.append(row[2])
    
#     voter_id_unique= list(set(voter_id))

#     county_unique= sorted(list(set(county)))

#     candidate_unique=sorted(list(set(candidate)))

#     count_candidate_0=0

#     count_candidate_1=0

#     count_candidate_2=0

#     count_candidate_3=0

#     for person in candidate:
#         if person == candidate_unique[0]:
#             count_candidate_0+=1

#         if person == candidate_unique[1]:
#             count_candidate_1+=1

#         if person == candidate_unique[2]:
#             count_candidate_2+=1

#         if person == candidate_unique[3]:
#             count_candidate_3+=1

#     count_candidate=[count_candidate_0, count_candidate_1, count_candidate_2, count_candidate_3]
    
#     total_votes=len(voter_id)
#     # print(len(csvreader))
#     print('Election Results')
#     print('-------------------------------------------------------------------')
    
#     print(f'Total Votes: {total_votes}')
#     percent_candidate=[count_candidate_0/total_votes, count_candidate_1/total_votes, count_candidate_2/total_votes, count_candidate_3/total_votes]
#     # print(len(voter_id_unique))
#     # print(county_unique)
#     # print(candidate_unique)

#     print('-------------------------------------------------------------------')
#     for x in range(0,len(candidate_unique)):
#         print(f'{candidate_unique[x]}: {count_candidate[x]} total votes at {round(percent_candidate[x]*100,3)}%')
    
#     winning_votes=max(count_candidate)
#     # print(winning_votes)
#     winning_index=count_candidate.index(winning_votes)
#     # print(winning_index)
#     winner=candidate_unique[winning_index]
#     print('-------------------------------------------------------------------')
#     print(f'Winner: {winner}')
#     print('-------------------------------------------------------------------')
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