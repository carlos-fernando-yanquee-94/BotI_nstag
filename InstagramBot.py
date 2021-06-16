from tkinter import *

import selenium
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, InvalidArgumentException
from selenium.webdriver.common.keys import Keys
import time

root = Tk()
#the screen pops up
root.title('Instagram Bot by Kidd')


def InstaBotPic(boxNumber, message, pathPic):
    inside = False
    invalidPath = True
    start = 1
    path = r"webDriver\chromedriver.exe"
    driver = webdriver.Chrome(path)
    driver.get("https://www.instagram.com")
    time.sleep(1)
    while not inside:
        try:
            time.sleep(1)
            # clicking the not now button
            driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()
            while not inside:
                inside = True
            break

        except NoSuchElementException:
            print('waiting')

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
            time.sleep(1)
            driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/form/input').send_keys(pathPic)
            time.sleep(1)
            start += 1

def InstaBotNoPic(boxNumber, message):
    inside = False
    start = 1
    path = r"webDriver\chromedriver.exe"
    driver = webdriver.Chrome(path)
    driver.get("https://www.instagram.com")
    time.sleep(1)

    while not inside:
        try:
            time.sleep(1)
            # clicking the not now button
            driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()
            while not inside:
                inside = True
            break
        except NoSuchElementException:
            print('waiting')

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
#just a space
space = Label(root, text="")
space.pack()

instructionsTitle = Label(root, text="Instructions:", font=("Arial", 12))
instructionsTitle.pack()
step1 = Label(root, text="Fill the information required, then click a start bot button.\nAfter clicking start bot"
                         " please log in with your Instagram credentials and press enter.\nOnce you press enter do "
                         "not perform any other action, otherwise the bot will crash.", font=("Arial", 9))
step1.pack()


#just a space
space = Label(root, text="")
space.pack()

#warnings on placing the number of messages
warningNumberText = Label(root, text="This bot will send the message to every contact in your Instagram inbox", font=("Arial", 12))
warningNumberText.pack()
# warningNumberText1 = Label(root, text="This number must be based on the number of chats you have in your inbox\n"
#                                       "The system will start sending the message from the chat 1 to the number you "
#                                       "enter.", font=("Arial", 9))
# warningNumberText1.pack()
# numberOfMessages = Entry(root, width=10, justify="center")
# numberOfMessages.pack()
# #space
space = Label(root, text="")
space.pack()


messageToSendText = Label(root, text="Please enter the message you want to send", font=("Arial", 12))
messageToSendText.pack()
messageToSend = Entry(root, width=50, justify="center")
messageToSend.pack()
startBotNoPic = Button(root, text="Start Bot WITH MESSAGE ONLY", command=lambda: InstaBotNoPic(100000,
                                                                                               messageToSend.get()))
startBotNoPic.pack()
space = Label(root, text="")
space.pack()


imageToSendText = Label(root, text="Please enter the FULL PATH of the image you want to send", font=("Arial", 12))
imageToSendText.pack()
imageToSendText1 = Label(root, text=r"e.g. C:\user\Documents\Your-Picture.jpg", font=("Arial", 9))
imageToSendText1.pack()
imageToSend = Entry(root, width=50, justify="center")
imageToSend.pack()


#code a button to start InstaBot()
startBotWitPic = Button(root, text="Start Bot WITH MESSAGE AND PICTURE", command=lambda: InstaBotPic(100000, messageToSend.get(), imageToSend.get()))
startBotWitPic.pack()
makeSureWarning = Label(root, text="Make sure the path is the full path, otherwise will crash\n"
                                   "To get the full image path\nRight click on the picture>Properties>Security>Object"
                                    " Name\nThe copy the address next to Object Name", font=("Arial", 9))
makeSureWarning.pack()

space = Label(root, text="")
space.pack()
space = Label(root, text="")
space.pack()

warningText = Label(root, text="This bot does not save your information.")
warningText.pack()
sourceText = Label(root, text="You can check the source code at\n"
                              "https://github.com/Daniel-Mejia-Leon/InstagramBotSelenium")
sourceText.pack()

root.mainloop()
