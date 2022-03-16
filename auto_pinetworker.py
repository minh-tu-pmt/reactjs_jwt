import sys
import re
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QFormLayout, QLineEdit, QPlainTextEdit, \
    QHBoxLayout, QCheckBox, QPushButton

list_except=["/users", "/login", "/logout", "/sign"]

def auto(url, NUM_POST, NUM_SCROLL=10):
    driver = webdriver.Chrome(executable_path='./chromedriver.exe')
    # url = "https://stackoverflow.com/questions/28431765/open-web-in-new-tab-selenium-python"
    driver.get(url)

    links = driver.find_elements_by_xpath("//a[@href]")
    links = [link.get_attribute("href") for link in links if link.get_attribute("href") is not None]

    links = [link for link in links if re.match(r"^(https|http)://[(a-z).]+/[a-z]+/", link)]
    links = [link for link in links if not any(word in link for word in list_except)]

    links = set(links)

    def get_height():
        return driver.execute_script("return document.body.scrollHeight")

    count = 0
    for link in links:
        if count == NUM_POST:
            break
        count += 1
        driver.get(link)
        WebDriverWait(driver, 10).until(lambda driver: get_height())
        for num in range(NUM_SCROLL):
            driver.execute_script("window.scrollTo(0, {});".format((num + 1) * 100))
            time.sleep(0.5)

class WindowFrm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Auto software")

        self.txtLink = QLineEdit()
        self.cbAnonymus = QCheckBox()
        self.txtQuantity = QLineEdit()
        self.txtTime = QLineEdit()

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

        txt = QPlainTextEdit()
        bottomLayout.addWidget(txt)

        outerLayout.addLayout(topLayout)
        outerLayout.addLayout(centerLayout)
        outerLayout.addLayout(bottomLayout)

        self.setGeometry(500, 500, 500, 500)
        self.setLayout(outerLayout)

    def runBtnClick(self):
        print("Run click", self.txtLink.text())
        isAnonymus = self.cbAnonymus.isChecked()
        print("is check: ", isAnonymus)
        # self.runBtn.setDisabled(True)
        num_post= int(self.txtQuantity.text())
        url=self.txtLink.text()
        auto(url, num_post)

def run():
    app = QApplication(sys.argv)

    window = WindowFrm()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    run()
