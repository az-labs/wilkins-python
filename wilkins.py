#!/usr/bin/env python

import requests
import tempfile
from urllib import urlencode
from xml.dom import minidom

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
        temp_response = tempfile.NamedTemporaryFile()
        temp_response.write(wn_html_result.text.encode("ascii"))
        print temp_response.name
        html_response = minidom.parse(temp_response.name)
        html_body = html_response.getElementsByTagName("body")
        print html_response


if __name__ == "__main__":
    x = Wilkins()
    print x.query_word("idiot")
