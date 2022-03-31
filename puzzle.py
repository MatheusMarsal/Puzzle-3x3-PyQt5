import sys
import time
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCursor, QFont, QColor
from PyQt5.QtWidgets import QApplication, QLCDNumber, QLabel, QPushButton, QShortcut, QWidget, QGraphicsDropShadowEffect, QStyle

class Tela(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setStyleSheet("background-color: white")

class Sombra():
    def criarSombra(self) -> QGraphicsDropShadowEffect:
        self.shadow = QGraphicsDropShadowEffect()
        self.shadow.setOffset(2, 2)
        self.shadow.setBlurRadius(10)
        self.shadow.setColor(QColor("#515151"))

        return self.shadow

class Botao():
    def criarBtn(self, nome, x, y, corFundo, corFonte) -> QPushButton:
        self.tam = 80 + tamanhoUI.tamanho

        self.btn = QPushButton(self)
        self.btn.setObjectName(str(corFundo + ', ' + corFonte))
        self.btn.setText(nome)
        self.btn.setGeometry(x, y, self.tam, self.tam)
        self.btn.setFont(QFont("Arial", 12, 1000))
        self.btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.btn.setStyleSheet("QPushButton {background-color: " + corFundo + "; color: " + corFonte + "; border-radius: 15%}")

        self.btn.pressed.connect(lambda:Botao.pressedBtn(self))
        self.btn.released.connect(lambda:Botao.releasedBtn(self))

        self.sombrio = Sombra.criarSombra(self)
        self.btn.setGraphicsEffect(self.sombrio)

        return self.btn

    def pressedBtn(self):
        self._sender = self.sender()
    
        self.coresBtn = self._sender.objectName()
        self.coresBtn = self.coresBtn.split(", ")

        self._sender.setStyleSheet('QPushButton {background-color: ' + self.coresBtn[0] + "; color: " + self.coresBtn[1] + '; border-radius: 13%}')
        self.sombra = self._sender.graphicsEffect()
        self.sombra.setBlurRadius(15)
        self.sombra.setOffset(-2, -2)

    def releasedBtn(self):
        self._sender = self.sender()
    
        self.coresBtn = self._sender.objectName()
        self.coresBtn = self.coresBtn.split(", ")

        self._sender.setStyleSheet('QPushButton {background-color: ' + self.coresBtn[0] + "; color: " + self.coresBtn[1] + '; border-radius: 15%}')
        self.sombra = self._sender.graphicsEffect()
        self.sombra.setBlurRadius(5)
        self.sombra.setOffset(2, 2)

    def mudarStyleSheet(self, corFundo, corFonte):
        self.setStyleSheet("QPushButton {background-color: " + corFundo + "; color: " + corFonte + "; border-radius: 15%}")
        self.setObjectName(str(corFundo + ', ' + corFonte))

    def mudarToolTip(self, proxCor):
        self.setToolTip('<font color = black>Proxima cor será: ' + proxCor +  '</font>')

class Menu(Tela):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Menu dos Puzzle")

        self.btn3x33 = Botao.criarBtn(self, '3x3 lvl 3', 20 ,20, 'red', 'black')

        self.btn3x34 = Botao.criarBtn(self, '3x3 lvl 4', 120 +  tamanhoUI.tamanho, 20, 'green', 'black')

        self.btn3x33.clicked.connect(self.clickBtn3x33)
        self.btn3x34.clicked.connect(self.clickBtn3x34)

    def clickBtn3x33(self):
        self.close()
        self.puzzle3x33 = Puzzle3x33()
        self.puzzle3x33.show()

    def clickBtn3x34(self):
        self.close()
        self.puzzle3x34 = Puzzle3x34()
        self.puzzle3x34.show()

class TelaPuzzle3x3(Tela):
    def __init__(self):
        super().__init__()
        self.i = 0
        self.startTime = time.time()
        self.btns = []
        
        self.index = 0
        self.multiplierY = 0

        for self.y in range(20, 221, 100):
            self.multiplierX = 0
            for self.x in range(20, 221, 100):
                self.btns.append(Botao.criarBtn(self, str(self.index + 1), self.x + self.multiplierX * tamanhoUI.tamanho, self.y + self.multiplierY * tamanhoUI.tamanho, 'black', 'white'))
                self.btns[self.index].setToolTip('<font color = black>Proxima cor será: Branco</font>')
                self.index += 1
                self.multiplierX += 1
            self.multiplierY += 1

        #Dimenções da Label
        self.lbly = 320 + (tamanhoUI.tamanho * 3)
        self.lblh = 200 + tamanhoUI.tamanho
        self.lblw = 60 + tamanhoUI.tamanho

        #Dimenções do LCD
        self.lcdx = 150 + (tamanhoUI.tamanho * 2)
        self.lcdy = 320 + (tamanhoUI.tamanho * 3)
        self.lcdh = 150 + tamanhoUI.tamanho
        self.lcdw = 60 + tamanhoUI.tamanho

        self.lblTentativas = QLabel(self)
        self.lblTentativas.setObjectName('lblTentativas')
        self.lblTentativas.setText('Tentativas')
        self.lblTentativas.setFont(QFont("Arial", 16, 1000))
        self.lblTentativas.setGeometry(20, self.lbly, self.lblh, self.lblw)

        self.lcdNumber = QLCDNumber(self)
        self.lcdNumber.setObjectName('lcdNumber')
        self.lcdNumber.setGeometry(self.lcdx, self.lcdy, self.lcdh, self.lcdw)
        
        self.reloadBtn = Botao.criarBtn(self, "", 0, 0, "rgba(230,230,230,0.5)", "White")
        self.reloadBtn.setGeometry(150 + (tamanhoUI.tamanho * 2) + 2, int(self.lcdy), int(self.lblw / 3 * 0.9), int(self.lblw / 3 * 0.9))
        self.reloadBtn.setIcon(self.style().standardIcon(getattr(QStyle, 'SP_BrowserReload')))
        self.reloadBtn.setToolTip("Restart")
        self.reloadBtn.clicked.connect(self.reloadBtn_Clcik)
        
        self.backBtn = Botao.criarBtn(self, "", 0, 0, "rgba(230,230,230,0.5)", "White")
        self.backBtn.setGeometry(150 + (tamanhoUI.tamanho * 2) + 2, int(self.lcdy + (self.lblw / 3)), int(self.lblw / 3 * 0.9), int(self.lblw / 3 * 0.9))
        self.backBtn.setIcon(self.style().standardIcon(getattr(QStyle, 'SP_ArrowBack')))
        self.backBtn.setToolTip("Voltar para o menu principal")
        self.backBtn.clicked.connect(self.backBtn_Clcik)
        
        #Em desenvolvimento

        #self.helpBtn = Botao.criarBtn(self, "", 0, 0, "rgba(230,230,230,0.5)", "White")
        #self.helpBtn.setGeometry(150 + (tamanhoUI.tamanho * 2) + 2, int(self.lcdy + (self.lblw / 3) * 2), int(self.lblw / 3 * 0.9), int(self.lblw / 3 * 0.9))
        #self.helpBtn.setIcon(self.style().standardIcon(getattr(QStyle, 'SP_TitleBarContextHelpButton')))
        #self.helpBtn.setToolTip("Ajuda")
        #self.helpBtn.clicked.connect(self.helpBtn_Clcik)

    def timeCount(self):
        self.tempo = time.time() - self.startTime

    def clickCount(self):
        self.i += 1
        self.lcdNumber.display(self.i)

    def chkFullColor(self, corFundo, corFonte):
        for self.btn in self.btns:
            if self.btn.styleSheet() != "QPushButton {background-color: " + corFundo + "; color: " + corFonte + "; border-radius: 15%}":
                return False

        self.timeCount()
        return True

    def atalhos(self):
        self.key1 = QShortcut("1", self)
        self.key2 = QShortcut("2", self)
        self.key3 = QShortcut("3", self)
        self.key4 = QShortcut("4", self)
        self.key5 = QShortcut("5", self)
        self.key6 = QShortcut("6", self)
        self.key7 = QShortcut("7", self)
        self.key8 = QShortcut("8", self)
        self.key9 = QShortcut("9", self)
        self.keyR = QShortcut("R", self)
        self.keyBack = QShortcut("Backspace", self)

        self.key1.activated.connect(self.btn1Click)
        self.key2.activated.connect(self.btn2Click)
        self.key3.activated.connect(self.btn3Click)
        self.key4.activated.connect(self.btn4Click)
        self.key5.activated.connect(self.btn5Click)
        self.key6.activated.connect(self.btn6Click)
        self.key7.activated.connect(self.btn7Click)
        self.key8.activated.connect(self.btn8Click)
        self.key9.activated.connect(self.btn9Click)
        self.keyR.activated.connect(self.reloadBtn_Clcik)
        self.keyBack.activated.connect(self.backBtn_Clcik)

    def btn_Clcik(self):
        self._sender = self.sender()

        if self._sender.text() == '1':
            self.btn1Click()
            return

        if self._sender.text() == '2':
            self.btn2Click()
            return

        if self._sender.text() == '3':
            self.btn3Click()
            return

        if self._sender.text() == '4':
            self.btn4Click()
            return

        if self._sender.text() == '5':
            self.btn5Click()
            return

        if self._sender.text() == '6':
            self.btn6Click()
            return

        if self._sender.text() == '7':
            self.btn7Click()
            return

        if self._sender.text() == '8':
            self.btn8Click()
            return

        if self._sender.text() == '9':
            self.btn9Click()
            return

    def btn1Click(self):
        self.clickCount()

        self.strStyle = self.btns[0]
        self.checkStyleSheet(self.strStyle)

        self.strStyle = self.btns[1]
        self.checkStyleSheet(self.strStyle)

        self.strStyle = self.btns[3]
        self.checkStyleSheet(self.strStyle)

        self.chkBtns()

    def btn2Click(self):
        self.clickCount()

        self.strStyle = self.btns[0]
        self.checkStyleSheet(self.strStyle)

        self.strStyle = self.btns[1]
        self.checkStyleSheet(self.strStyle)

        self.strStyle = self.btns[2]
        self.checkStyleSheet(self.strStyle)

        self.strStyle = self.btns[4]
        self.checkStyleSheet(self.strStyle)

        self.chkBtns()

    def btn3Click(self):
        self.clickCount()

        self.strStyle = self.btns[1]
        self.checkStyleSheet(self.strStyle)

        self.strStyle = self.btns[2]
        self.checkStyleSheet(self.strStyle)

        self.strStyle = self.btns[5]
        self.checkStyleSheet(self.strStyle)

        self.chkBtns()

    def btn4Click(self):
        self.clickCount()

        self.strStyle = self.btns[0]
        self.checkStyleSheet(self.strStyle)

        self.strStyle = self.btns[3]
        self.checkStyleSheet(self.strStyle)

        self.strStyle = self.btns[4]
        self.checkStyleSheet(self.strStyle)

        self.strStyle = self.btns[6]
        self.checkStyleSheet(self.strStyle)

        self.chkBtns()

    def btn5Click(self):
        self.clickCount()

        self.strStyle = self.btns[1]
        self.checkStyleSheet(self.strStyle)

        self.strStyle = self.btns[3]
        self.checkStyleSheet(self.strStyle)

        self.strStyle = self.btns[4]
        self.checkStyleSheet(self.strStyle)

        self.strStyle = self.btns[5]
        self.checkStyleSheet(self.strStyle)

        self.strStyle = self.btns[7]
        self.checkStyleSheet(self.strStyle)

        self.chkBtns()

    def btn6Click(self):
        self.clickCount()

        self.strStyle = self.btns[2]
        self.checkStyleSheet(self.strStyle)

        self.strStyle = self.btns[4]
        self.checkStyleSheet(self.strStyle)

        self.strStyle = self.btns[5]
        self.checkStyleSheet(self.strStyle)

        self.strStyle = self.btns[8]
        self.checkStyleSheet(self.strStyle)

        self.chkBtns()

    def btn7Click(self):
        self.clickCount()

        self.strStyle = self.btns[3]
        self.checkStyleSheet(self.strStyle)

        self.strStyle = self.btns[6]
        self.checkStyleSheet(self.strStyle)

        self.strStyle = self.btns[7]
        self.checkStyleSheet(self.strStyle)

        self.chkBtns()

    def btn8Click(self):
        self.clickCount()

        self.strStyle = self.btns[4]
        self.checkStyleSheet(self.strStyle)

        self.strStyle = self.btns[6]
        self.checkStyleSheet(self.strStyle)

        self.strStyle = self.btns[7]
        self.checkStyleSheet(self.strStyle)

        self.strStyle = self.btns[8]
        self.checkStyleSheet(self.strStyle)

        self.chkBtns()

    def btn9Click(self):
        self.clickCount()

        self.strStyle = self.btns[5]
        self.checkStyleSheet(self.strStyle)

        self.strStyle = self.btns[7]
        self.checkStyleSheet(self.strStyle)

        self.strStyle = self.btns[8]
        self.checkStyleSheet(self.strStyle)

        self.chkBtns()

    def reloadBtn_Clcik(self):
        for self.index in range(len(self.btns)):
            Botao.mudarStyleSheet(self.btns[self.index], "black", "white")
            Botao.mudarToolTip(self.btns[self.index], 'Branco')

        self.i = 0
        self.lcdNumber.display(self.i)

    def backBtn_Clcik(self):
        self.hide()
        menu.show()

    def helpBtn_Clcik(self):
        pass

class Puzzle3x33(TelaPuzzle3x3):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Puzzle 3x3 com 3 cores")

        for self.index in range(len(self.btns)):
            self.btns[self.index].clicked.connect(self.btn_Clcik)

        self.atalhos()

    def chkBtns(self):
        if self.chkFullColor('red', 'black'):
            print("Completo em {} segundos, em {} tentativas".format(int(self.tempo), self.i))
            resultado.tempo = int(self.tempo)
            resultado.tentativas = int(self.i)

            self.resultado = TelaResultado()
            self.resultado.show()

    def checkStyleSheet(self, strStyle):
        self.strStyle = strStyle

        if self.strStyle.styleSheet() == "QPushButton {background-color: black; color: white; border-radius: 15%}":
            Botao.mudarStyleSheet(self.strStyle, "white", "red")
            Botao.mudarToolTip(self.strStyle, 'Vermelho')

        elif self.strStyle.styleSheet() == "QPushButton {background-color: white; color: red; border-radius: 15%}":
            Botao.mudarStyleSheet(self.strStyle, "red", "black")
            Botao.mudarToolTip(self.strStyle, 'Preto')

        else:
            Botao.mudarStyleSheet(self.strStyle, "black", "white")
            Botao.mudarToolTip(self.strStyle, 'Branco')

class Puzzle3x34(TelaPuzzle3x3):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Puzzle 3x3 com 4 cores")

        for self.index in range(len(self.btns)):
            self.btns[self.index].clicked.connect(self.btn_Clcik)

    def chkBtns(self):
        if self.chkFullColor('green', 'black'):
            print("Completo em {} segundos, em {} tentativas".format(int(self.tempo), self.i))
            resultado.tempo = int(self.tempo)
            resultado.tentativas = int(self.i)

    def checkStyleSheet(self, strStyle):
        self.strStyle = strStyle

        if self.strStyle.styleSheet() == "QPushButton {background-color: black; color: white; border-radius: 15%}":
            Botao.mudarStyleSheet(self.strStyle, "white", "red")
            Botao.mudarToolTip(self.strStyle, 'Vermelho')

        elif self.strStyle.styleSheet() == "QPushButton {background-color: white; color: red; border-radius: 15%}":
            Botao.mudarStyleSheet(self.strStyle, "red", "green")
            Botao.mudarToolTip(self.strStyle, 'Verde')

        elif self.strStyle.styleSheet() == "QPushButton {background-color: red; color: green; border-radius: 15%}":
            Botao.mudarStyleSheet(self.strStyle, "green", "black")
            Botao.mudarToolTip(self.strStyle, 'Preto')

        else:
            Botao.mudarStyleSheet(self.strStyle, "black", "white")
            Botao.mudarToolTip(self.strStyle, 'Branco')

class Resultado(object):
    def __init__(self, tempo, tentativas):
        self._tempo = tempo
        self._tentativas = tentativas

    @property
    def tempo(self) -> float:
        return self._tempo

    @tempo.setter
    def tempo(self, tempo):
        self._tempo = tempo

    @property
    def tentativas(self) -> int:
        return self._tentativas

    @tentativas.setter
    def tentativas(self, tentativas):
        self._tentativas = tentativas

#Em desenvolvimento!
class TamanhoUI(object):
    def __init__(self, tamanho):
        self._tamanho = tamanho

    @property
    def tamanho(self) -> int:
        return self._tamanho

    @tamanho.setter
    def tamanho(self, tamanho):
        self._tamanho = tamanho

class Responsivo(Tela):
    def carregarAtalhos(self):
        self.keyPlus = QShortcut("+", self)
        self.keyMinus = QShortcut("-", self)
        self.key0 = QShortcut("0", self)

        self.key0.activated.connect(self.resetarUI)
        self.keyPlus.activated.connect(self.aumentarUI)
        self.keyMinus.activated.connect(self.diminuirUI)

    def aumentarUI(self):
        tamanhoUI.tamanho += 10
        self.refreshUI()

    def diminuirUI(self):
        if tamanhoUI.tamanho > 10:
            tamanhoUI.tamanho -= 10
            self.refreshUI()

    def resetarUI(self):
        tamanhoUI.tamanho =  40

class TelaResultado(Tela):
    def __init__(self):
        super().__init__()
        
        self.resize(320, 210)
        self.setWindowTitle("Puzzle resolvido!")
                
        self.btnVoltar = Botao.criarBtn(self, "Voltar para o menu", 0, 0, "rgba(10,10,10,0.5)", "White")
        self.btnVoltar.setGeometry(20, 100, 280, 80)
        self.btnVoltar.setToolTip("Voltar para o menu")
        self.btnVoltar.setFont(QFont("Arial", 12, 1000))
        self.btnVoltar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnVoltar.clicked.connect(self.clickBtnVoltar)

        self.lblTempo = QLabel(self)
        self.lblTempo.setObjectName('lblTempo')
        self.lblTempo.setText("Tempo: " + str(resultado.tempo) + " segundo(s)")
        self.lblTempo.setGeometry(20, 20, 200, 40)
        self.lblTempo.setFont(QFont("Arial", 12, 1000))

        self.lblTentativas = QLabel(self)
        self.lblTentativas.setObjectName('lblTentativas')
        self.lblTentativas.setText("Cliques: " + str(resultado.tentativas))
        self.lblTentativas.setGeometry(20, 50, 200, 40)
        self.lblTentativas.setFont(QFont("Arial", 12, 1000))

    def clickBtnVoltar(self):
        self.hide()

if __name__ == "__main__":
    app = QApplication([])
    resultado = Resultado(0, 0)
    tamanhoUI = TamanhoUI(40)
    menu = Menu()
    menu.show()
    sys.exit(app.exec())