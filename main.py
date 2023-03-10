
import sys
from pathlib import Path

from PyQt6.QtCore import QDir, QSize
from PyQt6.QtWidgets import (QApplication, QDialog,
                             QErrorMessage, QFileDialog, QGridLayout,
                             QInputDialog, QLabel, QLineEdit, QPushButton)

class Dialog(QDialog):

    def __init__(self, parent=None):
        super(Dialog, self).__init__(parent)

        self.openFilesPath = ''

        self.errorMessageDialog = QErrorMessage(self)

        self.selectLabel = QLabel()
        self.selectButton = QPushButton("Выбрать файл")

        self.startLabel = QLabel()
        self.startButton = QPushButton("СТАРТ")

        self.stopLabel = QLabel()
        self.stopButton = QPushButton("СТОП")

        self.selectButton.clicked.connect(self.showDialog)
        self.startButton.clicked.connect(self.start)
        self.stopButton.clicked.connect(self.stop)

        layout = QGridLayout()
        layout.setColumnStretch(1, 1)
        layout.setColumnMinimumWidth(1, 250)
        layout.addWidget(self.selectButton, 0, 0)
        layout.addWidget(self.selectLabel, 0, 1)
        layout.addWidget(self.startButton, 2, 0)
        layout.addWidget(self.stopButton, 3, 0)

        self.setLayout(layout)

        self.setWindowTitle("Passenger counter")
        self.setFixedSize(QSize(1200, 400))

    def showDialog(self):

        home_dir = str(Path.home())
        fname = QFileDialog.getOpenFileName(self, 'Open file', home_dir)

        if fname[0]:
            f = open(fname[0], 'r')
            self.selectLabel.setText(f.name)

    def start(self):
        d, ok = QInputDialog.getDouble(self, "QInputDialog.getDouble()",
                "Amount:", 37.56, -10000, 10000, 2)
        if ok:
            self.doubleLabel.setText("$%g" % d)

    def stop(self):
        items = ("Spring", "Summer", "Fall", "Winter")

        item, ok = QInputDialog.getItem(self, "QInputDialog.getItem()",
                "Season:", items, 0, False)
        if ok and item:
            self.itemLabel.setText(item)

    def setText(self):
        text, ok = QInputDialog.getText(self, "QInputDialog.getText()",
                "User name:", QLineEdit.Normal, QDir.home().dirName())
        if ok and text != '':
            self.selectLabel.setText(text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = Dialog()
    dialog.show()
    sys.exit(app.exec())