import pandas as pd
import numpy as np
import time 
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.action_chains import ActionChains

def ad_checker(sample_driver,check):
    while check == True:
        try:
            sample_driver.find_element_by_xpath('//*[@id="gn_interstitial_close_icon"]').click()
            check=False
        except:
            continue

driver = webdriver.Chrome()
driver.maximize_window()
driver.set_page_load_timeout(15)
url = "https://db.netkeiba.com/?pid=horse_search_detail"
driver.get(url)


sel = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[1]/div[1]/div[2]/form/table/tbody/tr[10]/td/select[1]") #Age
selector = Select(sel)
selector.select_by_value('3')

driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[1]/div[1]/div[2]/form/table/tbody/tr[9]/td/input[1]").click() #Sex

button = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div[1]/div[2]/form/div/input[1]") #Search button
actions = ActionChains(driver) 
actions.move_to_element(button).perform()
driver.execute_script("arguments[0].scrollIntoView();", button) #
button.click()
#driver.set_page_load_timeout(45)
#time.sleep(5)

#cell = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/form/table/tbody/tr[2]/td[2]/a")
#driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/form/table/tbody/tr[2]/td[2]/a")
#valString = cell.get_attribute('href')
#print(valString)
for x in range(2,21):
    id = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/form/table/tbody/tr"+ str([x])+"/td[2]/a").get_attribute('href')
    print(re.findall('\d+', ))