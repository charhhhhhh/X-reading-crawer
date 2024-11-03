# from cgitb import text
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
NOW_USER = "user1"

init_user_data = {
    "user1": {"gmail": "", "password": "", "pagemun": "", "pagesec": ""},
    "user2": {"gmail": "", "password": "", "pagemun": "", "pagesec": ""},
    "user3": {"gmail": "", "password": "", "pagemun": "", "pagesec": ""},
}


def save_user_data(user, data):
    all_data = load_user_data()
    all_data[user] = data
    with open(USER_DATA_FILE, "w") as f:
        json.dump(all_data, f, indent=4)


def load_user_data():
    if not os.path.exists(USER_DATA_FILE):
        with open(USER_DATA_FILE, "w") as f:
            json.dump(init_user_data, f, indent=4)
    with open(USER_DATA_FILE, "r") as f:
        return json.load(f)


def init_data(var, gmail, password, pagemun, pagesec):
    data = load_user_data()
    gmail.insert(0, data["user1"]["gmail"])
    password.insert(0, data["user1"]["password"])
    pagemun.insert(0, data["user1"]["pagemun"])
    pagesec.insert(0, data["user1"]["pagesec"])


def change_data(var, gmail, password, pagemun, pagesec):
    global NOW_USER

    old_data = {
        "gmail": gmail.get(),
        "password": password.get(),
        "pagemun": pagemun.get(),
        "pagesec": pagesec.get(),
    }
    save_user_data(NOW_USER, old_data)
    gmail.delete(0, "end")
    password.delete(0, "end")
    pagemun.delete(0, "end")
    pagesec.delete(0, "end")

    data = load_user_data()
    if var == 1:
        gmail.insert(0, data["user1"]["gmail"])
        password.insert(0, data["user1"]["password"])
        pagemun.insert(0, data["user1"]["pagemun"])
        pagesec.insert(0, data["user1"]["pagesec"])
        NOW_USER = "user1"
    elif var == 2:
        gmail.insert(0, data["user2"]["gmail"])
        password.insert(0, data["user2"]["password"])
        pagemun.insert(0, data["user2"]["pagemun"])
        pagesec.insert(0, data["user2"]["pagesec"])
        NOW_USER = "user2"

    elif var == 3:
        gmail.insert(0, data["user3"]["gmail"])
        password.insert(0, data["user3"]["password"])
        pagemun.insert(0, data["user3"]["pagemun"])
        pagesec.insert(0, data["user3"]["pagesec"])
        NOW_USER = "user3"


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
        text="gmail",
        height=1,
        font=entry_font,
    )
    lb2 = tk.Label(
        text="password",
        height=1,
        font=entry_font,
    )
    lb3 = tk.Label(
        text="讀多少頁",
        height=1,
        font=entry_font,
    )
    lb4 = tk.Label(
        text="隔幾秒翻頁",
        height=1,
        font=entry_font,
    )
    lb5 = tk.Label(
        text="切換使用者",
        height=1,
        font=("Arial", 12),
    )
    lb6 = tk.Label(
        text="徵求美工",
        height=1,
        font=("Arial", 12, "italic", "underline"),
    )
    startbtn = tk.Button(
        text="開始讀",
        font=("Arial", 30, BOLD),
        command=lambda: init(gmail.get(), password.get(), pagemun.get(), pagesec.get()),
    )

    gmail = tk.Entry(width=40)
    password = tk.Entry(
        width=40,
        show="*",
    )
    pagemun = tk.Entry(width=40)
    pagesec = tk.Entry(width=40)
    init_data(1, gmail, password, pagemun, pagesec)

    radioVar = tk.IntVar()
    radioVar.set(1)
    radio1 = tk.Radiobutton(
        text="1",
        variable=radioVar,
        value=1,
        font=("Arial", 12),
        command=lambda: change_data(radioVar.get(), gmail, password, pagemun, pagesec),
    )
    radio2 = tk.Radiobutton(
        text="2",
        variable=radioVar,
        value=2,
        font=("Arial", 12),
        command=lambda: change_data(radioVar.get(), gmail, password, pagemun, pagesec),
    )
    radio3 = tk.Radiobutton(
        text="3",
        variable=radioVar,
        value=3,
        font=("Arial", 12),
        command=lambda: change_data(radioVar.get(), gmail, password, pagemun, pagesec),
    )

    gmail.place(x=8, y=25)
    password.place(x=8, y=75)
    pagemun.place(x=8, y=125)
    pagesec.place(x=8, y=175)

    radio1.place(x=160, y=220)
    radio2.place(x=160, y=240)
    radio3.place(x=160, y=260)

    lb.place(x=0, y=-5)
    lb2.place(x=0, y=45)
    lb3.place(x=0, y=95)
    lb4.place(x=0, y=145)
    lb5.place(x=160, y=200)
    lb6.place(x=220, y=220)

    startbtn.place(x=80, y=250, anchor=CENTER)

    window.mainloop()


if __name__ == "__main__":
    main()
# pyinstaller --onefile --windowed --clean --add-data "logo.ico;." --icon "logo.ico" autoX.py
