from PyQt6.QtWidgets import QMainWindow
from CentralWidget import CentralWidget

class MainWindow(QMainWindow):
 def __init__(self, parent=None):
  super(MainWindow, self).__init__(parent)


   #Text für die Titelleiste des QMainWindows
  self.setWindowTitle("Einführung ins QMainWindow")

  #Setzt die Größe des Fensters auf feste Werte
   # self.setFixedWidth(800)
   # self.serFixedHeight(600)

  self.setMinimumWidth(480)
  self.setMinimumHeight(600)

  self.setMaximumWidth(800)
  self.setMaximumHeight(1024)

  central_widget = CentralWidget(self)
  self.setCentralWidget(central_widget)