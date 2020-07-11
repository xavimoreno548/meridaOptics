import sys
import json

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QTableWidget, QTableWidgetItem, QInputDialog, \
    QMessageBox
from PyQt5 import uic

import zerorpc


# MAIN WINDOW UI
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi("./client.ui", self)

        self.updateButton = self.findChild(QPushButton, "updateButton")
        self.updateButton.clicked.connect(self.onUpdateButtonClick)

        self.removeButton = self.findChild(QPushButton, "removeButton")
        self.removeButton.clicked.connect(self.onRemoveButtonClick)

        self.addButton = self.findChild(QPushButton, "addButton")
        self.addButton.clicked.connect(self.onAddButtonClick)

        self.dataTable = self.findChild(QTableWidget, "dataTable")

        self.show()
        self.onUpdateButtonClick()

    def onUpdateButtonClick(self):
        res = TCPClient.getAll()
        self.updateTable(res)

    def onRemoveButtonClick(self):
        id = self.getSelectedId()

        if (id):
            num, ok = QInputDialog.getInt(self, "Modificación", "Ingrese el numero para modificar en inventario")
            if (ok):
                res = TCPClient.remove(id, num)
                self.updateTable(res)
        else:
            QMessageBox.warning(self, "Alerta", "Seleccione primero el producto que desee modificar")

    def onAddButtonClick(self):
        id = self.getSelectedId()

        if (id):
            num, ok = QInputDialog.getInt(self, "Modificación", "Ingrese el numero para modificar en inventario")
            if (ok):
                res = TCPClient.insert(id, num)
                self.updateTable(res)
        else:
            QMessageBox.warning(self, "Alerta", "Seleccione primero el producto que desee modificar")

    def updateTable(self, data):
        self.dataTable.clearContents()
        self.dataTable.setRowCount(0)
        self.dataTable.clearSelection()

        row = 0
        for producto in data:
            self.dataTable.insertRow(row)
            col = 0
            for key, value in producto.items():
                item = QTableWidgetItem(str(value))
                self.dataTable.setItem(row, col, item)
                col += 1
            row += 1

    def getSelectedId(self):
        selection = self.dataTable.selectionModel()
        id = None

        if (selection.hasSelection()):
            row = selection.selectedRows()[0].row()
            id = int(self.dataTable.item(row, 0).text())

        self.dataTable.clearSelection()
        return id


# MAIN
if __name__ == "__main__":
    TCPClient = zerorpc.Client()
    TCPClient.connect("tcp://127.0.0.1:4242")

    app = QApplication(sys.argv)
    mainWindow = MainWindow()

    app.exec_()
