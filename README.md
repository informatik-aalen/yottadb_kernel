# YottaDB-kernel for Jupyter Notebook

## Description

This is a kernel for the M-Language in YottaDB

https://yottadb.com/

https://docs.yottadb.com/ProgrammersGuide/index.html

![Beispiel](PastedGraphic-6.tiff)

## Installation

To install `yottadb_kernel` from source:

```
python setup.py install
python -m yottadb_kernel.install
```

Make sure that the YottaDB environment variables are set!

The following command must work in order to use the kernel:

```
$ydb_dist/ydb
```

Type the command as is and don't expand the `ydb_dist` variable in the
command above!

## Using the Echo kernel

**Notebook**: The *New* menu in the notebook should show an option for an
YottaDB notebook.

**Console frontends**: To use it with the console frontends, add
`--kernel yottadb` to their command line arguments.

## License
Published under MIT-license

## Author
Winfried Bantel, Aalen University
