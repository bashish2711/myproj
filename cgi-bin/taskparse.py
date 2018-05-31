#!/usr/bin/python
import cgi, cgitb 
import string
import random
print 'Content-type:text/html\r\n\r\n'
form = cgi.FieldStorage()  #trying cgi method
sel = form.getvalue('which_algo')
algo =  {'RMS':'rm.py', 'EDF':'edf.py', 'LLF':'llf.py', 'RR':'rr.py', 'PRR':'prr.py', 'FCFS':'fcfs.py',
'SPN':'spn.py', 'SRT':'srt.py', 'HRRN':'hrrn.py', 'MLFQ':'mlfq.py'}
var = algo.keys()
for k in var:
	if sel == k: 
		code = algo[k]
html = """
<!DOCTYPE html>
<html>
<title>Thesis</title>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="/Aux/w3/w3.css"> <!--relative path dosn't work -->
<link rel="stylesheet" href="/Aux/w3/new.css"> <!--relative path dosn't work -->
<link rel="stylesheet" href="/Aux/w3/w3-theme-black.css">
<link rel="stylesheet" href="/Aux/w3/Roboto.css">
<link rel="stylesheet" href="/Aux/w3/font-awesome.min.css">
<head> 
<script>
  function resizeIframe(obj) {
    obj.style.height = obj.contentWindow.document.body.scrollHeight + 'px';
  }
</script>
</head>
<body>

        <iframe name="Iframe1" input type="text" id="info" frameborder="0" scrolling="no" width=100%% onload="this.style.height=this.contentDocument.body.scrollHeight +'px';" src=%s>
                 <p id="demo"></p>
        </iframe>
""" %(code)
print html
