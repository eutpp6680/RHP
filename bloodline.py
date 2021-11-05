import pandas as pd
import numpy as np
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement



#sample_driver.set_page_load_timeout(15)
driver = webdriver.Chrome()
driver.get("https://db.netkeiba.com/?pid=horse_search_detail")

#sel = Select(driver.find_element(By.NAME("under_age")))
sel = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div[1]/div[2]/form/table/tbody/tr[10]/td/select[1]")

selector = Select(sel)
selector.select_by_value('3')

#WebElement sel2 = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div[1]/div[2]/form/table/tbody/tr[9]/td/input[1]")


#sel2.click()

