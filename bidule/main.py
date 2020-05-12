# how to import one of our own modules from an entry point
# that is also how the module can be imported from a separate app

# note that it is NOT RECOMMENDED 
# to use relative import from an entry point
#
# but see main2.py however for more details

from bidule.machine import Machine

instance = Machine("Hello World")
instance.main()

