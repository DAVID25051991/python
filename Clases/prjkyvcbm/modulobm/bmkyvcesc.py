# @autor : Kevin Yesid Vasquez
# @fecha : 26 octubre 2023
# @ficha : 2740559 
# @Description : modulo para la ventana de dialogo buscaminas.ui

#Modulos o paquetes propios de python 
import time

import sys
# modulos o paquetes de pyqt5
# from PyQt5 import QtGui
# from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi

class DlgBuscaminas(QDialog):
    def __init__(self):
        super(DlgBuscaminas, self).__init__()
        loadUi('appescritorio/buscaminas.ui', self)

        # Celda i: 1, j: 1
        self.bttnCelda1_1.clicked.connect(self.celda11)
        # Celda i: 1, j: 2
        self.bttnCelda1_2.clicked.connect(self.celda12)
        # Celda i: 1, j: 3
        self.bttnCelda1_3.clicked.connect(self.celda13)
        # Celda i: 1, j: 4
        self.bttnCelda1_4.clicked.connect(self.celda14)

        # Celda i: 2, j: 1
        self.bttnCelda2_1.clicked.connect(self.celda21)
        # Celda i: 2, j: 2
        self.bttnCelda2_2.clicked.connect(self.celda22)
        # Celda i: 2, j: 3
        self.bttnCelda2_3.clicked.connect(self.celda23)
        # Celda i: 2, j: 4
        self.bttnCelda2_4.clicked.connect(self.celda24)

        # Celda i: 3, j: 1
        self.bttnCelda3_1.clicked.connect(self.celda31)
        # Celda i: 3, j: 2
        self.bttnCelda3_2.clicked.connect(self.celda32)
        # Celda i: 3, j: 3
        self.bttnCelda3_3.clicked.connect(self.celda33)
        # Celda i: 3, j: 4
        self.bttnCelda3_4.clicked.connect(self.celda34)

        # Celda i: 4, j: 1
        self.bttnCelda4_1.clicked.connect(self.celda41)
        # Celda i: 4, j: 2
        self.bttnCelda4_2.clicked.connect(self.celda42)
        # Celda i: 4, j: 3
        self.bttnCelda4_3.clicked.connect(self.celda43)
        # Celda i: 4, j: 4
        self.bttnCelda4_4.clicked.connect(self.celda44)

    #Funciones para insercion de datos en i:1 j:1-4
    def celda11 (self):
        self.bttnCelda1_1.setText("I:1, J:1")
        time.sleep(1)
        self.bttnCelda1_1.isEnable = False
    
    def celda12 (self):
        self.bttnCelda1_2.setText("I:1, J:2")
        time.sleep(1)
        self.bttnCelda1_2.isEnable = False

    def celda13 (self):
        self.bttnCelda1_3.setText("I:1, J:3")
        time.sleep(1)
        self.bttnCelda1_3.isEnable = False
    
    def celda14 (self):
        self.bttnCelda1_4.setText("I:1, J:4")
        time.sleep(1)
        self.bttnCelda1_4.isEnable = False


    #Funciones para insercion de datos en i:2 j:1-4
    def celda21 (self):
        self.bttnCelda2_1.setText("I:2, J:1")
        time.sleep(1)
        self.bttnCelda2_1.isEnable = False
    
    def celda22 (self):
        self.bttnCelda2_2.setText("I:2, J:2")
        time.sleep(1)
        self.bttnCelda2_2.isEnable = False

    def celda23 (self):
        self.bttnCelda2_3.setText("I:2, J:3")
        time.sleep(1)
        self.bttnCelda2_3.isEnable = False
    
    def celda24 (self):
        self.bttnCelda2_4.setText("I:2, J:4")
        time.sleep(1)
        self.bttnCelda2_4.isEnable = False


    #Funciones para insercion de datos en i:3 j:1-4
    def celda31 (self):
        self.bttnCelda3_1.setText("I:3, J:1")
        time.sleep(1)
        self.bttnCelda3_1.isEnable = False
    
    def celda32 (self):
        self.bttnCelda3_2.setText("I:3, J:2")
        time.sleep(1)
        self.bttnCelda3_2.isEnable = False

    def celda33 (self):
        self.bttnCelda3_3.setText("I:3, J:3")
        time.sleep(1)
        self.bttnCelda3_3.isEnable = False
    
    def celda34 (self):
        self.bttnCelda3_4.setText("I:3, J:4")
        time.sleep(1)
        self.bttnCelda3_4.isEnable = False


    #Funciones para insercion de datos en i:4 j:1-4
    def celda41 (self):
        self.bttnCelda4_1.setText("I:4, J:1")
        time.sleep(1)
        self.bttnCelda4_1.isEnable = False
    
    def celda42 (self):
        self.bttnCelda4_2.setText("I:4, J:2")
        time.sleep(1)
        self.bttnCelda4_2.isEnable = False

    def celda43 (self):
        self.bttnCelda4_3.setText("I:4, J:3")
        time.sleep(1)
        self.bttnCelda4_3.isEnable = False
    
    def celda44 (self):
        self.bttnCelda4_4.setText("I:4, J:4")
        time.sleep(1)
        self.bttnCelda4_4.isEnable = False


