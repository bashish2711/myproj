#!/usr/bin/python
#Particle Swarm OPtimization scheduling implementation

import string
import random
import fractions


def _lcm(a,b): return abs(a * b) / fractions.gcd(a,b) if a and b else 0

def lcm(a):
    return reduce(_lcm, a)

# Import modules for CGI handling 
import cgi, cgitb
import os
def func1(x):
    total=0
    for i in range(len(x)):
        total+=x[i]**2
    return total
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
   <a href=/pso_html_show.html target=_new> HTML Gantt Chart </a>
   <a href=/pso_out_show.txt target=_new> Text Log File </a>
   <p> Gantt Chart </p>
   <iframe name="Iframe2" frameborder="0" scrolling="no" width=100% onload="this.style.height=this.contentDocument.body.scrollHeight+20 +'px';" src="/pso_html_show.html" > </iframe>
   <p> Run Log </p>
   <iframe name="Iframe1" frameborder="0" scrolling="no" width=100% onload="this.style.height=this.contentDocument.body.scrollHeight +'px';" src="/pso_out_show.txt"> </iframe> 
   
   </body>
</html>
"""

out = "Content-type:text/html\r\n\r\n"
out += "RunTime\tName\tArrival\tBT\tStart\tUSE\tPRI\tEND\tSTATUS \n"

#A task instance as swarm particle
class Particle:
    def __init__(self,x0):
        self.position_i=x0          # particle position
        self.velocity_i=[]          # particle velocity
        self.period = []
        self.burst_time = []
        self.pos_best_i=[]          # best position individual
        self.err_best_i=-1          # best error individual
        self.err_i=-1               # error individual

        for i in range(0,num_dimensons):
            self.velocity_i.append(random.uniform(-1,1))

    # evaluate current fitness
    def evaluate(self,costFunc):
        self.err_i=costFunc(self.position_i)

        # check to see if the current position is an individual best
        if self.err_i < self.err_best_i or self.err_best_i==-1:
            self.pos_best_i=self.position_i
            self.err_best_i=self.err_i

    # update new particle velocity
    def update_velocity(self,pos_best_g):
        w=0.5       # constant inertia weight (how much to weigh the previous velocity)
        c1=1        # cognative constant
        c2=2        # social constant

        for i in range(0,num_dimensions):
            r1=random.random()
            r2=random.random()

            vel_cognitive=c1*r1*(self.pos_best_i[i]-self.position_i[i])
            vel_social=c2*r2*(pos_best_g[i]-self.position_i[i])
            self.velocity_i[i]=w*self.velocity_i[i]+vel_cognitive+vel_social

    # update the particle position based off new velocity updates
    def update_position(self,bounds):
        for i in range(0,num_dimensions):
            self.position_i[i]=self.position_i[i]+self.velocity_i[i]

            # adjust maximum position if necessary
            if self.position_i[i]>bounds[i][1]:
                self.position_i[i]=bounds[i][1]

            # adjust minimum position if neseccary
            if self.position_i[i] < bounds[i][0]:
                self.position_i[i]=bounds[i][0]
                
class PSO():
    def __init__(self,costFunc,x0,bounds,num_particles,maxiter):
        global num_dimensions

        num_dimensions=len(x0)
        err_best_g=-1                   # best error for group
        pos_best_g=[]                   # best position for group

        # establish the swarm
        swarm=[]
        for i in range(0,num_particles):
            swarm.append(Particle(x0))

        # begin optimization loop
        i=0
        while i < maxiter:
            #print i,err_best_g
            # cycle through particles in swarm and evaluate fitness
            for j in range(0,num_particles):
                swarm[j].evaluate(costFunc)

                # determine if current particle is the best (globally)
                if swarm[j].err_i < err_best_g or err_best_g == -1:
                    pos_best_g=list(swarm[j].position_i)
                    err_best_g=float(swarm[j].err_i)

            # cycle through swarm and update velocities and position
            for j in range(0,num_particles):
                swarm[j].update_velocity(pos_best_g)
                swarm[j].update_position(bounds)
            i+=1

        # print final results
        print 'FINAL:'
        print pos_best_g
        print err_best_g

if __name__ == '__main__':
    html_color = { 'T1':'red', 'T2':'blue', 'T3':'green', 'T4':'aqua', 'T5':'coral', 'T6':'red', 'T7':'blue', 'T8':'green', 'T9':'aqua', 'T10':'coral', 'Ideal':'grey', 'Finish':'black'}
    taskfile = open('../pi/tasks.txt')
    lines = taskfile.readlines()
    task_types = []
    tasks = []
    hyperperiod = []
    done_list = []
    num_dimensons = 90
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
            task_types.append(Particle(x0=line[0], burst_time=line[1], period=line[2]))
            #task_types.append(Particle(arrival_time=line[0], burst_time=line[1], period=line[2], deadline=line[3], name=name))
    #Calculate hyperperiod
    for task_type in task_types:
        hyperperiod.append(task_type.period)
    hyperperiod = lcm(hyperperiod)
    #Create task instances 
    for i in xrange(0, hyperperiod):
        for task_type in task_types:
            if  (i - task_type.arrival_time) % task_type.period == 0 and i >= task_type.arrival_time:
                start = i
                end = start + task_type.burst_time
                priority = start
                Particle(x0=task_type.arrival_time)

    #Html output at
    html = "Content-type:text/html\r\n\r\n"
    html = """num_dimensions
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
    padding: 9px;
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

        #Select task with highest priority
        # Print Tasks
        PSO(func1,initial,bounds,num_particles=15,maxiter=30)
        if len(ready_list) > 0:
            on_cpu = ready_list[0]
            done_list.append(on_cpu)
            html += '<td style="background-color:' + html_color[on_cpu.name] + ';">' + on_cpu.name + '</td>' + '\n'
            #on_cpu.priority += clock_step
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
            out += runtime, '\n No task uses the processor. '
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
    html_show = open('../pi/pso_html_show.html', 'w')
    html_show.write(html)
    html_show.close()
    out_show = open('../pi/pso_out_show.txt', 'w')
    out_show.write(out)
    out_show.close()
    print html
    print out

