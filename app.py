import sys
from PyQt5.QtWidgets import QApplication 
from controller.Login import Login 



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Login()
    app.exec()
