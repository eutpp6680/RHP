import pandas as pd
import numpy as np
import selenium
from selenium.webdriver import Chrome,ChromeOptions
import chromedriver_binary
import ssl
import time
ssl._create_default_https_context = ssl._create_unverified_context

def ad_checker(sample_driver,check):
    while check == True:
        try:
            sample_driver.find_element_by_xpath('//*[@id="gn_interstitial_close_icon"]').click()
            check=False
        except:
            continue

options = ChromeOptions()
sample_driver = Chrome(options=options)
url = "https://db.netkeiba.com/?pid=horse_search_detail"
sample_driver.get(url)
sample_driver.set_page_load_timeout(30)
sample_driver.find_element_by_xpath('//*[@id="check_sex_1"]').click()
sample_driver.set_page_load_timeout(5)
sample_driver.find_element_by_xpath('//*[@id="db_search_detail_form"]/form/table/tbody/tr[10]/td/select[2]/option[9]').click()
sample_driver.set_page_load_timeout(5)
ad_checker(sample_driver,check=True)
sample_driver.set_page_load_timeout(5)
sample_driver.find_element_by_xpath('//*[@id="check_other_02"]').click()
sample_driver.set_page_load_timeout(5)
sample_driver.find_element_by_xpath('//*[@id="db_search_detail_form"]/form/div/input[1]').click()
sample_driver.set_page_load_timeout(30)

ad_checker(sample_driver,check=True)
blood_list = []

for x in range(20):
    x += 2
    if 4==len(sample_driver.find_elements_by_xpath('//*[@id="contents_liquid"]/div/form/table/tbody/tr['+str(x)+']/td[5]/a')):
        sample_driver.find_element_by_xpath('//*[@id="contents_liquid"]/div/form/table/tbody/tr['+str(x)+']/td[5]/a[1]').click()
        sample_driver.set_page_load_timeout(30)

        blood_list_1 = []
        blood_list_1.append(sample_driver.current_url.split("/")[5])
        ad_checker(sample_driver,check=True)
        for y in range(32):
            y += 1
            sam = sample_driver.find_elements_by_xpath('//*[@id="contents"]/div[2]/diary_snap/table/tbody/tr[' + str(y) + ']')
            for z in range(len(sam)):
                blood_list_1.append(sam[z].text)
        blood_list.append(blood_list_1)
        sample_driver.back()
        sample_driver.set_page_load_timeout(30)
        ad_checker(sample_driver,check=True)
blood_list = pd.DataFrame(blood_list)

parent = []
parent.append("horse_id")
for parent1 in ["父","母"]:
    parent.append(parent1)
    for parent2 in ["父","母"]:
        parent.append(parent1+parent2)
        for parent3 in ["父","母"]:
            parent.append(parent1+parent2+parent3)
            for parent4 in ["父","母"]:
                parent.append(parent1+parent2+parent3+parent4)

for f in range(31):
    col = parent[f]
    blood_list = blood_list.rename(columns={f:col})

blood_list.to_csv("stallion.csv",encoding="utf-8")


print(blood_list.iloc[:,:20])
print(blood_list.iloc[:,20:40])
print(blood_list.iloc[:,60:80])
            



#//*[@id="contents"]/div[2]/diary_snap/table/tbody/tr[1]/td[1]
#//*[@id="contents"]/div[2]/diary_snap/table/tbody/tr[17]/td[1]

#//*[@id="contents"]/div[2]/diary_snap/table/tbody/tr[1]/td[2]
#//*[@id="contents"]/div[2]/diary_snap/table/tbody/tr[9]/td[1]
#//*[@id="contents"]/div[2]/diary_snap/table/tbody/tr[17]/td[2]
#//*[@id="contents"]/div[2]/diary_snap/table/tbody/tr[32]/td