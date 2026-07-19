
HELP_MESSAGE := "Available targets:\\n"
HELP_MESSAGE := $(HELP_MESSAGE)"help\\t\\t: this message (default)\\n"
help:
	@echo $(HELP_MESSAGE)

MAKEFLAGS += --always-make

LATEXMK = latexmk
INTERACTION = -interaction=batchmode
LUALATEX = lualatex
FLAGS = -$(LUALATEX) $(INTERACTION)
EXTRA_MEM = hash_extra=2000000 max_strings=2000000
TIMER = /usr/bin/time -l
VERAPDF = /Applications/verapdf/verapdf
PDFVERIFY = $(HOME)/Library/CloudStorage/Dropbox/programming/java/PDFverify
BFOPDF = $(PDFVERIFY)/bfopdf/bfopdf.jar
JOBNAME = TRENCH_DIFFEQ

HELP_MESSAGE := $(HELP_MESSAGE)"pdf\\t\\t: compile with latexmk\\n"
pdf:
	$(EXTRA_MEM) $(LATEXMK) $(FLAGS) $(JOBNAME)

HELP_MESSAGE := $(HELP_MESSAGE)"timed\\t\\t: time one compilation with lualatex\\n"
timed:
	$(EXTRA_MEM) $(TIMER) $(LUALATEX) $(INTERACTION) $(JOBNAME)

HELP_MESSAGE := $(HELP_MESSAGE)"verapdf\\t\\t: validate with veraPDF\\n"
verapdf:
	$(VERAPDF) $(JOBNAME).pdf

HELP_MESSAGE := $(HELP_MESSAGE)"bfopdf\\t\\t: validate with BFO\\n"
bfopdf:
	java -cp \"$(BFOPDF):$(PDFVERIFY)\" PDFverify $(JOBNAME).pdf

TEX_COMMANDS := $(TEX_COMMANDS) --add-tex-command="autoref p"
TEX_COMMANDS := $(TEX_COMMANDS) --add-tex-command="eqref p"
TEX_COMMANDS := $(TEX_COMMANDS) --add-tex-command="iftoggle p"
TEX_COMMANDS := $(TEX_COMMANDS) --add-tex-command="href p"
TEX_COMMANDS := $(TEX_COMMANDS) --add-tex-command="hyperref o"
TEX_COMMANDS := $(TEX_COMMANDS) --add-tex-command="label p"
TEX_COMMANDS := $(TEX_COMMANDS) --add-tex-command="nameref p"
TEX_COMMANDS := $(TEX_COMMANDS) --add-tex-command="personHref p"
TEX_COMMANDS := $(TEX_COMMANDS) --add-tex-command="ref p"
TEX_COMMANDS := $(TEX_COMMANDS) --add-tex-command="zcref op"

# to add newword to the aspell dictionary:
# echo "*newword\n#" | aspell -a
# --personal=valid_words.txt should work, but doesn't seem to
HELP_MESSAGE := $(HELP_MESSAGE)"misspellings\\t: check spelling\\n"
misspellings:
	echo '' > misspellings.txt
	for filename in text/*.tex ; do \
		echo "\\n$$filename misspellings:\\n" >> misspellings.txt ; \
		cat $$filename | aspell --mode=tex --ignore=3 $(TEX_COMMANDS) list \
		|  grep -vFf valid_words.txt \
		>> misspellings.txt ; \
	done
