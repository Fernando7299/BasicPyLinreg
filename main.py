# -*- coding: utf-8 -*-
"""
License:      Apache License 2.0
"""


import sys

#Importar aquí las librerías a utilizar
import pandas as pd     # Librería para leer datos desde un archivo
import matplotlib.pyplot as plt     # Librería para graficar 
import numpy as np      # Librería para extender funcionalidades
########################################
from VentanaPrincipal import Ui_MainWindow
#######################################

from PyQt5 import QtWidgets

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    """
    Ventana Principal de la aplicación
    """
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        
        ###
        self.opcion = ["lineal", "exponencial"]
        self.colores = ['black',    'silver',    'red',        'sienna',     'moccasin',          'gold',
          'orange',   'salmon',    'chartreuse', 'green',      'mediumspringgreen', 'lightseagreen',
         'darkcyan', 'royalblue', 'blue',       'blueviolet', 'purple',            'fuchsia',
           'pink',     'tan',       'olivedrab',  'tomato',     'yellow',            'turquoise']
        self.markers = ["o", "x"]
        self.decod = {"UTF-8":"utf_8", "UTF-16":"utf_16", "UTF-16LE":"utf_16_le", "UTF-16BE":"utf_16_be"}
        self.separ = {"comas" : ",", "tabulación" : "\t"}
        self.tipoGrafica = ["Graficar puntos y curva", "Graficar puntos", "Graficar curva"]
        ###
        #Aquí van los botones
        self.Importar.clicked.connect(self.leerArchivo)
        self.Graficar.clicked.connect(self.botonGraficar)
        self.cargarDatos.clicked.connect(self.cargarData)
        self.CalDatos.clicked.connect(self.seleccion)
        self.choose.addItems(list(self.opcion))
        self.colorP.addItems(list(self.colores))
        self.colorC.addItems(list(self.colores))
        self.marcadores.addItems(list(self.markers))
        self.combograficar.addItems(list(self.tipoGrafica))
        
        
    
    def leerArchivo(self):
        filePath, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', __file__)
        if filePath !="":
            self.ejeX.clear()
            self.ejeY.clear()
            self.separacion.clear()
            self.decodificacion.clear()
            self.pagina.clear()
            self.pendiente.clear()
            self.independiente.clear()
            self.independienteerror.clear()
            self.pendienteerror.clear()
            self.correlacion.clear()
            self.destandarX.clear()
            self.destandarY.clear()
            self.covarianza.clear()
            if filePath.endswith(".csv"):
                self.separacion.addItems(list(self.separ.keys()))
                self.decodificacion.addItems(list(self.decod.keys()))
            elif filePath.endswith(".txt"):
                self.separacion.addItems(list(self.separ.keys()))
                self.decodificacion.addItems(list(self.decod.keys()))
            elif filePath.endswith(".xlsx"):
                self.data = pd.ExcelFile(str(filePath))
                self.pagina.addItems(list(self.data.sheet_names))
            self.ruta = str(filePath)
        else:
            return


    def cargarData(self):
        try:
            self.ejeX.clear()
            self.ejeY.clear()
            Ruta = self.ruta
            if Ruta !="":
                if Ruta.endswith(".xlsx"):
                    #return
                    self.df = self.data.parse(self.pagina.currentText())
                else:
                    self.df = pd.read_csv(str(Ruta), sep = self.separ.get(self.separacion.currentText()), encoding = self.decod.get(self.decodificacion.currentText()))
                
            self.ejeX.addItems(list(self.df.columns.values))
            self.ejeY.addItems(list(self.df.columns.values))
        except:
            return        
        

    def seleccion(self):
        try:
            if self.choose.currentText() == "lineal":
                x = np.array(self.df[str(self.ejeX.currentText())])
                y = np.array(self.df[str(self.ejeY.currentText())])
                m, b, Rsqr,errM, errB, DesEstX, DesEstY,Cov = self.calculoValores(x, y)
                self.pendiente.setText(str(round(m,5)))
                self.independiente.setText(str(round(b,5)))
                self.correlacion.setText(str(round(Rsqr,5)))
                self.pendienteerror.setText(str(round(errM, 7)))
                self.independienteerror.setText(str(round(errB,7)))
                self.destandarX.setText(str(round(DesEstX,5)))
                self.destandarY.setText(str(round(DesEstY,5)))
                self.covarianza.setText(str(round(Cov,5)))
                #self.calcularValoresLineal()

            elif self.choose.currentText() == "exponencial":
                x = np.array(self.df[str(self.ejeX.currentText())])
                y = np.log(np.array(self.df[str(self.ejeY.currentText())]))
                m, b, Rsqr,errM, errB, DesEstX, DesEstY,Cov = self.calculoValores(x, y)
                self.pendiente.setText(str(round(m,5)))
                self.independiente.setText(str(round(b,5)))
                self.correlacion.setText(str(round(Rsqr,5)))
                self.pendienteerror.setText(str(round(errM, 7)))
                self.independienteerror.setText(str(round(errB,7)))
                self.destandarX.setText(str(round(DesEstX,5)))
                self.destandarY.setText(str(round(DesEstY,5)))
                self.covarianza.setText(str(round(Cov,5)))
                #self.calcularValoresExp()
            return m,b
        except:
            return

    def botonGraficar(self):
        try:
            if self.combograficar.currentText() == "Graficar puntos y curva":
                self.graficaPuntosCurva()           
            elif self.combograficar.currentText() == "Graficar curva":
                self.graficaCurva()
            elif self.combograficar.currentText() == 'Graficar puntos':
                self.graficaPuntos()
        except:
            return
     

    def calculoValores(self, arregloX, arregloY):
        try:
            x = arregloX
            y = arregloY
            n = len(x)
            xyProm = sum(x*y)/n
            xProm = sum(x)/n
            yProm = sum(y)/n
            xSqrProm = sum(x*x)/n
            ySqrProm = sum(y*y)/n 
            #############################
            cov = xyProm - xProm*yProm
            desviacionX = (xSqrProm - xProm**2)**0.5
            desviacionY = (ySqrProm - yProm**2)**0.5
            #############################
            coefCorr = (cov/(desviacionX*desviacionY))**2
            pend = cov/desviacionX**2
            independ = sum(y)/len(y) - pend*sum(x)/len(x)
            #############################
            sum1 = 0
            sum2 = 0
            i = 0
            for n in x:
                sum1 += (y[i] + pend*x[i] - independ)**2
                sum2 += (x[i] + xProm)**2
                i += 1
            varM = ((sum1)/((n - 2)*(sum2)))**0.5
            varB = (((1/n) + ((xProm**2)/sum2))*(sum1/(n - 2)))**0.5

            return pend, independ, coefCorr, varM, varB, desviacionX, desviacionY, cov
        except:
            return
    
  
   
    def graficaPuntos(self):
        tamPuntos = self.tPuntos.value()
        opacidadPuntos = self.opacidadP.value()/100
        color = str(self.colorP.currentText())
        marcador = str(self.marcadores.currentText())
        x = self.df[str(self.ejeX.currentText())]
        y = self.df[str(self.ejeY.currentText())]
        plt.xlabel(str(self.ejeX.currentText()).capitalize())
        plt.ylabel(str(self.ejeY.currentText()).capitalize())
        plt.scatter(x,y, color = color, marker = marcador, s = tamPuntos, alpha = opacidadPuntos)
        plt.show()

    def graficaCurva(self):
        grosor = self.grosorC.value()
        opacidadCurva = self.opacidadC.value()/100
        color = str(self.colorC.currentText())
        plt.xlabel(str(self.ejeX.currentText()).capitalize())
        plt.ylabel(str(self.ejeY.currentText()).capitalize())
        if self.choose.currentText() == "lineal":
            z = np.array(self.df[str(self.ejeX.currentText())] )
            valormin = float(min(z))
            valormax = float(max(z))
            x = np.arange(valormin,valormax)
            m,b = self.seleccion()
            plt.plot(x, m*x+b,color = color, alpha = opacidadCurva, linewidth = grosor)  
            plt.show() 
        else:
            z = np.array(self.df[str(self.ejeX.currentText())] )
            valormin = float(min(z))
            valormax = float(max(z))
            x = np.arange(valormin,valormax, (valormax-valormin)/100)
            m,b = self.seleccion()
            plt.plot(x, (np.e**b)*np.e**(m*x), color = color, alpha = opacidadCurva, linewidth = grosor)
            plt.show()
         
    
    def graficaPuntosCurva(self):
        tamPuntos = self.tPuntos.value()
        grosor = self.grosorC.value()
        opacidadPuntos = self.opacidadP.value()/100
        opacidadCurva = self.opacidadC.value()/100
        colorpuntos = str(self.colorP.currentText())
        colorcurva = str(self.colorC.currentText())
        marcador = str(self.marcadores.currentText())
        x = self.df[str(self.ejeX.currentText())]
        y = self.df[str(self.ejeY.currentText())]
        plt.xlabel(str(self.ejeX.currentText()).capitalize())
        plt.ylabel(str(self.ejeY.currentText()).capitalize())
        plt.scatter(x,y, color = colorpuntos, marker = marcador, alpha = opacidadPuntos, s = tamPuntos)
        if self.choose.currentText() == "lineal":
            z = self.df[str(self.ejeX.currentText())]
            valormin = float(min(z))
            valormax = float(max(z))
            x = np.arange(valormin,valormax)
            m,b = self.seleccion()
            plt.plot(x, m*x + b, color = colorcurva, alpha = opacidadCurva, linewidth = grosor)   
            plt.show()  
        else:
            z = np.array(self.df[str(self.ejeX.currentText())] )
            valormin = float(min(z))
            valormax = float(max(z))
            x = np.arange(valormin,valormax, (valormax-valormin)/100)
            m,b = self.seleccion()
            plt.plot(x, (np.e**b)*np.e**(m*x), color = colorcurva, alpha = opacidadCurva, linewidth = grosor)
            plt.show()
    

    
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
