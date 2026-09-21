# Markdown Generator

This directory contains various ways of creating Markdown for your site. In general, filenames that end with `.ipynb` or `.py` are similar, but may contain different documentation or are intended to be run from with GitHub when deploying your site.

## Python Scripts

The .py files are Python scripts that that can be run from the command line (ex., `python3 publications.py publications.csv`) with the objective of also ensuring that they have reduced requirements for packages, which may allow them to run when deploying your site from within GitHub.

## Jupyter Notebooks

### Publications from BibTeX

`files/freire.bib` is the source for the publication page. Install the parser and run the generator from the repository root:

```bash
python3 -m pip install -r requirements-publications.txt
python3 scripts/generate_publications.py
```

The command regenerates `_publications/` and removes stale entries. GitHub Actions runs it automatically when `files/freire.bib` changes.

These .ipynb files are Jupyter notebook files that convert a TSV containing structured data about talks (`talks.tsv`) or presentations (`presentations.tsv`) into individual markdown files that will be properly formatted for the academicpages template. The notebooks contain a lot of documentation about the process.
