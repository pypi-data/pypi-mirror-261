# ipymario

## Installation

```sh
pip install ipymario
```

## Development installation

Create a virtual environment and and install ipymario in *editable* mode with the
optional development dependencies:

```sh
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

All is set to open `example.ipynb` in JupyterLab, VS Code, or your favorite editor
to start developing. Any change made in the `js` folder will be directly reflected
in the notebook.
