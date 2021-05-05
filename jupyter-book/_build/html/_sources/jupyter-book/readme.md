## Build a jupyter-book

1. Install the most up to date version of [jupyter-book](https://jupyterbook.org):
```bash
pip install git+https://github.com/executablebooks/jupyter-book
```

1. Go to the root directory of the repository and run:
```bash
jupyter-book build . --path-output jupyter-book/.
```

1. Open Jupyter-book at `jupyter-book/_build/html/index.html`

## Build a pdf version of the jupyter-book

1. Install [pyppeteer](https://pypi.org/project/pyppeteer/)

1. Go to the root directory of the repository and run:
```bash
jupyter-book build . --builder pdfhtml --path-output jupyter-book/.   
```

1. Open `jupyter-book/_build/pdf/book.pdf`
