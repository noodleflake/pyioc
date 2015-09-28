#!/usr/bin/env python2.7
#
# Author: 'Martin Swanepoel'

from libs.service_locator import ServiceLocator
from services.configuration_local import ConfigurationLocal
from services.configuration_remote import ConfigurationRemote


class ConfigurationChain(object):
    def __init__(self):
        pass

    def get(self, key):
        #try local configuration first
        configuration_instance = ServiceLocator.resolve(ConfigurationLocal)
        if configuration_instance is not None:
            configuration_value = configuration_instance.get(key)
            if configuration_value is not None:
                return configuration_value
        #try remote configuration second
        configuration_instance = ServiceLocator.resolve(ConfigurationRemote)
        if configuration_instance is not None:
            configuration_value = configuration_instance.get(key)
            if configuration_value is not None:
                return configuration_value
        raise Exception('key not found')