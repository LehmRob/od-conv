# od-conv

This little project aims to convert gnosis.xml.pickle files to native python
pickle files. This is necessary to port the canfestival-od-editor to python3
https://github.com/sitec-systems/canfestival-od-editor.

## Usage

Use the `conv.py` script with an version of python2. If your distribution don't
ships a version of python2 any more use [pypy](https://www.pypy.org/).
For better differenting between the 'old' and the 'new' object dictionary use
another file extension for the new file (for example use odx)

    $ pypy conv.py -i canope.od -o canope.odx

For dumping the information stored in the odx file use `dump.py` with a version of
python3.

    $ python3 dump.py -f canopen.odx
