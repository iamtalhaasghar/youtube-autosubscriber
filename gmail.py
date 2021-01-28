from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
import time,os, random

URL = "https://accounts.google.com/signup/v2/webcreateaccount?continue=https%3A%2F%2Fwww.google.com%2Fsearch%3Fq%3Dgmail%2Bnew%2Baccount%26oq%3Dgmail%2B%26aqs%3Dchrome.5.69i57j0j69i61l3j0.4643j0j7%26sourceid%3Dchrome%26ie%3DUTF-8&hl=en&dsh=S-888255684%3A1582557994045316&gmb=exp&biz=false&flowName=GlifWebSignIn&flowEntry=SignUp"

PASSWORD = "***REMOVED***"


def readnames():
    f = open("names.txt")
    names = f.readlines()
    names = [i.strip() for i in names]
    return names

def generateUsername(firstName, lastName):
    import random
    number = random.randint(100,1000)
    username = '%s%d%s' % (firstName, number, lastName)
    if(len(username) > 30):
        username = username[:30]
    return username

def createAccount(driver, fName, lName):
    firstName = driver.find_element_by_id("firstName")
    lastName = driver.find_element_by_id("lastName")
    username = driver.find_element_by_id("username")
    password = driver.find_element_by_name("Passwd")
    confirmPassword = driver.find_element_by_name("ConfirmPasswd")
    nextbutton = driver.find_element_by_id("accountDetailsNext")


    firstName.send_keys(fName)
    lastName.send_keys(lName)
    username.send_keys(generateUsername(fName,lName))
    password.send_keys(PASSWORD)
    confirmPassword.send_keys(PASSWORD)
    nextbutton.click()

def main():
    
    u_name = '***REMOVED***'
    u_pass = '***REMOVED***'
    opts = webdriver.ChromeOptions()
    opts.binary_location = r"C:\chrome 74.0\Chrome-bin\chrome.exe"
    driver = webdriver.Chrome(options = opts)
    driver.get(URL)
    
    names = readnames()
    for name in names:
        name = name.split()
        createAccount(driver, name[0],name[1])
        input('Press any key to continue...')

main()
input('Press any key to continue...')
