# miksike.ee is a platform where you can polish your arithmetic skills
# computers are generally better at calculating than me so i felt the need to create this bot
# you dont need an account for miksike.ee, just pip install xpath, selenium and you are good to go

import xpath
from selenium import webdriver
import time
PATH = "C:\Program Files (x86)/chromedriver.exe"
driver = webdriver.Chrome(PATH)

def engine_on():
    driver.find_element_by_xpath("/html[1]/body[1]/form[2]/div[1]/table[1]/tbody[1]/tr[1]/td[2]/input[1]").click()
driver.get("https://www.miksike.ee/en/mmath.html?mode=nat&ex=1&ekrh=1080")
time.sleep(5)
engine_on() # function is needed otherwise selenium is searching for a button from the initial page


while True:
    try:
        tehe = driver.find_element_by_id("txtTehtav").text
        tehe = tehe.split("+") # those 2 lines basically purify the element content so we get actual numbers from the equation
        tehe = [s.replace("=", "") for s in tehe]
        tehe = int(tehe[0]) + int(tehe[1]) # for logical reasons, our number must be integrals and not strings!!!
        print(tehe)
    except ValueError: # pmst kui me võtame uue tehte, siis seal on mingi ebaloogiline info
        time.sleep(1) # peame veits ootama et saaks uue puhta tehte
    
