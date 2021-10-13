#!/usr/bin/python37all
import cgi
import json

print("Content-type: text/html\n\n")
data = cgi.FieldStorage()
s1 = data.getvalue('LED')
print("selection = " + data.getvalue('LED'))
s2 = data.getvalue('slider')
print("Content-type: text/html\n\n")
print("Duty Cycle = " + data.getvalue('slider'))
data = {"menu_choice":s1, "slider":s2}
with open('led_brightness_multiple.txt','w') as f:
  json.dump(data,f)
