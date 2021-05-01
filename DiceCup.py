import sys
from collections import Counter
 
for line in sys.stdin:
    NM = line.split()
    N = int(NM[0])
    M = int(NM[1])
    
if N not in range(4,21,1) or M not in range(4,21,1):
    raise ValueError("N and M must be in the range [4,20]")

outcome=[]
for i in range(1,N+1):
    for j in range(1,M+1):
        outcome.append(i+j)
counts=Counter(outcome)
res=[k for k,v in counts.items() if v==counts.most_common(1)[0][1]]
for i in res:
    print(i)
