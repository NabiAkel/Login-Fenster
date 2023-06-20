from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QSlider, QTextEdit, QTextBrowser, QGridLayout, QLabel, QPushButton, QLineEdit, \
    QApplication, QMessageBox


class CentralWidget(QWidget):
    def __init__(self, parent=None):
        super(CentralWidget, self).__init__(parent)

        self.buttenschliessen = QPushButton("Schliesen", self)
        self.buttenschliessen.clicked.connect(QApplication.instance().quit)

        self.label1 = QLabel(self)
        self.label1.setText("Benutzername")

        self.label2 = QLabel(self)
        self.label2.setText("Passwort")

        self.button = QPushButton("Login", self)
        self.button.clicked.connect(self.einlogin)

        self.textbox1 = QLineEdit(self)
        self.textbox1.move(20,20)

        self.textpasswort = QLineEdit(self)
        self.textpasswort.move(20, 20)
        self.textpasswort.setEchoMode(QLineEdit.EchoMode.Password)

        layout = QGridLayout(self)
        layout.addWidget(self.button, 3, 2)
        layout.addWidget(self.buttenschliessen, 3, 1)
        layout.addWidget(self.label1, 1, 1)
        layout.addWidget(self.label2, 2, 1)
        layout.addWidget(self.textbox1, 1, 2)
        layout.addWidget(self.textpasswort, 2, 2)

    def einlogin(self):
        if self.textpasswort.text() == "asd123" and self.textbox1.text() == "nabil":
            QMessageBox.information(self, "Titel", "success")
        else:
            QMessageBox.information(self, "Titel", "Passwort Falsch")