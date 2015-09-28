#!/usr/bin/env python2.7
#
# Author: 'Martin Swanepoel'

from libs.service_locator import ServiceLocator
from services.configuration_chain import ConfigurationChain
from services.postgres_connection import PostgresConnection
from services.configuration_local import ConfigurationLocal
from services.configuration_remote import ConfigurationRemote
from services.sms_gateway import SmsGateway


class Bootstrapper(object):
    def __init__(self):
        pass

    def initialize(self):
        #register a static instance of database connection pool
        postgres_connection = PostgresConnection('Driver=PostgreSQL Unicode;Server=X;Port=5432;Database=X;Uid=postgres;Pwd=X;', 'Main Connection')
        ServiceLocator.register(postgres_connection)

        #register a another static instance of database connection pool
        alternative_postgres_connection = PostgresConnection('Driver=PostgreSQL Unicode;Server=X2;Port=5432;Database=X;Uid=postgres;Pwd=X;', 'Alternative Connection')
        ServiceLocator.register(alternative_postgres_connection, 'alt_db')

        #register a dynamic instance of local configuration
        ServiceLocator.register(ConfigurationLocal)

        #register a dynamic instance of remote configuration
        # where __init__ postgres_connection parameter is mapped
        # to static instance PostgresConnection of key 'alt_db'
        ServiceLocator.register(ConfigurationRemote)
        ServiceLocator.map_parameter_to_service(ConfigurationRemote, 'postgres_connection', PostgresConnection, 'alt_db')

        #register a dynamic instance of chain configuration
        ServiceLocator.register(ConfigurationChain)

        #Resolve instance of chain configuration so
        # that we can get the sms gateways url
        configuration_chain = ServiceLocator.resolve(ConfigurationChain)
        static_url = configuration_chain.get('sms_url')

        #register a dynamic instance of sms gateway
        # where __init__ url parameter is mapped
        # to static value
        ServiceLocator.register(SmsGateway)
        ServiceLocator.map_parameter_to_static(SmsGateway, 'url', static_url)