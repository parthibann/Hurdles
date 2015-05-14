#-- Import section
import unittest, sys, StringIO, os
sys.path.append(os.path.join(os.path.dirname(__file__),'../'))
from Models import hurdles

#-- Global variables section
TestResult = unittest.TestResult

#-- It will do necessary actions based on the test result
class _TestResult(TestResult):
    #-- Initializing variables
    def __init__(self,jobId,testerName,testplan,buildName):
        TestResult.__init__(self)
        self.stdout0 = None
        self.stderr0 = None
        self.result = []
        self.jobId = jobId
        self.testerName = testerName
        self.testplan = testplan
        self.buildName = buildName

    def startTest(self, test):
        TestResult.startTest(self, test)
        # just one buffer for both stdout and stderr
        self.outputBuffer = StringIO.StringIO()
        stdout_redirector.fp = self.outputBuffer
        stderr_redirector.fp = self.outputBuffer
        self.stdout0 = sys.stdout
        self.stderr0 = sys.stderr
        sys.stdout = stdout_redirector
        sys.stderr = stderr_redirector
        
    def complete_output(self):
        """
        Disconnect output redirection and return buffer.
        Safe to call multiple times.
        """
        if self.stdout0:
            sys.stdout = self.stdout0
            sys.stderr = self.stderr0
            self.stdout0 = None
            self.stderr0 = None
        return self.outputBuffer.getvalue()
    
    
    def stopTest(self, test):
        # Usually one of addSuccess, addError or addFailure would have been called.
        # But there are some path in unittest that would bypass this.
        # We must disconnect stdout in stopTest(), which is guaranteed to be called.
        self.complete_output()
        
    def addSuccess(self, test):
        TestResult.addSuccess(self, test)
        output = self.complete_output()
        self.result.append((0, test, output, ''))
        self.updateTestCaseResult(str(test),output,'pass')
                        
    def addError(self, test, err):
        TestResult.addError(self, test, err)
        _, _exc_str = self.errors[-1]
        output = self.complete_output()
        self.result.append((2, test, output, _exc_str))
        self.updateTestCaseResult(str(test), err,'fail')
        
    def addFailure(self, test, err):
        TestResult.addFailure(self, test, err)
        _, _exc_str = self.failures[-1]
        output = self.complete_output()
        self.result.append((1, test, output, _exc_str))
        self.updateTestCaseResult(str(test),err,'fail')
        
    def updateTestCaseResult(self,testcaseName,notes,status):
        hurdles.addResult(self.jobId,self.testerName,self.testplan,self.buildName,testcaseName,notes,status)
         
#------------------------------------------------------------------------
#-- gets input from the user and pass it on to the _TestResult class
class HurdlesRunner():
    def __init__(self,jobId,testerName,testplan,buildName):
        self.jobId = jobId
        self.testerName = testerName
        self.testplan = testplan
        self.buildName = buildName
        
    def run(self,test):
        result = _TestResult(self.jobId,self.testerName,self.testplan,self.buildName)
        test(result)
        
#-------------------------------------------------------------------------        
class OutputRedirector(object):
    """ Wrapper to redirect stdout or stderr """
    def __init__(self, fp):
        self.fp = fp
 
    def write(self, s):
        self.fp.write(s)
 
    def writelines(self, lines):
        self.fp.writelines(lines)
 
    def flush(self):
        self.fp.flush()
 
stdout_redirector = OutputRedirector(sys.stdout)
stderr_redirector = OutputRedirector(sys.stderr)