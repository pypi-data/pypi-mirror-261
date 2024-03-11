# Makefile
# 
# Converts Markdown to other formats (HTML, PDF, DOCX, RTF, ODT, EPUB) using Pandoc
# <http://johnmacfarlane.net/pandoc/>
#
# Run "make" (or "make all") to convert to all other formats
#
# Run "make clean" to delete converted files
# ========================================================
# path to PANDOC BINARY
PANDOC_BIN=!!
MATHJAX_URL=!!
PANDOC_FILTERS_PATH=!!
# ========================================================
### Markdown extension (e.g. md, markdown, mdown).
MEXT = md
## All markdown files in the working directory
SRC = $(wildcard *.$(MEXT))

DATEFMT := "%Y-%B-%d"
## DIFFTYPE is passed to latexdiff --type=$(DIFFTYPE)
## One of:
#     UNDERLINE CTRADITIONAL TRADITIONAL CFONT FONTSTRIKE INVISIBLE CHANGEBAR
#     CHANGEBAR CULINECHBAR CFONTCBHBAR BOLD PDFCOMMENT
DIFFTYPE := "CULINECHBAR"
#
# Convert all files in this directory that have a .md suffix
SRC := $(wildcard *.md)

HTML=$(SRC:.md=.html) 
PDF=$(SRC:.md=.pdf) 
DOCX=$(SRC:.md=.docx) 
RTF=$(SRC:.md=.rtf) 
ODT=$(SRC:.md=.odt) 
EPUB=$(SRC:.md=.epub) 
TEX=$(SRC:.md=.tex)

RM=/bin/rm -rf


PANDOC_FILTERS=--filter $(PANDOC_FILTERS_PATH)/pandoc-eqnos --filter $(PANDOC_FILTERS_PATH)/pandoc-fignos --filter $(PANDOC_FILTERS_PATH)/pandoc-tablenos --filter $(PANDOC_FILTERS_PATH)/pantable --filter $(PANDOC_FILTERS_PATH)/pandoc-latex-admonition
PANDOC_OPTIONS=--standalone $(PANDOC_FILTERS) .revisions.yaml .settings.yaml
PANDOC_TAIL_OPTIONS=

PANDOC_HTML_OPTIONS=--to html5 --toc --css=.style/styling.css --mathjax=$(MATHJAX_URL) --number-sections
PANDOC_PDF_OPTIONS=--template=.style/styling.latex
PANDOC_DOCX_OPTIONS=
PANDOC_RTF_OPTIONS=
PANDOC_ODT_OPTIONS=
PANDOC_EPUB_OPTIONS=--to epub3
PANDOC_TEX_OPTIONS=--template=.style/styling.latex

TEMP= *.aux *.lof *.lot *.out *.toc


# Pattern-matching Rules

%.html : %.md
	$(PANDOC_BIN) $(PANDOC_OPTIONS) $(PANDOC_HTML_OPTIONS) -o $@ $< $(PANDOC_TAIL_OPTIONS) 

%.pdf : %.md
	$(PANDOC_BIN) $(PANDOC_OPTIONS) $(PANDOC_PDF_OPTIONS) -o $@ $< $(PANDOC_TAIL_OPTIONS) 
	
%.docx : %.md
	$(PANDOC_BIN) $(PANDOC_OPTIONS) $(PANDOC_DOCX_OPTIONS) -o $@ $< $(PANDOC_TAIL_OPTIONS) 

%.rtf : %.md
	$(PANDOC_BIN) $(PANDOC_OPTIONS) $(PANDOC_RTF_OPTIONS) -o $@ $< $(PANDOC_TAIL_OPTIONS) 

%.odt : %.md
	$(PANDOC_BIN) $(PANDOC_OPTIONS) $(PANDOC_ODT_OPTIONS) -o $@ $< $(PANDOC_TAIL_OPTIONS) 

%.epub : %.md
	$(PANDOC_BIN) $(PANDOC_OPTIONS) $(PANDOC_EPUB_OPTIONS) -o $@ $< $(PANDOC_TAIL_OPTIONS) 

%.tex : %.md
	$(PANDOC_BIN) $(PANDOC_OPTIONS) $(PANDOC_TEX_OPTIONS) -o $@ $< $(PANDOC_TAIL_OPTIONS) 

# Targets and dependencies

.PHONY: all clean

all : clean prepro $(HTML) $(PDF) $(DOCX) $(RTF) $(ODT) $(EPUB) $(TEX)

clean: 
	- $(RM) $(HTML) $(PDF) $(DOCX) $(RTF) $(ODT) $(EPUB) $(TEX) $(TEMP)

html: clean prepro $(HTML)
pdf: clean prepro $(PDF)
docx: clean prepro $(DOCX)
rtf: clean prepro $(RTF)
odt: clean prepro $(ODT)
epub: clean prepro $(EPUB)
tex: clean prepro $(TEX)

init:
	pproj init

prepro:
	pproj prepro

commit:
	pproj commit 

rollback:
	pproj rollback

pdfdiff:
	pproj pdfdiff --type $(DIFFTYPE)

source:
	$(PANDOC_BIN)  --extract-media=./fig -o $(MD_TARGET) $(MD_SOURCE)

serve:
	pproj serve 


