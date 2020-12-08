import unittest

from menu.combo.testregcombo import TestRegCombo
from menu.combo.testdietcombo import TestDietCombo
from menu.freeorder.Test_Regular import test_regular
from menu.freeorder.Test_Kid import test_kids

def my_suite():
    suite = unittest.TestSuite()
    result = unittest.TestResult()
    suite.addTest(unittest.makeSuite(test_regular))
    suite.addTest(unittest.makeSuite(test_kids))
    suite.addTest(unittest.makeSuite(TestRegCombo))
    suite.addTest(unittest.makeSuite(TestDietCombo))
    runner = unittest.TextTestRunner()
    print(runner.run(suite))
    
my_suite () 