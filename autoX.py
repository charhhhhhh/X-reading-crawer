from cgitb import text
from tkinter.font import BOLD
import selenium
import random
import json
import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from tkinter.constants import CENTER
import tkinter as tk
from tkinter import messagebox

USER_DATA_FILE = "user_data.json"


def save_user_data(data):
    with open(USER_DATA_FILE, "w") as f:
        json.dump(data, f)


def load_user_data():
    """從 JSON 文件中讀取使用者資料"""
    if os.path.exists(USER_DATA_FILE):
        with open(USER_DATA_FILE, "r") as f:
            return json.load(f)
    return None


def is_integer(text):
    return text.strip().isdigit()


def init(gm, pa, mu, se):
    if gm == "" or pa == "" or mu == "" or se == "":
        messagebox.showinfo("錯誤訊息", f"輸入未完全")
    elif not is_integer(mu):
        messagebox.showinfo("錯誤訊息", f"頁數爛了")
    elif not is_integer(se):
        messagebox.showinfo("錯誤訊息", f"間格爛了")
    else:
        print(f"{gm} {pa} {mu} {se}")
        save_user_data(data={"gmail": gm, "password": pa, "pagemun": mu, "pagesec": se})
        crawer(gm, pa, mu, se)


def crawer(Gmail, Password, Pagemun, Pagesec):
    # edge people
    Pagemun = int(Pagemun)
    Pagesec = int(Pagesec)

    driver = webdriver.Edge()
    url = "https://www.xreading.com/login/index.php"
    driver.get(url)

    username = driver.find_element("id", "username")
    password = driver.find_element("id", "password")
    loginbtn = driver.find_element("id", "loginbtn")

    sleep(2)
    username.send_keys(Gmail)
    password.send_keys(Password)
    loginbtn.click()
    try:
        driver.find_element(By.XPATH, '//*[@id="user-menu-toggle"]/span/span/span/span')
    except:
        messagebox.showinfo("錯誤訊息", "帳號或密碼爛了")
        return

    sleep(2)
    try:
        Readingbtn = driver.find_element(By.LINK_TEXT, "Continue Reading")
        Readingbtn.click()
    except:
        messagebox.showinfo("錯誤訊息", "未選取書籍/已閱讀完畢")
        return

    sleep(2)
    for i in range(Pagemun):
        driver.set_window_size(640, 750)
        sleep(Pagesec / 2)
        driver.execute_script("window.scrollBy(0, 375);")
        sleep(Pagesec / 2)
        driver.execute_script("window.scrollBy(0, 375);")
        btns = driver.find_elements(By.TAG_NAME, "button")
        for btn in btns:
            if btn.text == "Close":
                btn.click()
                end = 1
                messagebox.showinfo("完成訊息", "讀完整本書了")
                break
            elif btn.text == "Next":
                btn.click()
                print(f"now done {i+1}st page")
                break
        if i == Pagemun - 1:
            messagebox.showinfo("完成訊息", f"讀完{i+1}頁了")
            print(f"讀完{i+1}頁了")
    sleep(2)
    driver.close()
    print("done!")


def main():
    window = tk.Tk()
    window.title("autox autox autox autox ")
    window.geometry("300x300+800+500")
    window.resizable(False, False)
    current_dir = os.path.dirname(os.path.abspath(__file__))
    icon_path = os.path.join(current_dir, "logo.ico")
    window.iconbitmap(icon_path)
   
    entry_font = ("Arial", 14)
    lb = tk.Label(
        text="gmail gmail gmail gmail gmail gmail gmail",
        height=1,
        font=entry_font,
    )
    lb2 = tk.Label(
        text="password password password password",
        height=1,
        font=entry_font,

    )
    lb3 = tk.Label(
        text="讀多少頁 讀多少頁 讀多少頁 讀多少頁 讀多少頁 ",
        height=1,
        font=entry_font,

    )
    lb4 = tk.Label(
        text="隔幾秒翻頁 隔幾秒翻頁 隔幾秒翻頁 隔幾秒翻頁 ",
        height=1,
        font=entry_font,

    )
    startbtn = tk.Button(
        text="開始讀開始讀開始讀開始讀開始讀",
        font=("Arial", 30, BOLD),
        command=lambda: init(gmail.get(), password.get(), pagemun.get(), pagesec.get()),
    )

    lb.place(x=-35, y=-5)
    lb2.place(x=-40, y=45)
    lb3.place(x=-15, y=95)
    lb4.place(x=-50, y=145)
    startbtn.place(x=30, y=250, anchor=CENTER)

    user_data = load_user_data()
    if user_data:
        gmail = tk.Entry(width=40, textvariable=tk.StringVar(value=user_data["gmail"]))
        password = tk.Entry(width=40, show="*", textvariable=tk.StringVar(value=user_data["password"]))
        pagemun = tk.Entry(width=40, textvariable=tk.StringVar(value=user_data["pagemun"]))
        pagesec = tk.Entry(width=40, textvariable=tk.StringVar(value=user_data["pagesec"]))
    else:
        gmail = tk.Entry(width=40)
        password = tk.Entry(width=40, show="*")
        pagemun = tk.Entry(width=40)
        pagesec = tk.Entry(width=40)

    gmail.place(x=8, y=25)
    password.place(x=8, y=75)
    pagemun.place(x=8, y=125)
    pagesec.place(x=8, y=175)

    window.mainloop()

if __name__ == "__main__":
    main()
# pyinstaller --onefile --windowed --add-data "logo.ico;." autoX.py