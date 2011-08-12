all: pdf cleantmp
quick: quickpdf cleantmp
clean: cleantmp cleanpdf

print:
	xelatex '\def\mediaformat{print}\input{gitt}'
	makeindex gitt
	xelatex '\def\mediaformat{print}\input{gitt}'
	xelatex '\def\mediaformat{print}\input{gitt}'

pdf:
	xelatex '\def\mediaformat{screen}\input{gitt}'
	makeindex gitt
	xelatex '\def\mediaformat{screen}\input{gitt}'
	xelatex '\def\mediaformat{screen}\input{gitt}'

screen: pdf

quickpdf:
	xelatex gitt

cleantmp:
	rm -f *.aux *.log *.out *.toc *.idx *.ind *.ilg

cleanpdf:
	rm -f gitt.pdf
