import sys, time
from PyQt5.QtGui import QPaintEvent, QColor, QPainter, QKeyEvent, QMouseEvent, QPixmap, QPainterPath
from PyQt5.QtWidgets import QMessageBox, QApplication, QWidget
from PyQt5.QtCore import Qt, pyqtSignal, QRectF


class Snipping(QWidget):
    grabImageDone = pyqtSignal(str)

    def __init__(self):
        super(Snipping, self).__init__()
        self.setWindowFlags(Qt.WindowStaysOnTopHint and Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.reset_state()


    def reset_state(self):
        screen = QApplication.desktop().geometry()
        self.setFixedSize(screen.width(), screen.height())
        self.move(screen.topLeft())
        self.delta = self.geometry().topLeft()
        self.desktopPixmap = self.grab_screen_shot()
        self.selectedRect = QRectF()


    def take_screen_shot(self, path):
        time.sleep(0.5)
        self.reset_state()
        self.path = path
        self.show()


    def grab_screen_shot(self):
        ret = QPixmap(QApplication.desktop().geometry().size())
        p = QPainter(ret)
        for ele in QApplication.screens():
            p.drawPixmap(ele.geometry().topLeft() - self.delta, ele.grabWindow(0))
        return ret


    def paintEvent(self, event: QPaintEvent):
        p = QPainter(self)
        p.drawPixmap(0, 0, self.desktopPixmap)

        path = QPainterPath()
        path.addRect(QRectF(self.rect()))
        path.addRect(self.selectedRect)
        p.fillPath(path, QColor.fromRgb(255, 255, 255, 150))

        p.setPen(Qt.red)
        p.drawRect(self.selectedRect)


    def keyPressEvent(self, event: QKeyEvent):
        if event.key() == Qt.Key_Escape:
            self.hide()
            self.grabImageDone.emit("url")
        event.accept()


    def mousePressEvent(self, event: QMouseEvent):
        self.selectedRect.setTopLeft(event.globalPos() - self.delta)
        self.selectedRect.setBottomRight(event.globalPos() - self.delta)
        self.update()


    def mouseMoveEvent(self, event: QMouseEvent):
        self.selectedRect.setBottomRight(event.globalPos() - self.delta)
        self.update()


    def mouseReleaseEvent(self, event: QMouseEvent):
        self.grab_image()
        self.repaint()


    def grab_image(self):
        filePath = ""
        img = self.desktopPixmap.copy(self.selectedRect.toRect().normalized())
        if img.width == 0 or img.height == 0:
            msg = QMessageBox.warning(self, "WWA", "The image's width and height must be different from 0", QMessageBox.Ok)
        else:
            filePath = time.strftime("screenshot/%Y%m%d_%H%M%S.jpg")
            img.save(self.path + "/" + filePath)
        self.hide()
        self.grabImageDone.emit(filePath)



# if __name__ == "__main__":
#     QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
#     a = QApplication(sys.argv)
#     ss = Snipping()
#     ss.take_screen_shot("D:/")
#     sys.exit(a.exec_())
