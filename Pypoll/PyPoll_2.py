#PyPoll
#Bring in Dependencies
import os
import csv

# csvpath=os.path.join('..','users','smile','PythonStuff',' resources','election_data.csv')
csvpath=os.path.join('Resources', 'election_data.csv')

# csvpath=os.path.join('..', 'Resources', 'election_data.csv')
with open(csvpath, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

#Creates dictionary to be used for candidate name and vote count.
poll = {}
#Sets variable, total votes, to zero for count.
total_votes = 0
#create empty list for candidates and his/her vote count
candidates = []
num_votes = []
# creates vote percent list
vote_percent = []
winner_list = []

#gets data file
with open(csvpath, 'r') as csvfile:
    csvread = csv.reader(csvfile)

    #skips header line (don't want to count this)
    next(csvread, None)

    #creates dictionary from file using column 3 as keys, using each name only once.
    #counts votes for each candidate as entries
    #keeps a total vote count by counting up 1 for each loop (# of rows w/o header)
    #(used stack overflow to come up with "key to a dictonary")
    for row in csvread:
        total_votes += 1
        if row[2] in poll.keys():
            poll[row[2]] = poll[row[2]] + 1
        else:
            poll[row[2]] = 1

#takes dictionary keys and values and puts them into the lists, 
# candidates and num_votes
for key, value in poll.items():
    candidates.append(key)
    num_votes.append(value)

# creates vote percent list
for n in num_votes:  #n 
    vote_percent.append(round(n/total_votes*100, 1))  #stackoverflow for round function

# zips candidates, num_votes, vote_percent into tuples (this puts it all together, in a list that can not be changed list is a tuple)
total_data = list(zip(candidates, num_votes, vote_percent))

#creates winner_list to put winners 
for name in total_data:
    if max(num_votes) == name[1]:
        winner_list.append(name[0])

# makes winner_list a str with the first entry
winner = winner_list[0]

#will run if there is a tie and will put additional winners into a string separated by commas
if len(winner_list) > 1:
    for w in range(1, len(winner_list)):
        winner = winner + ", " + winner_list[w]

#print outs (n Python strings, the backslash "\" is the "escape" character. 
# It is used in representing certain whitespace characters:"\n" is a newline,
print('Election Results \n------------------------- \nTotal Votes: ' + str(total_votes) + 
      '\n-------------------------')
#prints using loop of tuples(immutable list we created)

for entry in total_data:
    print(entry[0] + ": " + str(entry[2]) +'%  (' + str(entry[1]) + ')')
print('------------------------- \nWinner: ' + winner + '\n-------------------------')

#prints to file
output_file = os.path.join("C:/Users/smile/PythonStuff/Output/PyPoll2")

with open(output_file, 'w') as txtfile:
    txtfile.writelines('Election Results \n------------------------- \nTotal Votes: ' + str(total_votes) + 
      '\n-------------------------\n')
    for entry in total_data:
        txtfile.writelines(entry[0] + ": " + str(entry[2]) +'%  (' + str(entry[1]) + ')\n')
    txtfile.writelines('------------------------- \nWinner: ' + winner + '\n-------------------------')