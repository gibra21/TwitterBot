from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pyautogui
from tkinter import *


windows = Tk()
windows.geometry("700x600")
emails=Label(windows, text="enter your email here", font="times 24 bold")
emails.grid(row=0,column=0)
entry1 = Entry(windows)
entry1.grid(row=0, column=6)

password=Label(windows, text="enter your password here", font="times 24 bold")
password.grid(row=2,column=0)
entry2 = Entry(windows)
entry2.grid(row=2, column=6)

hashtag=Label(windows, text="enter your email here", font="times 24 bold")
hashtag.grid(row=3,column=0)
entry3 = Entry(windows)
entry3.grid(row=3, column=6)

b1=Button(windows,text="GO", command=execute,width=12,bg="gray")
b1.grid(row=7,column=4)
windows.mainloop()

def execute():
    log=twitter_bot(str(entry1.get()),str(entry2.get()))
    log.login()
    log.like_tweet(entry3.get())


class twitter_bot:
    def __init__(self, username,password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()

    def login(self):
        bot = self.bot
        bot.get('https://x.com/home')
        time.sleep(5)
        email=bot.find_element_by_name("session[username_or_email]")
        password=bot.find_element_by_name("sessions[password]")
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(10)

    def like_tweet(self):
        bot=self.bot
        bot.get('https://x.com/search?q=python&src=typed_query'+str(entry3)+'&src=typed_query')
        while True:
            pyautogui.click(pyautogui.locateCenterOnScreen('heart.PNG'))
            time.sleep(3)
            bot.execute.script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(5)