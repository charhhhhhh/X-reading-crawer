from tkinter.font import BOLD
import selenium
import random

# from Pw import passwor, mail
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from tkinter.constants import CENTER  # 加到第一行
import tkinter as tk

# from setuptools import Command
import tkinter.messagebox


def is_integer(text):
    return text.strip().isdigit()


def init():
    gm = gmail.get()
    pa = password.get()
    mu = pagemun.get()
    se = pagesec.get()

    if gm == "" or pa == "" or mu == "" or se == "":
        tk.messagebox.showinfo("錯誤訊息", f"輸入未完全")  # type: ignore
    elif not is_integer(mu):
        tk.messagebox.showinfo("錯誤訊息", f"頁數爛了")  # type: ignore
    elif not is_integer(se):
        tk.messagebox.showinfo("錯誤訊息", f"間格爛了")  # type: ignore

    print(f"{gm} {pa} {mu} {se}")
    pass
    # print(f"{test.get()}")


def crawer():
    # edge people
    driver = webdriver.Edge()
    url = "https://www.xreading.com/login/index.php"
    driver.get(url)
    username = driver.find_element("id", "username")
    password = driver.find_element("id", "password")
    loginbtn = driver.find_element("id", "loginbtn")

    sleep(1)
    username.send_keys(mail)
    password.send_keys(passwor)
    loginbtn.click()

    Readingbtn = driver.find_element(By.LINK_TEXT, "Continue Reading")
    Readingbtn.click()

    sleep(3)
    for i in range(20):
        driver.set_window_size(640, 750)
        sleep(random.randint(25, 30))
        driver.execute_script("window.scrollBy(0, 375);")
        sleep(random.randint(20, 25))
        driver.execute_script("window.scrollBy(0, 375);")
        btns = driver.find_elements(By.TAG_NAME, "button")
        end = 0

        for btn in btns:
            if btn.text == "Close":
                btn.click()
                end = 1
                break
            elif btn.text == "Next":
                btn.click()
                print(f"now done {i+1}st page")
                break
        if end == 1:
            print(f"dook is done")
            break

    sleep(5)

    driver.close()
    print("done!")


window = tk.Tk()
window.title("autox autox autox autox autox autox autox autox autox autox autox ")
window.geometry("300x300")
window.resizable(False, False)
window.iconbitmap("logo.ico")

lb = tk.Label(
    text="gmail gmail gmail gmail gmail gmail gmail gmail gmail gmail gmail gmail gmail gmail gmail gmail gmail ",
    height=1,
    font=("Arial", 14),
)
lb.place(x=-35, y=-5)

gmail = tk.Entry(width=40)
gmail.place(x=8, y=25)

lb2 = tk.Label(
    text="password password password password password password password password password password password ",
    height=1,
    font=("Arial", 14),
)
lb2.place(x=-50, y=45)

password = tk.Entry(width=40)
password.place(x=8, y=75)

lb3 = tk.Label(
    text="讀多少頁 讀多少頁 讀多少頁 讀多少頁 讀多少頁 讀多少頁 讀多少頁 讀多少頁 讀多少頁 讀多少頁 讀多少頁 讀多少頁 讀多少頁 讀多少頁",
    height=1,
    font=("Arial", 14),
)
lb3.place(x=-15, y=95)

pagemun = tk.Entry(width=40)
pagemun.place(x=8, y=125)

lb4 = tk.Label(
    text="隔幾秒翻頁 隔幾秒翻頁 隔幾秒翻頁 隔幾秒翻頁 隔幾秒翻頁 隔幾秒翻頁 隔幾秒翻頁 隔幾秒翻頁 隔幾秒翻頁 隔幾秒翻頁 隔幾秒翻頁 隔幾秒翻頁 ",
    height=1,
    font=("Arial", 14),
)
lb4.place(x=-50, y=145)

pagesec = tk.Entry(width=40)
pagesec.place(x=8, y=175)

startbtn = tk.Button(
    text="開始讀開始讀開始讀開始讀開始讀開始讀開始讀開始讀開始讀開始讀開始讀開始讀開始讀開始讀",
    font=("Arial", 37, BOLD),
    command=init,
)
startbtn.place(x=30, y=250, anchor=CENTER)

window.mainloop()
