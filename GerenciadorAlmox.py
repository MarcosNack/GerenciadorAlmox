# pyinstaller.exe --onefile --windowed --icon=icone.ico GerenciadorAlmox.py

from PySide6.QtWidgets import QApplication
from controllers.interface import MainWindow
import sys


if __name__ == '__main__':    
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())