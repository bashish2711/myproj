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
<link rel="stylesheet" href="../w3/w3.css"> <!--relative path dosn't work -->
<link rel="stylesheet" href="../w3/w3-theme-black.css">
<link rel="stylesheet" href="../w3/Roboto.css">
<link rel="stylesheet" href="../w3/font-awesome.min.css">
<style>
html,body,h1,h2,h3,h4,h5,h6 {font-family: "Roboto", sans-serif;}
.w3-sidebar {
  z-index: 3;
  width: 250px;
  top: 43px;
  bottom: 0;
  height: inherit;
}
</style>
<body>

<!-- Navbar -->
<div class="w3-top">
  <div class="w3-bar w3-theme w3-top w3-left-align w3-large">
    <a class="w3-bar-item w3-button w3-right w3-hide-large w3-hover-white w3-large w3-theme-l1" href="javascript:void(0)" onclick="w3_open()">
    <i class="fa fa-bars"></i> </a>   
    <a href="../index.html" class="w3-bar-item w3-button w3-hide-small w3-hover-white">HOME</a>
    <a href="theory.html" class="w3-bar-item w3-button w3-hide-small w3-hover-white">THEORY</a>
    <a href="#" class="w3-bar-item w3-button w3-hide-small w3-hover-white">SIMULATOR</a>
    <a href="pi.html" class="w3-bar-item w3-button w3-hide-small w3-hover-white">RASPBERRY PI</a>
  </div>
</div>
<!--#include virtual ="table.html" -->


<!-- Main content: shift it to the right by 250 pixels when the sidebar is visible -->
  <div class="w3-padding-64">
    <div class="w3-container">
    
<div class= "w3-third" >
      <h1 class="w3-text-teal" id="H3" >Simulator Page </h1>
    <form action="#" method="post" class="demoForm" id="demoForm">
    <fieldset>
        <legend>Select a Scheduling Algorithm</legend>

"""
# RMS, EDF, LLF, RR, PRR, FCFS, SPN, SRT, HRRN, MLFQ
for algo in ("RMS", "EDF", "LLF", "RR", "PRR", "FCFS", "SPN", "SRT", "HRRN", "MLFQ"):
	html += '<input type="radio" value=%s name="algo"> %s <br>' %(algo , algo) 
html += """
    <p>
        <label>Total: $ <input type="text" name="total" class="num" value="8" readonly="readonly" /></label>
    </p>
    </fieldset>
</form>

     <p> <button class="w3-button w3-black w3-hover-green">Select</button> <p>
    </div> <!-- w3-third -->
<div class="w3-twothird w3-container" id="info">
<fieldset>
        <legend>Algorithm Property</legend>   
      <iframe name="Iframe1" src="result.txt" width=100%> 
      </iframe>
</fieldset>
</div>
</div>
</div>


  <footer id="myFooter">
    <div class=" w3-bottombar w3-container w3-theme-l2 w3-padding-small">
      <h4>Footer</h4>
    </div>
  </footer>

<!-- END MAIN -->
</div>
<script>
var algo = document.forms['demoForm'].elements['algo'];
for (var i=0, len=sz.length; i<len; i++) {
    algo[i].onclick = function() { // assign onclick handler function to each
        this.form.elements.total.value = this.value;
    };
}


</body>
</html>
"""
print html

