    # print Waiting time and turnaround time calculations:
    b_t=[]
    processes=[]
    for d in range(1, len(list(done_list))):
    	b_t.append(done_list[d].bt)
    	processes.append(done_list[d].name)
    
    wt=[]    #wt stands for waiting time
    avgwt=0  #average of waiting time
    tat=[]    #tat stands for turnaround time
    avgtat=0   #average of total turnaround time
    n=len(b_t)
    wt.insert(0,0)
    tat.insert(0,b_t[0])
    for i in range(1,len(b_t)):
    	wt.insert(i,wt[i-1]+b_t[i-1])
    	tat.insert(i,wt[i]+b_t[i])
    	avgwt+=wt[i]
    	avgtat+=tat[i]
    	avgwt=float(avgwt)/n
    	avgtat=float(avgtat)/n
    out += "\n"
    out += "Process\t  Burst Time\t  Waiting Time\t  Turn Around Time \n"
    for i in range(0,n):
    	out += str(processes[i])+"\t\t"+str(b_t[i])+"\t\t"+str(wt[i])+"\t\t"+str(tat[i])
    	out += "\n" 
    out += "Average Waiting time is: "+str(avgwt) + "\n"
    out += "Average Turn Arount Time is: "+str(avgtat) + "\n"

