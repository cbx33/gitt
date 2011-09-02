#!/usr/bin/python

import re
import sys
import os
from munger import mung

NAV = []
NO_CHAPS = 9
NO_AF = 8

NAVIGATION = open("html/nav.html").read()

CHAPHEAD = open("html/chap-head.html").read()
CHAPFOOT = open("html/chap-foot.html").read()

BASEHEAD = open("html/base-head.html").read()
BASEFOOT = open("html/base-foot.html").read()

TOCFILE = "gitt.tex"

NAVLINKS = re.findall(r"""<a href="([^"]*)">""", NAVIGATION)

PREV_BUT = """<p align="left"><a href="***PREV_URL***"><img src="images/prev.png" alt="Previous Day" height="29" border="0"></a></p>"""

NEXT_BUT = """<p align="right"><a href="***NEXT_URL***"><img src="images/next.png" alt="Next Day" height="29" border="0"></a></p>"""

PREV_NEXT = """<table border="0" cellpadding="0" cellspacing="0" width="100%">
					<tr>
						<td>***PREV_BUT***</td>
						<td>***NEXT_BUT***</td>
					</tr>
				</table>"""

IMAGE_BLOCK = """<center><table  border="0" cellpadding="0" cellspacing="0" class="image_float_left">
                    <tr>
                      <td style="padding:10px;"><img src="***SOURCE***" width="400" ></td>
                      <td class="fade_right">&nbsp;</td>
                    </tr>
                    <tr>
                      <td class="fade_bot_image"><div align="center">***CAPTION***</div></td>
                      <td class="fade_corner">&nbsp;</td>
                    </tr>
                  </table></center>"""

def get_prev_next(filename):
	linknum = NAVLINKS.index(filename)
	prev_but = ""
	next_but = ""
	if linknum - 1 >= 0:
		prev_but = PREV_BUT.replace("***PREV_URL***", NAVLINKS[linknum - 1])
	if linknum + 1 < len(NAVLINKS):
		next_but = NEXT_BUT.replace("***NEXT_URL***", NAVLINKS[linknum + 1])
	return PREV_NEXT.replace("***PREV_BUT***", prev_but).replace("***NEXT_BUT***", next_but)

def fix_file(data, prefix="file", index=""):
	chaps = re.match(".*?\\chapter\{.*?\}\n(.*)", data, re.S)
	chap = chaps.groups()[0]
	sections = re.findall("(\\\\section\{.*?\}.*?)((?=\\\\section)|($))", data, re.S)
	b = 1
	for j in sections:
		filename = prefix+index+"-"+str(b)+".html"
		f_output = open("site/"+filename, "w")
		f_output.write(CHAPHEAD.replace("***NAV***", NAVIGATION) + "<h1>Week " + index + "</h1>" + mung(j[0], IMAGE_BLOCK) + get_prev_next(filename) + CHAPFOOT)
		f_output.close()
		b += 1

def fix_simple_file(data, filename):
	f_output = open("site/"+filename+".html", "w")
	f_output.write(CHAPHEAD.replace("***NAV***", NAVIGATION) + mung(data, IMAGE_BLOCK) + get_prev_next(filename + ".html") + CHAPFOOT)
	f_output.close()

def build_simple_file(filename):
	f_output = open("site/"+filename+".html", "w")
	f_output.write(BASEHEAD + open("html/" + filename + ".html").read() + BASEFOOT)
	f_output.close()

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

def baseconvert(bformat="pdf"):
	files = os.listdir("./")
	for nfile in files:
		if ".tex" in nfile:
			dp = mung(open(nfile).read(), IMAGE_BLOCK, bformat=bformat)
			open("build/" + os.path.splitext(nfile)[0] + ".html", "w").write(dp)

def baseconcat():
	stringer = ""
	f = open("gitt.tex")
	data = f.read()
	f.close()
	info = re.findall(r"\\mainmatter(.*?)\\backmatter", data, re.S)
	files = re.findall(r"\\include\{(.*)\}", info[0])
	for filename in files:
		stringer += open("build/" + os.path.splitext(filename)[0] + ".html").read() + "\n"
	open("build/complete.html", "w").write(stringer)

def buildnav():
	info = os.listdir("site/")
	return info

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
	elif sys.argv[1] == "baseconvert":
		if len(sys.argv) > 2:
			baseconvert(sys.argv[2])
		else:
			baseconvert()
	elif sys.argv[1] == "baseconcat":
		baseconcat()
	elif sys.argv[1] == "simple":
		build_simple_file(sys.argv[2])
	else:
		singlefile(sys.argv[1])
