# Project Template

This repository contains template project resources intended for use during
internal mechanical engineering projects.

## Contents

### CAD

The `cad` directory is intended to house CAD (`.kcl`) files produced during the
project.

### Reporting

The `reporting` directory contains two template markdown files:

- [`report-template-design.md`](/reporting/report-template-design.md) is the
  suggested structure for documenting mechanical design work.

- [`report-template-simulation-analysis.md`](/reporting/report-template-simulation-analysis.md)
  is the suggested structure for documenting simulation or analyis work, whether
  analytical and hand-coded, or conducted using third-party simulation tools.

Note that markdown format has been chosen to facilitate both version control and
any subsequent rework/reuse of the content.

### Analysis

The `analysis` directory contains an example of a self-contained python script,
which manages dependencies via
[uv's script dependency support](https://docs.astral.sh/uv/guides/scripts/#declaring-script-dependencies).

This can be run using:

```bash
uv run analysis/analysis_example.py
```

However, for any more in-depth work, it is likely preferable to establish a
dedicated virtual environment and suitable code structure.

### Additional Notes

Thre repo also contains a [`.prettierrc`](/.prettierrc) file which is intended
to provide standardised styling for markdown files.

To check a given file, use:

```bash
npx prettier --check <your_file.md>
```

To format a specific file:

```bash
npx prettier --write <your_file.md>
```
