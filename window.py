from PyQt5.QtWidgets import QMainWindow, QMessageBox
from layout import Ui_MainWindow
from backend import IpCalculator
from PyQt5.QtCore import pyqtSlot


class Window(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ip_calculator = IpCalculator()
        self.ui.calculatBtn.clicked.connect(self.on_btn_clicked)

    @pyqtSlot()
    def on_btn_clicked(self):
        ip_address = self.ui.ipAdressEdit.toPlainText()
        mask = self.ui.maskEdit.toPlainText()
        try:
            self.ip_calculator.ip_address = ip_address
            self.ip_calculator.mask = mask
            hosts = self.ip_calculator.get_addresses()
            self.ui.adresseCountDisplay.display(str(sum(1 for _x in hosts.hosts())))
            hosts_text = ""
            for host in hosts.hosts():
                print(host)
                hosts_text += f"{host}\n"
            self.ui.availableAddresseTexBox.setText(hosts_text)
            self.ui.broadcastAddress.setText(str(self.ip_calculator.get_broadcast()))
        except NameError as e:
            alert = QMessageBox()
            alert.setIcon(QMessageBox.Critical)
            alert.setText("Błąd")
            alert.setInformativeText(str(e))
            alert.setWindowTitle("Błąd")
            alert.setMinimumWidth(400)
            alert.exec_()
        except Exception as e:
            print(e)
