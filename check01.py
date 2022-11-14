from selenium import webdriver
from setdata import *
import xu_ly_input
import selenium, json
import time

dict_data = {}
login = {"admin":"", "password":""}
params = xu_ly_input.setdata['parameters']
url = xu_ly_input.setdata['url']
list_check = xu_ly_input.setdata['list pass']

driver = webdriver.Chrome("/usr/bin/chromedriver")
driver.get(url)

try:
    for username, password in list_check:
        driver.find_element('id',params['id_user']).send_keys(username)
        driver.find_element('id',params['id_pass']).send_keys(password)
        driver.find_element('id',params['id_sbmt']).click()
        login["admin"] = username
        login["password"] = password
except selenium.common.exceptions.ElementNotInteractableException:
    print("There is a login restriction mechanism on the device!")
    print("Pleased, Unplug and Re-plug the device!")
    dict_data["Protect Device"] = "Login restriction mechanism on the device!"
    time.sleep(120)
    driver.close()
except selenium.common.exceptions.NoSuchElementException:
    print("Login successful!")
    dict_data["Default password vulnerable"] = login
    out_file = open("./output/out1.json", "w+")
    json.dump(dict_data, out_file, indent = 6)
    out_file.close()
    driver.close()
finally:
    out_file = open("./output/out1.json", "w+")
    json.dump(dict_data, out_file, indent = 6)
    out_file.close()
    driver.close()



    