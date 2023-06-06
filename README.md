# py-url-encode
Simple tool to url encode/decode strings. This tool supports encoding of all characters, only special characters and space instead of %20, for all your fuzzing needs.

# Usage

To see the help menu, run the script without any input.
```bash
$ python3 url-encode.py

usage: url-encode.py [-h] [--all] [--decode] [--space] input [input ...]
url-encode.py: error: the following arguments are required: input
```

Providing the input in two ways
```bash
# Any string after the optional flags seperated with spaces will be considered as input.
$ python3 url-encode.py string separated with spaces
string%20separated%20with%20spaces

# Alternatively, provide your inpute in single or double quotes.
$ python3 url-encode.py 'or as a single input in quotes'
or%20as%20a%20single%20input%20in%20quotes
```

Encoding
```bash
# By default, the script encodes only special characters.
$ python3 url-encode.py '$pecial önly'
%24pecial%20%C3%B6nly

# -a or --all flag for encoding every character.
$ python3 url-encode.py -a encode all
%65%6e%63%6f%64%65%20%61%6c%6c

# -s or --space to encode spaces as '+' instead of '%20'
# Works -a flag as well
$ python3 url-encode.py -s spaces are weird
spaces+are+weird

$ python3 url-encode.py -a -s spaces are weird
%73%70%61%63%65%73+%61%72%65+%77%65%69%72%64
```
