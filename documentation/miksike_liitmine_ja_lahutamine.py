import xpath
from selenium import webdriver
import time
PATH = "C:\Program Files (x86)/chromedriver.exe"
driver = webdriver.Chrome(PATH)

def engine_on():
    time.sleep(5)
    driver.find_element_by_xpath("/html[1]/body[1]/div[1]/form[2]/table[1]/tbody[1]/tr[1]/td[4]/a[1]").click() # pranglimine
    time.sleep(3)
    driver.find_element_by_xpath("/html[1]/body[1]/div[2]/div[1]/table[1]/tbody[1]/tr[2]/td[2]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[1]/td[4]/a[1]").click() #trenniväljak
    time.sleep(3)
    driver.find_element_by_xpath("/html[1]/body[1]/div[2]/div[2]/div[1]/table[1]/tbody[1]/tr[2]/td[1]/table[1]/tbody[1]/tr[3]/td[2]/a[1]").click() # liitmine

def newpage_on():
    driver.find_element_by_id("btnAlusta").click() # alusta


driver.get("https://www.miksike.ee/en.html#/en/gnews.html")
time.sleep(5)
engine_on()
time.sleep
driver.switch_to.window(driver.window_handles[1])
time.sleep(1)
newpage_on()


while True:
    try:
        tehe = eval(driver.find_element_by_id("txtTehtav").text[:-1])
        stringtehe = str(tehe)
        for i in range(len(str(tehe))):
            for n in range(10):
                if str(tehe)[i] == str(n):
                    driver.find_element_by_id("nr" + str(n)).click()
        driver.find_element_by_id("OK").click()
                

    except ValueError:
        time.sleep(0.01)
    except SyntaxError:
        time.sleep(0.01)
