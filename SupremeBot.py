from bs4 import BeautifulSoup
import urllib.request
import re
import requests
import random
import webbrowser
import csv
import threading
import requests
from selenium import webdriver
import time
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from tkinter import *
import winreg
import datetime



global isContinue 
global isFirst
isFirst = True
isContinue = 1



while(isContinue == 1):






        #set Chrome profile     
        print('Open Chrome')
        if isFirst:
                options = webdriver.ChromeOptions()
                options.add_argument("user-data-dir=C:\\Users\\Allan\\AppData\\Local\\Google\\Chrome\\User Data")                                   
                driver = webdriver.Chrome(executable_path ="D:\\Desktop\\python\\chromedriver.exe",options = options)
                isFirst = False
                ontime = False
                print('First time , enter any button to start')
                input()
        

        
        
        #Start to scrap Supreme
        SupUrl = "http://www.supremenewyork.com"
        #0'new'',1'shirts',2'tops_sweaters',3'shorts',4't-shirts',5'hats',6'bags',7'accessories',8'skate
        category = ['new','shirts','tops_sweaters','shorts','t-shirts','hats','bags','accessories','skate']
        print("Grabbing URL")
        r = requests.get('http://www.supremenewyork.com'+'/shop'+'/all'+'/'+category[8])
        soup = BeautifulSoup(r.text,'html.parser')
        CSOUP = soup.find_all('div',{"class":"inner-article"})
        array_length = len(CSOUP)
        print(array_length)
        #Type what u want
        WantedName = 'Truck'
        UrlList = []
        WantedList = []
        DesiredUrl = []
        isFound = False
        


        #Get each item's URL

        for i in range(array_length):        

                UrlList.append(CSOUP[i].find('a').get('href'))
                ItemRequest = requests.get(SupUrl+UrlList[i])
                EachSoup = BeautifulSoup(ItemRequest.text,'html.parser')
                ItemList = EachSoup.find_all('h1')
                EachName = ItemList[1].get_text()
                print(EachName)
                if WantedName in EachName:
                        #print(EachName)
                        DesiredUrl.append(SupUrl+UrlList[i])
                        print(DesiredUrl)
                        break
                

                        
                #print(SupUrl+UrlList[i])

        
             
        #add to cart
        driver.get(DesiredUrl[0])

##        driver.find_element_by_xpath('//*[@id="size"]').send_keys('Medium')
        driver.find_element_by_xpath('//*[@id="add-remove-buttons"]/input').click()
        #wait
        locatorCart=(By.XPATH,'//*[@id="cart"]/a[1]')
        WebDriverWait(driver, 20, 0.2).until(EC.visibility_of_element_located(locatorCart))
        driver.get('https://www.supremenewyork.com/checkout')



        #auto fill
        ##driver.find_element_by_xpath('//*[@id="credit_card_last_name"]').send_keys("Allan")
        ##driver.find_element_by_xpath('//*[@id="credit_card_first_name"]').send_keys("Wang")
        ##driver.find_element_by_xpath('//*[@id="order_email"]').send_keys("allanswer3@gmail.com")
        ##driver.find_element_by_xpath('//*[@id="order_tel"]').send_keys("0955235888")
        ##driver.find_element_by_xpath('//*[@id="order_billing_state"]').send_keys("東京都")
        ##driver.find_element_by_xpath('//*[@id="order_billing_city"]').send_keys("Chicago")
        ##driver.find_element_by_xpath('//*[@id="order_billing_address"]').send_keys("Taipei")
        ##driver.find_element_by_xpath('//*[@id="order_billing_zip"]').send_keys("114")
        ##driver.find_element_by_xpath('//*[@id="credit_card_type"]').send_keys("Mastercard")
        ##driver.find_element_by_xpath('//*[@id="cnb"]').send_keys("1111222233335555")
        ##driver.find_element_by_xpath('//*[@id="credit_card_month"]').send_keys("12")
        ##driver.find_element_by_xpath('//*[@id="credit_card_year"]').send_keys("25")
        ##driver.find_element_by_xpath('//*[@id="vval"]').send_keys("888")
        ##driver.find_element_by_xpath('//*[@id="order_terms"]').click()
        driver.find_element_by_css_selector('.checkout').click()

        print('Got you!!')
        print('Continue?')
        isContinue = int(input())


        print(isContinue)
        
        if isContinue == 1:
                driver.execute_script("window.open('http://google.com', 'new_window')")
                driver.switch_to_window(driver.window_handles[0])
                
        
        
        















        







