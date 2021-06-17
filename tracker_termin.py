from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait

from random import randint, random
import time
import winsound
from datetime import datetime

frequency = 840  # Set Frequency To 840 Hertz
duration = 10000  # Set Duration To 1000 ms == 1 second

PLZ = "YOUR_PLZ"
code = ["YOUR", "CODE", "HERE"]


def iserror():
    try:
        browser.find_element_by_xpath(
            '/html/body/app-root/div/app-page-its-login/div/div/div[2]/app-its-login-user/div/div/app-corona-vaccination/div[3]/div/div/div/div[1]/app-corona-vaccination-yes/form/div[1]/div')
        return False
    except:
        return True


def clickOnObject(xPath):
    WebDriverWait(browser, 5).until(
        expected_conditions.visibility_of_element_located((By.XPATH, xPath)))
    el = browser.find_element_by_xpath(xPath)
    el.click()


def checkTermine():
    for i in range(400):
        # fenster schliessen
        clickOnObject(
            '/html/body/app-root/div/app-page-its-search/app-its-search-slots-modal/div/div/div/div[2]/div/div/form/div[2]/button[2]')
        clickOnObject(
            '/html/body/app-root/div/app-page-its-search/div/div/div[2]/div/div/div[5]/div/div[1]/div[2]/div[2]/button')
        now = datetime.now()
        time.sleep(random())
        try:
            kasten = browser.find_element_by_xpath(
                '/html/body/app-root/div/app-page-its-search/app-its-search-slots-modal/div/div/div/div[2]/div/div/form/div[1]/span')
            print(now.strftime("%H:%M:%S"), " kein Termin vorhanden")
        except:

            winsound.Beep(frequency, duration)
            print("Termine verfuegbar!")

            print(now.strftime("%H:%M:%S"))
            return True
    return False


def delete_cache():
    browser.execute_script("window.open('');")
    time.sleep(2)
    browser.switch_to.window(browser.window_handles[-1])
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
    browser.close()  # close this tab
    browser.switch_to.window(browser.window_handles[0])  # switch back


options = webdriver.ChromeOptions()
# options.add_argument("--headless")
# options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920,1200")
# options.add_argument("--ignore-certificate-errors")
# options.add_argument("--disable-extensions")
# options.add_argument("--no-sandbox")
# options.add_argument("--disable-dev-shm-usage")
options.add_argument("--enable-webgl")

browser = webdriver.Chrome(
    executable_path=r"C:\\Program Files (x86)\\chromedriver\\chromedriver.exe", options=options)
flag = 0
while True:
    browser.get('https://google.de/')
    delete_cache()
    time.sleep(random()*240+120)

    now = datetime.now()
    try:
        browser.get(
            f"https://003-iz.impfterminservice.de/impftermine/service?plz={PLZ}")

        # accept cookies
        try:
            clickOnObject(
                '/html/body/app-root/div/div/div/div[2]/div[2]/div/div[1]/a')
        except:
            pass

        clickOnObject(
            '/html/body/app-root/div/app-page-its-login/div/div/div[2]/app-its-login-user/div/div/app-corona-vaccination/div[2]/div/div/label[1]/span')

        time.sleep(random()+1)
        browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        # enter code bc url doesn't work well
        # input1
        input1 = browser.find_element_by_xpath(
            '/html/body/app-root/div/app-page-its-login/div/div/div[2]/app-its-login-user/div/div/app-corona-vaccination/div[3]/div/div/div/div[1]/app-corona-vaccination-yes/form/div[1]/label/app-ets-input-code/div/div[1]/label/input')
        input1.send_keys(code[0])
        # input2
        input2 = browser.find_element_by_xpath(
            '/html/body/app-root/div/app-page-its-login/div/div/div[2]/app-its-login-user/div/div/app-corona-vaccination/div[3]/div/div/div/div[1]/app-corona-vaccination-yes/form/div[1]/label/app-ets-input-code/div/div[3]/label/input')
        input2.send_keys(code[1])
        # input3
        input3 = browser.find_element_by_xpath(
            '/html/body/app-root/div/app-page-its-login/div/div/div[2]/app-its-login-user/div/div/app-corona-vaccination/div[3]/div/div/div/div[1]/app-corona-vaccination-yes/form/div[1]/label/app-ets-input-code/div/div[5]/label/input')
        input3.send_keys(code[2])
        # press Termin suchen
        clickOnObject(
            '/html/body/app-root/div/app-page-its-login/div/div/div[2]/app-its-login-user/div/div/app-corona-vaccination/div[3]/div/div/div/div[1]/app-corona-vaccination-yes/form/div[2]/button')

        time.sleep(random()+3)

        # click on Termine Suchen nach dem code
        clickOnObject(
            '/html/body/app-root/div/app-page-its-search/div/div/div[2]/div/div/div[5]/div/div[1]/div[2]/div[2]/button')

    except Exception as e:
        continue
    time.sleep(random()*3+5)
    try:
        kasten = browser.find_element_by_xpath(
            '/html/body/app-root/div/app-page-its-search/app-its-search-slots-modal/div/div/div/div[2]/div/div/form/div[1]/span')
        print(now.strftime("%H:%M:%S"), " kein Termin vorhanden")
        flag = 1
    except:

        winsound.Beep(frequency, duration)
        print("Termine verfuegbar!")
        now = datetime.now()
        print(now.strftime("%H:%M:%S"))
        break
    termin = checkTermine()
    if termin:
        break
