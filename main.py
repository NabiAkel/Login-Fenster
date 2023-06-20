#Erstellen Sie ein Login-Fenster in PyQt, welches folgende Elemnte enthält:
#1. zwei Labels mit den Bezeichnungen Benutzername und Passwort.
#2. zwei Eingabefelder für den Benutzernamen und das Passwort
#3. einen Button zum Ausführen des Logins

#Verwenden Sie ein Gridlayout um die Elemente der GUI anzuordnen.

#für schnelle Programmierer:
#- Setzen Sie den Modus für das Eingabefeld das Passworts so, dass * oder Punkte statt den Zeichen angezeigt werden
#- Hinterlegen Sie einen festen Benutzernamen und ein festes Passwort im Quelltext. Stimmen  die festen Werte mit der Benutzereingabe überein, geben Sie print("szcces ") aus.
from PyQt6.QtWidgets import QApplication
from MainWindow import MainWindow
import sys

# All you need is http:/doc.gt.io/gtforpython-6/
if __name__ == '__main__':
    application = QApplication(sys.argv)

    main_window = MainWindow()
    main_window.show()

    application.exec()
