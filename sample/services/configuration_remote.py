#!/usr/bin/env python2.7
#
# Author: 'Martin Swanepoel'


class ConfigurationRemote(object):
    def __init__(self, postgres_connection):
        self.postgres_connection = postgres_connection
        print 'ConfigurationRemote instantiated with connection (%s)' % self.postgres_connection.get_name()

    def get(self, key):
        #sample data
        return 'https://clickatel.co.za/api/userid?987'