#!/usr/bin/python
import cgi, cgitb 
import string
import random
print 'Content-type:text/html\r\n\r\n'
form = cgi.FieldStorage()  #trying cgi method
algo =  {'RMS':'rm.py', 'EDF':'edf.py', 'LLF':'llf.py', 'RR':'rr.py', 'PRR':'prr.py', 'FCFS':'fcfs.py',
'SPN':'spn.py', 'SRT':'srt.py', 'HRRN':'hrrn.py', 'MLFQ':'mlfq.py'}
for key in form.keys():
	print algo[key]

