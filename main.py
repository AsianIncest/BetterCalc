#pyuic5 -x MainWindow.ui -o main_window.py
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QInputDialog, QMessageBox

from main_window import Ui_MainWindow
import sys
from bet_match import *

class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ApplicationWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

def button_add_click():
    x, _ = QInputDialog.getText(None, "BetterCalc", "Введите коэффициент.\n")
    if calc.testFloat(x):
        ui.listWidget.addItem(x)
    else:
        msg = QMessageBox()
        msg.setText("Неверный коэффициент, требуется целое либо вещественное.\nПример: 1.2")
        msg.setWindowTitle("BetterCalc")
        msg.setIcon(QMessageBox.Critical)
        msg.exec_()


def button_del_click():
    si = ui.listWidget.selectedItems()
    if len(si) == 0:
        return
    x = ui.listWidget.takeItem(ui.listWidget.indexFromItem(si[0]).row())

def button_clear_click():
    for _ in range(ui.listWidget.count()):
        ui.listWidget.takeItem(0)
    ui.textMarja.setText("0")

def button_marja_click():
    items = [ui.listWidget.item(i).text() for i in range(ui.listWidget.count())]
    calc.clearK()
    for i in items:
        calc.addK(i)
    m = calc.calcMarja()
    ui.textMarja.setText(str(m) if m != False else "0")

def button_calc_click():
    pass

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
calc = BetMatch()
###############################################
ui.button_add.clicked.connect(button_add_click)
ui.button_delete.clicked.connect(button_del_click)
ui.button_clear.clicked.connect(button_clear_click)
ui.button_marja.clicked.connect(button_marja_click)
ui.button_calc.clicked.connect(button_calc_click)
###############################################
MainWindow.show()
sys.exit(app.exec_())


