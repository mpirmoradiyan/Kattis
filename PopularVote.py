import sys

# Reading the file and store all the integers in a list
d=[]
for line in sys.stdin:    
    d.append(int(line))

T=d[0]     # The first line is the number of test cases

# Check the T to be <= 500
if T not in range(1,501,1):
    raise ValueError('T is not in valid range')

# Storing the position of first line of each test case in a dictionary
idDict ={}
idDict[1] = 1  # The first test case
for i in range(2,T+1):
    idDict[i]= idDict[i-1] +d[idDict[i-1]] + 1

# Storing the votes for each test case in a dictionary
voteDict={}
for i in range(1,T+1):
    if i == T:
        voteDict[i] = d[idDict[i]+1:]
    else:
        voteDict[i]=d[idDict[i]+1:idDict[i+1]]

# Check for number of candidates to be in [2,10]
# for _,v in idDict.items():
#     n = d[v]
#     if n not in range(2,11,1):
#         raise ValueError('n is out of range!')

# Check for number of votes to be <= 50000, and to check if there is at least 1 vote
# for _,votes in voteDict.items():
#     if sum(votes)==0:
#         raise ValueError('There should be at least one vote cast in each election!')
#     for vote in votes:
#         if vote >50000:
#             raise ValueError('Each candidate will not receive more than 50000 votes!')

# Output
# for k in voteDict.keys():
#     #if min(voteDict[k]) == max(voteDict[k]):
#     if all(item==voteDict[k][0] for item in voteDict[k]):
#         print('{0}'.format('no winner'))
#     elif max(voteDict[k]) <= sum(voteDict[k])/2:        
#         print('{0} {1} '.format(("minority winner"),(1+voteDict[k].index(max(voteDict[k])))))
#     elif max(voteDict[k]) > sum(voteDict[k])/2:
#         print('{0} {1} '.format(("majority winner"),(1+voteDict[k].index(max(voteDict[k])))))
#output
for k,v in voteDict.items():
    if len(v) not in range(2,11,1):
        print('Number of candidates are out of range!')
    elif sum(v)==0:
        print('There should be at least one vote cast in each election!')
    elif any(item>50000 for item in v):
        print('Each candidate will not receive more than 50000 votes!')
    elif len([item for item in v if item==max(v)])>1:
        print('{0}'.format('no winner'))
    elif max(voteDict[k]) <= sum(voteDict[k])/2:        
        print('{0} {1} '.format(("minority winner"),(1+voteDict[k].index(max(voteDict[k])))))
    elif max(voteDict[k]) > sum(voteDict[k])/2:
        print('{0} {1} '.format(("majority winner"),(1+voteDict[k].index(max(voteDict[k])))))