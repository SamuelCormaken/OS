def sjf_print(pro):
    n=len(pro)
    time=0
    i=0
    completed=[False]*n
    scheduled=[]
    while i<n:
        burst=999
        selected=-1
        for j in range(n):
            if completed[j]==False and pro[j]['arrival']<=time:
                if pro[j]['burst']<burst:
                    burst=pro[j]['burst']
                    selected=j
        if selected==-1:
            time+=1
        else:
            p=pro[selected]
            completed[selected]=True
            p['comp_time'] = time + p['burst']
            p['ta_time'] = p['comp_time'] - p['arrival']
            p['waiting_time'] = p['ta_time'] - p['burst']
            time = p['comp_time']
            scheduled.append(p)
            i+= 1
    print("Using SJF")
    print("PID\tAT\tBT\tCT\tTAT\tWT")
    for p in scheduled:
        print(p['pid'],"\t",p['arrival'],"\t",p['burst'],"\t",
              p['comp_time'],"\t",p['ta_time'],"\t",p['waiting_time'])
        

processes=[
     {'pid': 'P1', 'arrival': 0, 'burst': 3},
     {'pid': 'P2', 'arrival': 1, 'burst': 2},
     {'pid': 'P3', 'arrival': 2, 'burst': 1},
     {'pid': 'P4', 'arrival': 3, 'burst': 4},
    {'pid': 'P5', 'arrival': 0, 'burst': 2},
]

sjf_print(processes)