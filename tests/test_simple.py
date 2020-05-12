# 
# to run all your tests when they follow the naming conventions, just run 
# 
# $ pytest
# 
# at the root of the repo
#
# see naming conventions for example here:
# https://docs.pytest.org/en/latest/goodpractices.html
# 
#
#
# instead of 
#   from bidule.machine import Machine
# # see bidule/__init__.py about how this is possible

from bidule import Machine

def test_machine():
    machine = Machine('from tests')
    assert machine.main() == 0
