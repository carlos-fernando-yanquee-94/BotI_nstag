from tkinter import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

root = Tk()
#the screen pops up
root.title('Instagram Bot by Kidd')


def InstaBotPic(userName, passWord, boxNumber, message, pathPic):
    start = 1
    path = r"webDriver\chromedriver.exe"
    driver = webdriver.Chrome(path)
    driver.get("https://www.instagram.com")
    time.sleep(1)
    # finding the "user here" then placing the user
    bot = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(userName)
    # finding the "pw here" then placing the password
    driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(passWord)
    # clicking the LOG IN button
    driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button').click()
    time.sleep(7)
    # clicking the not now button
    driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()
    time.sleep(3)
    # clicking the second not now button
    driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()
    time.sleep(3)
    # clicking the inbox
    driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[2]/a').click()
    time.sleep(3)
    while int(boxNumber) > start:
        for i in range(1, int(boxNumber) + 1):
            print(i)
            # clicking the first box
            driver.find_element_by_xpath(
                '//*[@id="react-root"]/section/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div[' + str(start) + ']/a').click()
            time.sleep(1)
            #locating the text area and sending the text message
            driver.find_element_by_xpath(
                '//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea').send_keys(
                message)
            time.sleep(1)
            #locating the enter button
            driver.find_element_by_xpath(
                '//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button').click()
            # finding input for the image path
            driver.find_element_by_xpath(
                '//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/form/input').send_keys(pathPic)
            time.sleep(1)
            start += 1

def InstaBotNoPic(userName, passWord, boxNumber, message):
    start = 1
    path = r"webDriver\chromedriver.exe"
    driver = webdriver.Chrome(path)
    driver.get("https://www.instagram.com")
    time.sleep(1)
    # finding the "user here" then placing the user
    bot = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(userName)
    # finding the "pw here" then placing the password
    driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(passWord)
    # clicking the LOG IN button
    driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button').click()
    time.sleep(7)
    # clicking the not now button
    driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()
    time.sleep(3)
    # clicking the second not now button
    driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()
    time.sleep(3)
    # clicking the inbox
    driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[2]/a').click()
    time.sleep(3)
    while int(boxNumber) > start:
        for i in range(1, int(boxNumber) + 1):
            print(i)
            # clicking the first box
            driver.find_element_by_xpath(
                '//*[@id="react-root"]/section/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div[' + str(start) + ']/a').click()
            time.sleep(1)
            #locating the text area and sending the text message
            driver.find_element_by_xpath(
                '//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea').send_keys(
                message)
            time.sleep(1)
            #locating the enter button
            driver.find_element_by_xpath(
                '//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button').click()
            # finding input for the image path
            time.sleep(1)
            start += 1



#just a text
# text = Label(root, text="Instagram Bot", font=("Courier", 44))
# text.pack()
#just a space
space = Label(root, text="")
space.pack()

#just a text
welcomeText = Label(root, text="Welcome to your Instagram bot!", font=("Arial", 20))
welcomeText.pack()
warningText = Label(root, text="Please submit the required information. This bot does not save your information.")
warningText.pack()
sourceText = Label(root, text="You can check the source code at https://github.com/Daniel-Mejia-Leon/InstagramBotSelenium")
sourceText.pack()

#just a space
space = Label(root, text="")
space.pack()

enterUserText = Label(root, text="Place your Instagram user name", font=("Arial", 12))
enterUserText.pack()
#enter your userName
userName = Entry(root, width=30, justify="center", text="Insta_melach")
userName.pack()
space = Label(root, text="")
space.pack()

enterPasswordText = Label(root, text="Place your Instagram password", font=("Arial", 12))
enterPasswordText.pack()
#enter your password
password = Entry(root, show="*", width=30, justify="center")
password.pack()
space = Label(root, text="")
space.pack()

#warnings on placing the number of messages
warningNumberText = Label(root, text="Please enter the number of messages you want to send", font=("Arial", 12))
warningNumberText.pack()
warningNumberText1 = Label(root, text="Check your inbox and see how many people you are able to send a message to", font=("Arial", 8))
warningNumberText1.pack()
warningNumberText2 = Label(root, text="if you have only 3 chats then place 3, if u have 100 chats then place 100", font=("Arial", 8))
warningNumberText2.pack()
numberOfMessages = Entry(root, width=10, justify="center")
numberOfMessages.pack()
#space
space = Label(root, text="")
space.pack()


messageToSendText = Label(root, text="Please enter the message you want to send", font=("Arial", 12))
messageToSendText.pack()
messageToSend = Entry(root, width=50, justify="center")
messageToSend.pack()
startBotNoPic = Button(root, text="Start Bot WITH JUST MESSAGE", command=lambda: InstaBotNoPic(userName.get(), password.get(), numberOfMessages.get(), messageToSend.get()))
startBotNoPic.pack()
space = Label(root, text="")
space.pack()


imageToSendText = Label(root, text="Please enter the path of the image you want to send", font=("Arial", 12))
imageToSendText.pack()
imageToSendText1 = Label(root, text=r"e.g. C:\user\Documents\Your-Picture.jpg", font=("Arial", 8))
imageToSendText1.pack()
imageToSend = Entry(root, width=50, justify="center")
imageToSend.pack()

#code a button to start InstaBot()
startBotWitPic = Button(root, text="Start Bot WITH WESSAGE AND PICTURE", command=lambda: InstaBotPic(userName.get(), password.get(), numberOfMessages.get(), messageToSend.get(), imageToSend.get()))
startBotWitPic.pack()
space = Label(root, text="")
space.pack()
space = Label(root, text="")
space.pack()


# if start:
#     InstaBot(userNameFun(), passwordFun(), number, message)

# text.grid(row=0, column=0)
root.mainloop()
