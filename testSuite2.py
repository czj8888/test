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
import json

BASE=os.path.dirname(os.path.realpath(__file__))


from util import utilFunc
from config import configFile
from testCase import LoginLogout
from testCase import liveDailyDiscover
from testCase import liveCartRecommend
from testCase import liveTopProduct
from testCase import liveMall
from testCase import liveFindSimilar
from testCase import liveTrendingSearch
from testCase import liveProductRecommend
from testCase import liveFlashsale
from testCase import liveCategory
from testCase import liveSearch
from testCase import liveHomeCircle
day=configFile.day
## SELECT TESTCASE
# HomeRegularTest is the test case script. Change it when necessary!
# Testmy is test object name. Don't need to change

loginCase=LoginLogout.Testmy

dailyDiscoverCase=liveDailyDiscover.Testmy
cartRecommendCase=liveCartRecommend.Testmy
topProductCase=liveTopProduct.Testmy
mallCase=liveMall.Testmy
findSimilarCase=liveFindSimilar.Testmy
trendingSearchCase=liveTrendingSearch.Testmy
productDetailCase=liveProductRecommend.Testmy
flashsaleCase=liveFlashsale.Testmy
categoryCase=liveCategory.Testmy
searchCase=liveSearch.Testmy
homeCircleCase=liveHomeCircle.Testmy

if __name__=='__main__':

    print(utilFunc.readCounter('homeFlashSaleItem'))
    utilFunc.addCounter('homeFlashSaleItem')
    utilFunc.addCounter('homeFlashSaleItem')

    #unittest.main()
    def executeTestCase():
        suite = unittest.TestSuite()
        ## Add test case to the suite
        ## androidTest is the specific test case

        if configFile.phoneModel!='shit':
            #suite.addTest(loginCase("androidLogin"))




            # ...CART YMAL... #
            #suite.addTest(cartRecommendCase("androidCartYmalItemClick"))
            #suite.addTest(cartRecommendCase("androidCartYmalItemImpression"))



            #suite.addTest(topProductCase("androidTopProductLandingItemClick"))
            #suite.addTest(topProductCase("androidTopProductLandingItemImpression"))
            #suite.addTest(topProductCase("androidHomeTopProductSeeMoreClick"))
            #suite.addTest(topProductCase("androidHomeTopProductSeeMoreCardClick"))
            #time.sleep(180)

            ##..Search..##
            #suite.addTest(searchCase("searchSimilarButtonClick"))
            #suite.addTest(searchCase("searchItemClick"))

            ##..homeCircle..##
            #suite.addTest(homeCircleCase("homeCircleClick"))


            ##..trending search..##
            #suite.addTest(trendingSearchCase("homeTrendingSearchClusterClick"))

            ##..Flashsale..##
            suite.addTest(flashsaleCase("homeFlashsaleItemClick"))
            suite.addTest(flashsaleCase("flashSaleLandingItemClick"))

            # ...Mall... #(Mall iOS has some problem)
            #suite.addTest(mallCase("homeMallShopClick"))
            suite.addTest(mallCase("mallJustForYouItemClick"))
            suite.addTest(mallCase("mallPopularProductsItemClick"))

            # ...Top Product...#
            # suite.addTest(topProductCase("androidTopProductLandingPV"))
            suite.addTest(topProductCase("homeTopProductClusterClick"))
            suite.addTest(topProductCase("topProductLandingItemClick"))

            ##..Category..##
            #suite.addTest(categoryCase("homeCategoryClick"))

            # ...DAILY DISCOVER... #
            # suite.addTest(dailyDiscoverCase("androidHomeDailyDiscoverItemImpression"))
            #suite.addTest(dailyDiscoverCase("homeDailyDiscoverItemClick"))

            #suite.addTest(loginCase("androidLogout"))
            pass

        elif configFile.phoneModel=='iPhone':
            suite.addTest(findSimilarCase("iosFindSimilarPV"))
            pass
        runner = unittest.TextTestRunner()
        runner.run(suite)

    ## if it's the first run of today, then reset all the counters
    if utilFunc.isFirstRunToday(day):
        utilFunc.clearCounter()

    ## run the test case
    executeTestCase()

    ## upload to remote server
    BASE = os.path.abspath(os.curdir)
    utilFunc.uploadToServer(localPath=BASE+'/homeTest{}.csv'.format(day),remotePath=configFile.remotePath)

    ##record the last running date
    utilFunc.recordLastRun(day)

"""
    schedule.every().day.at("16:02").do(executeTestCase)

    while True:
        schedule.run_pending()
        print(datetime.datetime.now())
        time.sleep(1)
"""