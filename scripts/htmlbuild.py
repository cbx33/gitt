#!/usr/bin/python

import re
import sys
import os

NAVIGATION = open("html/nav.html").read()
NAV = []
NO_CHAPS = 9
NO_AF = 8
CHAPHEAD = open("html/chap-head.html").read()
CHAPFOOT = open("html/chap-foot.html").read()
TOCFILE = "gitt.tex"

IMAGEBLOCK = """<center><table  border="0" cellpadding="0" cellspacing="0" class="image_float_left">
                    <tr>
                      <td style="padding:10px;"><img src="***SOURCE***" width="400" ></td>
                      <td class="fade_right">&nbsp;</td>
                    </tr>
                    <tr>
                      <td class="fade_bot_image"><div align="center">***CAPTION***</div></td>
                      <td class="fade_corner">&nbsp;</td>
                    </tr>
                  </table></center>"""

def mung(data):
		
	data = data.replace(">", "&gt;") 
	data = data.replace("<", "&lt;")

	plob = re.findall("(\\\\index\{(.*?)\})", data)
	for i in plob:
		data = data.replace(i[0], "")

	plob = re.findall("(\\\\indexgit\{(.*?)\})", data)
	for i in plob:
		data = data.replace(i[0], '<span style="font-family:monospace;">git ' + i[1] + '</span>')

	plob = re.findall("(\\\\(.*?)\{(.*?)\}\n\n)", data, re.M)
	for i in plob:
		data = data.replace(i[0], i[0].replace("\n\n", "<br>"))

	plob = re.findall("(\n\n\\\\(.*?)\{(.*?)\})", data, re.M)
	for i in plob:
		data = data.replace(i[0], i[0].replace("\n\n", "<br>"))

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

	string = "\\begin{itemize}\n\\item Testing\n\\item Testing2\n\\item \\begin{itemize}\n \item tt\n\\end{itemize}\n\\end{itemize}\n"
	#plob = re.findall("(\\\\begin\{itemize\}((.*?)(?!\\\\begin\{itemize\})(.*?))\\\\end\{itemize\})", string, re.S)
	plob = re.findall("(\\\\begin\{itemize\}(((?!\\\\begin\{itemize\}).)*?)\\\\end\{itemize\})", string, re.S)
	while len(plob) != 0:
		print plob
		for i in plob:
			#print i[1]
			string = string.replace(i[0], i[1])
		plob = re.findall("(\\\\begin\{itemize\}(((?!\\\\begin\{itemize\}).)*?)\\\\end\{itemize\})", string, re.S)

	#NEED TO ITERATE UNTIL ALL LISTS ARE FOUND.....SO BASICALLY FIND A LIST WHICH DOES NOT CONTAIN A LIST AND PROCESS....AD INFIN
	#plob = re.findall("(\\\\begin\{itemize\}((.*?)\\\\end\{itemize\}))", data, re.S)
	#plob = re.findall("(\\\\begin\{itemize\}((.*?)(?!\\\\end\{itemize\})(.*?)\\\\end\{itemize\}))", data, re.S)
	plob = re.findall("(\\\\begin\{itemize\}(((?!\\\\begin\{itemize\}).)*?)\\\\end\{itemize\})", data, re.S)
	while len(plob) != 0:
		for i in plob:
			data = data.replace(i[0], '<div style="padding-left:10px;"><ul>' + i[1] + "</ul></div>")
			listd = i[1]
			nasty = re.findall("(\\\\item(.*?)((?=\\\\item)|(?=\\\\end\{itemize\})))", listd, re.S)
			for j in nasty:
				data = data.replace(j[0], '<li>' + j[1].strip() + '</li>'+"\n")
		plob = re.findall("(\\\\begin\{itemize\}(((?!\\\\begin\{itemize\}).)*?)\\\\end\{itemize\})", data, re.S)

	plob = re.findall("(\\\\begin\{enumerate\}((.*?)\\\\end\{enumerate\}))", data, re.S)
	for i in plob:
		data = data.replace(i[0], '<div style="padding-left:10px;"><ol>' + i[2] + "</ol></div>")
		listd = i[1]
		nasty = re.findall("(\\\\item(.*?)((?=\\\\item)|(?=\\\\end\{enumerate\})))", listd, re.S)
		for j in nasty:
			data = data.replace(j[0], '<li>' + j[1].strip() + '</li>'+"\n")

	plob = re.findall("(\\\\begin\{code\}\n*(.*?)\\\\end\{code\})", data, re.S)
	for i in plob:
		code = i[1].replace("\n", "<br>\n")
		bolded = re.findall("(.*?@.*?:.*?\$.*?<br>)\n", code)
		
		tb = []
		
		for linebold in bolded:
			if not linebold in tb:
				tb.append(linebold)
		for boldline in tb:
			code = code.replace(boldline, '<strong>' + boldline + '</strong>')
		
		data = data.replace(i[0], '<div id="codeblock">' + code + "</div>")
		
	plob = re.findall("(\\\\figuregit\{(.*?)\}\{(.*?)\}\{(.*?)\})", data, re.S)
	for i in plob:
		fignum = re.search("([0-9]+).(png|pdf)", i[2])
		data = data.replace(i[0], return_image(i[2].replace(".pdf", ".png").replace("images/", "images/chaps/"), 
							"<strong>Figure " + fignum.groups()[0] + "</strong><br>" + i[3]))

	plob = re.findall("(\\\\figuregith\{(.*?)\}\{(.*?)\}\{(.*?)\})", data, re.S)
	for i in plob:
		fignum = re.search("([0-9]+).(png|pdf)", i[2])
		data = data.replace(i[0], return_image(i[2].replace(".pdf", ".png").replace("images/", "images/chaps/"), 
							"<strong>Figure " + fignum.groups()[0] + "</strong><br>" + i[3]))

	plob = re.findall("(\\\\begin\{callout\}\{(.*?)\}\{(.*?)\}(.*?)\\\\end\{callout\})", data, re.S)
	for i in plob:
		data = data.replace(i[0], '<div id="calloutblock"><h3>' + i[1] + ' - ' + i[2] + '</h3>' + i[3] + "</div>")
	
	data = data.replace("\\ ", "&nbsp;")
	data = data.replace("\n\n\n", "<br><br>")
	data = data.replace("\n\n", "<br><br>")
	
	return data

def fix_file(data, prefix="file", index=""):
	chaps = re.match(".*?\\chapter\{.*?\}\n(.*)", data, re.S)
	chap = chaps.groups()[0]
	sections = re.findall("(\\\\section\{.*?\}.*?)((?=\\\\section)|($))", data, re.S)
	b = 1
	for j in sections:
		f_output = open("site/"+prefix+index+"-"+str(b)+".html", "w")
		f_output.write(CHAPHEAD.replace("***NAV***", NAVIGATION) + "<h1>Week " + index + "</h1>" + mung(j[0]) + CHAPFOOT)
		f_output.close()
		b += 1

def fix_simple_file(data, filename):
	f_output = open("site/"+filename+".html", "w")
	f_output.write(CHAPHEAD.replace("***NAV***", NAVIGATION) + mung(data) + CHAPFOOT)
	f_output.close()

def return_image(filename, caption):
	return(IMAGEBLOCK.replace("***SOURCE***", filename).replace("***CAPTION***", caption))

def alltex():
	navigation = ""
	f = open("gitt.tex")
	data = f.read()
	f.close()
	info = re.findall(r"\\mainmatter(.*?)\\backmatter", data, re.S)
	files = re.findall(r"\\include\{(.*)\}", info[0])
	for filename in files:
		if "chap" in filename:
			b = 1
			chapname = re.findall(r"\\chapter\{(.*?)\}", open(filename+".tex").read(), re.S)
			secname = re.findall(r"\\section\{(.*?)\}", open(filename+".tex").read(), re.S)
			navigation += '<strong>' + chapname[0] + '</strong><br>' + "\n"
			for section in secname:
				section_done = section.replace("''", '"').replace("``", '"')
				day = re.findall("(.*?)-(.*)", section_done)
				if not len(day) == 0:
					navigation += '<span>&bull; ' + day[0][0] + '</span> - <a href="' + filename + '-'+str(b)+'.html">' + day[0][1] + "</a><br>\n"
				else:
					navigation += '&bull;&nbsp;&nbsp;<a href="' + filename + '-'+str(b)+'.html">' + section_done + "</a><br>\n"
				b += 1
			navigation += '<div class="divider"></div>' + "\n"
		elif "afterhour" in filename:
			b = 1
			chapname = re.findall(r"\\chapter\{(.*?)\}", open(filename+".tex").read(), re.S)
			secname = re.findall(r"\\section\{(.*?)\}", open(filename+".tex").read(), re.S)
			navigation += '<strong>' + chapname[0] + '</strong><br>' + "\n"
			for section in secname:
				section_done = section.replace("''", '"').replace("``", '"')
				day = re.findall("(.*?)-(.*)", section_done)
				if not len(day) == 0:
					navigation += '<span>&bull; ' + day[0][0] + '</span> - <a href="' + filename + '-'+str(b)+'.html">' + day[0][1] + "</a><br>\n"
				else:
					navigation += '&bull;&nbsp;&nbsp;<a href="' + filename + '-'+str(b)+'.html">' + section_done + "</a><br>\n"
				b += 1
			navigation += '<div class="divider"></div>' + "\n"
		else:
			chapname = re.findall(r"\\chapter\{(.*?)\}", open(filename+".tex").read(), re.S)
			secname = re.findall(r"\\section\{(.*?)\}", open(filename+".tex").read(), re.S)
			navigation += '<strong>' + chapname[0] + '</strong><br>' + "\n"
			for section in secname:
				section_done = section.replace("''", '"').replace("``", '"')
				day = re.findall("(.*?)-(.*)", section_done)
				if not len(day) == 0:
					navigation += '<span>&bull; ' + day[0][0] + '</span> - <a href="' + filename + '.html">' + day[0][1] + "</a><br>\n"
				else:
					navigation += '&bull;&nbsp;&nbsp;<a href="' + filename + '.html">' + section_done + "</a><br>\n"
			navigation += '<div class="divider"></div>' + "\n"
	f = open("html/nav.html", "w")
	f.write(navigation)
	f.close()

def allchaps():
	for i in range(NO_CHAPS):
		f_input = open("chap"+str(i+1)+".tex")
		data = f_input.read()
		f_input.close()
		fix_file(data, prefix="chap", index=str(i+1))

def allafterhours():
	for i in range(NO_AF):
		f_input = open("afterhours"+str(i+1)+".tex")
		data = f_input.read()
		f_input.close()
		fix_file(data, prefix="afterhours", index=str(i+1))

def singlefile(filename):
	f_input = open(filename + ".tex")
	data = f_input.read()
	f_input.close()
	fix_simple_file(data, filename)

def buildnav():
	info = os.listdir("site/")
	print info
	

if len(sys.argv) < 2:
	print "Need to give me something to go on here"
else:
	if sys.argv[1] == "allchaps":
		allchaps()
	elif sys.argv[1] == "alltex":
		alltex()
	elif sys.argv[1] == "allafterhours":
		allafterhours()
	elif sys.argv[1] == "nav":
		buildnav()
	else:
		singlefile(sys.argv[1])
