req_seq = [14, 20, 29, 40, 50, 110]
mid=0
seek=0
head = 29
req_seq.sort()
direction=str(input("enter direction"))
for i in range(len(req_seq)):
    if head<req_seq[i]:
        mid=i
        break
if direction=="left":
    for i in range (mid-1,-1,-1):
        seek+=abs(head-req_seq[i])
        head=req_seq[i]
        print("entered")
    for i in range(len(req_seq)-1,mid-1,-1):
        seek+=abs(head-req_seq[i])
        head=req_seq[i]
elif direction=="right":
     for i in range (mid-1,len(req_seq)):
            seek+=abs(head-req_seq[i])
            head=req_seq[i]
            print("entered")
     for i in range(0,mid-1):
        seek+=abs(head-req_seq[i])
        head=req_seq[i]

print(seek)
