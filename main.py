from selenium import webdriver
import time 
import random 
from bs4 import BeautifulSoup
import re 
import argparse
import settings


parser = argparse.ArgumentParser(
        description=settings.DESCRIPTION,
        )

parser.add_argument('-u', '--username', type=str, required=True, help='username for Voobly')
parser.add_argument('-p', '--password', type=str, required=True, help='password for Voobly')

args = parser.parse_args()

def main():
    # Create Driver
    driver = webdriver.Chrome()
    driver.set_page_load_timeout(settings.PAGE_LOAD_TIMEOUT)

    # Initial page load
    driver.get(settings.URL)
    time.sleep(2)

    # Login to Voobly
    username_input = driver.find_element_by_id("username")
    username_input.clear()
    username_input.send_keys(args.username)
    time.sleep(2)
    password_input = driver.find_element_by_id("password")
    password_input.clear()
    password_input.send_keys(args.password)
    driver.find_elements_by_class_name("login-button")[0].click()
    time.sleep(2)


    # Refetch the page.
    # Looks like browser doesn't always navigate back 
    # to Rus' profile after a login.
    driver.get(settings.URL)
    time.sleep(2)

    # Navigate to matches
    driver.find_element_by_link_text("Matches").click()
    time.sleep(2)

    # Loop over each of the matches pages 
    # There are 1397 matches as at 7 January.
    # And 10 matchers per page.
    # But this guy plays a lot. There could be many more games played in the next few days.
    # An Error at the end of the loop should be fine.
    # So going for 160 loops.

    for i in range(160):
        print(f"{i+1} pages viewed")
        driver.find_element_by_link_text("→").click()
        time.sleep(2)






    time.sleep(10)
    #html = driver.execute_script("return document.documentElement.outerHTML")

if __name__=="__main__":
    main()
