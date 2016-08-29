#!/usr/bin/env python

import httplib

class Wilkins:
    """This class allows you to query words on WordNet's internet UI."""
    wn_request = None
    result = None

    def __init__(self):
        self.wn_request = httplib.HTTPConnection("www.python.org")
        result = dict()

    def query_word(self, word):
        print word
        self.wn_request.request("HEAD", "/index.html")
        wn_response = self.wn_request.getresponse()
        print wn_response.status, wn_response.reason


if __name__ == "__main__":
    x = Wilkins()
    print x.query_word("idiot")
