# Author: Harsha Mallajosyula
# MPP Candidate 2015
# Goldman School of Public Policy
# UC Berkeley
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException
import csv
import os
import sys
import logging
import random
import time
import codecs
import re
import datetime
from time import strftime

#writing to text file
class Logger(object):
    def __init__(self, filename="Default.log"):
        self.terminal = sys.stdout
        self.log = open(filename, "a")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

#sys.stdout = Logger("log_lastname_I_HM.cs
#sys.stdout = Logger(strftime("Logfiles/Patent_Search_Results_1A.txt"))
sys.stdout = Logger(strftime("Logfiles/Patent_Search_Results_1.csv"))

#setting proxy server
profile = webdriver.FirefoxProfile()
profile.set_preference("network.proxy.type", 1)
profile.set_preference("network.proxy.http", "proxy.server.address")
profile.set_preference("network.proxy.http_port", "port_number")
profile.update_preferences()
br = webdriver.Firefox(firefox_profile=profile)
br.implicitly_wait(15) # wait's for the page to get done loading before it does anything with it
#reading from csv:
#datafile = open('firminfo.csv', 'r')
#out = datafile.readlines()


with open('firminfo.csv', 'rU') as f:
    while 1:
        myline =f.readline()
        myline=myline.rstrip()
        name_variable = myline
        time.sleep(15)
        br.implicitly_wait(15)
        br.get('http://assignment.uspto.gov/#/search?')
        time.sleep(20)
        search=br.find_element_by_xpath('//*[@id="searchInput"]')
        search.send_keys(name_variable)
        search1= br.find_element_by_xpath('//*[@id="ember317"]/div[1]/div[3]/div/form/div[1]/div/div/div/input')
        search1.click()
        br.implicitly_wait(20)

        #check if search results are greater than zero
        date_start="01/01/2002"
        date_end = "01/01/2004"
        #search5_number = int(search5_number)
        #print search5_number
             #Execution Date Range
        time.sleep(15)
        br.find_element_by_xpath('//*[@id="patAssignorEarliestExDateHeader"]').click()
        time.sleep(20)
        search_from_date=br.find_element_by_xpath('//*[@id="dateRangeStart"]')
        search_from_date.send_keys("01/01/2002")
        time.sleep(20)
        search_to_date=br.find_element_by_xpath('//*[@id="dateRangeEnd"]')
        search_to_date.send_keys("01/01/2004")
        time.sleep(20)
            
            #date_start="01/01/2003"
            #date_end = "01/01/2005"
        search5_1=br.find_element_by_xpath('//*[@id="ember317"]/div[1]/div[4]/div/div[1]/div/div[1]/h1')
        time.sleep(20)
        search5_1=search5_1.text.encode('utf8')
        search5_1=search5_1.strip()
        search5_1=search5_1.replace('.','')
        search5_1=search5_1.replace(',','')
        search5_1=search5_1.replace("Results for", " ")
        print search5_1, ",", date_start, ",", date_end
        time.sleep(10)


br.quit()







