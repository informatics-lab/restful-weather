#!/usr/bin/env python

from bs4 import BeautifulSoup


class WCSCapabilities(object):
    def __init__(self, capabilities_xml):
        self.capabilities = capabilities_xml
        self.soup = BeautifulSoup(self.capabilities, 'xml')

    def get_coverage_ids(self):
        return [id.get_text() for id in self.soup.find_all('CoverageId')]

if __name__ == '__main__':
    with open('../../resources/wcs2.0-metocean/GetCapabilities.xml') as inf:
        in_xml = inf.read()
    capabilities = WCSCapabilities(in_xml)
    print capabilities.get_coverage_ids()
