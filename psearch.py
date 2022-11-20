#! /usr/bin/env python

# Imports
import requests
from bs4 import BeautifulSoup
import argparse
import sys

# Setup arguements
parser = argparse.ArgumentParser()
parser.add_argument("package", help="Package to search for in PYPI")
parser.add_argument("-q", "--quiet", help="Remove headers from output", action="store_true")
args = parser.parse_args()

if not args.quiet:
  print("Searching PYPI for: %s" % args.package)
  print("============================================================")

# Get search results and parse HTML
try:
  r = requests.get("https://pypi.org/search/?q=%s" % args.package)

  if r.status_code != 200:
    print("Could not get a result from https://pypi.org/search/")
    sys.exit()
except requests.exceptions.ConnectionError:
  print("Could not connect to https://pypi.org/search/")
  sys.exit()

html_parsed = BeautifulSoup(r.text, 'html.parser')

# Get <UL> of results and process
result_list = html_parsed.find('ul', class_="unstyled")
try:
  results = result_list.findChildren("li" , recursive=False)

# Build result list
  for res in results:
    name = res.find('span', class_="package-snippet__name").text
    ver = res.find('span', class_="package-snippet__version").text
    desc = res.find('p', class_="package-snippet__description").text

    print("%s %s => %s" % (name, ver, desc))
except AttributeError:
  print("No results found")
