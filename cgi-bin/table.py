#!/usr/bin/python
import os
import subprocess
print "Content-type:text/html\r\n\r\n"
os.system("python txtHtml.py")
print open("/var/www/pi/table.html").read()


