# Installation

Green Ideas can be installed by the Python package manager `pip`
or by cloning the repository and installing by hand. 

Installation via `pip` is recommended if you simply want to use
the package. 

## Install with pip
Installing Green Ideas with pip is as simple as:

```bash
pip install greenideas
```

You can then import the relevant classes (see [usage](usage.md))
and use Green Ideas in your project.

## Clone the git repository

If you want to contribute to or fork Green Ideas, you'll want to
clone the git repository and work with the code directly:

```bash
git clone https://github.com/chrishengler/greenideas.git
cd greenideas
poetry install
```

### Dictionaries
If you choose to work with the repository and want to use the default
English language dictionaries, you will need to also get the dictionary
repository. In your `greenideas` directory, run:

```bash
git submodule init
git submodule update
```
