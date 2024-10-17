# %%
import selenium
import random
from Pw import passwor, mail

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# edge people

# %%
driver = webdriver.Edge()
url = "https://www.xreading.com/login/index.php"

driver.get(url)

username = driver.find_element("id", "username")
password = driver.find_element("id", "password")
loginbtn = driver.find_element("id", "loginbtn")

sleep(1)
username.send_keys(mail)
password.send_keys(passwor)
loginbtn.click()

Readingbtn = driver.find_element(By.LINK_TEXT, "Continue Reading")
Readingbtn.click()


# %%

sleep(2)
for i in range(20):
    driver.set_window_size(640, 750)
    sleep(random.randint(25, 30))
    driver.execute_script("window.scrollBy(0, 375);")
    sleep(random.randint(20, 25))
    driver.execute_script("window.scrollBy(0, 375);")
    btns = driver.find_elements(By.TAG_NAME, "button")
    end = 0

    for btn in btns:
        if btn.text == "Close":
            btn.click()
            end = 1
            break
        elif btn.text == "Next":
            btn.click()
            print(f"now done {i+1}st page")
            break
    if end == 1:
        print(f"dook is done")
        break


# %%

sleep(5)

driver.close()
print("done!")
