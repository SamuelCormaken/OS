from collections import deque
def round_robin(pid, arrival, burst, quantum):
    n = len(pid)
    remaining_bt = burst[:]
    wt = [0] * n
    tat = [0] * n
    complete = [False] * n
    completion_time = [0] * n  
    time = 0
    queue = deque()
    queued = [False] * n
    for i in range(n):
        if arrival[i] == 0:
            queue.append(i)
            queued[i] = True
    while queue:
        i = queue.popleft()
        if remaining_bt[i] > quantum:
            time += quantum
            remaining_bt[i] -= quantum
        else:
            time += remaining_bt[i]
            wt[i] = time - arrival[i] - burst[i]
            remaining_bt[i] = 0
            complete[i] = True
            completion_time[i] = time  
        for j in range(n):
            if queued[j]==False and arrival[j] <= time:
                queue.append(j)
                queued[j] = True
        if complete[i]==False:
            queue.append(i)
    for i in range(n):
        tat[i] = wt[i] + burst[i]
    print("PID\tArrival time\tBurst time\tWaiting time\tTurnaround time \tCompletion time")
    for i in range(n):
        print(pid[i],"\t\t",arrival[i],"\t\t",burst[i],"\t\t",wt[i],"\t\t",tat[i],"\t\t",completion_time[i])
    avg_wt = sum(wt) / n
    avg_tat = sum(tat) / n
    print("\nAverage Waiting Time:",avg_wt)
    print("Average Turnaround Time:",avg_tat)
pid = ['p1', 'p2', 'p3', 'p4', 'p5']
arrival = [0, 1, 2, 3, 4]
burst = [5, 3, 1, 2, 3]
quantum = 2
round_robin(pid, arrival, burst, quantum)