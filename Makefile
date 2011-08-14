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

cleanimages:
	rm site/images/*.png

html:
	mkdir -p site/images
	rm -f site/*.html
	rm -f site/images/*
	python scripts/htmlbuild.py
	cp images/f*.png site/images/

images:
	inkscape -f images/source/af2-d1.svg -D -d 150 -e site/images/f-af2-d1.png
	inkscape -f images/source/af2-d2.svg -D -d 150 -e site/images/f-af2-d2.png
	inkscape -f images/source/af2-d3.svg -D -d 150 -e site/images/f-af2-d3.png
	inkscape -f images/source/af4-d2.svg -D -d 150 -e site/images/f-af4-d2.png
	inkscape -f images/source/w1-d1.svg -D -d 150 -e site/images/f-w1-d1.png
	inkscape -f images/source/w1-d2.svg -D -d 150 -e site/images/f-w1-d2.png
	inkscape -f images/source/w1-d3.svg -D -d 150 -e site/images/f-w1-d3.png
	inkscape -f images/source/w2-d1.svg -D -d 150 -e site/images/f-w2-d1.png
	inkscape -f images/source/w4-d1.svg -D -d 150 -e site/images/f-w4-d1.png
	inkscape -f images/source/w4-d2.svg -D -d 150 -e site/images/f-w4-d2.png
	inkscape -f images/source/w4-d3.svg -D -d 150 -e site/images/f-w4-d2.png
	inkscape -f images/source/w4-d2.svg -D -d 150 -e site/images/f-w4-d2.png
	inkscape -f images/source/w4-d3.svg -D -d 150 -e site/images/f-w4-d3.png
	inkscape -f images/source/w4-d4.svg -D -d 150 -e site/images/f-w4-d4.png
	inkscape -f images/source/w4-d5.svg -D -d 150 -e site/images/f-w4-d5.png
	inkscape -f images/source/w4-d6.svg -D -d 150 -e site/images/f-w4-d6.png
	inkscape -f images/source/w7-d1.svg -D -d 150 -e site/images/f-w7-d1.png
	inkscape -f images/source/w7-d2.svg -D -d 150 -e site/images/f-w7-d2.png
	inkscape -f images/source/w7-d3.svg -D -d 150 -e site/images/f-w7-d3.png
	inkscape -f images/source/w7-d4.svg -D -d 150 -e site/images/f-w7-d4.png
	inkscape -f images/source/w7-d5.svg -D -d 150 -e site/images/f-w7-d5.png
	inkscape -f images/source/w7-d6.svg -D -d 150 -e site/images/f-w7-d6.png
	inkscape -f images/source/w7-d7.svg -D -d 150 -e site/images/f-w7-d7.png
