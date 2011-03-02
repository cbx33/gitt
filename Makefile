all: clean pdf html

pdf:
	pdflatex gitt.tex

html:
	latex2html -html 4.0,unicode,latin1,utf8 -split 2 gitt.tex 

clean:
	rm gitt -Rf
