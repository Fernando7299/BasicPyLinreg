# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 500)
        MainWindow.setMinimumSize(QtCore.QSize(1024, 500))
        MainWindow.setMaximumSize(QtCore.QSize(1024, 500))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Importar = QtWidgets.QPushButton(self.centralwidget)
        self.Importar.setGeometry(QtCore.QRect(20, 10, 301, 81))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.Importar.setFont(font)
        self.Importar.setObjectName("Importar")
        self.ejeX = QtWidgets.QComboBox(self.centralwidget)
        self.ejeX.setGeometry(QtCore.QRect(100, 340, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.ejeX.setFont(font)
        self.ejeX.setObjectName("ejeX")
        self.ejeY = QtWidgets.QComboBox(self.centralwidget)
        self.ejeY.setGeometry(QtCore.QRect(100, 390, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.ejeY.setFont(font)
        self.ejeY.setObjectName("ejeY")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 340, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 390, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(370, 110, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(370, 160, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(370, 210, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.pendiente = QtWidgets.QTextBrowser(self.centralwidget)
        self.pendiente.setGeometry(QtCore.QRect(420, 110, 91, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pendiente.sizePolicy().hasHeightForWidth())
        self.pendiente.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pendiente.setFont(font)
        self.pendiente.setObjectName("pendiente")
        self.independiente = QtWidgets.QTextBrowser(self.centralwidget)
        self.independiente.setGeometry(QtCore.QRect(420, 160, 91, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.independiente.sizePolicy().hasHeightForWidth())
        self.independiente.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.independiente.setFont(font)
        self.independiente.setObjectName("independiente")
        self.correlacion = QtWidgets.QTextBrowser(self.centralwidget)
        self.correlacion.setGeometry(QtCore.QRect(420, 210, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.correlacion.setFont(font)
        self.correlacion.setObjectName("correlacion")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(340, 10, 16, 451))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.colorP = QtWidgets.QComboBox(self.centralwidget)
        self.colorP.setGeometry(QtCore.QRect(850, 10, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(11)
        self.colorP.setFont(font)
        self.colorP.setObjectName("colorP")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(680, 10, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(680, 60, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.colorC = QtWidgets.QComboBox(self.centralwidget)
        self.colorC.setGeometry(QtCore.QRect(850, 60, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.colorC.setFont(font)
        self.colorC.setObjectName("colorC")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(680, 110, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(680, 160, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(680, 210, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.opacidadP = QtWidgets.QSlider(self.centralwidget)
        self.opacidadP.setGeometry(QtCore.QRect(850, 120, 160, 22))
        self.opacidadP.setMinimum(1)
        self.opacidadP.setMaximum(100)
        self.opacidadP.setProperty("value", 100)
        self.opacidadP.setOrientation(QtCore.Qt.Horizontal)
        self.opacidadP.setInvertedAppearance(True)
        self.opacidadP.setInvertedControls(False)
        self.opacidadP.setObjectName("opacidadP")
        self.opacidadC = QtWidgets.QSlider(self.centralwidget)
        self.opacidadC.setGeometry(QtCore.QRect(850, 170, 160, 22))
        self.opacidadC.setMinimum(1)
        self.opacidadC.setMaximum(100)
        self.opacidadC.setProperty("value", 100)
        self.opacidadC.setOrientation(QtCore.Qt.Horizontal)
        self.opacidadC.setInvertedAppearance(True)
        self.opacidadC.setObjectName("opacidadC")
        self.marcadores = QtWidgets.QComboBox(self.centralwidget)
        self.marcadores.setGeometry(QtCore.QRect(850, 210, 151, 31))
        self.marcadores.setObjectName("marcadores")
        self.CalDatos = QtWidgets.QPushButton(self.centralwidget)
        self.CalDatos.setGeometry(QtCore.QRect(390, 20, 231, 51))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.CalDatos.setFont(font)
        self.CalDatos.setObjectName("CalDatos")
        self.choose = QtWidgets.QComboBox(self.centralwidget)
        self.choose.setGeometry(QtCore.QRect(20, 430, 291, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.choose.setFont(font)
        self.choose.setEditable(False)
        self.choose.setObjectName("choose")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(20, 110, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(20, 150, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.cargarDatos = QtWidgets.QPushButton(self.centralwidget)
        self.cargarDatos.setGeometry(QtCore.QRect(20, 260, 291, 41))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.cargarDatos.setFont(font)
        self.cargarDatos.setObjectName("cargarDatos")
        self.separacion = QtWidgets.QComboBox(self.centralwidget)
        self.separacion.setGeometry(QtCore.QRect(170, 110, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.separacion.setFont(font)
        self.separacion.setObjectName("separacion")
        self.decodificacion = QtWidgets.QComboBox(self.centralwidget)
        self.decodificacion.setGeometry(QtCore.QRect(170, 150, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.decodificacion.setFont(font)
        self.decodificacion.setObjectName("decodificacion")
        self.pagina = QtWidgets.QComboBox(self.centralwidget)
        self.pagina.setGeometry(QtCore.QRect(120, 210, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pagina.setFont(font)
        self.pagina.setEditable(False)
        self.pagina.setObjectName("pagina")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(20, 210, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(10, 310, 321, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.Graficar = QtWidgets.QPushButton(self.centralwidget)
        self.Graficar.setGeometry(QtCore.QRect(700, 390, 301, 81))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.Graficar.setFont(font)
        self.Graficar.setAccessibleDescription("")
        self.Graficar.setObjectName("Graficar")
        self.pendienteerror = QtWidgets.QTextBrowser(self.centralwidget)
        self.pendienteerror.setGeometry(QtCore.QRect(540, 110, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pendienteerror.setFont(font)
        self.pendienteerror.setObjectName("pendienteerror")
        self.independienteerror = QtWidgets.QTextBrowser(self.centralwidget)
        self.independienteerror.setGeometry(QtCore.QRect(540, 160, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.independienteerror.setFont(font)
        self.independienteerror.setObjectName("independienteerror")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(650, 10, 16, 451))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.combograficar = QtWidgets.QComboBox(self.centralwidget)
        self.combograficar.setGeometry(QtCore.QRect(700, 330, 301, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.combograficar.setFont(font)
        self.combograficar.setObjectName("combograficar")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(680, 250, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.grosorC = QtWidgets.QSlider(self.centralwidget)
        self.grosorC.setGeometry(QtCore.QRect(850, 260, 160, 22))
        self.grosorC.setMinimum(1)
        self.grosorC.setMaximum(50)
        self.grosorC.setProperty("value", 3)
        self.grosorC.setSliderPosition(3)
        self.grosorC.setOrientation(QtCore.Qt.Horizontal)
        self.grosorC.setInvertedAppearance(False)
        self.grosorC.setObjectName("grosorC")
        self.tPuntos = QtWidgets.QSlider(self.centralwidget)
        self.tPuntos.setGeometry(QtCore.QRect(850, 300, 160, 22))
        self.tPuntos.setMinimum(1)
        self.tPuntos.setMaximum(200)
        self.tPuntos.setProperty("value", 10)
        self.tPuntos.setOrientation(QtCore.Qt.Horizontal)
        self.tPuntos.setInvertedAppearance(False)
        self.tPuntos.setObjectName("tPuntos")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(680, 290, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.destandarX = QtWidgets.QTextBrowser(self.centralwidget)
        self.destandarX.setGeometry(QtCore.QRect(540, 280, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.destandarX.setFont(font)
        self.destandarX.setObjectName("destandarX")
        self.destandarY = QtWidgets.QTextBrowser(self.centralwidget)
        self.destandarY.setGeometry(QtCore.QRect(540, 330, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.destandarY.setFont(font)
        self.destandarY.setObjectName("destandarY")
        self.covarianza = QtWidgets.QTextBrowser(self.centralwidget)
        self.covarianza.setGeometry(QtCore.QRect(470, 380, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.covarianza.setFont(font)
        self.covarianza.setObjectName("covarianza")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(370, 280, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(370, 330, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(380, 380, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(380, 250, 251, 16))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(560, 80, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Linreg v.0.1.0"))
        self.Importar.setText(_translate("MainWindow", "Importar "))
        self.label.setText(_translate("MainWindow", "Eje X"))
        self.label_2.setText(_translate("MainWindow", "Eje Y"))
        self.label_3.setText(_translate("MainWindow", "m"))
        self.label_4.setText(_translate("MainWindow", "b"))
        self.label_5.setText(_translate("MainWindow", "r^2"))
        self.label_6.setText(_translate("MainWindow", "Color (puntos)"))
        self.label_7.setText(_translate("MainWindow", "Color (curva)"))
        self.label_8.setText(_translate("MainWindow", "Opacidad (puntos)"))
        self.label_9.setText(_translate("MainWindow", "Opacidad (curva)"))
        self.label_10.setText(_translate("MainWindow", "Marcador (puntos)"))
        self.CalDatos.setText(_translate("MainWindow", "Calcular datos"))
        self.label_11.setText(_translate("MainWindow", "Separación"))
        self.label_12.setText(_translate("MainWindow", "Decodificación"))
        self.cargarDatos.setText(_translate("MainWindow", "Cargar Datos"))
        self.label_13.setText(_translate("MainWindow", "Pagina"))
        self.Graficar.setText(_translate("MainWindow", "Graficar"))
        self.label_14.setText(_translate("MainWindow", "Grosor (curva)"))
        self.label_15.setText(_translate("MainWindow", "Tamaño (puntos)"))
        self.label_16.setText(_translate("MainWindow", "Desviacion Estandar \"x\""))
        self.label_17.setText(_translate("MainWindow", "Desviacion Estandar \"y\""))
        self.label_18.setText(_translate("MainWindow", "Covarianza"))
        self.label_19.setText(_translate("MainWindow", "Errores"))

