#!/usr/bin/python
taskfile = open('tasks.txt')
lines = taskfile.readlines()
task_types = []
tasks = []
hyperperiod = []
html = """
<html>
<meta HTTP-EQUIV="REFRESH" content="60">
<head><title>TXT to html</title></head>
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
</head>
"""

    #Allocate task types
html += "<table width=50% border=1 align="center" style="margin: 0px auto;" > <caption><h2>Task Table</h2></caption>" 
for header in "Name", "A.T.", "B.T", "Period", "Deadline":
	html += "<th> %s </th>" %header
	
html += "<tr>"
for line in lines[1:]:
    line = line.split('\t') 
    if len(line) == 5:
    	html += "<td> %s </td>" %line[4]
    elif len(line) == 4:
    	name = 'Task'
    	html += "<td> %s </td>" %name
    	  
    for i in range (0,4):
        line[i] = int(line[i])
        html += "<td> %s </td>" %line[i]

    html += "</tr>"
            
html += "<table>"
html += "</body></html>"
output = open('/var/www/pi/table.html', 'w')
output.write(html)
output.close()
       
