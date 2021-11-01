import pandas as pd
import numpy as np
import selenium
from selenium.webdriver import Chrome,ChromeOptions
import chromedriver_binary
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

options = ChromeOptions()
sample_driver = Chrome(options=options)
url = "https://db.netkeiba.com/?pid=horse_search_detail"
sample_driver.get(url)
sample_driver.set_page_load_timeout(15)
sample_driver.find_element_by_xpath('//*[@id="check_sex_1"]').click()
sample_driver.find_element_by_xpath('//*[@id="gn_interstitial_close_icon"]').click()
sample_driver.find_element_by_xpath('//*[@id="check_other_02"]').click()
sample_driver.find_element_by_xpath('//*[@id="db_search_detail_form"]/form/div/input[1]').click()
sample_driver.set_page_load_timeout(15)

sample_driver.find_element_by_xpath('//*[@id="gn_interstitial_close_icon"]').click()
for x in range(20):
    x+=2
    if 4==len(sample_driver.find_elements_by_xpath('//*[@id="contents_liquid"]/div/form/table/tbody/tr['+str(x)+']/td[5]/a')):
        sample_driver.find_element_by_xpath('//*[@id="contents_liquid"]/div/form/table/tbody/tr['+str(x)+']/td[5]/a[1]').click()

        sample_driver.find_element_by_xpath('//*[@id="gn_interstitial_close_icon"]').click()
        for y in range(5):
            y+=1
            for z in range(2):
                z+=1
                print(sample_driver.find_element_by_xpath('//*[@id="contents"]/div[2]/diary_snap/table/tbody/tr[1]/td['+str(y)+']/a['+str(z)+']').text)



#//*[@id="contents"]/div[2]/diary_snap/table/tbody/tr[17]/td[1]/a[1]