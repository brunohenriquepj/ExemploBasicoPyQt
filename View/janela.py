# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'janela.ui'
#
# Created: Tue Sep 20 00:12:01 2016
#      by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(788, 430)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.barra_de_progresso_001 = QtGui.QProgressBar(self.centralwidget)
        self.barra_de_progresso_001.setGeometry(QtCore.QRect(100, 120, 201, 61))
        self.barra_de_progresso_001.setProperty("value", 100)
        self.barra_de_progresso_001.setObjectName(_fromUtf8("barra_de_progresso_001"))
        self.botao_inicia_processo = QtGui.QPushButton(self.centralwidget)
        self.botao_inicia_processo.setGeometry(QtCore.QRect(50, 40, 95, 29))
        self.botao_inicia_processo.setStyleSheet(_fromUtf8("background-color: rgb(15, 67, 255);\n"
"color: white;\n"
"border: 0px;"))
        self.botao_inicia_processo.setObjectName(_fromUtf8("botao_inicia_processo"))
        self.barra_de_progresso_002 = QtGui.QProgressBar(self.centralwidget)
        self.barra_de_progresso_002.setGeometry(QtCore.QRect(390, 120, 201, 61))
        self.barra_de_progresso_002.setProperty("value", 0)
        self.barra_de_progresso_002.setObjectName(_fromUtf8("barra_de_progresso_002"))
        self.botao_para_processo = QtGui.QPushButton(self.centralwidget)
        self.botao_para_processo.setGeometry(QtCore.QRect(180, 40, 95, 29))
        self.botao_para_processo.setStyleSheet(_fromUtf8("background-color: rgb(255, 39, 24);\n"
"border: 0px;\n"
"color: white;"))
        self.botao_para_processo.setObjectName(_fromUtf8("botao_para_processo"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 788, 27))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Interface Qt Designer", None))
        self.botao_inicia_processo.setText(_translate("MainWindow", "Iniciar", None))
        self.botao_para_processo.setText(_translate("MainWindow", "Parar", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

