#!/usr/bin/env python2.7
#
# Author: 'Martin Swanepoel'


class PostgresConnection(object):
    def __init__(self, connection_string, name, connection_count=10):
        self.connection_string = connection_string
        self.name = name
        self.connection_count = connection_count
        self.usage_count = 0

    def fetchone(self, query):
        self.usage_count += 1
        print 'Using (%s) for data fetch' % self.name
        return [
            'SampleData1',
            'SampleData2',
            'SampleData3',
        ]

    def get_name(self):
        return self.name

    def get_usage_count(self):
        return self.usage_count