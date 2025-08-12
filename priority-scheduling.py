def priority_scheduling(pids, priorities, arrival_times, burst_times):
    n = len(pids)
    completed = 0
    current_time = 0
    is_completed = [False] * n
    completion_times = [0] * n
    waiting_times = [0] * n
    turnaround_times = [0] * n

    while completed < n:
        ready_queue = []
        for i in range(n):
            if (arrival_times[i] <= current_time) and (not is_completed[i]):
                ready_queue.append(i)

        if len(ready_queue) == 0:
            next_arrival = float('inf')
            for i in range(n):
                if is_completed[i]==False and arrival_times[i] < next_arrival:
                    next_arrival = arrival_times[i]
            current_time = next_arrival
            continue

        chosen_index = ready_queue[0]
        for idx in ready_queue:
            if priorities[idx] < priorities[chosen_index]:
                chosen_index = idx
            elif priorities[idx] == priorities[chosen_index]:
                if arrival_times[idx] < arrival_times[chosen_index]:
                    chosen_index = idx

        start_time = max(current_time, arrival_times[chosen_index])
        completion_time = start_time + burst_times[chosen_index]
        turnaround_time = completion_time - arrival_times[chosen_index]
        waiting_time = start_time - arrival_times[chosen_index]

        completion_times[chosen_index] = completion_time
        turnaround_times[chosen_index] = turnaround_time
        waiting_times[chosen_index] = waiting_time
        current_time = completion_time
        is_completed[chosen_index] = True
        completed += 1

    print(f"{'PID':<5}{'Priority':<9}{'Arrival':<8}{'Burst':<6}{'Completion':<11}{'Waiting':<8}{'Turnaround'}")
    for i in range(n):
        print(f"{pids[i]:<5}{priorities[i]:<9}{arrival_times[i]:<8}{burst_times[i]:<6}{completion_times[i]:<11}{waiting_times[i]:<8}{turnaround_times[i]}")
pids = ['p1', 'p2', 'p3', 'p4', 'p5']
priorities = [2, 0, 3, 1, 4]
arrival_times = [0, 5, 12, 2, 9]
burst_times = [11, 28, 2, 10, 16]
priority_scheduling(pids, priorities, arrival_times, burst_times)
