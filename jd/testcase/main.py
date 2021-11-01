import unittest

suite1=unittest.defaultTestLoader.discover(start_dir='.',pattern='*.py')
runner=unittest.TextTestRunner()
runner.run(suite1)
