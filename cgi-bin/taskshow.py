#!/usr/bin/python
import cgi, cgitb 
import string
import random
print 'Content-type:text/html\r\n\r\n'
form = cgi.FieldStorage()  #trying cgi method

html = """
<html>
<title>Thesis</title>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="/Aux/w3/w3.css"> <!--relative path dosn't work -->
<link rel="stylesheet" href="/Aux/w3/new.css"> <!--relative path dosn't work -->
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
    <div class="w3-container w3-third">
    <h2 class="w3-text-teal" id="tasklist" >Default Task List </h2>
    <iframe name="tasklist" input type="text" id="info" src="../default_tasks.txt" width=105% height="300px" >
    </iframe> <p>
    <form id="def_task" action="txtHtml.py" method="post" target="tasktable" >
    <button class="w3-button w3-black w3-hover-green"  id="default"  name="default" value="default" onclick="defcheck()"  >Check Tasks List</button> 
    </form>
    <form id="edit_task" action="../upload.html" method="post" target="tasklist" >
    <button class="w3-button w3-black w3-hover-green" >Edit Tasks List</button>
    </form>
    <form id="algo_post" action="txtHtml.py" method="post" target="tasktable"> 
        <input type="checkbox" checked> Use Above Task Table 
    
    </form>
    </div>
    """
# Function Defined earlier

html += """
<script>
function deefcheck() {
var y = document.getElementById("def_post")
var z = document.getElementById("t_check")
    if (z)
     { y.action = "cgi-bin/taskshow.py" 
      alert("Using Default Task Table"); }
    else 
    { var cust;
    if (confirm("Use Custom Task Table ? ")) {
        y.action = "info/edfinfo.html" 
        cust = "Using Custom Task Table";
    } else {
        cust = "Using Default Task Table";
        y.action = "info/rmsinfo.html"
    } }
}
</script>
"""

algorithm = form.getvalue('algo')
algo_script = form.getfirst('algo_post')
html += """
    <div class="w3-twothird w3-container">
	<h2 class="w3-text-teal" id="tasktable" > Task Table </h2>
        Selected Algorithm is:   <input type="text" id="result" value=%s >
        %s Will be executed. 
        """ %(algorithm , algo_script)
html += """
        
 	<iframe name="tasktable" input type="text" id="info" width=100% height="300px">
      	</iframe>
      	<!img src="/home/ashish/proj/html/img/pi3.png" alt="Raspberry Pi" >
      	<!--<p class="w3-border w3-padding-large w3-padding-32 w3-center">AD</p>
      	<p class="w3-border w3-padding-large w3-padding-64 w3-center">AD</p>
      	-->
    </div>
  </div>
"""

html += """
</body>
</html>
"""
print html
