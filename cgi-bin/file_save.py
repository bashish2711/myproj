#!/usr/bin/python

import cgi, os
import cgitb; cgitb.enable()
print "Content-Type: text/html\n"
form = cgi.FieldStorage()

# Get filename here.
fileitem = form['filename']
# Test if the file was uploaded
if fileitem.filename:
   # strip leading path from file name to avoid 
   # directory traversal attacks
   fn = os.path.basename(fileitem.filename)
   # for windows machine:
   #fn = os.path.basename(fileitem.filename.replace("\\", "/" ))
   tasks = "deftask"
   path = open('/temp/' + tasks, 'wb')
   path.write(fileitem.file.read())
   message = 'The file "' + fn + '" was uploaded successfully'

else:
   message = 'No file was uploaded'
   
print """\
<html>
<body>
   <p>%s</p>
   <p> You can access file <a href=/cgi-bin/txtHtml.py?in=%s&out=customTaskOut target=_new>%s</a> now  </p>
</body>
</html>
""" % (message,tasks, fn)
