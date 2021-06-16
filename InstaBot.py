from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from secretStuff import secretInsta

def InstaBot(userName, passWord, boxNumber, message):
    picture = "C:\cork360\Documentos\Robot-Video.jpg"
    path = "C:\cork360\Documentos\webDriver\chromedriver.exe"
    driver = webdriver.Chrome(path)
    driver.get("https://www.instagram.com")
    time.sleep(1)
    #finding the "user here" then placing the user
    bot = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(userName)
    #finding the "pw here" then placing the password
    driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(passWord)
    #clicking the LOG IN button
    driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button').click()
    time.sleep(5)
    #clicking the not now button
    driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()
    time.sleep(1)
    #clicking the second not now button
    driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()
    time.sleep(1)
    #clicking the inbox
    driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[2]/a').click()
    time.sleep(2)
    time.sleep(1)
    # clicking the first box
    driver.find_element_by_xpath(
        '//*[@id="react-root"]/section/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div[' + boxNumber + ']/a').click()
    time.sleep(1)
    driver.find_element_by_xpath(
        '//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea').send_keys(
        message)
    driver.find_element_by_xpath(
        '//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button').click()
    # finding input for the image path
    driver.find_element_by_xpath(
        '//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/form/input').send_keys(image)
    time.sleep(1)

time.sleep(1)
#clicking the textInput
#driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea').send_keys("test")

# def selectClickAndSend(box, message):
#     driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div[' + box + ']/a').click()
#     time.sleep(1)
#     driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')\
#         .send_keys(message)
#     driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button').click()
#
# def sendImageAndText(box, message, image):
#     time.sleep(1)
#     # clicking the first box
#     driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div[' + box + ']/a').click()
#     time.sleep(1)
#     driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea').send_keys(message)
#     driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button').click()
#     # finding input for the image path
#     driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/form/input').send_keys(image)
#     time.sleep(1)


# box1 = "1"
# box2 = "2"
# box3 = "3"
# box4 = "4"
# message = "Hasta la vista baby!"
#
# sendImageAndText(box1, message, picture)
# sendImageAndText(box2, message, picture)
# sendImageAndText(box3, message, picture)
# sendImageAndText(box4, message, picture)



