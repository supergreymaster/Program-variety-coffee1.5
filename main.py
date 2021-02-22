import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QTableWidgetItem, QWidget

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(396, 300)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(20, 270, 181, 23))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(50, 30, 331, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(20, 70, 361, 192))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(210, 270, 171, 23))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Обновить"))
        self.label.setText(_translate("Form", "Информация по кофе"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "id"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Название"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Степень обжарки"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Молотый, в зернах"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Описание вкуса"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Form", "Цена"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Form", "Объём упаковки"))
        self.pushButton_2.setText(_translate("Form", "Добавить"))


class Ui_Form1(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(434, 300)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 10, 401, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_name = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_name.setObjectName("label_name")
        self.horizontalLayout.addWidget(self.label_name)
        self.label_roasting = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_roasting.setObjectName("label_roasting")
        self.horizontalLayout.addWidget(self.label_roasting)
        self.label_grains = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_grains.setObjectName("label_grains")
        self.horizontalLayout.addWidget(self.label_grains)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(20, 40, 401, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEdit_name = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.horizontalLayout_2.addWidget(self.lineEdit_name)
        self.lineEdit_roasting = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit_roasting.setObjectName("lineEdit_roasting")
        self.horizontalLayout_2.addWidget(self.lineEdit_roasting)
        self.lineEdit_grains = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit_grains.setObjectName("lineEdit_grains")
        self.horizontalLayout_2.addWidget(self.lineEdit_grains)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(50, 80, 371, 41))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_taste = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_taste.setObjectName("label_taste")
        self.horizontalLayout_3.addWidget(self.label_taste)
        self.label_price = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_price.setObjectName("label_price")
        self.horizontalLayout_3.addWidget(self.label_price)
        self.label_v = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.label_v.setObjectName("label_v")
        self.horizontalLayout_3.addWidget(self.label_v)
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(20, 120, 401, 41))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lineEdit_taste = QtWidgets.QLineEdit(self.horizontalLayoutWidget_4)
        self.lineEdit_taste.setObjectName("lineEdit_taste")
        self.horizontalLayout_4.addWidget(self.lineEdit_taste)
        self.lineEdit_price = QtWidgets.QLineEdit(self.horizontalLayoutWidget_4)
        self.lineEdit_price.setObjectName("lineEdit_price")
        self.horizontalLayout_4.addWidget(self.lineEdit_price)
        self.lineEdit_v = QtWidgets.QLineEdit(self.horizontalLayoutWidget_4)
        self.lineEdit_v.setObjectName("lineEdit_v")
        self.horizontalLayout_4.addWidget(self.lineEdit_v)
        self.lineEdit_4 = QtWidgets.QLineEdit(Form)
        self.lineEdit_4.setGeometry(QtCore.QRect(20, 200, 31, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 180, 47, 13))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(90, 180, 261, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(90, 210, 321, 16))
        self.label_3.setObjectName("label_3")
        self.Button = QtWidgets.QPushButton(Form)
        self.Button.setGeometry(QtCore.QRect(20, 250, 75, 23))
        self.Button.setObjectName("Button")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_name.setText(_translate("Form", "Название"))
        self.label_roasting.setText(_translate("Form", "Степень прожарки"))
        self.label_grains.setText(_translate("Form", "Вид зёрен"))
        self.label_taste.setText(_translate("Form", "Описание вкуса"))
        self.label_price.setText(_translate("Form", "Цена"))
        self.label_v.setText(_translate("Form", "Объём упаковки"))
        self.label.setText(_translate("Form", "Ряд"))
        self.label_2.setText(_translate("Form", "Если поле не заполнено, то изменятся он не будет"))
        self.label_3.setText(_translate("Form", "Если колонка \"ряд\" не заполнена, данные добавятся в конец "))
        self.Button.setText(_translate("Form", "Добавить"))


class Window2(QWidget, Ui_Form1):
    def __init__(self):
        super(Window2, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Window2')
        self.Button.clicked.connect(self.work)
        # print(self.name, self.roasting, self.grains, self.taste, self.price, self.v, )

    def work(self):
        self.name = self.lineEdit_name.text()
        self.roasting = self.lineEdit_roasting.text()
        self.grains = self.lineEdit_grains.text()
        self.taste = self.lineEdit_taste.text()
        self.price = self.lineEdit_price.text()
        self.v = self.lineEdit_v.text()
        self.row = self.lineEdit_4.text()
        if self.row:
            try:
                a = int(self.row)
                if a <= 0:
                    self.add()
                else:
                    self.change()
            except ValueError:
                self.add()
        else:
            self.add()

    def add(self):
        con = sqlite3.connect("data/coffee.db")
        # name,roasting,grains,taste,price,v
        cur = con.cursor()
        cur.execute(f"""INSERT INTO Сoffee(name,roasting,grains,taste,price,v)
                        VALUES('{self.name}', '{self.roasting}', '{self.grains}',
                        '{self.taste}', '{self.price}', '{self.v}')""")
        con.commit()
        print("Добавление произошло успешно")

    def change(self):
        con = sqlite3.connect("data/coffee.db")
        cur = con.cursor()
        res = cur.execute(f"SELECT id FROM Сoffee").fetchall()
        a = max([int(i[0]) for i in res])
        if a < int(self.row) and int(self.row) > 0:
            self.add()
            return
        if self.name:
            cur.execute(f"""UPDATE Сoffee SET name = '{self.name}' 
                            WHERE id == '{self.row}'""")
            con.commit()
        if self.roasting:
            cur.execute(f"""UPDATE Сoffee SET roasting = '{self.roasting}' 
                                        WHERE id == '{self.row}'""")
            con.commit()
        if self.grains:
            cur.execute(f"""UPDATE Сoffee SET grains = '{self.grains}' 
                                        WHERE id == '{self.row}'""")
            con.commit()
        if self.taste:
            cur.execute(f"""UPDATE Сoffee SET taste = '{self.taste}' 
                                        WHERE id == '{self.row}'""")
            con.commit()
        if self.price:
            cur.execute(f"""UPDATE Сoffee SET price = '{self.price}' 
                                        WHERE id == '{self.row}'""")
            con.commit()
        if self.v:
            cur.execute(f"""UPDATE Сoffee SET v = '{self.v}' 
                                        WHERE id == '{self.row}'""")
            con.commit()
        print("Изменение прошло успешно")



class MyWidget(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.work)
        self.pushButton_2.clicked.connect(self.loc)

    def work(self):
        con = sqlite3.connect("data/coffee.db")
        cur = con.cursor()
        req = cur.execute("SELECT * FROM Сoffee").fetchall()
        print(req)
        self.tableWidget.setRowCount(len(req))
        for i in range(len(req)):
            for j in range(len(req[i])):
                item = QTableWidgetItem()
                item.setText(str(req[i][j]))
                self.tableWidget.setItem(i, j, item)

    def loc(self):
        self.w2 = Window2()
        self.w2.show()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    sys.excepthook = except_hook
    ex.show()
    sys.exit(app.exec_())



