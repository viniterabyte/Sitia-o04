from PySide6 import QtWidgets
from PySide6.QtUiTools import QUiLoader
from ModuloInserir import inserir
from ModuloConverterData import converterData

class TelaPrincipal(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        carregador = QUiLoader()
        self.tela = carregador.load("Tela.ui")
        self.componentes()
    
    def componentes(self):
        self.caixaCorrente = self.tela.findChild(QtWidgets.QLineEdit, "caixaCorrente")
        self.caixaValor = self.tela.findChild(QtWidgets.QLineEdit, "caixaValor")
        self.caixaCategoria = self.tela.findChild(QtWidgets.QComboBox, "caixaCategoria")
        self.caixaData = self.tela.findChild(QtWidgets.QDateEdit, "caixaData")
        self.dep = self.tela.findChild(QtWidgets.QLineEdit, "dep")
        self.btnEnviar = self.tela.findChild(QtWidgets.QPushButton, "btnEnviar")
        self.btnEnviar.clicked.connect(self.cadastrarFinancas)
        
        

    def cadastrarFinancas(self):
        tipo = self.caixaCorrente.text()
        data = self.caixaData.text()
        cate = self.caixaCategoria.currentText()
        val = self.caixaValor.text()
        desc = self.dep.text()
        inserir(tipo, desc, val, cate, converterData(data))

    
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    interface = TelaPrincipal()
    interface.tela.showMaximized()
    app.exec()