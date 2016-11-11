#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup
from urllib import urlencode
import argparse
import json

# Author: Omar Elazhary <omazhary@gmail.com>
# License: MIT


class Wilkins:
    """This class allows you to query words on WordNet's internet UI."""
    wn_request = None
    html_parser = None
    parameters = None
    result = None

    def __init__(self):
        self.wn_request = "http://wordnetweb.princeton.edu/perl/webwn"
        self.parameters = dict()
        self.result = dict()

    def query_word(self, word):
        self.parameters = {"s": word, "o0": 1, "o1": 1, "o2": "", "o3": "",
                           "o4": "", "o5": "", "o6": "", "o7": "", "o8": 1,
                           "o9": "", "c": 8, "i": -1, "sub": "Change"}
        wn_uri = "%s?%s" % (self.wn_request, urlencode(self.parameters))
        wn_html_result = requests.get(wn_uri)
        soup = BeautifulSoup(wn_html_result.text.encode("ascii"),
                             'html.parser')
        self.result["type"] = soup.find_all("h3")[0].text
        synonyms = soup.find_all("li")[0].find_all("a")
        # Remove the first entry as it's just garbage:
        del synonyms[0]
        # Remove the second entry as it's just the word type again:
        del synonyms[0]
        self.result["synonyms"] = []
        self.result["residual"] = []
        for synonym in synonyms:
            self.result["synonyms"].append(synonym.text.split('#')[0])
            # Need to figure out what the residual is, to be able to parse it.
            self.result["residual"].append(synonym.text.split('#')[1])
        return self.result


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
            description="Query the online WordNet endpoint.")
    parser.add_argument(
            '--word', metavar='w', type=str,
            help='The word about which you would like to query WordNet.')
    parser.add_argument(
            '--output', metavar='o', type=str,
            help='The output format you would prefer: [json]')

    args = vars(parser.parse_args())

    word = ""
    output = ""

    if not args["word"]:
        pass
    if not args["output"]:
        output = "json"
    else:
        output = args["output"]

    word = args["word"]

    x = Wilkins()
    result = x.query_word(word)
    if output == "json":
        print(json.dumps(result))
