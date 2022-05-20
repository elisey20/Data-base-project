import sys, os
from PyQt6 import QtWidgets
from windows import design


class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.Button.clicked.connect(self.browse_folder)

    def browse_folder(self):
        self.listWidget.clear()
        directory = QtWidgets.QFileDialog.getExistingDirectory(self, "Выберите папку")

        if directory:
            self.listWidget.addItems(os.listdir(directory))


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    window.show()

    app.exec()


if __name__ == "__main__":
    main()
