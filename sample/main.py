#!/usr/bin/env python2.7
#
# Author: 'Martin Swanepoel'

from bootstrapper import Bootstrapper
from tests import Tests


def main():
    bootstrapper = Bootstrapper()
    bootstrapper.initialize()

    tests = Tests()
    tests.run()


if __name__ == '__main__':
    main()