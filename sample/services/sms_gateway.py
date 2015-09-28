#!/usr/bin/env python2.7
#
# Copyright(c) 2015 softlogic.co.za
#
# Author: 'Martin Swanepoel'


class SmsGateway(object):
    def __init__(self, url):
        print 'SmsGateway instantiated with url (%s)' % url

    def send(self, destination, message):
        return True