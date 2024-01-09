#Modulos o paquetes propios de python 
import time

import sys
import typing
from PyQt5 import QtCore
# modulos o paquetes de pyqt5
# from PyQt5 import QtGui
# from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QDialog, QWidget
from PyQt5.uic import loadUi

class DlgPrincipal(QDialog):
    def __init__(self,registro):
        super(DlgPrincipal, self).__init__()
        loadUi('appescritorio/principal_deec_crud.ui',self)
        self.lbUsuario.setText(registro[0][0])
        colunas = ['id','usuario','clave','correo']
        #self.btlUsuarios.add(columnas)