"""`Configuration` provider custom type specification example."""

import os
import decimal

from dependency_injector import providers


class Calculator:
    def __init__(self, pi: decimal.Decimal):
        self.pi = pi


config = providers.Configuration()

calculator_factory = providers.Factory(
    Calculator,
    pi=config.pi.as_(decimal.Decimal),
)


if __name__ == '__main__':
    # Emulate environment variables
    os.environ['PI'] = '3.1415926535897932384626433832'

    config.pi.from_env('PI')

    calculator = calculator_factory()

    assert calculator.pi == decimal.Decimal('3.1415926535897932384626433832')
