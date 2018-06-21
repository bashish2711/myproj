#!/usr/bin/python
import os
import subprocess
import cgi, cgitb
process = subprocess.Popen(['ls', '-a'], stdout=subprocess.PIPE)
out, err = process.communicate()
print "Content-type:text/html\r\n\r\n"
print("<p>" + out  + "</p>")

