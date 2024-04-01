
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

def menu():
    print("메뉴")
def topic():
    print("주제")
def game():
    print("술게임")
def conver():
    print("대화")




class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(400, 400, 500, 500)
        self.setWindowTitle("AI ChatBot")
        self.setWindowIcon(QIcon("Python/AI-icon.png"))
        label = QLabel()
        label.setPixmap(QPixmap("Python/AI-img.png"))
        self.setCentralWidget(label)
        
        btn = QPushButton(text="메뉴 추천", parent=self)
        btn.move(5,420)
        btn.resize(110, 50)
        btn.clicked.connect(menu)
        btn = QPushButton(text="대화주제 추천", parent=self)
        btn.move(130,420)
        btn.resize(130, 50)
        btn.clicked.connect(topic)
        btn = QPushButton(text="술게임", parent=self)
        btn.move(265,420)
        btn.resize(110, 50)
        btn.clicked.connect(game)
        btn = QPushButton(text="대화모드", parent=self)
        btn.move(390,420)
        btn.resize(110, 50)
        btn.clicked.connect(conver)
        

app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()
