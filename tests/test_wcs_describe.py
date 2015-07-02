#!/usr/bin/env python

import unittest
from restful_weather.wcs_parser import wcs_describe


class TestWCSDescribe(unittest.TestCase):
    def setUp(self):
        with open('./tests/resources/wcs2.0-metocean/DescribeCoverage.xml') \
          as inf:
            in_xml = inf.read()
            self.describe = wcs_describe.WCSDescribeCoverage(in_xml)

    def test_get_parameters(self):
        expected = [u'msl-pressure', u'pressure']
        params = self.describe.parameters
        self.assertEqual(params, expected)

    def test_get_datamasks(self):
        expected = {u'msl-pressure': u'maskId_GFS_Latest_MeanSea_1',
                    u'pressure': u'maskId_GFS_Latest_MeanSea_1'}
        masks = self.describe.masks
        self.assertEqual(masks, expected)
