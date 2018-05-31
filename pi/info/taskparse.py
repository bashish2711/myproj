#!/usr/bin/python
import cgi, cgitb 
import string
import random
print 'Content-type:text/html\r\n\r\n'
form = cgi.FieldStorage()  #trying cgi method

infile = form.getvalue('in')
outfile = form.getvalue('out')
algoposted = form.getvalue('algo_post')

print infile, outfile, algoposted
