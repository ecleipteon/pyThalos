#!/usr/bin/python3

import argparse
import requests

parser = argparse.ArgumentParser()
parser.add_argument("-T", "--remote_address", help="Thalos server address")
args = parser.parse_args()

print(args.remote_address)
