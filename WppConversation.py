from selenium import webdriver
import time
from selenium.webdriver.firefox.webdriver import FirefoxProfile
from selenium.webdriver.common.keys import Keys
import os
class WppMsg:
    def __init__(self,id,text):
        id = id.replace("[","").replace("]","").replace(",","").replace(":","")
        idParts = id.split(" ",2)
        self.time = idParts[0]
        self.date = idParts[1]
        self.author = idParts[2]
        self.text = text
    def __str__(self):
        return self.time+"|"+self.date+"|"+self.author+"|"+self.text
class WppConv:
    def __init__(self,userName,profilePath):
        profile = FirefoxProfile(profilePath)
        driver = webdriver.Firefox(profile)
        driver.get("https://web.whatsapp.com/")
        driver.implicitly_wait(15)
        self.driver = driver
        self.userName = userName
    def goToChat(self, contactName):
        chat_divs = self.driver.find_elements_by_class_name('X7YrQ')
        target_div = [i for i in chat_divs if contactName in i.text][0]
        target_div.click()
        time.sleep(5)
        text_field = self.driver.find_element_by_css_selector("div._3u328.copyable-text.selectable-text")
        text_field.click()
        self.text_field = text_field
        self.contactName = contactName
    def sendMessage(self, message):
        parts = message.split()
        self.text_field.click()
        for part in parts:
            self.text_field.send_keys(part)
            self.text_field.send_keys(" ")
            if "\n" in parts:
                self.text_field.send_keys(Keys.SHIFT, Keys.ENTER)
        self.text_field.send_keys(Keys.ENTER)
    def sendMedia(self, mediaPath, Comment = ""):
        print("Sending media")
        mediaType = self.getMediaType(mediaPath)
        consoleCommand = "xclip -selection clipboard -t " + mediaType +  " -i " + mediaPath
        os.system(consoleCommand)
        self.text_field.send_keys(Keys.LEFT_CONTROL,"v")
        time.sleep(1)
        new_text_field = self.driver.find_element_by_css_selector("div._3u328.copyable-text.selectable-text")
        new_text_field.click()
        parts = Comment.split()
        for part in parts:
            new_text_field.send_keys(part)
            new_text_field.send_keys(" ")
            if "\n" in parts:
                new_text_field.send_keys(Keys.SHIFT, Keys.ENTER)
        new_text_field.send_keys(Keys.ENTER)
    def getMediaType(self, mediaPath):
        extension = mediaPath.split(".")[-1]
        print(extension)
        if extension == "png":
            return "image/png"
        elif extension == "mp4":
            print("mp4")
            return "video/mp4"
    def getMessages(self):
        messages = []
        raw_messages = self.driver.find_elements_by_class_name("copyable-text")
        for message in raw_messages:
            idRaw = message.get_attribute("data-pre-plain-text")
            if idRaw != None:
                id = idRaw.replace("\n","")
                if self.userName not in id:
                    messages.append(WppMsg(id,message.text))
        return messages
    def getOwnMessages(self, ownName):
        messages = []
        raw_messages = self.driver.find_elements_by_class_name("copyable-text")
        for message in raw_messages:
            idRaw = message.get_attribute("data-pre-plain-text")
            if idRaw != None:
                id = idRaw.replace("\n","")
                if ownName in id:
                    messages.append(WppMsg(id,message.text))
        return messages
    def getAllMessages(self):
        messages = []
        raw_messages = self.driver.find_elements_by_class_name("copyable-text")
        for message in raw_messages:
            idRaw = message.get_attribute("data-pre-plain-text")
            if idRaw != None:
                id = idRaw.replace("\n","")
                messages.append(WppMsg(id,message.text))
        return messages
