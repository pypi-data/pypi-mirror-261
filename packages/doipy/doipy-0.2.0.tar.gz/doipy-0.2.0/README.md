# DOIPY

## Install

Simply run

```shell
$ pip install doipy
```

## Usage

This `doipy` package has two methods:

* `hello(name: str)`: say hello to the input name.
* `create(files: list[BinaryIO])`: loop through a list of files and do something.

To use it in the Command Line Interface, run:

```shell
$ doipy hello <username> <password>
# DOIP requires user authentication for 0.DOIP/Op.Hello

$ doipy create file1 file2 file3
# Output of the create command

$ doipy search <query string> --username <username> --password <password>
```

To use it in the Python code simply import it and call the exposed methods.

```python
from doipy import hello, create

hello(name='John')

with open('file1.txt', 'rb') as file1, open('file2.png', 'rb') as file2:
    create(files=[file1, file2])
```

## For developer

The project is managed by [Poetry](https://python-poetry.org/). Therefore, make sure that Poetry is installed in your
system. Then run

```shell
$ poetry install
```

to install all dependencies.

Then, install `doipy` package in editable mode. To do so, under the root directory, run:

```shell
$ pip install --editable .
```
## Create FDO 

1) create a digital object (DO) of the data bitstream
`doipy create <file> --md-file <md-file> --client-id <client-id> --password <password>`
note down the "id" of the created DO.
2) create a digital object (DO) of the metadata bitstream
`doipy create <metadata-file> --md-file <md-metadata-file> --client-id <client-id> --password <password>`
not down the "id" of the created DO.

3) Create FDO
`doipy create_fdo <id-data-DO> <id-metadata-DO>--client-id <client-id> --password <password>`
