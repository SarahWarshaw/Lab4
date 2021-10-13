#!/usr/bin/python37all
import cgi
import json

print("Content-type: text/html\n\n")
data = cgi.FieldStorage()
s1 = data.getvalue('LED')
s2 = data.getvalue('slider')
data = {"menu_choice":s1, "slider":s2}
with open('led_brightness_multiple.txt','w') as f:
  json.dump(data,f)

print("""
Content-type:text/html\n\n
<html>
<head>
<meta http-equiv="refresh" content="30">
</head>
<body>
<div style="width:600px;background:#71F282;border:1px;text-align:center">
<br>
<font size="3" color = "black" face = "helvetica">
<b>LED Brightness</b>
<br>
""")

if s1 ==13:
  print('RED LED BRIGHTNESS = %s' %s2) 
elif s1 ==19:
  print('WHITE LED BRIGHTNESS = %s' %s2) 
else:
  print('BLUE LED BRIGHTNESS = %s' %s2) 


print("""
<form action = "/cgi-bin/led_brightness.py" method = "POST">
  <input type = "radio" name = "LED" value = "13" checked> LED 1<br>
  <input type = "radio" name = "LED" value = "19"> LED 2<br>
  <input type = "radio" name = "LED" value = "26"> LED 3<br>
  <input type ="range" name = "slider" min = "0" max="100" value="0"><br>
  <input type="submit" value = "Change LED brightness">
</form>
</div>
</body>
</html>
""")