# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 10:24:29 2021
Created on Fri Dec 24 10:24:29 2021

@author: koki
"""

from bs4 import BeautifulSoup
import re
#import pandas as pd
#import numpy as np
from tqdm import tqdm
#import pickle
import time
#import math
#import statistics
from selenium import webdriver
#from selenium.webdriver.common.keys import Keys as keys
#from selenium.webdriver.common.by import By

url='https://db.netkeiba.com/?pid=horse_search_detail'
driver = webdriver.Chrome("chromedriver.exe")
driver.get(url)

element=driver.find_element_by_id("check_sex_2")
driver.execute_script("arguments[0].click();", element)
'''
element2=driver.find_element_by_class_name("field")
driver.execute_script("arguments[0].click();", element2)
'''

element3=driver.find_element_by_id("check_other_02")
driver.execute_script("arguments[0].click();", element3)

element4=driver.find_element_by_class_name("button")
driver.execute_script("arguments[0].click();", element4)

driver.set_page_load_timeout(15)

kettou_list_list=[]
for i in range(2):
    try:
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        table=soup.find_all('td', {'class': 'xml txt_l'})
        horse_id_list=re.findall(r'/horse/([!-~]{10})',str(table))
        
        kettou_list=[]
        for hi in tqdm(horse_id_list):
            try:
                kettou='https://db.netkeiba.com/horse/ped/'+str(hi)
                kettou_list.append(kettou)
                time.sleep(1)
            except:
                continue
            
        kettou_list_list.extend(kettou_list)
        element5=driver.find_element_by_link_text("次")
        element5.click()
        time.sleep(1)
    except:
        continue

#breedmare_df=pd.DataFrame(data=horse_id_list,columns=['horse_id'])
#breedmare_df=breedmare_df.assign(馬名='')
