#!/usr/bin/python
import cgi, cgitb 
import string
import random
##########################################
## This is CGI Script and is called as "http://localhost/cgi-bin/outHtml.py?in=infile&out=outfile"
## were default1 is input txt file name and default1out is output html file name
##########################################
print 'Content-type:text/html\r\n\r\n'
form = cgi.FieldStorage()  #trying cgi method , instantiation
infile = form.getvalue('in')
outfile = form.getvalue('out')
algoposted = form.getvalue('algo_post')
#print infile, outfile
#infile="fcfs_out_show.txt"
#outfile="fcfs_out_show.html"
#print infile
infile="../pi/" + infile
outfile="../pi/" + outfile
#print infile, outfile
#if (infile):
#	print "infile is :" , infile
#else:
#	print "Please provide in file"
#if (outfile):
#	print "outfile is :" , outfile
#else:
#	print "Please provide out file"
#print algoposted
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
for header in "RunTime", "Name", "Arrival Time","Burst Time", "Start Time", "Use", "Priority", "End Time" , "Status":
	html += "<th> %s </th>" %header
	
html += "<tr>"
for line in lines[3:]:  # three lines are excluded for comments
    line = line.split('\t') 
    for i in range (0,8):
        line[i] = str(line[i])
        html += "<td> %s </td>" %line[i]
    if len(line) == 9:
    	html += "<td> %s </td>" %line[8]
    #elif len(line) == 8:
    #	name = 'Task'
    #	html += "<td> %s </td>" %name
    #	  

    html += "</tr>"
            
html += "</table> \n </center> \n"
html += "</body> \n </html>"
output = open(outfile, 'w')
output.write(html)
output.close()
print html       
