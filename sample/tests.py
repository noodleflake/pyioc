#!/usr/bin/env python2.7
#
# Author: 'Martin Swanepoel'

from libs.service_locator import ServiceLocator
from services.configuration_chain import ConfigurationChain
from services.configuration_local import ConfigurationLocal
from services.configuration_remote import ConfigurationRemote
from services.postgres_connection import PostgresConnection
from services.sms_gateway import SmsGateway


class Tests(object):
    def __init__(self):
        pass

    def run(self):
        self.test_postgres_singleton()
        self.test_configuration_local_dynamic()
        self.test_configuration_remote_dynamic()
        self.test_configuration_chain_dynamic()
        self.test_sms_gateway_dynamic()

    def test_postgres_singleton(self):
        #get default postgres connection
        postgres_connection = ServiceLocator.resolve(PostgresConnection)
        dummy_data = postgres_connection.fetchone('SELECT * FROM SomeDummy')
        print dummy_data

        postgres_connection_2 = ServiceLocator.resolve(PostgresConnection)
        dummy_data2 = postgres_connection_2.fetchone('SELECT * FROM SomeDummy2')
        print dummy_data2

        #check if the instance is being reused (singleton)
        # -- we used it twice
        connection_usage_count = postgres_connection_2.get_usage_count()
        print 'Postgres connection was used \'%s\' times' % connection_usage_count
        if connection_usage_count != 2:
            print 'test_postgres_singleton (FAIL)'
            return
        print 'test_postgres_singleton (PASS)'

    def test_configuration_local_dynamic(self):
        #get default local configuration
        configuration_local = ServiceLocator.resolve(ConfigurationLocal)
        configuration_value = configuration_local.get('sample_key')
        print configuration_value
        if configuration_value != 'http://clickatel.co.za/api/userid?123':
            print 'test_configuration_local_dynamic (FAIL)'
            return
        print 'test_configuration_local_dynamic (PASS)'

    def test_configuration_remote_dynamic(self):
        #get default local configuration
        configuration_remote = ServiceLocator.resolve(ConfigurationRemote)
        configuration_value = configuration_remote.get('sample_key')
        print configuration_value
        if configuration_value != 'https://clickatel.co.za/api/userid?987':
            print 'test_configuration_remote_dynamic (FAIL)'
            return
        print 'test_configuration_remote_dynamic (PASS)'

    def test_configuration_chain_dynamic(self):
        #get default local configuration
        configuration_chain = ServiceLocator.resolve(ConfigurationChain)
        configuration_value = configuration_chain.get('sample_key')
        print configuration_value
        if configuration_value != 'http://clickatel.co.za/api/userid?123':
            print 'test_configuration_chain_dynamic (FAIL)'
            return
        print 'test_configuration_chain_dynamic (PASS)'

    def test_sms_gateway_dynamic(self):
        #get default sms gateway
        sms_gateway = ServiceLocator.resolve(SmsGateway)
        success_value = sms_gateway.send('+2783456789', 'Hello from Python!')
        print success_value
        if not success_value:
            print 'test_sms_gateway_dynamic (FAIL)'
            return
        print 'test_sms_gateway_dynamic (PASS)'