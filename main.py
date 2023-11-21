import sys
from random import randint

from PyQt5.QtGui import QPainter, QColor
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication


class Classwork(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.qp = QPainter()
        self.flag = False
        self.qbtn.clicked.connect(self.drawf)

    def drawf(self):
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            self.qp = QPainter()
            self.qp.begin(self)
            self.draw()
            self.qp.end()

    def draw(self):
        R = randint(20, 400)
        self.qp.setBrush(QColor(255, 255, 0))
        self.qp.drawEllipse(int(randint(0, 800) - R / 2),
                            int(randint(0, 580) - R / 2), R, R)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Classwork()
    sys.excepthook = except_hook
    ex.show()
    sys.exit(app.exec())