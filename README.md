# pyioc
`pyioc` is a single file IoC (or ServiceLocator) in Python ([Python](https://www.python.org)) for resolving (locating) services anywhere in your scripts.

# Features
* [x] Lifetime containers
* [x] Singleton and Instance containers
* [x] Automatically resolve instance and pass onto another objects __init__ function
* [x] Use 'key' or 'type' to a resolve service

## Installation

	$ git clone github.com/noodleflake/pyioc
    
## Sample Usage

In the repository see `sample` directory

```python
from libs.service_locator import ServiceLocator

#Singleton Register
ServiceLocator.register(Smtp())
ServiceLocator.register(Smtp(), 'with_key')

#Dynamic Register
ServiceLocator.register(Smtp)
ServiceLocator.register(Smtp, 'with_key')

#Resolve
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