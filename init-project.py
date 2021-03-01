

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys

if len(sys.argv) < 4:
    raise Exception(
        "ex:file.py 'GITHUB USERNAME' 'PASSWORD' 'PROJECT_NAME' 'IS_PUBLIC=true/false'")

username = sys.argv[1]
password = sys.argv[2]
name = sys.argv[3]
is_public = sys.argv[4]

if is_public != "true" and is_public != "false":
    raise Exception("3 args [true,false]")

driver = webdriver.Edge("./msedgedriver")

target_url = "https://github.com/login"
driver.get(target_url)

login_field = driver.find_element_by_id("login_field")
password_field = driver.find_element_by_id("password")

login_field.send_keys(username)
password_field.send_keys(password)

# ENTER
password_field.send_keys(Keys.RETURN)

driver.get("https://github.com/new")

project_name = driver.find_element_by_name("repository[name]")
project_name.send_keys(name)

success_name = False

while success_name == False:
    try:
        success_element = driver.find_element_by_class_name("success")
        success_name = True
    except:
        success_name = False

if is_public == "true":
    public_private = driver.find_element_by_name("repository[visibility]")
    public_private.click()

btn_submit = driver.find_element_by_class_name("btn-primary")
btn_submit.click()

url = driver.find_element_by_id("empty-setup-clone-url")
