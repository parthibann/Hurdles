#-- import Section
#-- import all your testsuites(class level testcases here)
from TestSuites import apiTest
import unittest

#-- Add All your Testsuites Here
Suites = []
Suites.append(apiTest.functionality1)

#-- It will return the testSuites in HTML format
def testSuitesInHtmlFormat():
    testcases = ""
    for testSuite in Suites:
        loadSuite = unittest.TestLoader().loadTestsFromTestCase(testSuite)
        totalTestCases = loadSuite.countTestCases()
        for test in range(totalTestCases):
            strTest = str(loadSuite._tests[test])
            _suiteName = strTest.split('.')[-1][0:-1]
            _testName = strTest.split(' ')[0]
            chkboxValue = {"module":strTest.split(' ')[1][1:-1],"method":_testName}
            testCaseRow = '<tr><td><input type="checkbox" class="chkTest" name="chkTest" value="'+str(chkboxValue)+'"></th><th>'+_suiteName+'</th><th>'+_testName+'</th></tr>'
            testcases = testcases + testCaseRow
    return testcases