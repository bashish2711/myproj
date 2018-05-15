#Least laxity first scheduling implementation

import string
import random
import fractions

def _lcm(a,b): return abs(a * b) / fractions.gcd(a,b) if a and b else 0

def lcm(a):
    return reduce(_lcm, a)

#A task instance
class TaskIns(object):

     #Constructor (should only be invoked with keyword parameters)
    def __init__(self, start, end, priority, name, bt):
        self.start    = start
        self.end      = end
        self.usage    = 0
        self.priority = priority
        self.name     = name.replace("\n", "")
        self.id = int(random.random() * 10000)
        self.bt = bt

    #Allow an instance to use the cpu (periodic)
    def use(self, usage):
        self.usage += usage
        if self.usage >= self.bt:
            self.status = "Finish"
        else:
            self.status = " "
        print on_cpu.get_unique_name() + " " + "\t %s \t %s \t %s \t %s \t %s \t %s \t %s" %(self.start, self.bt, self.start, clock_step , self.priority, self.end, self.status)    
        if self.usage >= self.end - self.start:
            return True
        return False
    
    #Default representation
    #def __repr__(self):
    #    return str(self.name) + "#" + str(self.id) + " - start: " + str(self.start) + " priority: " + str(self.priority) + budget_text

    #Get name as Name#id
    def get_unique_name(self):
        return str(self.name) + "#" + str(self.id)

#Task types (templates for periodic tasks)
class TaskType(object):

    #Constructor
    def __init__(self, period, arrival_time, burst_time, deadline, name):
        self.period    = period
        self.arrival_time   = arrival_time
        self.burst_time = burst_time
        self.deadline  = deadline
        self.name      = name

#Priority comparison
def priority_cmp(one, other):
    if one.priority < other.priority:
        return -1
    elif one.priority > other.priority:
        return 1
    return 0

#Deadline monotonic comparison
def tasktype_cmp(self, other):
    if self.deadline < other.deadline:
        return -1
    if self.deadline > other.deadline:
        return 1
    return 0

if __name__ == '__main__':
    #Variables
    html_color = { 'T1':'red', 'T2':'blue', 'T3':'green', 'T4':'aqua', 'T5':'coral', 'Empty':'grey', 'Finish':'black'}
    taskfile = open('tasks.txt')
    lines = taskfile.readlines()
    task_types = []
    tasks = []
    hyperperiod = []
    done_list = []

    #Allocate task types
    for line in lines[3:]:
        line = line.split('\t')
        for i in range (0,4):
            line[i] = int(line[i])
        if len(line) == 5:
            name = line[4]
        elif len(line) == 4:
            name = 'Task'
        else:
            raise Exception('Invalid tasks.txt file structure')
        if int(line[0])>=0:
            task_types.append(TaskType(arrival_time=line[0], burst_time=line[1], period=line[2], deadline=line[3], name=name))
        
    #Calculate hyperperiod
    for task_type in task_types:
        hyperperiod.append(task_type.period)
    hyperperiod = lcm(hyperperiod)

    #Sort types rate monotonic
    task_types = sorted(task_types, tasktype_cmp)


    #Create task instances 
    for i in xrange(0, hyperperiod):
        for task_type in task_types:
            if  (i - task_type.arrival_time) % task_type.period == 0 and i >= task_type.arrival_time:
                start = i
                end = start + task_type.burst_time
                priority = task_type.deadline - task_type.burst_time -task_type.arrival_time
                tasks.append(TaskIns(start=start, end=end, priority=priority, name=task_type.name, bt=task_type.burst_time))

    #Html output start
    html = "<!DOCTYPE html><html><head><title>LLF Scheduling</title></head><body>"

    #Check utilization
    utilization = 0
    for task_type in task_types:
        utilization += float(task_type.burst_time) / float(task_type.period)
    if utilization > 1:
        print 'Utilization error!'
        html += '<br /><br />Utilization error!<br /><br />'

    #Simulate clock
    clock_step = 1
    for i in xrange(0, hyperperiod, clock_step):
        #Fetch ready_list tasks that can use cpu and sort by priority
        ready_list = []
        for t in tasks:
            if t.start <= i:
                ready_list.append(t)
        ready_list = sorted(ready_list, priority_cmp)

        #Select task with highest priority
        if len(ready_list) > 0:
            on_cpu = ready_list[0]
            done_list.append(on_cpu)
            html += '<div style="float: left; text-align: center; width: 110px; height: 20px; background-color:' + html_color[on_cpu.name] + ';">' + on_cpu.get_unique_name() + '</div>'
            on_cpu.priority += clock_step
            if on_cpu.use(clock_step):
                tasks.remove(on_cpu)
                html += '<div style="float: left; text-align: center; width: 10px; height: 20px; background-color:' + html_color['Finish'] + ';"></div>'
               # print "Finish!" ,
          #  else:
			#	print "TBD"
        else:
            print 'No task uses the processor. '
            html += '<div style="float: left; text-align: center; width: 110px; height: 20px; background-color:' + html_color['Empty'] + ';">Empty</div>'
        print "\n"
            

    #Print remaining periodic tasks
    html += "<br /><br />"
    for p in tasks:
        print p.get_unique_name() + " is dropped due to overload!"
        html += "<p>" + p.get_unique_name() + " is dropped due to overload!</p>"
    
        
    # Print Waiting time and turnaround time calculations:
    b_t=[]
    processes=[]
    for d in range(0, 25):
    	print done_list[d].name, done_list[d+1].bt, "\n"
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
    print("\n")
    print("Process\t  Burst Time\t  Waiting Time\t  Turn Around Time")
    for i in range(0,n):
    	print(str(processes[i])+"\t\t"+str(b_t[i])+"\t\t"+str(wt[i])+"\t\t"+str(tat[i]))
    	print("\n")
    print("Average Waiting time is: "+str(avgwt))
    print("Average Turn Arount Time is: "+str(avgtat))

    #Html output end
    html += "</body></html>"
    output = open('output.html', 'w')
    output.write(html)
    output.close()
