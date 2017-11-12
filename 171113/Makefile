.PHONY: all clean

SVGS=$(wildcard *.svg)
SVGPDFS=$(patsubst %.svg,%.pdf,$(SVGS))

all: 171113.pdf

171113.pdf: 171113.tex $(filter-out 171113.pdf, $(wildcard *.tex 171113.*)) $(SVGPDFS)
	pdflatex -shell-escape "$<" && pdflatex -shell-escape "$<"

%.pdf: %.svg
	inkscape -D "--file=$<" "--export-pdf=$@"

clean:
	rm $(filter-out 171113.tex,$(wildcard 171113.*)) *.pdf >/dev/null 2>&1
