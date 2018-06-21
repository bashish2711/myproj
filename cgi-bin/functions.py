import random
from llf import run_time
def html_head():
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
	"""

def cgi_start():
	out = "Content-type:text/html\r\n\r\n"
	out += "RunTime\tName\tArrival\tBT\tStart\tUSE\tPRI\tEND\tSTATUS \n"
	err = "Content-type:text/html\r\n\r\n"
	err += "<br> <b> Error Log: </b> \n"
	param = "Content-type:text/html\r\n\r\n"
	param += "Name\tArrival\tBT\tStart\tEND\tFinish\tResponse Time\tWaiting Time\tTurn Around Time \n"

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
        self.wt = 0
        self.tat = 0
        self.rt = 0
    def name_cmp(self, other):
    	if self.name == other.name:
       	 return 1
       	else:
       		return -1
    	return 0

    #Allow an instance to use the cpu (periodic)
    def use(self, usage):
        global out, run_time, param
        self.run_time = run_time+clock_step-1
        self.usage += usage
        self.start = self.run_time
        self.finish = self.start + clock_step
        self.wt = self.finish - self.at - self.bt
        self.tat = self.finish - self.at        
        self.rt = self.start - self.at

        if self.usage >= self.bt:
            self.status = "Finish"
        else:
            self.status = " "
        out += str(self.run_time) + "\t" + str(on_cpu.name) +"\t"+ str(self.at)+"\t" + str(self.bt)+"\t"  + str(self.start) +"\t"+ str(clock_step) +"\t"+ str(self.priority) +"\t"+ str(self.finish)+"\t"+  str(self.status) + "\n"
        if self.status == "Finish":
        	param += (self.name + "\t"+ str(self.at)+"\t"+  str(self.bt) +  "\t"+  str(self.finish) +  "\t"+  str(self.rt) + "\t"+  str(self.wt)+ "\t"+ str(self.tat)+"\t" +"\n")
        	return 1
        
        
        if self.usage >= self.end - self.at:
            return True
            self.start=0
        return False
        self.start=0
        
    def wt(self, status):
            global param
            if self.status=="Finish":
                return True
   
    #Default representation
    #def __repr__(self):
    #    return str(self.name) + "#" + str(self.id) + " - at: " + str(self.at) + " priority: " + str(self.priority) + budget_text

    #Get name as Name#id
    def get_unique_name(self):
        return str(self.name) + "#" + str(self.id)

