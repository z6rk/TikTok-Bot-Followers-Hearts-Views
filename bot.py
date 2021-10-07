
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import pyfiglet
from time import sleep

def loop1():
    global i
    sleep(10)
    try:
        driver.find_element_by_xpath("//*[@id=\"main\"]/div/div[4]/div/button").click()
    except:
        print("You didn't solve the captcha yet. Need to refresh to avoid endless loop.")
        driver.refresh()
        loop1()
    try:
        sleep(2)
        driver.find_element_by_xpath("//*[@id=\"sid4\"]/div/form/div/input").send_keys(vidUrl)
        sleep(1)
        driver.find_element_by_xpath("//*[@id=\"sid4\"]/div/form/div/div/button").click()
        sleep(2)
        driver.find_element_by_xpath("//*[@id=\"c2VuZC9mb2xsb3dlcnNfdGlrdG9V\"]/div[1]/div/form/button").click()
        sleep(10)
        driver.refresh()
        i += 1
        total = i * 500
        print("Success delivered!")
        sleep(360)
        loop1()
    except:
        print("A generic error occurred. Now will retry again")
        driver.refresh()
        sleep(20)
        loop1()

def loop2():
    print("You need Premium Version")
    print("Link: https://sellix.io/product/615d80d4b4ef9")


def loop3():
    print("You need Premium Version")
    print("Link: https://sellix.io/product/615d80d4b4ef9")

def loop4():
    print("You need Premium Version")
    print("Link: https://sellix.io/product/615d80d4b4ef9")

def loop5():
    print("You need Premium Version")
    print("Link: https://sellix.io/product/615d80d4b4ef9")

print("Author: https://github.com/NoNameoN-A")

vidUrl = "https://www.tiktok.com/@github_nonameon/video/7016217842693557510" #Change it

bot = int(input("What do you want to do?\n1 - Auto views\n2 - Auto hearts\n3 - Auto comments heart\n4 - Auto followers\n5 - Auto Share\n6 - Simple reload\n"))

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(executable_path=r'C:/Users/Alessandro/Desktop/Altro/bot/chromedriver.exe',chrome_options=chrome_options)

driver.get("https://vipto.de/")

if bot == 1:
    loop1()
elif bot == 2:
    loop2()
elif bot == 3:
    loop3(1)
elif bot == 4:
    loop4()
elif bot == 5:
    loop5()
else:
    print("You can insert just 1, 2, 3, 4, 5 or 6")

