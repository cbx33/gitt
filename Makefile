all: pdf html

pdf:
	pdflatex gitt.tex
	pdflatex gitt.tex
	pdflatex gitt.tex

html:
	latex2html -html 4.0,unicode,latin1,utf8 -split 2 gitt.tex 

clean:
	rm gitt -Rf
	rm -f *.aux *.log *.out *.toc gitt.pdf

join:
	pdfjoin images/source/fcover.pdf gitt.pdf --rotateoversize 'false' --outfile output.pdf

final: pdf join

