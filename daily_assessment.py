#!/usr/bin/env python
from selenium import webdriver 
from time import sleep 
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.webdriver.chrome.options import Options 

from selenium.webdriver import ActionChains
from getpass import getpass
from auth import webhook_url, usr, pwd
import json
import requests

def pushNotification(message):
    #webhook_url = 'https://hooks.slack.com/services/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'
    slack_data = {'text': "%s"%message}

    response = requests.post(
        webhook_url, data=json.dumps(slack_data),
        headers={'Content-Type': 'application/json'}
    )
    if response.status_code != 200:
        raise ValueError(
            'Request to slack returned an error %s, the response is:\n%s'
            % (response.status_code, response.text)
        )

if __name__ == "__main__":
    
    try:
 
        driver = webdriver.Chrome(executable_path='/home/pranshu/Desktop/Pranshu/Personal/automate_daily_assessment/webdrivers/chromedriver')

        driver.get('https://daily-student.cmu.edu/') 
        print ("Opened SIO Login") 
        sleep(0.5) 
        
        username_box = driver.find_element_by_id('username') 
        username_box.send_keys(usr) 
        print ("Email Id entered") 
        sleep(0.5) 
        
        password_box = driver.find_element_by_id('passwordinput') 
        password_box.send_keys(pwd) 
        print ("Password entered") 
        sleep(0.5)
        
        login_box = driver.find_element_by_class_name('loginbutton') 
        login_box.click() 
        sleep(5)

        x_offset = 720
        y_offset = 137
        elem = driver.find_element_by_css_selector("#pageHeader")
        ac = ActionChains(driver)
        ac.move_to_element_with_offset(elem, x_offset, y_offset).click().perform() 
        sleep(10)

        q1 = driver.find_element_by_id('Field12_1')
        q1.click()
        sleep(0.5)

        q2 = driver.find_element_by_id('Field3_1')
        q2.click()
        sleep(0.5)

        q3 = driver.find_element_by_id('Field5_2')
        q3.click()
        sleep(0.5)

        print ("Fields filled") 

        submit = driver.find_element_by_id('saveForm') 
        submit.click() 
        print ("Done") 
        driver.quit() 
        print("Finished") 
        pushNotification("Submitted Daily Assessment")

    except Exception as e:
        print("Failed")
        message = "ERROR {} in Daily Assessment",format(e)
        pushNotification(message)