import os

import csv

election_data_path=os.path.join("Resources","election_data.csv")
#election data CSV file patch

election_output_path=os.path.join("Analysis","election_analysis.txt")
#output text file for election data analysis

voter_id_unique=[]

county_unique=[]

candidate_unique=[]

with open(election_data_path) as csvfile:
    
    csvreader=csv.reader(csvfile, delimiter=",")
    # print(csvreader)

    header=next(csvreader)
    # print(header)
    # row1=next(csvreader)
    # print(row1)

    for row in csvreader:
        # print(row)

        if row[0] not in voter_id_unique:
            voter_id_unique.append(row[0])

        if row[1] not in county_unique:
            county_unique.append(row[1])

        if row[2] not in candidate_unique:
            candidate_unique.append(row[2])
    
    print(len(csvreader))
    print(len(voter_id_unique))
    print(county_unique)
    print(candidate_unique)