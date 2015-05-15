#------------------- Import Section ---------------------

import os, json, threading
from bottle import get,post,run,template,request,static_file,response,redirect
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
from Models import hurdles
from Modules import jobProcessor
import TestManager

#------------- Global Variables Section -----------------

pwd = os.path.abspath(os.path.dirname(__file__))

#--------------------- API's Section --------------------
#-- Returns landingpage of the application.
@get('/')
def index():
    return template('Views/landingpage.tpl')

#-- Returns static resources (js, css, images).
@get('/static/<filepath:path>')
def static_files(filepath):
    return static_file(filepath,root=pwd+'/Static')

#-- Returns the homepage
@post('/login')
def do_login():
    userName = request.forms.get('userName')
    testplan = request.forms.get('testPlan')
    buildName = request.forms.get('buildName')
    apiKey = request.forms.get('apikey')
    testRunner = request.forms.get('TestRunner')
    response.set_cookie("username",userName)
    response.set_cookie("testplan",testplan)
    response.set_cookie("buildName",buildName)
    response.set_cookie("apiKey",apiKey)
    response.set_cookie("testRunner",testRunner)
    return template('Views/homepage.tpl',username=userName)

#-- Clears the cookie and returns the homepage
@post('/logout')
def do_logout():
    response.set_cookie("username","",expires=0)
    response.set_cookie("testplan","",expires=0)
    response.set_cookie("buildName","",expires=0)
    response.set_cookie("apiKey","",expires=0)
    response.set_cookie("testRunner","",expires=0)
    return template('Views/landingpage.tpl')

#-- It will return all the testSuites
@get('/testSuites')
def testSites():
    return template('Views/testSuites.tpl', TestCases = str(TestManager.testSuitesInHtmlFormat()))

#-- To create a job
@post('/createJob')
def do_createJob():
    userName = request.get_cookie('username')
    testPlan = request.get_cookie('testplan')
    buildName = request.get_cookie('buildName')
    apiKey = request.get_cookie('apiKey')
    testRunner = request.get_cookie('testRunner')
    scheduledOn = request.forms.get('schedule')
    #mode = request.forms.get('mode')
    selectedTestCases = request.forms.getall('chkTest')
    jobDetails = json.dumps({"testCases":selectedTestCases,"testPlan":testPlan,"build":buildName})
    hurdles.createJob(userName,apiKey,jobDetails,testRunner,scheduledOn,'Inactive')
    redirect('/jobs')

#-- It will return the jobs
@get('/jobs')
def jobs():
    jobDetails = hurdles.getAllJobs()
    return template('Views/jobs.tpl',jobs=jobDetails)

#-- It will return the results
@get('/results')
def results():
    results = hurdles.getAllResults()
    return template('Views/results.tpl',results=results)

#-------------------Scheduler section--------------------
sched = BackgroundScheduler()

@sched.scheduled_job('interval', minutes=1)
def timed_job():
    threads = []
    inactiveJobs = hurdles.getAllInactiveJobs()
    for inactiveJob in inactiveJobs:
        scheduledon = inactiveJob[5]
        currentTime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        if scheduledon < currentTime:
            jobId = inactiveJob[0]
            testRunner = inactiveJob[4]
            if testRunner == 'Hurdles':
                t = threading.Thread(target=jobProcessor.runTestUsingHurdlesRunner,args=(jobId,))
                threads.append(t)
            elif testRunner == 'Testlink':
                t = threading.Thread(target=jobProcessor.runTestUsingTestLinkRunner,args=(jobId,))
                threads.append(t)
    for thread in threads:
        thread.start()

sched.start() #-- To run the scheduled jobs

#--------------------Database section--------------------
#-- To create Database
dbpath = pwd+'/Database/hurdles.db'
if os.path.isfile(dbpath):
    hurdles.updateSchema()
else:
    hurdles.createDB()

#--------------------Webserver section-------------------
#-- To launch application
run(host="0.0.0.0", port=8181, debug=True,server='paste')
