#!/usr/bin/env python
import cgi
#import cgitb; cgitb.enable()  # for troubleshooting
import os, sys, os.path

print "Content-type: text/html\n\n"

form=cgi.FieldStorage()
if "subject":
    print "<h1>Nothing entered!.</h1>"
else:
   subject = form["subject"].value
   print "<P>{} chosed".format(subject)
   #then maybe this to run the scripts?
   mypath = /path/to/scripts/
   runcmd = mypath + subject
   os.system(runcmd)
