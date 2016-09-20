# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import QThread, SIGNAL
from threading import Thread
from threading import Lock
import threading, time, sys

#Aqui importamos nosso arquivo janela.py da View
import View.janela

class Processo(QThread):
    def __init__(self):
        QThread.__init__(self)
        self.porcentagem1 = 100
        self.porcentagem2 = 0

    def __del__(self):
        self.wait()

    def run(self):
        while True:
            self.contagem_barra_de_progresso_001()
            #Emite um sinal para o Connect na classe Interface,
            #passando o valor da porcentagem da barra de progresso
            #decrementado
            self.emit(
                    SIGNAL('recarrega_barra_de_progresso_um(QString)'),
                    str(self.porcentagem1)
                )
            self.contagem_barra_de_progresso_002()
            #Emite um sinal para o Connect na classe Interface,
            #passando o valor da porcentagem da barra de progresso
            #incrementado
            self.emit(
                    SIGNAL('recarrega_barra_de_progresso_dois(QString)'),
                    str(self.porcentagem2)
                )
            #Rodando em 0.01 segundo para mostrar que o Qthread
            #funciona, rsrs
            time.sleep(0.01)

    def contagem_barra_de_progresso_001(self):
        self.porcentagem1 = self.porcentagem1 - 1
        if (self.porcentagem1 == 0):
            self.porcentagem1 = 100


    def contagem_barra_de_progresso_002(self):
        self.porcentagem2 = self.porcentagem2 + 1
        if (self.porcentagem2 == 100):
            self.porcentagem2 = 0


class Interface(
        QtGui.QMainWindow,
        View.janela.Ui_MainWindow
    ):

    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        #Ao clicar no botão 'iniciar', chamo a 'função inica_interface'
        #abaixo
        self.botao_inicia_processo.clicked.connect(
            self.inica_interface
        )

    def inica_interface(self):
        #Recebo a classe processo na minha varável
        #local processo
        self.processo = Processo()
        #Na classe processo tenho uma função chamada 'run',
        #aqui inicializo ela '.start()' e inia a thread principal
        #deste software
        self.processo.start()
        #Desativa botão iniciar
        self.botao_inicia_processo.setEnabled(False)
        #Ativa botão parar
        self.botao_para_processo.setEnabled(True)
        #Conexão para o SIGNAL enviado na classe Processo e
        #chama a função 'recarrega_barra_de_progresso_um' da classe
        #interface
        self.connect(
            self.processo,
            SIGNAL('recarrega_barra_de_progresso_um(QString)'),
            self.recarrega_barra_de_progresso_um
        )
        #Conexão para o SIGNAL enviado na classe Processo e
        #chama a função 'recarrega_barra_de_progresso_dois' da classe
        #interface
        self.connect(
            self.processo,
            SIGNAL('recarrega_barra_de_progresso_dois(QString)'),
            self.recarrega_barra_de_progresso_dois
        )
        #Ao clicar no botão parar,
        #para a thread principal executa pela função 'run' da classe processo
        self.botao_para_processo.clicked.connect(self.processo.terminate)

    def recarrega_barra_de_progresso_um(self, porcentagem):
        print 'Porcentagem barra de progresso 001: %d' % int(float(porcentagem))
        self.barra_de_progresso_001.setValue(int(float(porcentagem)))

    def recarrega_barra_de_progresso_dois(self, porcentagem):
        print 'Porcentagem barra de progresso 002: %d' % int(float(porcentagem))
        self.barra_de_progresso_002.setValue(int(float(porcentagem)))

def main():
    app = QtGui.QApplication(sys.argv)
    form = Interface()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()
