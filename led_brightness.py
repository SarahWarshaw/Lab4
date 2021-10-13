#!/usr/bin/python37all
import cgi
import json

data = cgi.FieldStorage()
s1 = data.getvalue('menu_choice')
print("Content-type: text/html\n\n")
print("selection = " + s1)
s2 = data.getvalue('slider')
print("Content-type: text/html\n\n")
print("Duty Cycle = " + str(s2))
data = {"menu_choice":s1, "slider":s2}
with open('led_brightness_multiple.txt','w') as f:
  json.dump(data,f)
