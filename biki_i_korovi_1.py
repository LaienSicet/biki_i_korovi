from random import choice
from PyQt5 import QtCore, QtGui, QtWidgets


gg = 0 #маркер завершения игры
p = 0 #попытки
ohi = "" # ошибки и вообще тех. строка
a = 0 #загаданное число
stroka = "" # история
hislo = 0 # число знаков
hislo_kolor = 0 # число цветов
bik = "" # быки
kor = "" # коровы
kolor_0 = ["", "grey", "red", "yellow", "green", "blue", "purple", "white", "black"] # база цветов

def kno(l, m):
    'кнопки изменения цветов кнопок'
    global mat_kolo
    if mat_kolo[l][m] < len(kolor)-1:
        mat_kolo[l][m] += 1
    else:
        mat_kolo[l][m] = 0
    ui.setupUi(MainWindow)
    ui.textBrowser.setText(stroka)
    ui.label_2.setText(f"быков: {bik}")
    ui.label_3.setText(f"коров: {kor}")
    if len(q) != 1:
        ui.label.setText(f"так.... вообще, есть {len(q)} вариантов.")
    else:
        ui.label.setText("всё же очевидно. всего 1(один) вариант остался!!!")

def del_raz():
    global mat_kolo
    mat_kolo = [[0 for i in range(10)] for j in range(hislo)]
    ui.setupUi(MainWindow)
    ui.textBrowser.setText(stroka)
    ui.label_2.setText(f"быков: {bik}")
    ui.label_3.setText(f"коров: {kor}")
    if len(q) != 1:
        ui.label.setText(f"так.... вообще, есть {len(q)} вариантов.")
    else:
        ui.label.setText("всё же очевидно. всего 1(один) вариант остался!!!")


def nohalo():
    'кнопка "начало".'
    global q, a, hislo, stroka, ohi, gg, p, matri, mat_kolo, hislo_kolor, kolor
    hislo = ui.spinBox.value()
    matri = [[i for i in range(10)] for j in range(hislo)]
    mat_kolo = [[0 for i in range(10)] for j in range(hislo)]
    hislo_kolor = ui.spinBox_2.value()
    kolor = kolor_0[:hislo_kolor:]
    q = [str(i).rjust(hislo, "0") for i in range(10 ** hislo)]
    a = str(choice(q))
    stroka = ""
    ohi = "начали!!!"
    gg = 0
    p = 0
    ui.setupUi(MainWindow)


def proverka():
    'кнопка "проверка".'
    global ohi, p, gg, stroka, bik, kor
    ui.label.setText("")
    if a == 0:
        ohi = "нечего проверять. число не загадано."
        ui.label.setText(ohi)
        return False
    b = ui.textEdit.toPlainText()
    if len(b) != hislo:
        ohi = f"длина загаданного числа ({hislo} знак.)"
        ui.label.setText(ohi)
        return False
    elif b.isdigit() != True:
        ohi = "число должно содержать исключительно цифры."
        ui.label.setText(ohi)
        return False
    if gg == 1:
        ohi = "уже разгаданно."
        ui.label.setText(ohi)
        return False
    p += 1
    if a == b:
        ui.label.setText(f"             победа! c {p} попытки.")
        gg = 1
    bik = 0
    kor = 0
    for i, n in enumerate(b):
        if n == a[i]:
            bik += 1
        elif n in a:
            kor += 1
    q1 = q.copy()
    for m in q1:
        bik1 = 0
        kor1 = 0
        for i, n in enumerate(b):
            if n == m[i]:
                bik1 += 1
            elif n in m:
                kor1 += 1
        if bik != bik1 or kor != kor1:
            q.remove(m)
    if gg == 0:
        ui.label_2.setText(f"быков: {bik}")
        ui.label_3.setText(f"коров: {kor}")
        if len(q) != 1:
            ui.label.setText(f"так.... вообще, есть {len(q)} вариантов.")
        else:
            ui.label.setText("всё же очевидно. всего 1(один) вариант остался!!!")

    stroka += f"число:   {b}     |    быков: {bik},     коров: {kor}.    |     есть {len(q)} вариантов.\n\n"
    ui.textBrowser.setText(stroka)
    ui.label_6.setText(f"попыток: {str(p)}.")


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1140, 680)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.spi_m = [] # список для вспомогательных кнопок

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 600, 700, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 470, 170, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(70, 530, 170, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(540, 590, 170, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")

        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(20, 110, 660, 350))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(75)
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")

        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(270, 480, 155, 60))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(530, 480, 150, 100))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.clicked.connect(proverka)
        self.pushButton.setObjectName("pushButton")

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(970, 580, 140, 70))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.clicked.connect(del_raz)
        self.pushButton_3.setObjectName("pushButton")


        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 20, 220, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(120, 55, 40, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.spinBox.setRange(1, 7)
        self.spinBox.setFont(font)
        if hislo == 0:
            self.spinBox.setProperty("value", 4)
        else:
            self.spinBox.setProperty("value", hislo)
        self.spinBox.setObjectName("spinBox")

        self.spinBox_2 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_2.setGeometry(QtCore.QRect(900, 600, 40, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.spinBox_2.setRange(1, len(kolor_0))
        self.spinBox_2.setFont(font)
        if hislo_kolor == 0:
            self.spinBox_2.setProperty("value", 3)
        else:
            self.spinBox_2.setProperty("value", hislo_kolor)
        self.spinBox_2.setObjectName("spinBox")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(300, 30, 150, 60))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.clicked.connect(nohalo)
        self.pushButton_2.setObjectName("pushButton_2")

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(970, 10, 140, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")

        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(40, 80, 200, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")

        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(720, 40, 220, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")

        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(800, 590, 90, 50))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")


#########################################################  вспомогательные кнопки, для размышления.
        l = 0
        for i in range(hislo):
            self.spi_s = []
            m = 0
            for j in range(10):
                self.pushButton_dm_1 = QtWidgets.QPushButton(self.centralwidget)
                self.pushButton_dm_1.setGeometry(QtCore.QRect(710 + l*60, 80 + m*50, 40, 40))
                font = QtGui.QFont()
                font.setFamily("Segoe Print")
                font.setPointSize(14)
                font.setBold(True)
                font.setWeight(75)
                self.pushButton_dm_1.setFont(font)
                self.pushButton_dm_1.k = mat_kolo[l][m]
                self.pushButton_dm_1.setStyleSheet(f"background-color:{kolor[self.pushButton_dm_1.k]}")
                self.pushButton_dm_1.setObjectName("pushButton_dm_1")

                self.spi_s.append(self.pushButton_dm_1)
                m += 1
            l += 1
            self.spi_m.append(self.spi_s)

####################################################################################################
        if hislo > 0:          #### когда разберусь КАК это оптимизировать, исправлю. пока громоздко.
            self.spi_m[0][0].clicked.connect(lambda: kno(0, 0))
            self.spi_m[0][1].clicked.connect(lambda: kno(0, 1))
            self.spi_m[0][2].clicked.connect(lambda: kno(0, 2))
            self.spi_m[0][3].clicked.connect(lambda: kno(0, 3))
            self.spi_m[0][4].clicked.connect(lambda: kno(0, 4))
            self.spi_m[0][5].clicked.connect(lambda: kno(0, 5))
            self.spi_m[0][6].clicked.connect(lambda: kno(0, 6))
            self.spi_m[0][7].clicked.connect(lambda: kno(0, 7))
            self.spi_m[0][8].clicked.connect(lambda: kno(0, 8))
            self.spi_m[0][9].clicked.connect(lambda: kno(0, 9))
        if hislo > 1:
            self.spi_m[1][0].clicked.connect(lambda: kno(1, 0))
            self.spi_m[1][1].clicked.connect(lambda: kno(1, 1))
            self.spi_m[1][2].clicked.connect(lambda: kno(1, 2))
            self.spi_m[1][3].clicked.connect(lambda: kno(1, 3))
            self.spi_m[1][4].clicked.connect(lambda: kno(1, 4))
            self.spi_m[1][5].clicked.connect(lambda: kno(1, 5))
            self.spi_m[1][6].clicked.connect(lambda: kno(1, 6))
            self.spi_m[1][7].clicked.connect(lambda: kno(1, 7))
            self.spi_m[1][8].clicked.connect(lambda: kno(1, 8))
            self.spi_m[1][9].clicked.connect(lambda: kno(1, 9))
        if hislo > 2:
            self.spi_m[2][0].clicked.connect(lambda: kno(2, 0))
            self.spi_m[2][1].clicked.connect(lambda: kno(2, 1))
            self.spi_m[2][2].clicked.connect(lambda: kno(2, 2))
            self.spi_m[2][3].clicked.connect(lambda: kno(2, 3))
            self.spi_m[2][4].clicked.connect(lambda: kno(2, 4))
            self.spi_m[2][5].clicked.connect(lambda: kno(2, 5))
            self.spi_m[2][6].clicked.connect(lambda: kno(2, 6))
            self.spi_m[2][7].clicked.connect(lambda: kno(2, 7))
            self.spi_m[2][8].clicked.connect(lambda: kno(2, 8))
            self.spi_m[2][9].clicked.connect(lambda: kno(2, 9))
        if hislo > 3:
            self.spi_m[3][0].clicked.connect(lambda: kno(3, 0))
            self.spi_m[3][1].clicked.connect(lambda: kno(3, 1))
            self.spi_m[3][2].clicked.connect(lambda: kno(3, 2))
            self.spi_m[3][3].clicked.connect(lambda: kno(3, 3))
            self.spi_m[3][4].clicked.connect(lambda: kno(3, 4))
            self.spi_m[3][5].clicked.connect(lambda: kno(3, 5))
            self.spi_m[3][6].clicked.connect(lambda: kno(3, 6))
            self.spi_m[3][7].clicked.connect(lambda: kno(3, 7))
            self.spi_m[3][8].clicked.connect(lambda: kno(3, 8))
            self.spi_m[3][9].clicked.connect(lambda: kno(3, 9))
        if hislo > 4:
            self.spi_m[4][0].clicked.connect(lambda: kno(4, 0))
            self.spi_m[4][1].clicked.connect(lambda: kno(4, 1))
            self.spi_m[4][2].clicked.connect(lambda: kno(4, 2))
            self.spi_m[4][3].clicked.connect(lambda: kno(4, 3))
            self.spi_m[4][4].clicked.connect(lambda: kno(4, 4))
            self.spi_m[4][5].clicked.connect(lambda: kno(4, 5))
            self.spi_m[4][6].clicked.connect(lambda: kno(4, 6))
            self.spi_m[4][7].clicked.connect(lambda: kno(4, 7))
            self.spi_m[4][8].clicked.connect(lambda: kno(4, 8))
            self.spi_m[4][9].clicked.connect(lambda: kno(4, 9))
        if hislo > 5:
            self.spi_m[5][0].clicked.connect(lambda: kno(5, 0))
            self.spi_m[5][1].clicked.connect(lambda: kno(5, 1))
            self.spi_m[5][2].clicked.connect(lambda: kno(5, 2))
            self.spi_m[5][3].clicked.connect(lambda: kno(5, 3))
            self.spi_m[5][4].clicked.connect(lambda: kno(5, 4))
            self.spi_m[5][5].clicked.connect(lambda: kno(5, 5))
            self.spi_m[5][6].clicked.connect(lambda: kno(5, 6))
            self.spi_m[5][7].clicked.connect(lambda: kno(5, 7))
            self.spi_m[5][8].clicked.connect(lambda: kno(5, 8))
            self.spi_m[5][9].clicked.connect(lambda: kno(5, 9))
        if hislo > 6:
            self.spi_m[6][0].clicked.connect(lambda: kno(6, 0))
            self.spi_m[6][1].clicked.connect(lambda: kno(6, 1))
            self.spi_m[6][2].clicked.connect(lambda: kno(6, 2))
            self.spi_m[6][3].clicked.connect(lambda: kno(6, 3))
            self.spi_m[6][4].clicked.connect(lambda: kno(6, 4))
            self.spi_m[6][5].clicked.connect(lambda: kno(6, 5))
            self.spi_m[6][6].clicked.connect(lambda: kno(6, 6))
            self.spi_m[6][7].clicked.connect(lambda: kno(6, 7))
            self.spi_m[6][8].clicked.connect(lambda: kno(6, 8))
            self.spi_m[6][9].clicked.connect(lambda: kno(6, 9))
####################################################################################

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 750, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "быки и коровы"))
        self.label.setText(_translate("MainWindow", ohi)) #'*тех. строка*"всё же очевидно. всего 1(один) вариант остался!!!"'
        self.label_2.setText(_translate("MainWindow", "быков:  "))
        self.label_3.setText(_translate("MainWindow", "коров:  "))
        self.label_6.setText(_translate("MainWindow", f"попыток: {str(p)}."))
        self.pushButton.setText(_translate("MainWindow", "проверить"))
        self.label_4.setText(_translate("MainWindow", "количество знаков:"))
        self.pushButton_2.setText(_translate("MainWindow", "начать"))
        self.label_5.setText(_translate("MainWindow", "разработчик: Тарасов Д. Л."))
        self.label_7.setText(_translate("MainWindow", "(рекомендуется: от 3 до 5.)"))
        self.label_8.setText(_translate("MainWindow", "для размышления:"))
        self.label_9.setText(_translate("MainWindow", "цветов:"))
        self.pushButton_3.setText(_translate("MainWindow", "сброс \nразмышлений"))
        f = 0
        for i in self.spi_m:
            f1 = 0
            for j in i:
                j.setText(str(matri[f][f1]))
                f1 += 1
            f += 1


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
