# Project Template

This repository provides a structured starting point for mechanical engineering
projects, which may include design, simulation, and experimental validation
work. It includes LaTeX reporting templates, an example Python analysis script,
and a directory for CAD files.

## Contents

### CAD

The `cad/` directory is intended to house CAD files, such as `.kcl` source
files, created during the project lifecycle.

### Analysis

The `analysis/` directory contains an example self-contained Python script that
uses
[uv](https://docs.astral.sh/uv/guides/scripts/#declaring-script-dependencies) to
manage dependencies:

```
uv run analysis/analysis_example.py
```

For more complex analysis work, it is recommended to establish a dedicated
virtual environment. uv is still the preferred tool for this purpose.

### Reporting

The `reporting/` directory contains LaTeX templates for generating high-quality
and easily version controlled reports. These templates are designed to provide a
baseline structure for document-centric engineering workflow, and can be
customised to suit the needs of the relevant organisation or project. They are
organised into three types:

- **Design Report**: `reporting/templates/design_report/`
- **Simulation & Analysis Report**:
  `reporting/templates/simulation_analysis_report/`
- **Test Report**: `reporting/templates/test_report/`

Each template includes:

- A `Makefile` to automate compilation using `latexmk`.
- A `bib` file for references.
- A logo placeholder in `assets/logo.pdf`.
- A `build/` directory containing generated PDF and auxiliary files.

#### Compiling a Report

To build a report, navigate into the desired template directory and run:

```
make
```

To format a given report, run:

```
make format
```

Note that it is advised that users create a new directory based on the relevant
template document directory for each new document. This can be achieved by
duplicating the relevant folder such that the `/assets` directory and `Makefile`
remain.

Note that you must ensure you have the required LaTeX toolchain installed (see
[Prerequisites](#prerequisites)).

## Supporting Files

Large binary files or additional supporting material that should not be stored
in Git should be stored elsewhere, e.g., in Dropbox, Google Drive, on a NAS etc.

When referencing such files, include links in this `README.md` or relevant
project documentation files.

## Prerequisites

To make full use of this template, install the following:

### Python & Analysis

- [Python 3.10+](https://www.python.org/)
- [uv](https://docs.astral.sh/uv/) for dependency management

### LaTeX & Reporting

It is strongly recommended that [TexLive 2025](https://www.tug.org/texlive/) is
installed. In addition, you will need:

- `latexmk` (included in most TeX distributions).
- `make` (for invoking the Makefiles).

To verify `latexmk` is available:

```
latexmk --version
```

## Additional Notes

A [`.prettierrc`](/.prettierrc) file is included to enforce consistent markdown
formatting, if required.

To check formatting:

```
npx prettier --check your_file.md
```

To automatically format:

```
npx prettier --write your_file.md
```

## VSCode Integration

The repository includes a `.vscode/settings.json` to configure project-local
editor behavior.
