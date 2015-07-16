#!/usr/bin/env python

import unittest

from restful_weather.wcs_parser import wcs_capabilities


class TestWCSParser(unittest.TestCase):
    def setUp(self):
        with open('./tests/resources/wcs2.0-metocean/GetCapabilities.xml') \
          as inf:
            in_xml = inf.read()
            self.capabilities = wcs_capabilities.Capabilities(in_xml)

    def test_get_coverage_ids(self):
        expected = [u'GFS_2015-06-18T06.00.00Z_AGL',
                    u'GFS_2015-06-18T06.00.00Z_AMSL',
                    u'GFS_2015-06-18T06.00.00Z_Atmosphere',
                    u'GFS_2015-06-18T06.00.00Z_AtmosphereTop',
                    u'GFS_2015-06-18T06.00.00Z_Ground',
                    u'GFS_2015-06-18T06.00.00Z_ISBL',
                    u'GFS_2015-06-18T06.00.00Z_MaxWind',
                    u'GFS_2015-06-18T06.00.00Z_MeanSea',
                    u'GFS_2015-06-18T06.00.00Z_Tropopause',
                    u'GFS_2015-06-18T06.00.00Z_ZeroIsotherm',
                    u'GFS_Latest_AGL',
                    u'GFS_Latest_AMSL',
                    u'GFS_Latest_Atmosphere',
                    u'GFS_Latest_AtmosphereTop',
                    u'GFS_Latest_Ground',
                    u'GFS_Latest_ISBL',
                    u'GFS_Latest_MaxWind',
                    u'GFS_Latest_MeanSea',
                    u'GFS_Latest_Tropopause',
                    u'GFS_Latest_ZeroIsotherm']

        ids = self.capabilities.coverages
        self.assertEqual(ids, expected)
