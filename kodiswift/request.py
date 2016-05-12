# -*- coding: utf-8 -*-
"""
    kodiswift.request
    ------------------

    This module contains the Request class. This class represents an incoming
    request from Kodi.

    :copyright: (c) 2012 by Jonathan Beluch
    :license: GPLv3, see LICENSE for more details.
"""
from __future__ import absolute_import

from .common import unpickle_args
from ._compat import urlparse


class Request(object):
    """The request objects contains all the arguments passed to the plugin via
    the command line.

    :param url: The complete plugin URL being requested. Since Kodi typically
                passes the URL query string in a separate argument from the
                base URL, they must be joined into a single string before being
                provided.
    :param handle: The handle associated with the current request.
    """

    def __init__(self, url, handle):
        #: The entire request url.
        self.url = url

        #: The current request's handle, an integer.
        self.handle = int(handle)

        # urlparse doesn't like the 'plugin' scheme, so pass a protocol
        # relative url, e.g. //plugin.video.helloxbmc/path
        self.scheme, remainder = url.split(':', 1)
        parts = urlparse.urlparse(remainder)
        self.netloc, self.path, self.query_string = (
            parts[1], parts[2], parts[4])
        self.args = unpickle_args(urlparse.parse_qs(self.query_string))
