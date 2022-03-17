import sys
import re

from PyQt5.QtGui import QIntValidator
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QFormLayout, QLineEdit, QPlainTextEdit, \
    QHBoxLayout, QCheckBox, QPushButton

list_except=["/users", "/login", "/logout", "/sign"]

class WindowFrm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Auto software")

        self.txtLink = QLineEdit()
        self.cbAnonymus = QCheckBox()
        self.txtQuantity = QLineEdit()
        self.txtQuantity.setValidator(QIntValidator())
        self.txtTime = QLineEdit()
        self.txtTime.setValidator(QIntValidator())

        outerLayout = QVBoxLayout()
        topLayout = QFormLayout()
        centerLayout = QHBoxLayout()
        bottomLayout = QVBoxLayout()
        topLayout.addRow("<b>Link</b>", self.txtLink)

        anonymus = QFormLayout()
        anonymus.addRow("Anonymus", self.cbAnonymus)
        quantity = QFormLayout()
        quantity.addRow("So luong", self.txtQuantity)
        time = QFormLayout()
        time.addRow("Thoi gian", self.txtTime)

        self.runBtn = QPushButton(text="Run")
        self.runBtn.clicked.connect(self.runBtnClick)

        centerLayout.addLayout(anonymus)
        centerLayout.addLayout(quantity)
        centerLayout.addLayout(time)
        centerLayout.addWidget(self.runBtn)

        self.txtHistory = QPlainTextEdit()
        bottomLayout.addWidget(self.txtHistory)

        outerLayout.addLayout(topLayout)
        outerLayout.addLayout(centerLayout)
        outerLayout.addLayout(bottomLayout)

        self.setGeometry(500, 500, 500, 500)
        self.setLayout(outerLayout)

    def runBtnClick(self):
        isAnonymus = self.cbAnonymus.isChecked()
        num_post= int(self.txtQuantity.text())
        timeAlive = int(self.txtTime.text())
        url=self.txtLink.text()
        self.auto(url,timeAlive,mode=isAnonymus,NUM_POST=num_post)

    def auto(self, url, timeAlive, mode=False, NUM_POST=1):
        TIME_OUT_SCROLL = 0.5 #seconds
        options = webdriver.ChromeOptions()

        if mode:
            options.add_argument("--incognito")

        driver = webdriver.Chrome(executable_path='./chromedriver.exe', options=options)

        # url = "https://stackoverflow.com/questions/28431765/open-web-in-new-tab-selenium-python"
        driver.get(url)

        links = driver.find_elements_by_xpath("//a[@href]")
        links = [link.get_attribute("href") for link in links if link.get_attribute("href") is not None]

        links = [link for link in links if re.match(r"^(https|http)://[(a-z).]+/[a-z]+/", link)]
        links = [link for link in links if not any(word in link for word in list_except)]

        links = set(links)
        links = list(links)

        links=links[:NUM_POST]
        strHistory = '---History from '+url+' ---\n'
        for index in range(len(links)):
            strHistory+= str(index+1)+'. '+links[index]+'\n'

        self.txtHistory.setPlainText(strHistory)
        print(strHistory)

        def get_height():
            return driver.execute_script("return document.body.scrollHeight")

        for link in links:
            # body = driver.find_element_by_tag_name("body")
            # body.send_keys(Keys.CONTROL + 't')
            driver.get(link)
            WebDriverWait(driver, 10).until(lambda driver: get_height())
            NUM_SCROLL = round(timeAlive/TIME_OUT_SCROLL)
            offset = round(get_height()/NUM_SCROLL)
            for num in range(NUM_SCROLL):
                driver.execute_script("window.scrollTo(0, {});".format((num + 1) * offset))
                time.sleep(TIME_OUT_SCROLL)

        driver.close()


def run():
    app = QApplication(sys.argv)

    window = WindowFrm()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    run()
