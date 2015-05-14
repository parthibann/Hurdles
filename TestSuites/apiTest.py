import sys
import unittest
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__),'../'))

class functionality1(unittest.TestCase):
    """Explain the functionality here """

    def setUp(self):
        """Setup required for running testcases."""
    
    def tearDown(self):
        """Clear the objects that are created in the setup."""
        
    def test_1_TC1_testcase(self):
        "Explain the testcase here"
        self.fail("failed to demonstrate test failure.")

    def test_2_TC2_testcase(self):
        "Explain the testcase here"
        pass

    def test_3_TC3_testcase(self):
        "Explain the testcase here"
        self.fail("failed to demonstrate test failure.")

    def test_4_TC4_testcase(self):
        "Explain the testcase here"
        print "welcome"
        
if __name__ == '__main__':
    unittest.main()