#!/usr/bin/python

import re

NO_CHAPS = 9
NO_AF = 8

def mung(data):
	data = data.replace(">", "&gt;") 
	data = data.replace("<", "&lt;")

	data = data.replace("``", '"')
	data = data.replace("''", '"')

	data = data.replace("\\%", "%")
	data = data.replace("\\$", "$")

	data = data.replace("\\LaTeX", "LaTeX")

	data = data.replace("\\%", "&#37;")
	data = data.replace("\\_", "_")
	data = data.replace("\\newline", "")

	data = data.replace("\\ldots", "...")
	data = data.replace("\\textasciitilde{}", "~")
	data = data.replace("\\textasciitilde", "~")
	data = data.replace("\\textasciicircum", "^")
	data = data.replace("\{", "{")
	data = data.replace("\}", "}")

	plob = re.findall("(%.*?\n)", data, re.M)
	for i in plob:
		data = data.replace(i, "")
		
	plob = re.findall("(\\\\index\{(.*?)\})", data)
	for i in plob:
		data = data.replace(i[0], "")

	plob = re.findall("(\\\\indexgit\{(.*?)\})", data)
	for i in plob:
		data = data.replace(i[0], '<span style="font-family:monospace;">git ' + i[1] + '</span>')

	plob = re.findall("(\\\\clearpage)", data)
	for i in plob:
		data = data.replace(i, "")

	plob = re.findall("(\\\\cleardoublepage)", data)
	for i in plob:
		data = data.replace(i, "")

	plob = re.findall("(\\\\thoughtbreak)", data)
	for i in plob:
		data = data.replace(i, " * * * ")

	plob = re.findall("(\\\\textbf\{(.*?)\})", data)
	for i in plob:
		data = data.replace(i[0], "<strong>" + i[1] + "</strong>")

	plob = re.findall("(\\\\emph\{(.*?)\})", data)
	for i in plob:
		data = data.replace(i[0], "<em>" + i[1] + "</em>")

	plob = re.findall("(\\\\rotatebox\{(.*?)\}\{(.*?)\})", data)
	for i in plob:
		data = data.replace(i[0], i[2])

	plob = re.findall("(\\\\texttt\{(.*?)\})", data)
	for i in plob:
		data = data.replace(i[0], '<span style="font-family:monospace;">' + i[1] + "</span>")

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
		data = data.replace(i[0], '<div id="trenchblock"><strong>In the trenches...</strong><br>' + i[1] + "</div>")

	plob = re.findall("(\\\\begin\{center\}(.*?)\\\\end\{center\})", data, re.S)
	for i in plob:
		data = data.replace(i[0], '<center>' + i[1] + "</center>")

	plob = re.findall("(\\\\begin\{table\}(.*?)\\\\end\{table\})", data, re.S)
	for i in plob:
		data = data.replace(i[0], i[1])
		
	plob = re.findall("(\\\\begin\{tabular\}\{(.*?)\}(.*?)\\\\end\{tabular\})", data, re.S)
	for i in plob:
		data = data.replace(i[0], "<table>" + i[2] + "</table>")
		listd = i[2]
		nasty = re.findall(r"((.*?)([\\ ]*)\\hline)", i[2], re.S)
		for j in nasty:
			itemstr = ""
			items = j[1].split(" & ")
			for item in items:
				itemstr += "<td>" + item + "</td>"
			row = "<tr>" + itemstr + "</tr>"
			data = data.replace(j[0], row)

	plob = re.findall("(\\\\begin\{itemize\}((.*?)\\\\end\{itemize\}))", data, re.S)
	for i in plob:
		data = data.replace(i[0], '<div style="padding:10px;"><ul>' + i[2] + "</ul></div>")
		listd = i[1]
		nasty = re.findall("(\\\\item(.*?)((?=\\\\item)|(?=\\\\end\{itemize\})))", listd, re.S)
		for j in nasty:
			data = data.replace(j[0], '<li>' + j[1].strip() + '</li>'+"\n")

	plob = re.findall("(\\\\begin\{enumerate\}((.*?)\\\\end\{enumerate\}))", data, re.S)
	for i in plob:
		data = data.replace(i[0], '<div style="padding:10px;"><ol>' + i[2] + "</ol></div>")
		listd = i[1]
		nasty = re.findall("(\\\\item(.*?)((?=\\\\item)|(?=\\\\end\{enumerate\})))", listd, re.S)
		for j in nasty:
			data = data.replace(j[0], '<li>' + j[1].strip() + '</li>'+"\n")

	plob = re.findall("(\\\\begin\{code\}\n*(.*?)\\\\end\{code\})", data, re.S)
	for i in plob:
		#code = i[1].replace("\n\n", "<br>\n<br>\n")
		code = i[1].replace("\n", "<br>\n")
		#bolded = re.findall("(^.*?@.*?:.*?\$.*?<br>)\n", code)
		bolded = re.findall("(.*?@.*?:.*?\$.*?<br>)\n", code)
		
		data = data.replace(i[0], '<div id="codeblock">' + code + "</div>")
		for boldline in bolded:
			data = data.replace(boldline, '<strong>' + boldline + '</strong>')


	plob = re.findall("(\\\\figuregit\{(.*?)\}\{(.*?)\}\{(.*?)\})", data, re.S)
	for i in plob:
		data = data.replace(i[0], '<img src="' + i[2].replace(".pdf", ".png") + '"><br>' + i[3] + "<br>")

	plob = re.findall("(\\\\figuregith\{(.*?)\}\{(.*?)\}\{(.*?)\})", data, re.S)
	for i in plob:
		data = data.replace(i[0], '<img src="' + i[2].replace(".pdf", ".png") + '"><br>' + i[3] + "<br>")

	plob = re.findall("(\\\\begin\{callout\}\{(.*?)\}\{(.*?)\}(.*?)\\\\end\{callout\})", data, re.S)
	for i in plob:
		data = data.replace(i[0], '<div id="calloutblock"><h3>' + i[1] + ' - ' + i[2] + '</h3>' + i[3] + "</div>")
	
	data = data.replace("\\ ", "&nbsp;")
	data = data.replace("\n\n", "<br><br>")
	
	return data

def fix_file(data, prefix="file", index=""):
	chaps = re.match(".*?\\chapter\{.*?\}\n(.*)", data, re.S)
	chap = chaps.groups()[0]
	#sections = re.findall("\\section\{.*?\}(.*)((?=\\\\section)|($))", data, re.S)
	sections = re.findall("(\\\\section\{.*?\}.*?)((?=\\\\section)|($))", data, re.S)
	b = 1
	for j in sections:
		f_output = open("site/"+prefix+index+"-"+str(b)+".html", "w")
		f_output.write(CHAPHEAD + mung(j[0]) + CHAPFOOT)
		f_output.close()
		b += 1

CHAPHEAD = open("html/chap-head.html").read()
CHAPFOOT = open("html/chap-foot.html").read()

for i in range(NO_CHAPS):
	f_input = open("chap"+str(i+1)+".tex")
	data = f_input.read()
	f_input.close()
	fix_file(data, prefix="chap", index=str(i+1))


for i in range(NO_AF):
	f_input = open("afterhours"+str(i+1)+".tex")
	f_output = open("site/afterhours"+str(i+1)+".html", "w")
	data = f_input.read()
	f_input.close()
	str_data = mung(data)
	f_output.write(str_data)
	f_output.close()
