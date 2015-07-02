#!/usr/bin/env python

from bs4 import BeautifulSoup
from collections import defaultdict


class Describe(object):
    def __init__(self, description_xml):
        self.description = description_xml
        self.soup = BeautifulSoup(self.description, 'xml')
        self.parameters = self.get_parameters()
        self.masks = self.mask_lookup()

    def mask_lookup(self):
        return {mask.get('fieldName'): mask.string for
                mask in self.soup.find_all('dataMaskReference')}

    def get_parameters(self):
        return [mask.get('fieldName') for
                mask in
                self.soup.find_all('dataMaskReference')]
