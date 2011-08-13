#!/usr/bin/python

import re

f = open("../chap1.tex")
data = f.read()
f.close()

data = data.replace("``", '"')
data = data.replace("''", '"')

data = data.replace("\n\n", "<br>")

plob = re.findall("(\\\\thoughtbreak)", data)
for i in plob:
	data = data.replace(i, " * * * ")

plob = re.findall("(\\\\textbf\{(.*?)\})", data)
for i in plob:
	data = data.replace(i[0], "<b>" + i[1] + "</b>")

plob = re.findall("(\\\\subsubsection\{(.*?)\})", data)
for i in plob:
	data = data.replace(i[0], "<h4>" + i[1] + "</h4>")

plob = re.findall("(\\\\subsection\{(.*?)\})", data)
for i in plob:
	data = data.replace(i[0], "<h3>" + i[1] + "</h3>")

plob = re.findall("(\\\\section\{(.*?)\})", data)
for i in plob:
	data = data.replace(i[0], "<h2>" + i[1] + "</h2>")

plob = re.findall("(\\\\chapter\{(.*?)\})", data)
for i in plob:
	data = data.replace(i[0], "<h1>" + i[1] + "</h1>")

plob = re.findall("(\\\\begin\{trenches\}(.*?)\\\\end\{trenches\})", data, re.S)
for i in plob:
	data = data.replace(i[0], '<div style="padding:10px;">' + i[1] + "</div>")

plob = re.findall("(\\\\begin\{callout\}(.*?)\\\\end\{callout\})", data, re.S)
for i in plob:
	data = data.replace(i[0], '<div style="padding:20px;border:3px solid #000">' + i[1] + "</div>")

plob = re.findall("(\\\\index\{(.*?)\})", data)
for i in plob:
	data = data.replace(i[0], "")

f = open("testout.html", "w")
f.write(data)
f.close()
