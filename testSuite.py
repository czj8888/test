from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import time
import unittest
import logging
import datetime
import subprocess
import schedule
import csv
import sys
import os

BASE=os.path.dirname(os.path.realpath(__file__))

from util import utilFunc
from config import configFile
from testCase import HomeRegularTest


## SELECT TESTCASE
# HomeRegularTest is the test case script. Change it when necessary!
# Testmy is test object name. Don't need to change
testCase=HomeRegularTest.Testmy

if __name__=='__main__':
    #unittest.main()
    def executeTestCase():
        suite = unittest.TestSuite()
        ## Add test case to the suite
        ## androidTest is the specific test case

        if configFile.phoneModel=='HUAWEI':
            if(configFile.superBrandDay==True):
                print("It is super brand day")
                suite.addTest(testCase("androidTestBrandDay"))
            else:
                print("not super brand day")
                suite.addTest(testCase("androidTest"))

        elif configFile.phoneModel=='iPhone':
            if (configFile.superBrandDay == True):
                print("It is super brand day")
                suite.addTest(testCase("iosTestBrandDay"))
            else:
                print("not super brand day")
                suite.addTest(testCase("iosTest"))
        runner = unittest.TextTestRunner()
        runner.run(suite)
        utilFunc.uploadToServer()

    executeTestCase()

"""
    schedule.every().day.at("16:02").do(executeTestCase)

    while True:
        schedule.run_pending()
        print(datetime.datetime.now())
        time.sleep(1)
"""