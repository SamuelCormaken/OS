req_seq=[]
visited=[]
n=int(input())
i=0
while(i<n):
    x=int(input("Enter into array "))
    req_seq.append(x)
    i=i+1
head=50
seek=0
found=False
visited.append(head)
for i in range(len(req_seq)):
    found=False
    for j in range(len(visited)):
            if req_seq[i]==visited[j]:
                 found=True
    if found==True:
         continue
    seek+=abs(head-req_seq[i])
    visited.append(head)
    head=req_seq[i]
print (seek)