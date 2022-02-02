import pandas as pd
import numpy as np
import time
from time import sleep 
import re
from pandas.core.frame import DataFrame
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement, getAttribute_js
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome()
driver.maximize_window()
driver.set_page_load_timeout(15)
url = "https://db.netkeiba.com/?pid=horse_search_detail"
driver.get(url)

sel = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[1]/div[1]/div[2]/form/table/tbody/tr[10]/td/select[1]") #NewAge: lower limit
#sel = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div[1]/div[2]/form/table/tbody/tr[10]/td/select[1]") #old_Age: lower limit
selector = Select(sel)
selector.select_by_value('2')

sel2 = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[1]/div[1]/div[2]/form/table/tbody/tr[10]/td/select[2]") #NewAge: upper limit
#sel2 = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div[1]/div[2]/form/table/tbody/tr[10]/td/select[2]") #old_Age: upper limit
selector2 = Select(sel2)
selector2.select_by_value('none')


driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[1]/div[1]/div[2]/form/table/tbody/tr[9]/td/input[1]").click() #New_Sex
#driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[1]/div[1]/div[2]/form/table/tbody/tr[9]/td/input[1]").click() #old_Sex


button = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[1]/div[1]/div[2]/form/div/input[1]") #New_Search button
#button = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div[1]/div[2]/form/div/input[1]") #old_Search button

actions = ActionChains(driver) 
actions.move_to_element(button).perform()
driver.execute_script("arguments[0].scrollIntoView();", button) #
driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[1]/div[1]/div[2]/form/table/tbody/tr[17]/td/input[2]").click() #options
button.click()
#driver.set_page_load_timeout(45)
#time.sleep(5)

#cell = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/form/table/tbody/tr[2]/td[2]/a")
#driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/form/table/tbody/tr[2]/td[2]/a")
#valString = cell.get_attribute('href')
#print(valString)

data = []
table_winning = []
driver.set_page_load_timeout(35)
#next_size = len(next_button)
#pager = driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div/div[2]")

while True:
    driver.set_page_load_timeout(35) 
    time.sleep(3)  
    next_button = driver.find_elements(By.XPATH, "/html/body/div[1]/div[3]/div/div/div[2]/a[2]") #Search Next button 
    next_button1st = driver.find_elements(By.XPATH,"/html/body/div[1]/div[3]/div/div/div[2]/a") #Search for 1st Next button
    prev_button = driver.find_elements(By.XPATH,"/html/body/div[1]/div[3]/div/div/div[2]/a[1]") #Search Previous button
    #next_button = driver.find_elements(By.XPATH, "/html/body/div[1]/div[2]/div/div/div[2]/a[2]") #Search Next button(OLD)
    #next_button1st = driver.find_elements(By.XPATH,"/html/body/div[1]/div[2]/div/div/div[2]/a") #Search for 1st Next button(OLD)
    #prev_button = driver.find_elements(By.XPATH,"/html/body/div[1]/div[2]/div/div/div[2]/a[1]") #Search Previous button
    
    try:
        for x in range(2,21):
            time.sleep(2)
            driver.set_page_load_timeout(40)  
            id = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/form/table/tbody/tr"+ str([x])+"/td[2]/a").get_attribute('href')
            num_id = re.findall('\d+',id) #Filter only the numbers
            blood = "https://db.netkeiba.com/horse/ped/"+ str(num_id[0])+"/" #Make link for bloodpath   
            data.append([num_id[0],blood]) #Append to a list temporary, create a DataFrame later as a whole
            #----Goes to each horse database
            WebDriverWait(driver,40).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[3]/div/form/table/tbody/tr"+ str([x])+"/td[2]/a"))).click()
            #time.sleep(6)
            y = 0 #iterable
            #Loop to get all the table data
            while True:  
                sets = [] 
                try:   
                    for z in range(1,50):
                         driver.set_page_load_timeout(40)  
                         date = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[4]/div/table/tbody/tr " + str([z]) +"/td[1]/a").get_attribute('innerHTML')
                         held = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[4]/div/table/tbody/tr " + str([z]) +"/td[2]/a").get_attribute('innerHTML')
                         weather = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[4]/div/table/tbody/tr " + str([z]) +"/td[3]").get_attribute('innerHTML')
                         r_value = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[4]/div/table/tbody/tr" + str([z]) + "/td[4]").get_attribute('innerHTML')
                         race_name = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[4]/div/table/tbody/tr" + str([z]) + "/td[5]/a").get_attribute('innerHTML')
                         total_horse = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[4]/div/table/tbody/tr" + str([z]) + "/td[7]").get_attribute('innerHTML')
                         bracket_num = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[4]/div/table/tbody/tr" + str([z]) + "/td[8]").get_attribute('innerHTML')
                         horse_num =  driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[4]/div/table/tbody/tr" + str([z]) + "/td[9]").get_attribute('innerHTML')
                         odds = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[4]/div/table/tbody/tr" + str([z]) + "/td[10]").get_attribute('innerHTML')  
                         popularity = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[4]/div/table/tbody/tr" + str([z]) + "/td[11]").get_attribute('innerHTML')  
                         place = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[4]/div/table/tbody/tr" + str([z]) + "/td[12]").get_attribute('innerHTML')  
                         rider = driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[4]/div/table/tbody/tr" + str([z]) + "/td[13]/a").get_attribute('innerHTML')
                         penalty = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[4]/div/table/tbody/tr" + str([z]) + "/td[14]").get_attribute('innerHTML') 
                         distance = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[4]/div/table/tbody/tr" + str([z]) + "/td[15]").get_attribute('innerHTML') 
                         track_condition = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[4]/div/table/tbody/tr" + str([z]) + "/td[16]").get_attribute('innerHTML')
                         race_time =  driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[4]/div/table/tbody/tr" + str([z]) + "/td[18]").get_attribute('innerHTML')
                         margin = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[4]/div/table/tbody/tr" + str([z]) + "/td[19]").get_attribute('innerHTML')
                         passing = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[4]/div/table/tbody/tr" + str([z]) + "/td[21]").get_attribute('innerHTML')
                         pace =  driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[4]/div/table/tbody/tr" + str([z]) + "/td[22]").get_attribute('innerHTML')
                         fin = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[4]/div/table/tbody/tr" + str([z]) + "/td[23]").get_attribute('innerHTML')
                         horse_weight = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[4]/div/table/tbody/tr" + str([z]) + "/td[24]").get_attribute('innerHTML')
                         loser_horse = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[4]/div/table/tbody/tr" + str([z]) + "/td[27]/a").get_attribute('innerHTML')
                         prize = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[4]/div/table/tbody/tr" + str([z]) + "/td[28]").get_attribute('innerHTML')
                         sets.append([date,held,weather,r_value,race_name,total_horse,bracket_num,horse_num,odds,popularity,place,rider,penalty,distance,track_condition,race_time,margin,passing,pace,fin,horse_weight,loser_horse,prize])
                         #held = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[4]/div/table/tbody/tr" + str ([w]) + "/td" + str([z]) + "/a").get_attribute("innerHTML")
                         #weather = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[4]/div/table/tbody/tr" + str ([w]) + "/td" + str([z])).get_attribute("InnerHTML")       
                except:
                    print("going back error")
                    print(sets)
                    df2 = DataFrame(sets, columns=['Date','Host','Weather','R_value','Race_name','Total_horse','Bracket_number','Horse_number','Odds','Popularity','Place','Rider','Penalty','Distance','Track_condition','Race_time','Margin','Passing','Pace','Fin','Horse_weight','Loser_horse','Prize'])
                    df2.to_csv(str(num_id[0])+'.csv')
                    driver.back()
                    break
            #id_path = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/form/table/tbody/tr"+ str([x])+"/td[2]/a")
            #id = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/form/table/tbody/tr"+ str([x])+"/td[2]/a").get_attribute('href')
            #print(len(next_button1st))
            #print(len(next_button))
        print("Completed Batch")
        if(len(next_button1st) == 1):
            time.sleep(5) 
            WebDriverWait(driver,40).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[3]/div/div/div[2]/a"))).click()
        elif(len(next_button) == 1):
            time.sleep(5)
            WebDriverWait(driver,40).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[3]/div/div/div[2]/a[2]"))).click()
        else: 
            break
    except:
        break



    next_button1st = driver.find_elements(By.XPATH,"/html/body/div[1]/div[3]/div/div/div[2]/a") #Search for 1st Next button
    #next_button = driver.find_elements(By.XPATH, "/html/body/div[1]/div[2]/div/div/div[2]/a[2]")
    #time.sleep(5)
    #next_button.click()
##
df = DataFrame(data, columns=['ID','blood_path'])
df.to_csv('id+path2.csv')

