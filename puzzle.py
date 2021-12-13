# This Python file uses the following encoding: utf-8
import sys
import time
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLCDNumber

class Widget(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.resize(320, 400)
        self.setWindowTitle("Puzzle")

        self.i = 0
        self.startTime = time.time()

        self.carregarLCD()
        self.carregarBtns()
        self.linkClicks()

        self.timeCount()

    def carregarLCD(self):
        self.lcdNumber = QLCDNumber(self)
        self.lcdNumber.setObjectName('lcdNumber')
        self.lcdNumber.setGeometry(150, 320, 150, 60)

    def carregarBtns(self):
        self.btn1 = QPushButton(self)
        self.btn1.setObjectName('btn1')
        self.btn1.setText('1')
        self.btn1.setGeometry(20, 20, 80, 80)
        self.btn1.setStyleSheet("background-color: black")

        self.btn2 = QPushButton(self)
        self.btn2.setObjectName("btn2")
        self.btn2.setText('2')
        self.btn2.setGeometry(120, 20, 80, 80)
        self.btn2.setStyleSheet("background-color: black")

        self.btn3 = QPushButton(self)
        self.btn3.setObjectName("btn3")
        self.btn3.setText('3')
        self.btn3.setGeometry(220, 20, 80, 80)
        self.btn3.setStyleSheet("background-color: black")

        self.btn4 = QPushButton(self)
        self.btn4.setObjectName("btn4")
        self.btn4.setText('4')
        self.btn4.setGeometry(20, 120, 80, 80)
        self.btn4.setStyleSheet("background-color: black")

        self.btn5 = QPushButton(self)
        self.btn5.setObjectName("btn5")
        self.btn5.setText('5')
        self.btn5.setGeometry(120, 120, 80, 80)
        self.btn5.setStyleSheet("background-color: black")

        self.btn6 = QPushButton(self)
        self.btn6.setObjectName("btn6")
        self.btn6.setText('6')
        self.btn6.setGeometry(220, 120, 80, 80)
        self.btn6.setStyleSheet("background-color: black")

        self.btn7 = QPushButton(self)
        self.btn7.setObjectName("btn7")
        self.btn7.setText('7')
        self.btn7.setGeometry(20, 220, 80, 80)
        self.btn7.setStyleSheet("background-color: black")

        self.btn8 = QPushButton(self)
        self.btn8.setObjectName("btn8")
        self.btn8.setText('8')
        self.btn8.setGeometry(120, 220, 80, 80)
        self.btn8.setStyleSheet("background-color: black")

        self.btn9 = QPushButton(self)
        self.btn9.setObjectName("btn9")
        self.btn9.setText('9')
        self.btn9.setGeometry(220, 220, 80, 80)
        self.btn9.setStyleSheet("background-color: black")

    def linkClicks(self):
        self.btn1.clicked.connect(self.btn1Click)
        self.btn2.clicked.connect(self.btn2Click)
        self.btn3.clicked.connect(self.btn3Click)
        self.btn4.clicked.connect(self.btn4Click)
        self.btn5.clicked.connect(self.btn5Click)
        self.btn6.clicked.connect(self.btn6Click)
        self.btn7.clicked.connect(self.btn7Click)
        self.btn8.clicked.connect(self.btn8Click)
        self.btn9.clicked.connect(self.btn9Click)
    
    def chkBtns(self):
        if self.chkFullRed():
            print("Completo em {} segundos, em {} tentativas".format(int(self.tempo), self.i))

    def chkFullRed(self):
        if self.btn1.styleSheet() != "background-color: red":
            return False

        if self.btn2.styleSheet() != "background-color: red":
            return False

        if self.btn3.styleSheet() != "background-color: red":
            return False

        if self.btn4.styleSheet() != "background-color: red":
            return False

        if self.btn5.styleSheet() != "background-color: red":
            return False

        if self.btn6.styleSheet() != "background-color: red":
            return False

        if self.btn7.styleSheet() != "background-color: red":
            return False

        if self.btn8.styleSheet() != "background-color: red":
            return False

        if self.btn9.styleSheet() != "background-color: red":
            return False

        return True

    def timeCount(self):
        self.tempo = time.time() - self.startTime
        if self.tempo > 1:
            print(str(int(self.tempo)))

    def clickCount(self):
        self.timeCount()
        self.i += 1
        self.lcdNumber.display(self.i)

    def checkStyleSheet(self, strStyle):
        if (self.strStyle.styleSheet()) == "background-color: black":
            self.strStyle.setStyleSheet("background-color: white")
        elif (self.strStyle.styleSheet()) == "background-color: white":
            self.strStyle.setStyleSheet("background-color: red")
        else:
            self.strStyle.setStyleSheet("background-color: black")

    def btn1Click(self):
        self.clickCount()

        self.strStyle = self.btn1
        self.checkStyleSheet(self.strStyle)

        self.strStyle = self.btn2
        self.checkStyleSheet(self.strStyle)

        self.strStyle = self.btn4
        self.checkStyleSheet(self.strStyle)
        
        self.chkBtns()

    def btn2Click(self):
        self.clickCount()
        
        self.strStyle = self.btn1
        self.checkStyleSheet(self.strStyle)

        self.strStyle = self.btn2
        self.checkStyleSheet(self.strStyle)

        self.strStyle = self.btn3
        self.checkStyleSheet(self.strStyle)
        
        self.strStyle = self.btn5
        self.checkStyleSheet(self.strStyle)

        self.chkBtns()

    def btn3Click(self):
        self.clickCount()
        
        self.strStyle = self.btn2
        self.checkStyleSheet(self.strStyle)

        self.strStyle = self.btn3
        self.checkStyleSheet(self.strStyle)

        self.strStyle = self.btn6
        self.checkStyleSheet(self.strStyle)

        self.chkBtns()

    def btn4Click(self):
        self.clickCount()
        
        self.strStyle = self.btn1
        self.checkStyleSheet(self.strStyle)

        self.strStyle = self.btn4
        self.checkStyleSheet(self.strStyle)

        self.strStyle = self.btn5
        self.checkStyleSheet(self.strStyle)
        
        self.strStyle = self.btn7
        self.checkStyleSheet(self.strStyle)

        self.chkBtns()

    def btn5Click(self):
        self.clickCount()
        
        self.strStyle = self.btn2
        self.checkStyleSheet(self.strStyle)

        self.strStyle = self.btn4
        self.checkStyleSheet(self.strStyle)

        self.strStyle = self.btn5
        self.checkStyleSheet(self.strStyle)
        
        self.strStyle = self.btn6
        self.checkStyleSheet(self.strStyle)
        
        self.strStyle = self.btn8
        self.checkStyleSheet(self.strStyle)

        self.chkBtns()

    def btn6Click(self):
        self.clickCount()
        
        self.strStyle = self.btn3
        self.checkStyleSheet(self.strStyle)

        self.strStyle = self.btn5
        self.checkStyleSheet(self.strStyle)

        self.strStyle = self.btn6
        self.checkStyleSheet(self.strStyle)
        
        self.strStyle = self.btn9
        self.checkStyleSheet(self.strStyle)

        self.chkBtns()

    def btn7Click(self):
        self.clickCount()
        
        self.strStyle = self.btn4
        self.checkStyleSheet(self.strStyle)

        self.strStyle = self.btn7
        self.checkStyleSheet(self.strStyle)

        self.strStyle = self.btn8
        self.checkStyleSheet(self.strStyle)
        
        self.chkBtns()

    def btn8Click(self): 
        self.clickCount()
        
        self.strStyle = self.btn5
        self.checkStyleSheet(self.strStyle)

        self.strStyle = self.btn7
        self.checkStyleSheet(self.strStyle)

        self.strStyle = self.btn8
        self.checkStyleSheet(self.strStyle)
        
        self.strStyle = self.btn9
        self.checkStyleSheet(self.strStyle)

        self.chkBtns()

    def btn9Click(self):  
        self.clickCount()
          
        self.strStyle = self.btn6
        self.checkStyleSheet(self.strStyle)

        self.strStyle = self.btn8
        self.checkStyleSheet(self.strStyle)

        self.strStyle = self.btn9
        self.checkStyleSheet(self.strStyle)

        self.chkBtns()

if __name__ == "__main__":
    app = QApplication([])
    window = Widget()
    window.show()
    sys.exit(app.exec())