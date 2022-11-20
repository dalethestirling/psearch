# psearch.py

Since the PIP search endpoint has been permanently deprecated and disabled due to excessive traffic driven by unidentified traffic. 

[PyPI XMLRPC Search Disabled Incident Report](https://status.python.org/incidents/grk0k7sz6zkp)

I am too lazy to switch to the browser to search for Python packages. So I spent time writing this script to search packages from the command line.

###Install
Install prerequisites using the `requirements.txt` file.

`pip install -r requirements.txt`
 

###Usage
`./psearch.py [-h] [-q|--quiet] package`

#####Options
`-h, --help`: Print usage information

`-q, --quiet`: Print results without headers