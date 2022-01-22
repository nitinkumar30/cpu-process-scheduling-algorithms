
# First Come First Serve
n = int(input("Enter no of processes:"))

# variables and array initializations
arrival_time = []
burst_time = []
completion_time = []
execution_time = 0
turn_around_time = []
waiting_time = []
avg_tat=0
avg_wt=0

for i in range(n):
    a = int(input("Enter Arrival Time of Process {0}: ".format(i)))
    b = int(input("Enter Burst Time of Process {0}: ".format(i)))
    arrival_time.append(a) # Arrival time of corresponding processes here
    burst_time.append(b) # Burst time of corresponding processes here


for i in range(n):
    if arrival_time[i] <= execution_time:
        c = execution_time + burst_time[i]
        execution_time = c
        
    else:
        execution_time = arrival_time[i]
        c = execution_time + burst_time[i]
        execution_time  = c
    completion_time.append(c) # completion time in total
    turn_around_time.append(completion_time[i] - arrival_time[i])
    
    waiting_time.append(turn_around_time[i] - burst_time[i])
    print("\n--------------------------------------------------------------------------------------------------------------\n")
    print("Process\t\tArrival Time\tBurst Time\tCompletion Time\t\tTurn Around Time\tWaiting Time")
    print("P"+str(i+1) + '\t\t\t' +str(arrival_time[i]) + '\t\t' +str(burst_time[i])+ '\t\t' +str(completion_time[i])+ '\t\t\t' +str(turn_around_time[i])+ '\t\t' +str(waiting_time[i])+ '\t\t')

for i in range(len(arrival_time)):
    avg_tat += turn_around_time[i]
    avg_wt += waiting_time[i]

print("Average Turn Around Time:", avg_tat/n)
print("Average Waiting Time:", avg_wt/n)
