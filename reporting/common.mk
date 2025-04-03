# Shared Makefile rules

# Find the main .tex file in the current directory.
TEX_FILES := $(wildcard *.tex)
MAIN_TEX := $(firstword $(TEX_FILES))
MAIN_NAME := $(basename $(MAIN_TEX))
MAIN_PDF := build/$(MAIN_NAME).pdf

.PHONY: all clean build format

# Default target builds the PDF.
all: build

# Build the PDF.
build: $(MAIN_PDF)

$(MAIN_PDF): $(MAIN_TEX) $(MAIN_NAME).bib
	mkdir -p build
	latexmk -pdf -bibtex -outdir=build $(MAIN_TEX)

# Format the document.
format:
	latexindent -m -l=../indentconfig.yaml -w $(MAIN_TEX)

# Clean build artifacts.
clean:
	rm -rf build/