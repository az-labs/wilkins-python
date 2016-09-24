#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup
from urllib import urlencode

class Wilkins:
    """This class allows you to query words on WordNet's internet UI."""
    wn_request = None
    html_parser = None
    parameters = None
    result = None

    def __init__(self):
        self.wn_request = "http://wordnetweb.princeton.edu/perl/webwn"
        self.parameters = dict()
        result = dict()

    def query_word(self, word):
        self.parameters = { "s" : word, "o0" : "", "o1" : "" }
        wn_uri = "%s?%s" % (self.wn_request, urlencode(self.parameters))
        wn_html_result = requests.get(wn_uri)
        soup = BeautifulSoup(wn_html_result.text.encode("ascii"), 'html.parser')


if __name__ == "__main__":
    x = Wilkins()
    print x.query_word("idiot")
