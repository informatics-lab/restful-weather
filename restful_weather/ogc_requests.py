#!/usr/bin/env python

'''
OGC Web Services request builder.

Example:

service = ogc_requests.WebCoverageService(url, api_key='key')
service.get_capabilities()
service.describe_coverage(coverageid)
'''

import urllib2
import urllib


def _get_request(base_url, **kwargs):
    values = urllib.urlencode(kwargs)
    url = base_url + '?' + values
    return urllib2.urlopen(url).read()


def _capitalise_keys(dictionary):
    return dict((key.upper(), val) for key, val in dictionary.iteritems())


class OGCService(object):
    def __init__(self, url, **kwargs):
        self.base_url = url
        self.params = _capitalise_keys(kwargs)

    def get_capabilities(self, **kwargs):
        params = self.params.copy()
        params.update(_capitalise_keys(kwargs))
        params['REQUEST'] = 'GetCapabilities'
        return _get_request(self.base_url, **params)


class WebCoverageService(OGCService):
    def __init__(self, url, version='2.0.0', **kwargs):
        params = _capitalise_keys(kwargs)
        params['SERVICE'] = 'WCS'
        params['VERSION'] = version
        super(WebCoverageService, self).__init__(url, **params)

    def describe_coverage(self, coverageid, **kwargs):
        params = self.params.copy()
        params.update(_capitalise_keys(kwargs))
        params['REQUEST'] = 'DescribeCoverage'
        params['COVERAGEID'] = coverageid
        return _get_request(self.base_url, **params)
