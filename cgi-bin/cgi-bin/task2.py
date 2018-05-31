#!/usr/bin/python
import cgi, cgitb 
import string
import random
print 'Content-type:text/html\r\n\r\n'
print """
<form action = "/cgi-bin/task3.py" method = "post" target = "_blank">
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


print '</body></html>'
