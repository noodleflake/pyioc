#!/usr/bin/env python2.7
#
# Author: 'Martin Swanepoel'

import inspect
import types


class ServiceLocator(object):
    __services = []
    __service_mappings = []

    @staticmethod
    def resolve(type, key=None):
        for service in ServiceLocator.__services:
            if service['key'] == key and service['value'] == type:
                ctor_parameters = {}
                if len(ServiceLocator.__service_mappings) > 0:
                    args = inspect.getargspec(service['value'].__init__).args
                    if len(args) > 1:
                        for service_mapping in ServiceLocator.__service_mappings:
                            source_service_type = service_mapping['source_service_type']
                            if source_service_type == type:
                                parameter_service_key = service_mapping['parameter_service_key']
                                parameter_name = service_mapping['parameter_name']
                                parameter_static = service_mapping['parameter_static']
                                parameter_service_type = service_mapping['parameter_service_type']
                                if parameter_name in args:
                                    if parameter_service_type is not None:
                                        ctor_parameters[parameter_name] = ServiceLocator.resolve(parameter_service_type,
                                                                                                 parameter_service_key)
                                    else:
                                        ctor_parameters[parameter_name] = parameter_static
                return service['value'](**ctor_parameters)
            elif service['key'] == key and isinstance(service['value'], type):
                return service['value']

    @staticmethod
    def register(service_item, key=None):
        for service in ServiceLocator.__services:
            if service['key'] == key and ServiceLocator.extract_type(service['value']) == ServiceLocator.extract_type(
                    service_item):
                raise Exception(
                    'service key %s of type %s already exists' % ('' if key is None else key, str(service_item)))
        ServiceLocator.__services.append({'key': key, 'value': service_item})

    @staticmethod
    def remove(type, key=None):
        item_to_remove = None
        for service in ServiceLocator.__services:
            if service['key'] == key and ServiceLocator.extract_type(service['value']) == ServiceLocator.extract_type(
                    type):
                item_to_remove = service
                break
        if item_to_remove is not None:
            ServiceLocator.__services.remove(item_to_remove)

    @staticmethod
    def map_parameter_to_service(for_service, ctor_param_name, ctor_param_type, ctor_param_service_key=None):
        service_mapping = dict()
        service_mapping['source_service_type'] = for_service
        service_mapping['parameter_name'] = ctor_param_name
        service_mapping['parameter_service_type'] = ctor_param_type
        service_mapping['parameter_service_key'] = ctor_param_service_key
        service_mapping['parameter_static'] = None
        ServiceLocator.__service_mappings.append(service_mapping)

    @staticmethod
    def map_parameter_to_static(for_service, ctor_param_name, ctor_param_value):
        service_mapping = dict()
        service_mapping['source_service_type'] = for_service
        service_mapping['parameter_name'] = ctor_param_name
        service_mapping['parameter_service_type'] = None
        service_mapping['parameter_service_key'] = None
        service_mapping['parameter_static'] = ctor_param_value
        ServiceLocator.__service_mappings.append(service_mapping)

    @staticmethod
    def extract_type(item):
        if ServiceLocator.is_type_of_class(item):
            return item
        return type(item)

    @staticmethod
    def is_type_of_class(item):
        return item is type or isinstance(item, types.TypeType)
