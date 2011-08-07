all: pdf cleantmp
quick: quickpdf cleantmp
clean: cleantmp cleanpdf

print:
	pdflatex print
	makeindex print
	pdflatex print
	pdflatex print

pdf:
	pdflatex gitt
	makeindex gitt
	pdflatex gitt
	pdflatex gitt

quickpdf:
	pdflatex gitt

cleantmp:
	rm -f *.aux *.log *.out *.toc *.idx *.ind *.ilg

cleanpdf:
	rm -f gitt.pdf
