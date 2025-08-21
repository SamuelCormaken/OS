import sys
req_seq=[176,39,49,114,90,26]
req_seq.sort()
head=39
sum=0
print(req_seq)
visited=[]
visited.append(head)
h=0
def isvisited(x):
    for i in visited:
        if i==x:
            return True
    return False
while(len(visited)<len(req_seq)):
    compare=sys.maxsize
    for j in req_seq:
        if not isvisited(j):
          diff=abs(head-j)  
          if diff<compare:
            compare=diff
            h=j
    print(f"Node traversed is {h}")       
    head=h
    visited.append(h)
    sum+=compare
print(sum)