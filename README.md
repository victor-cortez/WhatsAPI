# WhatsAPI
Simple Whatsapp API for you to enhance communication. It uses a selenium driver to open firefox on a whatsapp web page and automates reading and writing of messages, allowing for conversation with multiple chats. It is super simple and only requires one python file to work with your project.

Requirements:
Linux, Xclip, and Selenium with Firefox

Usage:

Set-up:
0- Install firefox and selenium drivers: https://selenium-python.readthedocs.io/installation.html
1 - Install xclip: https://zoomadmin.com/HowToInstall/UbuntuPackage/xclip
2- Connect your whatsapp web to your firefox browser
3- Get the location of the firefox browser profile (example: /home/YOURUSERNAME/.mozilla/firefox/es7r9q00.default-release/)
4- Close your browser. To run this firefox must be close and you must have no other whatsapp web session.
5- Add the code WppConversation.py into your project directory, it is all you need from this repo (if you want some cool functions for groups download GroupModules.py too)
6- Build your code using the stuff below: (Remember that selenium can only read the loaded html on the page, therefore it has a small limit on how much old messages and chats it can find)

import WppConversation as wpc => Main import
myConv = wpc.WppConv("Whatsapp Name as it appears") => Creates a new whatsapp user, also opens a firefox tab with whatsapp web
myConv.goToChat("Chat name as it appears") => Opens up a conversation
myConv.sendMessage("Message test") => Sends a message to the open chat. Long messages might take some additional time.
myConv.sendMedia(mediaPath, Comment = "") => Sends media (it detects the format)  with attached comments(Currently it is buggy with videos, but works perfectly with images) 
myConv.getMessages(self) => Gets all the messages not from the user it can find on the conversation, returns a list of WppMsg objects
myConv.getOwnMessages(ownName) => Gets all the messages send by the name specified that it can find on the conversation returns a list of WppMsg objects
getAllMessages(self): => Gets all the messages it can find on the conversation, returns a list of WppMsg objects

WppMsg objects:
They simple hold information and have the fields:
msg.id, msg.time, msg.date, msg.author, msg.text (All of these variables in text format) #Todo: Make time and date time objects

7- Extra: If you want to use the group modules available enter their code and check which ones you want to use, for each one there is a specific library you will have to install and further instructions will be found on their respective repositories. This code only reads messages and responds depending on what module the user called. It is pretty simple and we encourage you to modify it.
