# @autor : Kevin Yesid Vasquez
# @fecha : 24 octubre 2023
# @ficha : 2740559 
# @Description : programa principal para el aplicativo de escritorio

#Modulos o paquetes propios de python 
from fileinput import close
import time

from modulobm.bmkyvcesc import DlgBuscaminas as dlgbm

# modulos o paquetes de pyqt5
# from PyQt5 import QtGui
# from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi

import sys

# Clase para implemntar la funcionalidad de la ventana de dialogon para un el inicio de sesion 
class DlgInicio(QDialog):
    def __init__(self):
        super(DlgInicio, self).__init__()
        loadUi('appescritorio/inicio_sesion.ui', self)

        self.bttnInicio.clicked.connect(self.inicio)

    # Funcion que se ejecuta al presionar el boton inicio
    def inicio(self):
        # print("Se ha precionado el boton 'bttnInicio'")
        # print(self.txtUsuario.text())
        # print(self.txtClave.text())
        usuario = self.txtUsuario.text()
        clave = self.txtClave.text()
        
        principaldeec = connector.connet(host="localhost", user="root", password="Evenat1123*")
        micursor=principaldeec.cursor()
        principaldeec.execute("SELECT usuario,clave, FROM usuarios Were usuario = '"+usuario +"'AND clave='"+clave +"'")
        registro = micursor.fetchall()


        #validar que los campos no esten vacios 
        if registroÑ
            usu = registro[0][0]
            cl = registro [0][1]
            cadena = "usuario: "+ usu + "\ncontraseña: " + cl 
            #self.lbMensaje.style = "color: #00ff00"
            self.lblMensaje.setTex(cadena+ "\nUsuario y Contraseña correctas..")
            self.ppal= DlgPrincipal(registro)
            self.ppal.show()
            DlgInicio.close()
        
        else:
            self.lblMensaje.setTex("usuario o contraseña incorrectas")


        # if usuario == "david" and clave == "root":
            # cadena = "Usuario: " + usuario + "\nContraseña: " + clave
            # self.lblMensaje.setText(cadena + "\nUsuario y contraseña correctas ...")
           ## implementar la funcionalidad para llamar la ventana buscaminas 
            # self.Windowsbm = dlgbm()
            # self.Windowsbm.show()
            # objDialogo.close()
        # else:
            # self.lblMensaje.setText("Usuario y contraseña Incorrectas...")
            # time.sleep(5)
            # self.lblMensaje.setText("")
           

# Programa principalw
app = QApplication(sys.argv)
objDialogo = DlgInicio()# objDialogo: objeto
objDialogo.show()
sys.exit(app.exec_()) 