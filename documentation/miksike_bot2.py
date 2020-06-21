# täiesti ümber tehtud
# võrreldes eelmise versiooniga on errorite handlemine, tehete kiirus palju paremad
# robot sisestab ise vastuseid
# nüüd keskendume liitmise asemel võrdlemisele

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
    driver.find_element_by_xpath("/html[1]/body[1]/div[2]/div[2]/div[1]/table[1]/tbody[1]/tr[2]/td[1]/table[1]/tbody[1]/tr[4]/td[2]/a[1]").click() # võrdlemine
    
def newpage_on():
    driver.find_element_by_xpath("/html[1]/body[1]/form[2]/div[1]/table[1]/tbody[1]/tr[1]/td[2]/input[1]").click() # alusta

driver.get("https://www.miksike.ee/en.html#/en/gnews.html") # lehele minek
time.sleep(10) # time for you to put in account details
engine_on()
time.sleep(3)
print(driver.window_handles)
driver.switch_to_window(driver.window_handles[1])
time.sleep(1)
newpage_on()

while True:
    try:
        tehe = driver.find_element_by_id("aVrd1").text
        tehe2 = driver.find_element_by_id("aVrd2").text
        tehe = eval(tehe)
        tehe2 = eval(tehe2)
        if tehe == tehe2:
            driver.find_element_by_xpath("/html[1]/body[1]/form[2]/div[2]/input[2]").click()
        if tehe > tehe2:
            driver.find_element_by_xpath("/html[1]/body[1]/form[2]/div[2]/input[3]").click()
        if tehe < tehe2:
            driver.find_element_by_xpath("/html[1]/body[1]/form[2]/div[2]/input[1]").click()

    except TypeError:
        time.sleep(0.05)
    except SyntaxError:
        time.sleep(0.05)
    

