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
    ui.spisok_l[1][0].setText(f"быков: {bik}")
    ui.spisok_l[2][0].setText(f"коров: {kor}")
    if len(q) != 1:
        ui.spisok_l[0][0].setText(f"так.... вообще, есть {len(q)} вариантов.")
    else:
        ui.spisok_l[0][0].setText("всё же очевидно. всего 1(один) вариант остался!!!")

def del_raz():
    global mat_kolo
    mat_kolo = [[0 for i in range(10)] for j in range(hislo)]
    ui.setupUi(MainWindow)
    ui.textBrowser.setText(stroka)
    ui.spisok_l[1][0].setText(f"быков: {bik}")
    ui.spisok_l[2][0].setText(f"коров: {kor}")
    if len(q) != 1:
        ui.spisok_l[0][0].setText(f"так.... вообще, есть {len(q)} вариантов.")
    else:
        ui.spisok_l[0][0].setText("всё же очевидно. всего 1(один) вариант остался!!!")


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
    ui.spisok_l[0][0].setText("")
    if a == 0:
        ohi = "нечего проверять. число не загадано."
        ui.spisok_l[0][0].setText(ohi)
        return False
    b = ui.textEdit.toPlainText()
    if len(b) != hislo:
        ohi = f"длина загаданного числа ({hislo} знак.)"
        ui.spisok_l[0][0].setText(ohi)
        return False
    elif b.isdigit() != True:
        ohi = "число должно содержать исключительно цифры."
        ui.spisok_l[0][0].setText(ohi)
        return False
    if gg == 1:
        ohi = "уже разгаданно."
        ui.spisok_l[0][0].setText(ohi)
        return False
    p += 1
    if a == b:
        ui.spisok_l[0][0].setText(f"             победа! c {p} попытки.")
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
        ui.spisok_l[1][0].setText(f"быков: {bik}")
        ui.spisok_l[2][0].setText(f"коров: {kor}")
        if len(q) != 1:
            ui.spisok_l[0][0].setText(f"так.... вообще, есть {len(q)} вариантов.")
        else:
            ui.spisok_l[0][0].setText("всё же очевидно. всего 1(один) вариант остался!!!")

    stroka += f"число:   {b}     |    быков: {bik},     коров: {kor}.    |     есть {len(q)} вариантов.\n\n"
    ui.textBrowser.setText(stroka)
    ui.spisok_l[5][0].setText(f"попыток: {str(p)}.")


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1140, 680)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.spi_m = [] # список для вспомогательных кнопок

        font_1, font_2, font_3, font_4, font_5, font_6 = QtGui.QFont(), QtGui.QFont(), QtGui.QFont(), QtGui.QFont(),\
            QtGui.QFont(), QtGui.QFont()
        self.spisok_f = [[font_1, 7], [font_2, 10], [font_3, 12], [font_4, 14], [font_5, 16], [font_6, 20]]

        for i in self.spisok_f:
            i[0].setFamily("Segoe Print")
            i[0].setPointSize(i[1])
            i[0].setBold(True)
            i[0].setWeight(75)

        self.baza_l = [[20, 600, 700, 30, font_3, ohi], [70, 470, 170, 50, font_6, 'быков:  '],
                       [70, 530, 170, 50, font_6, 'коров:  '], [30, 20, 220, 30, font_5, 'количество знаков:'],
                       [970, 10, 140, 30, font_1, 'разработчик: Тарасов Д. Л.'],
                       [540, 590, 170, 50, font_5, f"попыток: {str(p)}."],
                       [40, 80, 200, 30, font_2, '(рекомендуется: от 3 до 5.)'],
                       [720, 40, 220, 30, font_5, 'для размышления:'], [800, 590, 90, 50, font_5, 'цветов:']]
        self.spisok_l = []
        for i in self.baza_l:
            self.label = QtWidgets.QLabel(self.centralwidget)
            self.label.setGeometry(QtCore.QRect(i[0], i[1], i[2], i[3]))
            self.label.setFont(i[4])
            self.spisok_l.append([self.label, i[5]])

        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.pushButton, self.pushButton_2, self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget),\
            QtWidgets.QPushButton(self.centralwidget), QtWidgets.QPushButton(self.centralwidget)
        self.spinBox, self.spinBox_2 = QtWidgets.QSpinBox(self.centralwidget), QtWidgets.QSpinBox(self.centralwidget)
        self.spisok_t_p =[[self.textBrowser, 20, 110, 660, 350, font_3], [self.textEdit, 270, 480, 155, 60, font_6],
                          [self.pushButton, 530, 480, 150, 100, font_5], [self.pushButton_2, 300, 30, 150, 60, font_5],
                          [self.pushButton_3, 970, 580, 140, 70, font_3], [self.spinBox, 120, 55, 40, 30, font_3],
                          [self.spinBox_2, 900, 600, 40, 30, font_3]]

        for i in self.spisok_t_p:
            i[0].setGeometry(QtCore.QRect(i[1], i[2], i[3], i[4]))
            i[0].setFont(i[5])

        self.pushButton.clicked.connect(proverka)
        self.pushButton_2.clicked.connect(nohalo)
        self.pushButton_3.clicked.connect(del_raz)

        self.spinBox.setRange(1, 7)
        if hislo == 0:
            self.spinBox.setProperty("value", 4)
        else:
            self.spinBox.setProperty("value", hislo)

        self.spinBox_2.setRange(1, len(kolor_0))
        if hislo_kolor == 0:
            self.spinBox_2.setProperty("value", 3)
        else:
            self.spinBox_2.setProperty("value", hislo_kolor)
#########################################################  вспомогательные кнопки, для размышления.
        l = 0
        for i in range(hislo):
            self.spi_s = []
            m = 0
            for j in range(10):
                self.pushButton_dm_1 = QtWidgets.QPushButton(self.centralwidget)
                self.pushButton_dm_1.setGeometry(QtCore.QRect(710 + l*60, 80 + m*50, 40, 40))
                self.pushButton_dm_1.setFont(font_4)
                self.pushButton_dm_1.k = mat_kolo[l][m]
                self.pushButton_dm_1.setStyleSheet(f"background-color:{kolor[self.pushButton_dm_1.k]}")

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
        for i in self.spisok_l:
            i[0].setText(_translate("MainWindow", i[1]))

        self.pushButton.setText(_translate("MainWindow", "проверить"))
        self.pushButton_2.setText(_translate("MainWindow", "начать"))
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
