#!/usr/bin/python
import cgi, cgitb 
import string
import random
##########################################
## This is CGI Script and is called as "http://localhost/cgi-bin/txtHtml.py?in=default1&out=default1out"
## were default1 is input txt file name and default1out is output html file name
##########################################
print 'Content-type:text/html\r\n\r\n'
form = cgi.FieldStorage()  #trying cgi method , instantiation
infile = form.getvalue('in')
outfile = form.getvalue('out')
algoposted = form.getvalue('algo_post')
if (infile):
	print "infile is :" , infile
else:
	print "Please provide in file"
if (outfile):
	print "outfile is :" , outfile
else:
	print "Please provide out file"
print algoposted
#if (outfile):
#    outFile = open(outfile)
#else:
#    outFile = open(
#    outFile = open('sample_tasks.txt')
taskfile = open(infile)   
print taskfile 
lines = taskfile.readlines()
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