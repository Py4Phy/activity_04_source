NAME  := assignment
LATEX := $(NAME).tex
PDF   := $(NAME).pdf

TEX := $(SKELETON)/tex

%.pdf: %.tex
	pdflatex -shell-escape $<
	pdflatex -shell-escape $<

.phony: all see

all: $(PDF)

see: $(PDF)
	open $^



