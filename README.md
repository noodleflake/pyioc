# pyioc
`pyioc` is a single file IoC (or ServiceLocator) in [Python](https://www.python.org) for resolving (locating) services anywhere in your scripts.

# Features
* [x] Singleton and Instance containers
* [x] Automatically resolve the __init__ parameter dependancies of an instance
* [x] Use 'key' and\or 'type' to a resolve a service

## Installation

	$ git clone https://github.com/noodleflake/pyioc
    
## Sample Usage

In the pyioc repository see `sample` directory

```python
from libs.service_locator import ServiceLocator

#Singleton Register
postgres_connection = PostgresConnection('ConnectionStringHere')
smtp = Smtp(postgres_connection)
ServiceLocator.register(postgres_connection)
ServiceLocator.register(smtp)
ServiceLocator.register(smtp, 'with_key')

#Dynamic Register
ServiceLocator.register(PostgresConnection)
ServiceLocator.register(Smtp)
ServiceLocator.register(Smtp, 'with_key')

#We tell the locator to use a static value when resolving\instantiating 'PostgresConnection'
ServiceLocator.map_parameter_to_static(PostgresConnection, 'connection_string', 'ConnectionStringHere')
#We tell the locator to use a service value when resolving\instantiating 'Smtp'
ServiceLocator.map_parameter_to_service(Smtp, 'postgres_connection', PostgresConnection)

#Resolve
ServiceLocator.resolve(PostgresConnection)
ServiceLocator.resolve(Smtp)
ServiceLocator.resolve(Smtp, 'with_key')

```
    
# Contributing

Start with clicking the star button to make the author and his neighbors happy. Then fork the repository and submit a pull request for whatever change you want to be added to this project.

If you have any questions, just open an issue.

# Author
Martin Swanepoel <martinswanepoel88@gmail.com>

# Licence

This project is released under the MIT licence. See [LICENCE](LICENCE) for more details.