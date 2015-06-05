#-------------------------------------------------------------------
# About		: hurdles.py
# This module creates the database (hurdles.db) inside the Database
# folder during the start of the application, if DB exists it does
# not create instead it will update the database with new schema.
# This module contains methods that are used to update the
# data-tables.
#-------------------------------------------------------------------

#-- Import section
import sqlite3, os

#-- Global variables
pwd = os.path.abspath(os.path.dirname(__file__))
dbpath = pwd + '/hurdles.db'

#-- To Create Database tables
def createDB():
    conn = sqlite3.connect(dbpath) #-- creating db connection
    #-- creating jobs table (schema - 1)
    conn.execute('''CREATE TABLE JOBS
    (jobId INTEGER PRIMARY KEY,
    testerName TEXT NOT NULL,
    apiKey TEXT,
    jobDetails TEXT NOT NULL,
    testRunner TEXT NOT NULL,
    scheduledON TEXT NOT NULL,
    status TEXT NOT NULL);''')
    #-- creating results table (schema -1)
    conn.execute('''CREATE TABLE RESULTS
    (id INTEGER PRIMARY KEY,
    jobId INTEGER NOT NULL,
    testerName TEXT NOT NULL,
    testplan TEXT NOT NULL,
    build TEXT NOT NULL,
    testcaseName TEXT NOT NULL,
    comments TEXT,
    status TEXT NOT NULL);''')
    conn.close() #-- close db connection

#-- To update database tables
def updateSchema():
    pass

#-- To create a job
def createJob(testerName,apiKey,jobDetails,testRunner,scheduledOn,status):
    conn = sqlite3.connect(dbpath)
    conn.execute("INSERT INTO JOBS (testerName,apiKey,jobDetails,testRunner,scheduledON,status) VALUES (?,?,?,?,?,?);",
    (testerName,apiKey,jobDetails,testRunner,scheduledOn,status))
    conn.commit()
    conn.close()

#-- It will return all the jobs
def getAllJobs():
    conn = sqlite3.connect(dbpath)
    cur = conn.cursor()
    cur.execute("SELECT * FROM JOBS")
    rows = cur.fetchall()
    conn.close()
    return rows

#-- It will return all the inactive jobs
def getAllInactiveJobs():
    conn = sqlite3.connect(dbpath)
    cur = conn.cursor()
    cur.execute("SELECT * FROM JOBS where status='Inactive'")
    rows = cur.fetchall()
    return rows

#-- It will return the particular jobDetails
def getJobUsingJobId(jobId):
    conn = sqlite3.connect(dbpath)
    cur = conn.cursor()
    cur.execute("SELECT * FROM JOBS where jobId='"+str(jobId)+"'")
    row = cur.fetchall()
    return row

#-- It will update the job status
def updateJobStatus(jobId,status):
    conn = sqlite3.connect(dbpath)
    conn.execute("UPDATE JOBS SET status='"+status+"'where jobId='"+str(jobId)+"'")
    conn.commit()
    conn.close()

#-- To add the testcase result
def addResult(jobId,testerName,testplan,build,testcaseName,comments,status):
    conn = sqlite3.connect(dbpath)
    conn.execute("INSERT INTO RESULTS (jobId,testerName,testplan,build,testcaseName,comments,status) VALUES (?,?,?,?,?,?,?)",
    (jobId,testerName,testplan,build,testcaseName,comments,status))
    conn.commit()
    conn.close()

#-- It will return all the results
def getAllResults():
    conn = sqlite3.connect(dbpath)
    cur = conn.cursor()
    cur.execute("SELECT * FROM RESULTS")
    rows = cur.fetchall()
    return rows
