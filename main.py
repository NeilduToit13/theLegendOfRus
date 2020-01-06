from selenium import webdriver
import time 
import random 
from bs4 import BeautifulSoup
import re 

# Special thanks to Juanjo Quispe for providing this 
# link in a Youtube comment
URL = 'https://www.voobly.com/profile/view/124230024'
PAGE_LOAD_TIMEOUT = 30

def main():
    with webdriver.Firefox() as driver:
        driver.set_page_load_timeout(PAGE_LOAD_TIMEOUT)

        driver.get(URL)

        html = driver.execute_script("return document.documentElement.outerHTML")
        print(html)


if __name__=="__main__":
    main()
