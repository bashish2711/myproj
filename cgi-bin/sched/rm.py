#!/usr/bin/python
#Least laxity first scheduling implementation

import string
import random
import fractions


def _lcm(a,b): return abs(a * b) / fractions.gcd(a,b) if a and b else 0

def lcm(a):
    return reduce(_lcm, a)

# Import modules for CGI handling 
import cgi, cgitb
import os
print "Content-type:text/html\r\n\r\n"
print """
<html>
   <head> </head>
   <meta name="viewport" content="width=device-width, initial-scale=1">
	<style>
	table {
    border-collapse: collapse;
    border-spacing: 0;
    width: 100%;
    border: 1px solid #ddd;
		}

	th, td {
    text-align: left;
    /* padding: 8px; */
		}

	tr:nth-child(even){background-color: #f2f2f2}
	</style>
   <title> Sucess </title>
   <body>
   <h2> The code Executed Successfully </h2>
   <a href=/rm_html_show.html target=_new> HTML Gantt Chart </a>
   <a href=/rm_out_show.txt target=_new> Text Log File </a>
   <p> Gantt Chart </p>
   <iframe name="Iframe2" frameborder="0" scrolling="no" width=100% onload="this.style.height=this.contentDocument.body.scrollHeight+20 +'px';" src="/rm_html_show.html" > </iframe>
   <p> Run Log </p>
   <iframe name="Iframe1" frameborder="0" scrolling="no" width=100% onload="this.style.height=this.contentDocument.body.scrollHeight +'px';" src="/rm_out_show.txt"> </iframe> 
   
   </body>
</html>
"""

out = "Content-type:text/html\r\n\r\n"
out += "RunTime\tName\tArrival\tBT\tStart\tUSE\tPRI\tEND\tSTATUS \n"

#A task instance
class TaskIns(object):

     #Constructor (should only be invoked with keyword parameters)
    def __init__(self, at, start, end, priority, name, bt):
        self.at    = at
        self.end      = end
        self.usage    = 0
        self.priority = priority
        self.name     = name.replace("\n", "")
        self.id = int(random.random() * 10000)
        self.bt = bt
        self.run_time = 0
        self.start = start
        self.finish = 0
    def name_cmp(self, other):
    	if self.name == other.name:
       	 return 1
       	else:
       		return -1
    	return 0

    #Allow an instance to use the cpu (periodic)
    def use(self, usage):
        global out, run_time
        self.run_time = run_time+clock_step-1
        self.usage += usage
        self.start = self.run_time
        self.finish = self.start + clock_step
        if self.usage >= self.bt:
            self.status = "Finish"
        else:
            self.status = " "
        out += str(self.run_time) + "\t" + str(on_cpu.name) +"\t"+ str(self.at)+"\t" + str(self.bt)+"\t"  + str(self.start) +"\t"+ str(clock_step) +"\t"+ str(self.priority) +"\t"+ str(self.finish)+"\t"+  str(self.status) 
        
        self.wt(self.status)
        if self.usage >= self.end - self.at:
            return True
            self.start=0
        return False
        self.start=0
        
    def wt(self, status):
            if self.status=="Finish":
        	print "%s arrived at %s started at %s last started at  %s and finished at %s" %(self.name, self.at, self.start, self.start, self.finish) 
    
    #Default representation
    #def __repr__(self):
    #    return str(self.name) + "#" + str(self.id) + " - at: " + str(self.at) + " priority: " + str(self.priority) + budget_text

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
    html_color = { 'T1':'red', 'T2':'blue', 'T3':'green', 'T4':'aqua', 'T5':'coral', 'Ideal':'grey', 'Finish':'black'}
    taskfile = open('../pi/tasks.txt')
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
                priority = start + task_type.period
                tasks.append(TaskIns(at=task_type.arrival_time, start=start, end=end, priority=priority, name=task_type.name, bt=task_type.burst_time))

    #Html output at
    html = "Content-type:text/html\r\n\r\n"
    html = """
    <!DOCTYPE html><html><head><title>LLF Scheduling</title></head><body>
           <meta name="viewport" content="width=device-width, initial-scale=1">
	<style>
	table {
    border-collapse: collapse;
    border-spacing: 0;
    width: 100%;
    border: 1px solid #ddd;
		}

	th, td {
    text-align: left;
    padding: 8px;
		}

	tr:nth-child(even){background-color: #f2f2f2}
	</style>
   <title> Sucess </title>
   		<div style="overflow-x:auto">
		<table> <tr>

		"""
    #Check utilization
    utilization = 0
    for task_type in task_types:
        utilization += float(task_type.burst_time) / float(task_type.period)
    if utilization > 1:
        out += 'Utilization error!'
        html += '<br /><br />Utilization error!<br /><br />'

    #Simulate clock
    clock_step = 1
    run_time = 0
    for i in xrange(0, hyperperiod, clock_step):
        #Fetch ready_list tasks that can use cpu and sort by priority
        ready_list = []
        for t in tasks:
            if t.at <= i:
                ready_list.append(t)
        ready_list = sorted(ready_list, priority_cmp)

        #Select task with highest priority
        # Print Tasks
        if len(ready_list) > 0:
            on_cpu = ready_list[0]
            done_list.append(on_cpu)
            html += '<td style="background-color:' + html_color[on_cpu.name] + ';">' + on_cpu.name + '</td>' + '\n'
           # on_cpu.priority += clock_step
            if on_cpu.use(clock_step):
                tasks.remove(on_cpu)
                run_time += clock_step
                #out += "\n"
                # Not Print Finish as it is showing on Gantt chart
                #html += '<td style="text-align: center; width: 10px; height: 50px; background-color:' + html_color['Finish'] + ';"></td>'  + '\n'
               # out += "Finish!" ,
            else:
            	# Processor is not used but runtime is going
            	run_time += clock_step
            	
        else:
            out += str(run_time) + '\t No task uses the processor. '
            # Processor is not used but runtime is going
            run_time += clock_step
            html += '<td style="background-color:' + html_color['Ideal'] + ';">I</td>'  + '\n'
        out += "\n"
            

    #out += remaining periodic tasks
    html += "<br /><br />"
    for p in tasks:
        out += p.get_unique_name() + " is dropped due to overload!"
        html += "<p>" + p.get_unique_name() + " is dropped due to overload!</p>"
    
    #Table done, print period below table
    html += "</tr>"
    # at New row to print runtime
    html += "<tr>"
    for run_time in range(0, hyperperiod+1) :
    	html +='<td style="padding: 8px 8px 8px 0px;">' + str(run_time) + '</td>'
       
    #Html output end
    html += "</body></html>"
    html_show = open('../pi/rm_html_show.html', 'w')
    html_show.write(html)
    html_show.close()
    out_show = open('../pi/rm_out_show.txt', 'w')
    out_show.write(out)
    out_show.close()

