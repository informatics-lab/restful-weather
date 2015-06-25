#!/usr/bin/env python

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
        self.capabilities = self.get_capabilities()

    def get_capabilities(self, **kwargs):
        params = self.params.copy()
        params.update(_capitalise_keys(kwargs))
        params['REQUEST'] = 'GetCapabilities'
        return _get_request(self.base_url, **params)


class WebCoverageService(OGCService):
    def __init__(self, url, **kwargs):
        params = _capitalise_keys(kwargs)
        params['SERVICE'] = 'WCS'
        super(WebCoverageService, self).__init__(url, **params)
