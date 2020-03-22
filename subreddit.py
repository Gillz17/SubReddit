from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class redditBot():
    def __init__(self):
        #Start the webdriver
        self.driver = webdriver.Chrome("C:/Users/zmc17/Documents/Python Scripts/Reddit API/chromedriver.exe")

    def login(self):
        driver = self.driver
        #Go to reddit
        driver.get("http://old.reddit.com/")
        #Send username
        driver.find_element_by_name("user").send_keys("ENTER YOUR USERNAME")
        #Send password
        driver.find_element_by_name("passwd").send_keys("ENTER YOUR PASSWORD")
        #Click login button
        loginBtn = driver.find_element_by_xpath('/html/body/div[3]/div[2]/form/div[4]/button')
        loginBtn.click()
        #Wait for it to login before advancing
        time.sleep(5)

    def rndSub(self):
        driver = self.driver
        #Open the output file
        file = open("subreddits.txt", "w")

        #Grab 10 random subreddits and output them to a file
        for x in range(50):
            driver.get("http://old.reddit.com/r/random")
            currentURL = driver.current_url
            file.write(currentURL + "\n")
            print(currentURL)
        #Close the file
        file.close    

    def close(self):
        self.driver.close()

reddit = redditBot()
reddit.login()
reddit.rndSub()
reddit.close()