#!/usr/bin/python
import cgi, cgitb , os
import string
import random
print 'Content-type:text/html\r\n\r\n'
form = cgi.FieldStorage()  #trying cgi method

html = """
<html>
<title>Thesis</title>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="/Aux/w3/w3.css"> 
<link rel="stylesheet" href="/Aux/w3/new.css"> 
<link rel="stylesheet" href="/Aux/w3/w3-theme-black.css">
<link rel="stylesheet" href="/Aux/w3/Roboto.css">
<link rel="stylesheet" href="/Aux/w3/font-awesome.min.css">
<body>

<!-- Navbar -->
<div class="w3-top">
  <div class="w3-bar w3-theme w3-top w3-left-align w3-large">
    <a class="w3-bar-item w3-button w3-right w3-hide-large w3-hover-white w3-large w3-theme-l1" href="javascript:void(0)" onclick="w3_open()">
    <i class="fa fa-bars"></i> </a>   
    <a href="../index.html" class="w3-bar-item w3-button w3-hide-small w3-hover-white">HOME</a>
    <a href="../theory.html" class="w3-bar-item w3-button w3-hide-small w3-hover-white">THEORY</a>
    <a href="../simulator.html" class="w3-bar-item w3-button w3-hide-small w3-hover-white">SIMULATOR</a>
    <a href="../pi.html" class="w3-bar-item w3-button w3-hide-small w3-hover-white">RASPBERRY PI</a>
  </div>
</div>
<div class="w3-main">
  <div class="w3-row w3-padding-64">
"""

algorithm = form.getvalue('algo')
task_list = {'RMS':'rm.py', 'EDF':'edf.py', 'LLF':'llf.py', 'RR':'rr.py', 'PRR':'prr.py', 'FCFS':'fcfs.py', 'SPN':'spn.py', 'SRT':'srt.py', 'HRRN':'hrrn.py', 'MLFQ':'mlfq.py'}
print algorithm
html += """
	<h2 class="w3-text-teal" id="tasktable" > Task Table </h2>
        Selected Algorithm is:   <input type="text" id="result" value=%s >
        %s Will be executed. 
        """ %(algorithm , algorithm)
html += """
 	<center> 
 	    <p>
        <iframe name="tasktable" input type="text" id="info" width=95% height="300px" src="/rr_html_show.html">
      	</iframe>
        </center>
    </div>
  </div>
"""
html += """
<center>
<form id="algomore" name="algomore" action="" method="post">
"""

for algor in task_list.keys():
	html += """
    <input type="radio" class="w3-radio" id= %s value= %s  name="algorithm" onclick="runner(this.value)"> %s </input>
     """ %(algor, algor, algor)
html += """
<p>
<button class="w3-button w3-black w3-hover-green">Select</button>
</form>    
</center>
"""
html += """
</body>


</html>
"""
print html
