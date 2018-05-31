#!/usr/bin/python
import cgi, cgitb 
import string
import random
print 'Content-type:text/html\r\n\r\n'
form = cgi.FieldStorage()  #trying cgi method

html = """
<html>
<style>
  .hide { position:absolute; top:-1px; left:-1px; width:1px; height:1px; }
</style>

<iframe name="hiddenFrame"></iframe>

<form action="txtHtml.py" method="post" target="hiddenFrame">
  <input name="signed" type="checkbox">
  <input value="Save" type="submit">
</form>
<body>

<iframe id="myFrame" src="/info/table.html" style="height:380px;width:100%"></iframe>

<p>Click the "Tryit" button to hide the first H1 element in the iframe (another document).</p>

<button onclick="myFunction()">Try it</button>

<script>
function myFunction() {
  var iframe = document.getElementById("myFrame");
  var elmnt = iframe.contentWindow.document.getElementsByTagName("H2")[0];
  elmnt.style.display = "none";
}
</script>

</body>
</html>
"""
print html
    
    
