#!/usr/bin/python
import cgi, cgitb 
import string
import random
print 'Content-type:text/html\r\n\r\n'
form = cgi.FieldStorage()  #trying cgi method , instantiation
infile = form.getvalue('in')
outfile = form.getvalue('out')
if (infile) && open(infile):
	print "infile is :" , infile
else:
	print "Please provide in file"
if (outfile):
	print "outfile is :" , outfile
else:
	print "Please provide out file"

#if (outfile):
#    outFile = open(outfile)
#else:
#    outFile = open(
#    outFile = open('sample_tasks.txt')
taskfile = open(infile)   
print taskfile 
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
    width: 80%;
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
html += "<center> <table><h2>" 
for header in "Name", "A.T.", "B.T", "Period", "Deadline":
	html += "<th> %s </th>" %header
	
html += "<tr>"
for line in lines[3:]:  # three lines are excluded for comments
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
            
html += "</table> \n </center> \n"
html += "</body> \n </html>"
output = open(outfile, 'w')
output.write(html)
output.close()
print html       
