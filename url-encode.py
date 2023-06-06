import sys
import argparse
import urllib.parse

def special_only_encode(input_list):
    parsed = ''
    for i in input_list:
        parsed += urllib.parse.quote(i) + '%20'
    return parsed[:-3]


def special_only_encode_space(input_list):
    parsed = ''
    for i in input_list:
        parsed += urllib.parse.quote(i) + '+'
    return parsed[:-1]


def to_utf8_url_encode(string):
    url_encoded = ''
    for i in string.encode():
        url_encoded += '%' + hex(i)[2:]
    return url_encoded


def all_chars_encode(input_list):
    parsed = ''
    for i in input_list:
        for j in i:
            parsed += to_utf8_url_encode(j)
        parsed += '%20'
    return parsed[:-3]


def all_chars_encode_space(input_list):
    parsed = ''
    for i in input_list:
        for j in i:
            parsed += to_utf8_url_encode(j)
        parsed += '+'
    return parsed[:-1]


def decode(input_list):
    decoded = ''
    for i in input_list:
        decoded += urllib.parse.unquote_plus(i) + ' '
    return decoded[:-1]


parser = argparse.ArgumentParser()

parser.add_argument('--all', '-a', help='Encode all characters.', action='store_true')
parser.add_argument('--decode', '-d', help='URL decode.', action='store_true')
parser.add_argument('--space', '-s', help='Use \'+\' for spaces instead of %20.', action='store_true')
parser.add_argument('input', help='Input to be URL encoded.', type=str, nargs='+')

args = parser.parse_args()

all_flag = args.all
decode_flag = args.decode
space_flag = args.space
input_list = args.input

result = None

if decode_flag:
    result = decode(input_list)
else:
    if all_flag:
        if space_flag:
            result = all_chars_encode_space(input_list)
        else:
            result = all_chars_encode(input_list)
    else:
        if space_flag:
            result = special_only_encode_space(input_list)
        else:
            result = special_only_encode(input_list)

print(result)
