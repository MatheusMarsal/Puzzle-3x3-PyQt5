# This Python file uses the following encoding: utf-8
import sys
import time
from PyQt5 import QtCore
from PyQt5.QtGui import QCursor, QFont
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QPushButton, QLCDNumber

class Puzzle3x33(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.resize(320, 400)
        self.setWindowTitle("Puzzle 3x3 com 3 cores")

        self.i = 0
        self.startTime = time.time()

        self.carregarLCD()
        self.carregarBtns()
        self.carregarLabel()
        self.linkClicks()

        self.timeCount()

    def carregarLabel(self):
        self.lblTentativas = QLabel(self)
        self.lblTentativas.setObjectName('lblTentativas')
        self.lblTentativas.setObjectName('btn1')
        self.lblTentativas.setText('Tentativas')
        self.lblTentativas.setGeometry(20, 290, 200, 80)
        self.lblTentativas.setFont(QFont("Arial", 16, 1000))

    def carregarLCD(self):
        self.lcdNumber = QLCDNumber(self)
        self.lcdNumber.setObjectName('lcdNumber')
        self.lcdNumber.setGeometry(150, 320, 150, 60)

    def carregarBtns(self):
        self.btn1 = QPushButton(self)
        self.btn1.setObjectName('btn1')
        self.btn1.setText('1')
        self.btn1.setGeometry(20, 20, 80, 80)
        self.btn1.setFont(QFont("Arial", 12, 1000))
        self.btn1.setStyleSheet("QPushButton {background-color : black; color: white}")
        self.btn1.setToolTip('<font color = black>Proxima cor será: Branco</font>')
        self.btn1.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

        self.btn2 = QPushButton(self)
        self.btn2.setObjectName("btn2")
        self.btn2.setText('2')
        self.btn2.setGeometry(120, 20, 80, 80)
        self.btn2.setFont(QFont("Arial", 12, 1000))
        self.btn2.setStyleSheet("QPushButton {background-color : black; color: white}")
        self.btn2.setToolTip('<font color = black>Proxima cor será: Branco</font>')
        self.btn2.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

        self.btn3 = QPushButton(self)
        self.btn3.setObjectName("btn3")
        self.btn3.setText('3')
        self.btn3.setGeometry(220, 20, 80, 80)
        self.btn3.setFont(QFont("Arial", 12, 1000))
        self.btn3.setStyleSheet("QPushButton {background-color : black; color: white}")
        self.btn3.setToolTip('<font color = black>Proxima cor será: Branco</font>')
        self.btn3.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

        self.btn4 = QPushButton(self)
        self.btn4.setObjectName("btn4")
        self.btn4.setText('4')
        self.btn4.setGeometry(20, 120, 80, 80)
        self.btn4.setFont(QFont("Arial", 12, 1000))
        self.btn4.setStyleSheet("QPushButton {background-color : black; color: white}")
        self.btn4.setToolTip('<font color = black>Proxima cor será: Branco</font>')
        self.btn4.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

        self.btn5 = QPushButton(self)
        self.btn5.setObjectName("btn5")
        self.btn5.setText('5')
        self.btn5.setGeometry(120, 120, 80, 80)
        self.btn5.setFont(QFont("Arial", 12, 1000))
        self.btn5.setStyleSheet("QPushButton {background-color : black; color: white}")
        self.btn5.setToolTip('<font color = black>Proxima cor será: Branco</font>')
        self.btn5.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

        self.btn6 = QPushButton(self)
        self.btn6.setObjectName("btn6")
        self.btn6.setText('6')
        self.btn6.setGeometry(220, 120, 80, 80)
        self.btn6.setFont(QFont("Arial", 12, 1000))
        self.btn6.setStyleSheet("QPushButton {background-color : black; color: white}")
        self.btn6.setToolTip('<font color = black>Proxima cor será: Branco</font>')
        self.btn6.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

        self.btn7 = QPushButton(self)
        self.btn7.setObjectName("btn7")
        self.btn7.setText('7')
        self.btn7.setGeometry(20, 220, 80, 80)
        self.btn7.setFont(QFont("Arial", 12, 1000))
        self.btn7.setStyleSheet("QPushButton {background-color : black; color: white}")
        self.btn7.setToolTip('<font color = black>Proxima cor será: Branco</font>')
        self.btn7.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

        self.btn8 = QPushButton(self)
        self.btn8.setObjectName("btn8")
        self.btn8.setText('8')
        self.btn8.setGeometry(120, 220, 80, 80)
        self.btn8.setFont(QFont("Arial", 12, 1000))
        self.btn8.setStyleSheet("QPushButton {background-color : black; color: white}")
        self.btn8.setToolTip('<font color = black>Proxima cor será: Branco</font>')
        self.btn8.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

        self.btn9 = QPushButton(self)
        self.btn9.setObjectName("btn9")
        self.btn9.setText('9')
        self.btn9.setGeometry(220, 220, 80, 80)
        self.btn9.setFont(QFont("Arial", 12, 1000))
        self.btn9.setStyleSheet("QPushButton {background-color : black; color: white}")
        self.btn9.setToolTip('<font color = black>Proxima cor será: Branco</font>')
        self.btn9.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

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
            resultado.tempo = int(self.tempo)
            resultado.tentativas = int(self.i)
            windowSolved.__init__()
            windowSolved.show()

    def chkFullRed(self):
        if self.btn1.styleSheet() != "QPushButton {background-color : red; color: black}":
            return False

        if self.btn2.styleSheet() != "QPushButton {background-color : red; color: black}":
            return False

        if self.btn3.styleSheet() != "QPushButton {background-color : red; color: black}":
            return False

        if self.btn4.styleSheet() != "QPushButton {background-color : red; color: black}":
            return False

        if self.btn5.styleSheet() != "QPushButton {background-color : red; color: black}":
            return False

        if self.btn6.styleSheet() != "QPushButton {background-color : red; color: black}":
            return False

        if self.btn7.styleSheet() != "QPushButton {background-color : red; color: black}":
            return False

        if self.btn8.styleSheet() != "QPushButton {background-color : red; color: black}":
            return False

        if self.btn9.styleSheet() != "QPushButton {background-color : red; color: black}":
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
        if (self.strStyle.styleSheet()) == "QPushButton {background-color : black; color: white}":
            self.strStyle.setStyleSheet("QPushButton {background-color : white; color: red}")
            self.strStyle.setToolTip('<font color = black>Proxima cor será: Vermelho</font>')
                                        
        elif (self.strStyle.styleSheet()) == "QPushButton {background-color : white; color: red}":
            self.strStyle.setStyleSheet("QPushButton {background-color : red; color: black}")
            self.strStyle.setToolTip('<font color = black>Proxima cor será: Preto</font>')
        else:
            self.strStyle.setStyleSheet("QPushButton {background-color : black; color: white}")
            self.strStyle.setToolTip('<font color = black>Proxima cor será: Branco</font>')

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

class Puzzle3x34(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.resize(320, 400)
        self.setWindowTitle("Puzzle 3x3 com 4 cores")

        self.i = 0
        self.startTime = time.time()

        self.carregarLCD()
        self.carregarBtns()
        self.carregarLabel()
        self.linkClicks()

        self.timeCount()

    def carregarLabel(self):
        self.lblTentativas = QLabel(self)
        self.lblTentativas.setObjectName('lblTentativas')
        self.lblTentativas.setObjectName('btn1')
        self.lblTentativas.setText('Tentativas')
        self.lblTentativas.setGeometry(20, 290, 200, 80)
        self.lblTentativas.setFont(QFont("Arial", 16, 1000))

    def carregarLCD(self):
        self.lcdNumber = QLCDNumber(self)
        self.lcdNumber.setObjectName('lcdNumber')
        self.lcdNumber.setGeometry(150, 320, 150, 60)

    def carregarBtns(self):
        self.btn1 = QPushButton(self)
        self.btn1.setObjectName('btn1')
        self.btn1.setText('1')
        self.btn1.setGeometry(20, 20, 80, 80)
        self.btn1.setFont(QFont("Arial", 12, 1000))
        self.btn1.setStyleSheet("QPushButton {background-color : black; color: white}")
        self.btn1.setToolTip('<font color = black>Proxima cor será: Branco</font>')
        self.btn1.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

        self.btn2 = QPushButton(self)
        self.btn2.setObjectName("btn2")
        self.btn2.setText('2')
        self.btn2.setGeometry(120, 20, 80, 80)
        self.btn2.setFont(QFont("Arial", 12, 1000))
        self.btn2.setStyleSheet("QPushButton {background-color : black; color: white}")
        self.btn2.setToolTip('<font color = black>Proxima cor será: Branco</font>')
        self.btn2.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

        self.btn3 = QPushButton(self)
        self.btn3.setObjectName("btn3")
        self.btn3.setText('3')
        self.btn3.setGeometry(220, 20, 80, 80)
        self.btn3.setFont(QFont("Arial", 12, 1000))
        self.btn3.setStyleSheet("QPushButton {background-color : black; color: white}")
        self.btn3.setToolTip('<font color = black>Proxima cor será: Branco</font>')
        self.btn3.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

        self.btn4 = QPushButton(self)
        self.btn4.setObjectName("btn4")
        self.btn4.setText('4')
        self.btn4.setGeometry(20, 120, 80, 80)
        self.btn4.setFont(QFont("Arial", 12, 1000))
        self.btn4.setStyleSheet("QPushButton {background-color : black; color: white}")
        self.btn4.setToolTip('<font color = black>Proxima cor será: Branco</font>')
        self.btn4.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

        self.btn5 = QPushButton(self)
        self.btn5.setObjectName("btn5")
        self.btn5.setText('5')
        self.btn5.setGeometry(120, 120, 80, 80)
        self.btn5.setFont(QFont("Arial", 12, 1000))
        self.btn5.setStyleSheet("QPushButton {background-color : black; color: white}")
        self.btn5.setToolTip('<font color = black>Proxima cor será: Branco</font>')
        self.btn5.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

        self.btn6 = QPushButton(self)
        self.btn6.setObjectName("btn6")
        self.btn6.setText('6')
        self.btn6.setGeometry(220, 120, 80, 80)
        self.btn6.setFont(QFont("Arial", 12, 1000))
        self.btn6.setStyleSheet("QPushButton {background-color : black; color: white}")
        self.btn6.setToolTip('<font color = black>Proxima cor será: Branco</font>')
        self.btn6.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

        self.btn7 = QPushButton(self)
        self.btn7.setObjectName("btn7")
        self.btn7.setText('7')
        self.btn7.setGeometry(20, 220, 80, 80)
        self.btn7.setFont(QFont("Arial", 12, 1000))
        self.btn7.setStyleSheet("QPushButton {background-color : black; color: white}")
        self.btn7.setToolTip('<font color = black>Proxima cor será: Branco</font>')
        self.btn7.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

        self.btn8 = QPushButton(self)
        self.btn8.setObjectName("btn8")
        self.btn8.setText('8')
        self.btn8.setGeometry(120, 220, 80, 80)
        self.btn8.setFont(QFont("Arial", 12, 1000))
        self.btn8.setStyleSheet("QPushButton {background-color : black; color: white}")
        self.btn8.setToolTip('<font color = black>Proxima cor será: Branco</font>')
        self.btn8.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

        self.btn9 = QPushButton(self)
        self.btn9.setObjectName("btn9")
        self.btn9.setText('9')
        self.btn9.setGeometry(220, 220, 80, 80)
        self.btn9.setFont(QFont("Arial", 12, 1000))
        self.btn9.setStyleSheet("QPushButton {background-color : black; color: white}")
        self.btn9.setToolTip('<font color = black>Proxima cor será: Branco</font>')
        self.btn9.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

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
        if self.chkFullGreen():
            print("Completo em {} segundos, em {} tentativas".format(int(self.tempo), self.i))
            resultado.tempo = int(self.tempo)
            resultado.tentativas = int(self.i)
            windowSolved.__init__()
            windowSolved.show()

    def chkFullGreen(self):
        if self.btn1.styleSheet() != "QPushButton {background-color : green; color: black}":
            return False

        if self.btn2.styleSheet() != "QPushButton {background-color : green; color: black}":
            return False

        if self.btn3.styleSheet() != "QPushButton {background-color : green; color: black}":
            return False

        if self.btn4.styleSheet() != "QPushButton {background-color : green; color: black}":
            return False

        if self.btn5.styleSheet() != "QPushButton {background-color : green; color: black}":
            return False

        if self.btn6.styleSheet() != "QPushButton {background-color : green; color: black}":
            return False

        if self.btn7.styleSheet() != "QPushButton {background-color : green; color: black}":
            return False

        if self.btn8.styleSheet() != "QPushButton {background-color : green; color: black}":
            return False

        if self.btn9.styleSheet() != "QPushButton {background-color : green; color: black}":
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
        if (self.strStyle.styleSheet()) == "QPushButton {background-color : black; color: white}":
            self.strStyle.setStyleSheet("QPushButton {background-color : white; color: red}")
            self.strStyle.setToolTip('<font color = black>Proxima cor será: Vermelho</font>')
                                        
        elif (self.strStyle.styleSheet()) == "QPushButton {background-color : white; color: red}":
            self.strStyle.setStyleSheet("QPushButton {background-color : red; color: green}")
            self.strStyle.setToolTip('<font color = black>Proxima cor será: Verde</font>')

        elif (self.strStyle.styleSheet()) == "QPushButton {background-color : red; color: green}":
            self.strStyle.setStyleSheet("QPushButton {background-color : green; color: black}")
            self.strStyle.setToolTip('<font color = black>Proxima cor será: Preto</font>')

        else:
            self.strStyle.setStyleSheet("QPushButton {background-color : black; color: white}")
            self.strStyle.setToolTip('<font color = black>Proxima cor será: Branco</font>')

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

class PuzzleSolved(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.resize(320, 210)
        self.setWindowTitle("Puzzle resolvido!")
        
        self.btnVoltarMenu = QPushButton(self)
        self.btnVoltarMenu.setObjectName('btnVoltarMenu')
        self.btnVoltarMenu.setText('Voltar para o menu')
        self.btnVoltarMenu.setGeometry(20, 100, 280, 80)
        self.btnVoltarMenu.setFont(QFont("Arial", 12, 1000))
        self.btnVoltarMenu.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.btnVoltarMenu.clicked.connect(self.clickBtnVoltarMenu)

        self.lblTempo = QLabel(self)
        self.lblTempo.setObjectName('lblTempo')
        self.lblTempo.setText("Tempo: " + str(resultado.tempo) + " segundo(s)")
        self.lblTempo.setGeometry(20, 20, 200, 50)
        self.lblTempo.setFont(QFont("Arial", 12, 1000))

        self.lblTentativas = QLabel(self)
        self.lblTentativas.setObjectName('lblTentativas')
        self.lblTentativas.setText("Cliques: " + str(resultado.tentativas))
        self.lblTentativas.setGeometry(20, 50, 200, 50)
        self.lblTentativas.setFont(QFont("Arial", 12, 1000))

    def clickBtnVoltarMenu(self):
        self.hide()
        window3x33.hide()
        window3x34.hide()
        menu.show()

class Menu(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.resize(300, 120)
        self.setWindowTitle("Menu dos Puzzle")
        
        self.btn3x33 = QPushButton(self)
        self.btn3x33.setObjectName('btn3x33')
        self.btn3x33.setText('3x3 lvl 3')
        self.btn3x33.setGeometry(20, 20, 80, 80)
        self.btn3x33.setFont(QFont("Arial", 12, 1000))
        self.btn3x33.setStyleSheet("QPushButton::hover {background-color : red; color: black;}")
        self.btn3x33.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.btn3x33.clicked.connect(self.clickBtn3x33)

        self.btn3x34 = QPushButton(self)
        self.btn3x34.setObjectName('btn3x34')
        self.btn3x34.setText('3x3 lvl 4')
        self.btn3x34.setGeometry(120, 20, 80, 80)
        self.btn3x34.setFont(QFont("Arial", 12, 1000))
        self.btn3x34.setStyleSheet("QPushButton::hover {background-color : green; color: black;}")
        self.btn3x34.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.btn3x34.clicked.connect(self.clickBtn3x34)

    def clickBtn3x33(self):
        self.close()
        window3x33.__init__()
        window3x33.show()
    
    def clickBtn3x34(self):
        self.close()
        window3x34.__init__()
        window3x34.show()

class Resultado(object):
    def __init__(self, tempo, tentativas):
        self._tempo = tempo
        self._tentativas = tentativas

    @property
    def tempo(self):
        return self._tempo

    @tempo.setter
    def tempo(self, tempo):
        self._tempo = tempo

    @property
    def tentativas(self):
        return self._tentativas

    @tentativas.setter
    def tentativas(self, tentativas):
        self._tentativas = tentativas

if __name__ == "__main__":
    app = QApplication([])
    resultado = Resultado(0, 0)
    window3x33 = Puzzle3x33()
    window3x34 = Puzzle3x34()
    windowSolved = PuzzleSolved()
    menu = Menu()
    menu.show()
    sys.exit(app.exec())