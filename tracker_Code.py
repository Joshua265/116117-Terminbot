from random import randint, random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

import time
import winsound
from datetime import datetime
import sys
import getopt

try:
    opts, args = getopt.getopt(sys.argv[1:], "hp:b:", ["plz=", "bday="])
except getopt.GetoptError:
    print('test.py -p <PLZ> -b <bday DDMMYYYY>')
    sys.exit(2)
for opt, arg in opts:
    if opt == '-h':
        print('test.py -p <PLZ> -b <bday DDMMYYYY>')
        sys.exit()
    elif opt in ("-p", "--plz"):
        PLZ = arg
    elif opt in ("-b", "--bday"):
        geburtsdatum = arg

frequency = 840  # Set Frequency To 840 Hertz
duration = 1000  # Set Duration To 1000 ms == 1 second

url = 'https://003-iz.impfterminservice.de/impftermine'
url1 = f"https://003-iz.impfterminservice.de/impftermine/service?plz={PLZ}"
flag = 0


def delete_cache():
    time.sleep(2)
    # for old chromebrowser versions use clearbrowserData
    browser.get('chrome://settings/clearBrowserData')
    time.sleep(2)
    actions = ActionChains(browser)
    actions.send_keys(Keys.TAB * 3 + Keys.DOWN * 3)  # send right combination
    actions.perform()
    time.sleep(2)
    actions = ActionChains(browser)
    actions.send_keys(Keys.TAB * 4 + Keys.ENTER)  # confirm
    actions.perform()
    time.sleep(5)  # wait some time to finish


def clickOnObject(xPath):
    WebDriverWait(browser, 5).until(
        expected_conditions.visibility_of_element_located((By.XPATH, xPath)))
    el = browser.find_element_by_xpath(xPath)
    el.click()


code = False

browser = webdriver.Chrome(
    executable_path=r"C:\\Program Files (x86)\\chromedriver\\chromedriver.exe")
while True:
    if code == True:
        break
    delete_cache()
    browser.get(url)
    time.sleep(random()+1)
    browser.get(url1)
    # accept cookies
    try:
        clickOnObject(
            '/html/body/app-root/div/div/div/div[3]/div[2]/div/div[1]/a')
    except:
        pass
    try:
        clickOnObject(
            '//a[@class="cookies-info-close btn kv-btn btn-magenta"]')
    except:
        pass

    # Anspruch pruefen
    for i in range(20):
        if code == True:
            break
        while True:
            try:
                clickOnObject(
                    '/html/body/app-root/div/app-page-its-login/div/div/div[2]/app-its-login-user/div/div/app-corona-vaccination/div[2]/div/div/label[2]')
                break
            except:
                continue
        time.sleep(random()*3+5)
        try:
            kasten = browser.find_element_by_xpath(
                "/html/body/app-root/div/app-page-its-login/div/div/div[2]/app-its-login-user/div/div/app-corona-vaccination/div[3]/div/div/div/div[2]/div/div/div")
            print("kein Termin vorhanden")
            time.sleep(random()*120+120)

        except:

            # insert data
            browser.execute_script(
                "window.scrollTo(0,document.body.scrollHeight)")
            # impfberechtigt ja
            clickOnObject(
                '/html/body/app-root/div/app-page-its-login/div/div/div[2]/app-its-login-user/div/div/app-corona-vaccination/div[3]/div/div/div/div[2]/div/app-corona-vaccination-no/form/div[1]/div/div/label[1]/span')

            # geburtsdatum eingeben
            bday_input = browser.find_element_by_xpath(
                '//input[@formcontrolname="birthdate"]')
            # bday_input = browser.find_element_by_xpath(
            #     '/html/body/app-root/div/app-page-its-login/div/div/div[2]/app-its-login-user/div/div/app-corona-vaccination/div[3]/div/div/div/div[2]/div/app-corona-vaccination-no/form/div[4]/div/div/input')
            bday_input.send_keys(geburtsdatum)

            # pruefung durchfuehren
            clickOnObject('//button[@type="submit"]')
            winsound.Beep(frequency, duration)
            now = datetime.now()
            print(f"Termin in {PLZ}!")

            print(now.strftime("%H:%M:%S"))

            try:
                kasten = browser.find_element_by_xpath(
                    '/html/body/app-root/div/app-page-its-login/div/div/div[2]/app-its-login-user/div/div/app-corona-vaccination/div[3]/div/div/div/div[2]/div/app-corona-vaccination-no/form/div[2]')
                for i in range(10000000):
                    clickOnObject('//button[@type="submit"]')
                    time.sleep(1)
                    kasten = browser.find_element_by_xpath(
                        '/html/body/app-root/div/app-page-its-login/div/div/div[2]/app-its-login-user/div/div/app-corona-vaccination/div[3]/div/div/div/div[2]/div/app-corona-vaccination-no/form/div[2]')

            except:
                code = True
                break
