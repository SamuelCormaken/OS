def fcfs(processes):
    n= len(processes)
    completed= [False] * n 
    time= 0
    schedule= []
    while len(schedule) < n:
        least_time= 999
        selected= -1
        for i in range(n):
            if completed[i]==False and processes[i]['arrival'] < least_time:
                least_time= processes[i]['arrival']
                selected=i
        p= processes[selected]
        completed[selected]= True
        if time<p['arrival']:
            time= p['arrival']
        p['comp_time']= time + p['burst']
        p['ta_time']= p['comp_time'] - p['arrival']
        p['waiting_time']= p['ta_time'] - p['burst']
        time = p['comp_time']
        schedule.append(p)
    print("FCFS Scheduling")
    print("PID\tAT\tBT\tCT\tTAT\tWT")
    for p in schedule:
        print(p['pid'], end="\t")
        print(p['arrival'], end="\t")
        print(p['burst'], end="\t")
        print(p['comp_time'], end="\t")
        print(p['ta_time'], end="\t")
        print(p['waiting_time'])
processes = [
    {'pid': 'P1', 'arrival': 0, 'burst': 3},
    {'pid': 'P2', 'arrival': 1, 'burst': 2},
    {'pid': 'P3', 'arrival': 2, 'burst': 1},
    {'pid': 'P4', 'arrival': 3, 'burst': 4},
]
fcfs(processes)
