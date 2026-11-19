import sys 
from PyQt5 import QtWidgets, uic

class ContadorPalabras(QtWidgets.QMainWindow):
      
    def __init__(self):
        super().__init__()
        #Carga de nuestra vista
        uic.loadUi("contadorPalabras.ui",self)
        self.btnContar.clicked.connect(self.ContarPalabras)
        

    def ContarPalabras(self):
        # Recuperar el texto ✅
        texto = self.edtCaracteres.text()
        
        # Separar las palabras ✅
        textoSeparado = texto.split()
        
        # Contar las palabras✅
        cantidadPalabras = len(textoSeparado)
        self.tvPalabras.setText(f"Palabras:{cantidadPalabras}")
        
        # Contar los caracteres ✅
        totalCaracteres = 0
        for palabra in textoSeparado:
            totalCaracteres += len(palabra)
        self.tvCaracteres.setText(f"Caracteres: {totalCaracteres}")
        
        # aqui abajo lógica
        if cantidadPalabras >= 20:
            self.tvPalabras.setStyleSheet("font: 11pt 'MS Shell Dlg 2'; color: #ff756b")
        else: 
            self.tvPalabras.setStyleSheet("font: 11pt 'MS Shell Dlg 2'; color: #000000")
            
        if totalCaracteres >= 120:
            self.tvCaracteres.setStyleSheet("font: 11pt 'MS Shell Dlg 2'; color: #ff756b")
        else: 
            self.tvCaracteres.setStyleSheet("font: 11pt 'MS Shell Dlg 2'; color: #000000")
            


app = QtWidgets.QApplication(sys.argv)
ventana = ContadorPalabras()
ventana.show()
sys.exit(app.exec())