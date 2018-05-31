#!/usr/bin/python
import cgi, cgitb
import string
import random
import os
print 'Content-type:text/html\r\n\r\n'
print """
<form action = "" method = "post">
<select name = "dropdown">
<option value = "Maths" selected>Maths</option>
<option value = "Physics">Physics</option>
</select>
<input type = "submit" value = "Submit"/>
</form>
"""
print '<html><head><title>DM Scheduling</title></head><body>'

    #Check utilization
print '<br /><br />Utilization!<br /><br />'
form = cgi.FieldStorage()
if form.getvalue('dropdown') == "Maths":
        os.system('python task1.py')

print '</body></html>'
~                       
