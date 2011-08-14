all: pdf cleantmp
quick: quickpdf cleantmp
clean: cleantmp cleanpdf
web: images html

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

html:
	mkdir -p site/images
	rm -f site/*.html
	rm -f site/images/*
	python scripts/htmlbuild.py
	cp images/f*.png site/images/

images:
	
