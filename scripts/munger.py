#####
# Munger.py - LaTeX converter to HTML  #
#             Peter Savage             #
                                   #####

import re

def mung(data, IMAGE_BLOCK="", base=False):

	data = data.replace(">", "&gt;")
	data = data.replace("<", "&lt;")

	plob = re.findall("(\\\\texttt\{(.*?)\})", data)
	for i in plob:
		data = data.replace(i[0], '<code class="ncode">' + i[1] + "</code>")

	plob = re.findall("(\\\\index\{(.*?)\})", data)
	for i in plob:
		data = data.replace(i[0], "")

	plob = re.findall("(\\\\indexgit\{(.*?)\})", data)
	for i in plob:
		data = data.replace(i[0], '<code class="ncode">git ' + i[1] + '</code>')

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
		if base == False:
			data = data.replace(i[0], '<div id="trenchblock"><strong>In the trenches...</strong><br>' + i[1] + "</div>")
		if base == True:
			data = data.replace(i[0], '<hr><div id="trenchblock"><strong>In the trenches...</strong><br>' + i[1] + "</div><hr>")

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

	plob = re.findall("(\\\\begin\{itemize\}(((?!\\\\begin\{itemize\}).)*?)\\\\end\{itemize\})", data, re.S)
	while len(plob) != 0:
		for i in plob:
			data = data.replace(i[0], '<div style="padding-left:10px;"><ul>' + i[1].strip() + "</ul></div>")
			listd = i[1]
			nasty = re.findall("(\\\\item(.*?)((?=\\\\item)|($)))", listd, re.S)
			for j in nasty:
				data = data.replace(j[0], '<li>' + j[1].strip() + '</li>'+"\n")
		plob = re.findall("(\\\\begin\{itemize\}(((?!\\\\begin\{itemize\}).)*?)\\\\end\{itemize\})", data, re.S)

	plob = re.findall("(\\\\begin\{enumerate\}(((?!\\\\begin\{enumerate\}).)*?)\\\\end\{enumerate\})", data, re.S)
	while len(plob) != 0:
		for i in plob:
			data = data.replace(i[0], '<div style="padding-left:10px;"><ol>' + i[1].strip() + "</ol></div>")
			listd = i[1]
			nasty = re.findall("(\\\\item(.*?)((?=\\\\item)|($)))", listd, re.S)
			for j in nasty:
				data = data.replace(j[0], '<li>' + j[1].strip() + '</li>'+"\n")
		plob = re.findall("(\\\\begin\{enumerate\}(((?!\\\\begin\{enumerate\}).)*?)\\\\end\{enumerate\})", data, re.S)

	plob = re.findall("(\\\\begin\{code\}\n*(.*?)\\\\end\{code\})", data, re.S)
	for i in plob:
		if base == False:
			code = i[1].replace("\n", "<br/>\n")
			bolded = re.findall("(.*?@.*?:.*?\$.*?<br>)\n", code)

			tb = []

			for linebold in bolded:
				if not linebold in tb:
					tb.append(linebold)
			for boldline in tb:
				code = code.replace(boldline, '<strong>' + boldline.replace("<br>","") + '</strong><br/>')
			data = data.replace(i[0], '<div id="codeblock"><code>' + code + "</code></div>")

		if base == True:
			ddta = ""
			code = i[1].split("\n")
			for line in code:
				ddta += "<code>" + line + "</code><br/>\n"
			data = data.replace(i[0], '<br><div id="codeblock">' + ddta.replace(" ", "&nbsp;") + "</div>")

	plob = re.findall("(\\\\figuregit\{(.*?)\}\{(.*?)\}\{(.*?)\})", data, re.S)
	for i in plob:
		fignum = re.search("([0-9]+).(png|pdf)", i[2])
		data = data.replace(i[0], return_image(i[2].replace(".pdf", ".png").replace("images/", "images/chaps/"),
							"<strong>Figure " + fignum.groups()[0] + "</strong><br>" + i[3],
							IMAGE_BLOCK))

	plob = re.findall("(\\\\figuregith\{(.*?)\}\{(.*?)\}\{(.*?)\})", data, re.S)
	for i in plob:
		fignum = re.search("([0-9]+).(png|pdf)", i[2])
		data = data.replace(i[0], return_image(i[2].replace(".pdf", ".png").replace("images/", "images/chaps/"),
							"<strong>Figure " + fignum.groups()[0] + "</strong><br>" + i[3],
							IMAGE_BLOCK))

	plob = re.findall("(\\\\begin\{callout\}\{(.*?)\}\{(.*?)\}(.*?)\\\\end\{callout\})", data, re.S)
	for i in plob:
		if base == False:
			data = data.replace(i[0], '<div id="calloutblock"><h3>' + i[1] + ' - ' + i[2] + '</h3>' + i[3] + "</div>")
		elif base == True:
			data = data.replace(i[0], '<hr><div id="calloutblock"><h3>' + i[1] + ' - ' + i[2] + '</h3>' + i[3] + "</div><hr>")

	data = data.replace("\\ ", "&nbsp;")
	data = data.replace("\n\n\n", "<br><br>")
	data = data.replace("\n\n", "<br><br>")

	return data
	
def return_image(filename, caption, IMAGE_BLOCK):
	return(IMAGE_BLOCK.replace("***SOURCE***", filename).replace("***CAPTION***", caption))
