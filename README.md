# pyioc
`pyioc` is a single file IoC (or ServiceLocator) in [Python](https://www.python.org) for resolving (locating) services anywhere in your scripts.

# Features
* [x] Singleton and Instance containers
* [x] Automatically resolve the \_\_init\_\_ function's parameter dependancies
* [x] Use 'key' and\or 'type' to a resolve a service

## Installation

	$ git clone https://github.com/noodleflake/pyioc
    
## Sample Usage

In the pyioc repository see `sample` directory

```python
from libs.service_locator import ServiceLocator

#Either Register Singleton (Entire lifetime of application)
postgres_connection = PostgresConnection('ConnectionStringHere')
smtp = Smtp(postgres_connection)
ServiceLocator.register(postgres_connection)
ServiceLocator.register(smtp)
ServiceLocator.register(smtp, 'with_key')

#OR Register Dynamic (New instance when resolved)
ServiceLocator.register(PostgresConnection)
ServiceLocator.register(Smtp)
ServiceLocator.register(Smtp, 'with_key')

#map_parameter_to_static and map_parameter_to_service is only applicable to dynamic instances
#We tell the locator to use a static value when resolving\instantiating 'PostgresConnection'
map_to_type = PostgresConnection
init_param_name = 'connection_string'
init_param_value = 'ConnectionStringHere'
ServiceLocator.map_parameter_to_static(map_to_type, init_param_name, init_param_value)
#We tell the locator to use a service instance when resolving\instantiating 'Smtp'
map_to_type = Smtp
init_param_name = 'postgres_connection'
init_param_type = PostgresConnection
ServiceLocator.map_parameter_to_service(map_to_type, init_param_name, init_param_type)

#Resolve PostgresConnection and use it
postgres_connection = ServiceLocator.resolve(PostgresConnection)
db_data = postgres_connection.fetchone()

#Resolve Smtp and use it
smtp = ServiceLocator.resolve(Smtp)
smtp = ServiceLocator.resolve(Smtp, 'with_key')
success = smtp.send_mail('martinswanepoel88@gmail', 'Hello from Python')

```
    
# Contributing

Start with clicking the star button to make the author and his neighbors happy. Then fork the repository and submit a pull request for whatever change you want to be added to this project.

If you have any questions, just open an issue.

# Author
Martin Swanepoel <martinswanepoel88@gmail.com>

# Licence

This project is released under the MIT licence. See [LICENCE](LICENCE) for more details.