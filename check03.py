from selenium import webdriver
from time import sleep
import selenium, json
import xu_ly_input

username="admin"
password="admin"

dict_ver = {"version software":"", "version hardware":""}

url = xu_ly_input.setdata['url']
driver = webdriver.Chrome("/usr/bin/chromedriver")
driver.get(url)

params = xu_ly_input.setdata['parameters']
try:
    driver.find_element('id',params['id_user']).send_keys(username)
    driver.find_element('id',params['id_pass']).send_keys(password)
    driver.find_element('id',params['id_sbmt']).click()
    print("Login successful!")
    driver.refresh()

    driver.switch_to.frame("mainFrame")
    ver_soft = driver.find_element('id',params['id_soft']).get_attribute("innerHTML")
    ver_hard = driver.find_element('id',params['id_hard']).get_attribute("innerHTML")
    dict_ver["version hardware"] = ver_hard
    dict_ver["version software"] = ver_soft
    dict_data = {"Version Device":dict_ver}
    
    out_file = open("./output/out3.json", "w+")
    json.dump(dict_data, out_file, indent = 6)
    out_file.close()
    driver.close()
except selenium.common.exceptions.NoSuchElementException:
    dict_data = {"Version Device":"No find version software and hardware"}
    out_file = open("./output/out3.json", "w+")
    json.dump(dict_data, out_file, indent = 6)
    out_file.close()
    driver.close()