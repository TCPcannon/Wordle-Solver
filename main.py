"""
@name		WordleSolver
@author		tcpcannon.github.io
@created	2/9/2022 | 12:39 PM
@desc       Solves wordles on [ https://www.powerlanguage.co.uk/wordle ]
"""
from pydoc import cli
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import random

def doGameRow(letters):
    n = 1
    js = 'document.querySelector("body > game-app").shadowRoot.querySelector("#board > game-row:nth-child(%s)").shadowRoot.querySelector("div > game-tile:nth-child(%s)")' % (n, n)
    element = driver.execute_script(js)
    
    
    

def randLine():
        file = open("C:\\Users\\cannonball\\Documents\\Coding\\python\\wordle\\words.txt").read().splitlines()
        return random.choice(file)
        
def loop():


    print("\n----------------S T A R T E D - L O O P-------------------\n")
    #send input
    temp = randLine()
    driver.find_element_by_class_name("nightmode").send_keys("humor")
    #send keyboard input
    driver.find_element_by_class_name("nightmode").send_keys(Keys.RETURN)
    sleep(2)
    print("sleeping")
    doGameRow("humor")

    print("\n----------------P A S T E D [  ]-------------------\n")
    sleep(10)


if (__name__ == '__main__'):

    print("init")

    #setup chromedriver.exe
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options, executable_path="C:\\Users\\cannonball\\Documents\\Coding\\python\\wordle\\chromedriver.exe")
    driver.implicitly_wait(0.5)
    
    #launch URL
    driver.get("https://www.powerlanguage.co.uk/wordle/")
    print("\n----------------G O T - D R I V E R-------------------\n")
    sleep(1)

    # getting the elements
    x = driver.find_element_by_class_name("nightmode").click()
    print("\n----------------C L I C K E D - T A G-------------------\n")
    sleep(1)
    
    # Main LOOP
    i = 0
    while (i <= 6):
        print("\n----------------[ i = %s ]-------------------\n" % i)
        loop()
        i+=1

    
    print("\n----------------C O L O R-------------------\n")
    # end job
    sleep(2)
    print("\n----------------Q U I T T I N G-------------------\n")
    driver.quit()


