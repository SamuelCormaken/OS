req_seq = [14, 20, 29, 40, 50, 110]
head = 29
seek = 0
left = []
right = []
direction = input("Enter direction (left or right): ")

for i in req_seq:
    if i < head:
        left.append(i)
    elif i > head:
        right.append(i)

left.sort()
right.sort()

if direction == "left":
    for i in reversed(left):
        seek += abs(head - i)
        head = i
    for i in right:
        seek += abs(head - i)
        head = i

elif direction == "right":
    for i in right:
        seek += abs(head - i)
        head = i
    for i in reversed(left):
        seek += abs(head - i)
        head = i

else:
    print("Invalid direction entered")

print("Total seek time:", seek)
