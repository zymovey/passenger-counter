
import sys
from pathlib import Path

from PyQt6.QtCore import QDir, Qt, QSize, QFileInfo
from PyQt6.QtWidgets import (QApplication, QCheckBox, QColorDialog, QDialog,
        QErrorMessage, QFileDialog, QFontDialog, QFrame, QGridLayout,
        QInputDialog, QLabel, QLineEdit, QMessageBox, QPushButton)

class Dialog(QDialog):
    MESSAGE = "<p>Message boxes have a caption, a text, and up to three " \
            "buttons, each with standard or custom texts.</p>" \
            "<p>Click a button to close the message box. Pressing the Esc " \
            "button will activate the detected escape button (if any).</p>"

    def __init__(self, parent=None):
        super(Dialog, self).__init__(parent)

        self.openFilesPath = ''

        self.errorMessageDialog = QErrorMessage(self)

        #frameStyle = QFrame.Sunken | QFrame.Panel

        self.selectLabel = QLabel()
        #self.integerLabel.setFrameStyle(frameStyle)
        self.selectButton = QPushButton("Выбрать файл")

        self.startLabel = QLabel()
        #self.doubleLabel.setFrameStyle(frameStyle)
        self.startButton = QPushButton("СТАРТ")

        self.stopLabel = QLabel()
        #self.itemLabel.setFrameStyle(frameStyle)
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
            #with f:
                #data = f.read()
                #self.selectLabel.setText(data)
                #self.selectLabel.setText(F)
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

                #self.textEdit.setText(data)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = Dialog()
    dialog.show()
    sys.exit(app.exec())