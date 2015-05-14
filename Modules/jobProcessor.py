#-- Import section
from TestLinkRunner import TestLinkRunner
from HurdlesRunner import HurdlesRunner
from datetime import datetime
import sys, os, json, unittest
sys.path.append(os.path.join(os.path.dirname(__file__),'../'))
from Models import hurdles


#-- Global variables section
TestlinkXMLRPCurl = "http://localhost/testlink/lib/api/xmlrpc/v1/xmlrpc.php"

#-- It will run the selected tests using testlink runner
def runTestUsingTestLinkRunner(jobId):
    job = hurdles.getJobUsingJobId(jobId)
    apiKey = job[0][2]
    jobDetails = json.loads(job[0][3])
    testplanId = jobDetails["testPlan"]
    buildName = jobDetails["build"]
    testcases = jobDetails["testCases"]
    hurdles.updateJobStatus(jobId,'active')
    for testcase in testcases:
        testcase = json.loads(str(testcase).replace("'",'"'))
        modulename = testcase["module"]
        methodname = testcase["method"]
        module = stringToClass(modulename)
        suite = unittest.TestSuite()
        suite.addTest(module(methodname))
        runner = TestLinkRunner(TestlinkXMLRPCurl,apiKey,testplanId,buildName)
        runner.run(suite)
    hurdles.updateJobStatus(jobId,'completed')


#-- It will run the selected tests using Hurdles runner
def runTestUsingHurdlesRunner(jobId):
    job = hurdles.getJobUsingJobId(jobId)
    testerName = job[0][1]
    jobDetails = json.loads(job[0][3])
    testplan = jobDetails["testPlan"]
    buildName = jobDetails["build"]
    testcases = jobDetails["testCases"]
    hurdles.updateJobStatus(jobId,'active')
    for testcase in testcases:
    	testcase = json.loads(str(testcase).replace("'",'"'))
        modulename = testcase["module"]
        methodname = testcase["method"]
        module = stringToClass(modulename)
        suite = unittest.TestSuite()
        suite.addTest(module(methodname))
        runner = HurdlesRunner(jobId,testerName,testplan,buildName)
        runner.run(suite)
    hurdles.updateJobStatus(jobId,'completed')

#-- It will return the class object of the given class name
def stringToClass(importName):
    className = importName.split('.')[-1]
    moduleName = importName[:-(len(className)+1)]
    mod = __import__(moduleName)
    components = moduleName.split('.')
    for comp in components[1:]:
        mod = getattr(mod,comp)
    class_ = getattr(mod,className)
    return class_