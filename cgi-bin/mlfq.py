#!/usr/bin/python
import cgi, cgitb
print "Content-type:text/html\r\n\r\n"
form = cgi.FieldStorage()  #trying cgi method , instantiation
infile = form.getvalue('in')
#infile ='deftask1'
#outfile = infile + '.html'
print """
<html>
   <head> </head>
   <meta name="viewport" content="width=device-width, initial-scale=1">
	<style>
	table {
    border-collapse: collapse;
    border-spacing: 0;
    width: 100%;
    border: 1px solid #ddd;
		}

	th, td {
    text-align: left;
    /* padding: 8px; */
		}

	tr:nth-child(even){background-color: #f2f2f2}
	</style>
   <title> Not Implemented</title>
   <body>
   <h2> The code is not written </h2>

   </body>
</html>
"""
