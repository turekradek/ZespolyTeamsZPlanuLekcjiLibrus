from PyQt5 import QtCore, QtGui, QtWidgets
import nauczyciele


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(829, 671)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tekst1 = QtWidgets.QLabel(self.centralwidget)
        self.tekst1.setGeometry(QtCore.QRect(10, 10, 401, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.tekst1.setFont(font)
        self.tekst1.setStyleSheet(
            "QLabel{\n"
            "   \n"
            "    background-color: rgb(182, 255, 171);\n"
            "    border: 2px solid green;\n"
            "    border-radius: 20px;\n"
            "}\n"
            "QLabel:hover{\n"
            "    background-color: rgb(45, 225, 34);\n"
            "    border: 4px solid green;\n"
            "}"
        )
        self.tekst1.setObjectName("tekst1")
        self.tekst2 = QtWidgets.QLabel(self.centralwidget)
        self.tekst2.setGeometry(QtCore.QRect(420, 10, 401, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.tekst2.setFont(font)
        self.tekst2.setStyleSheet(
            "QLabel{\n"
            "background-color: rgb(155, 212, 255);\n"
            "border: 2px solid blue;\n"
            "}\n"
            "QLabel:hover{\n"
            "    background-color: rgb(55, 182, 255);\n"
            "    border: 4px solid blue;\n"
            "}"
        )
        self.tekst2.setObjectName("tekst2")
        self.combonauczyciel = QtWidgets.QComboBox(
            self.centralwidget,
            editable=False,
        )
        self.combonauczyciel.setGeometry(QtCore.QRect(10, 80, 401, 61))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.combonauczyciel.setFont(font)
        self.combonauczyciel.setStyleSheet(
            "\n"
            "QComboBox{\n"
            "background-color: rgb(163, 255, 129);\n"
            "border: 3px solid green;\n"
            "}\n"
            "QComboBox:hover{\n"
            "    background-color:rgb(163, 255, 89);\n"
            "    border: 1px solid green;\n"
            "    font-size: 16px;\n"
            "}"
        )
        self.combonauczyciel.setObjectName("combonauczyciel")

        nauczyciele_n = nauczyciele.nauczyciele_lista()  ########
        self.combonauczyciel.addItems(nauczyciele_n)
        self.comboklasy = QtWidgets.QComboBox(
            self.centralwidget,
            editable=False,
        )
        self.comboklasy.setGeometry(QtCore.QRect(420, 80, 401, 61))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.comboklasy.setFont(font)
        self.comboklasy.setStyleSheet(
            "QComboBox{\n"
            "background-color:  rgb(107, 96, 255);\n"
            "border: 3px solid blue;\n"
            "}\n"
            "QComboBox:hover{\n"
            "    background-color: rgb(55, 182, 255);\n"
            "    border: 1px solid blue;\n"
            "}"
        )
        self.comboklasy.setObjectName("comboklasy")
        klasy = nauczyciele.klasy_lista()  ########
        self.comboklasy.addItems(klasy)
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(10, 200, 401, 251))
        self.textBrowser.setPlaceholderText(
            "Tutaj poka???? si?? lekcje wybranego nauczyciela:"
        )
        self.textBrowser.setStyleSheet(
            "QTextBrowser{\n"
            "    background-color: rgb(227, 227, 227);\n"
            "    font-size: 14px;\n"
            "\n"
            "}"
        )
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(420, 200, 401, 251))
        self.textBrowser_2.setPlaceholderText(
            "Tutaj poka???? si?? lekcje wybranej klasy :"
        )

        self.textBrowser_2.setStyleSheet(
            "QTextBrowser{\n"
            "    background-color: rgb(227, 227, 227);\n"
            "    font-size: 14px;\n"
            "\n"
            "}"
        )
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(240, 470, 131, 51))
        self.lcdNumber.setObjectName("lcdNumber")
        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_2.setGeometry(QtCore.QRect(650, 470, 131, 51))
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 470, 111, 41))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(490, 480, 111, 41))
        self.label_2.setObjectName("label_2")

        self.pushButton = QtWidgets.QPushButton(
            self.centralwidget,
            clicked=lambda: self.do_pliku(f"{self.textEdit.toPlainText()}"),
        )
        # powy??ej
        self.pushButton.setGeometry(QtCore.QRect(650, 560, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(
            "QPushButton{\n"
            "    background-color: rgb(255, 35, 57);\n"
            "    font-size: 20px;\n"
            "\n"
            "}\n"
            "\n"
            "QPushButton:hover{\n"
            "background-color: rgb(255, 0, 0);\n"
            "font-size: 26px;\n"
            "}"
        )
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 560, 311, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(390, 560, 231, 41))
        self.textEdit.setStyleSheet("QTextEdit{font-size: 16px;}")

        self.textEdit.setObjectName("textEdit")
        self.textEdit.setPlaceholderText("nazwa pliku z poleceniami")

        self.pushButton_2 = QtWidgets.QPushButton(
            self.centralwidget,
            clicked=lambda: self.press_it(f"{self.combonauczyciel.currentText()}"),
        )
        self.pushButton_2.setGeometry(QtCore.QRect(130, 150, 121, 41))
        self.pushButton_2.setStyleSheet(
            "QPushButton{\n"
            "background-color: rgb(163, 255, 129);\n"
            "border: 3px solid green;\n"
            "}\n"
            "QPushButton:hover{\n"
            "    background-color:rgb(163, 255, 89);\n"
            "    border: 1px solid green;\n"
            "    font-size: 16px;\n"
            "}"
        )
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(
            self.centralwidget,
            clicked=lambda: self.press_it2(f"{self.comboklasy.currentText()}"),
        )
        self.pushButton_3.setGeometry(QtCore.QRect(560, 150, 121, 41))
        self.pushButton_3.setStyleSheet(
            "QPushButton{\n"
            "background-color:  rgb(107, 96, 255);\n"
            "border: 3px solid blue;\n"
            "}\n"
            "QPushButton:hover{\n"
            "    background-color: rgb(55, 182, 255);\n"
            "    border: 1px solid blue;\n"
            "    font-size: 16px;\n"
            "}"
        )
        self.pushButton_3.setObjectName("pushButton_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 829, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def press_it(self, pressed):
        a = nauczyciele.lekcje_nauczyciela(pressed)
        self.textBrowser.setText(a)
        ile = nauczyciele.ile_lekcji_na_tydzien(pressed)
        self.lcdNumber.display(ile)

    def press_it2(self, pressed):
        a = nauczyciele.lekcje_poindeksie(pressed)
        self.textBrowser_2.setText(a[0])
        ile = a[1]
        self.lcdNumber_2.display(ile)

    def do_pliku(self, pressed):
        nauczyciele.polecenia_do_pliku(pressed)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tekst1.setText(_translate("MainWindow", "Wybierz nauczyciela "))
        self.tekst2.setText(_translate("MainWindow", "Wybierz klas?? "))
        self.label.setText(_translate("MainWindow", "lekcje nauczyciela"))
        self.label_2.setText(_translate("MainWindow", "lekcje klasy"))
        self.pushButton.setText(_translate("MainWindow", "zapis"))
        self.label_3.setText(
            _translate(
                "MainWindow", "podaj nazwe pliku w jakim chcesz zapisac polecenia "
            )
        )
        self.pushButton_2.setText(_translate("MainWindow", "Pokaz lekcje"))
        self.pushButton_3.setText(_translate("MainWindow", "Pokaz lekcje"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
