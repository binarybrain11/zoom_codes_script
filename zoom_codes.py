import os
import time
try:
    from pynput.keyboard import Key, Controller
    from selenium import webdriver
except:
    os.system("pip3 install -r ./REQUIREMENTS.txt")
    from pynput.keyboard import Key, Controller
    from selenium import webdriver


class meeting:
    def __init__(self, name, code, password):
        self.name = "unnamed"
        self.code = "0"
        self.password = "0"

def main():
    try:
        open("zoom_codes.txt", "x")
        os.system("del /f zoom_codes.txt")
        os.system("python setup.py")
    except:
        True == True
    codes = open("zoom_codes.txt", "r")
    n_meetings = int(codes.readline())
    meetings = []
    for i in range(n_meetings):
        meetings.append(meeting)
        meetings[i].name = codes.readline()
        meetings[i].code = codes.readline()
        meetings[i].password = codes.readline()
        print(str(i+1)+") " + meetings[i].name, end="")
    selection = int(input())
    if (selection <= n_meetings):

        settings = open("settings.txt", "r")
        settings.readline()
        url = settings.readline()
        keyboard = Controller()

        driver = webdriver.Chrome()

        driver.get(url + meetings[selection-1].code + "?status=success")
        driver.find_element_by_link_text("click here").click()
        settings.readline()
        time.sleep(int(settings.readline()))
        keyboard.press(Key.tab)
        keyboard.release(Key.tab)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        settings.readline()
        time.sleep(int(settings.readline()))
        if meetings[selection-1].password != '0\n':
            for i in meetings[selection-1].password:
                keyboard.press(i)
                keyboard.release(i)
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)
    else:
        print(str(selection) + " isn't an option! ")


main()