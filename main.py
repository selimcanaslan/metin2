from PyQt5 import QtCore, QtGui, QtWidgets
from combo_values import combo_values
from makezero import makeZero
from calculate_price import Items
from calculate_multi_item import MultiItems
from process_succeed import succeed
# from export import export
from costume_price import CostumeInfo
from select_path import path
import os


class Ui_MainWindow(object):
    def __init__(self):
        self.selected_path = ""

    def call_combo(self):
        combo_values(self)

    def call_make_zero(self):
        makeZero(self)

    def price_calculate(self):
        item1_name = self.item_combo.currentText()
        item1_price = self.won_line_1.text()
        item1 = Items(item1_name, item1_price)

        item2_name = self.item_combo.currentText()
        item2_price = self.won_line_2.text()
        item2 = Items(item2_name, item2_price)

        item3_name = self.item_combo.currentText()
        item3_price = self.won_line_3.text()
        item3 = Items(item3_name, item3_price)

        item4_name = self.item_combo.currentText()
        item4_price = self.won_line_4.text()
        item4 = Items(item4_name, item4_price)

        item5_name = self.item_combo.currentText()
        item5_price = self.won_line_5.text()
        item5 = Items(item5_name, item5_price)

        item6_name = self.item_combo.currentText()
        item6_price = self.won_line_6.text()
        item6 = Items(item6_name, item6_price)

        item7_name = self.item_combo.currentText()
        item7_price = self.won_line_7.text()
        item7 = Items(item7_name, item7_price)

        item8_name = self.item_combo.currentText()
        item8_price = self.won_line_8.text()
        item8 = Items(item8_name, item8_price)

        item9_name = self.item_combo.currentText()
        item9_price = self.won_line_9.text()
        item9 = Items(item9_name, item9_price)

        item10_name = self.item_combo.currentText()
        item10_price = self.won_line_10.text()
        item10 = Items(item10_name, item10_price)

        toplam = Items.calculate(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10)
        self.revenue_sum.setText(str(toplam))
        number_of_metinstones = self.number_of_metinstones.text()
        min_count = self.min_edit.text()
        won_per_metin = int(toplam) / int(number_of_metinstones)
        won_per_min = int(toplam) / int(min_count)
        self.revenue_per_metinstone.setText(str(format(won_per_metin, '.2f')) + " won")
        self.revenue_per_min.setText(str(format(won_per_min, '.2f')) + " won")
        self.metin_per_min()
        succeed()
        # export(self)

    def metin_per_min(self):
        number_of_metinstones = self.number_of_metinstones.text()
        min_count = self.min_edit.text()
        metin_per_min = int(number_of_metinstones) / int(min_count)
        self.text1.setText("Dakika başına " + str(format(metin_per_min, '.2f')) + " Metin Kestiniz")

    def multi_item_price_calculate(self):
        won = self.toplu_won.text()
        yang = self.toplu_yang.text()
        miktar = self.miktar.text()
        giden = MultiItems(won, yang, miktar)
        toplam_won, toplam_yang = MultiItems.multi_calculate(giden)
        self.toplam_fiyat.setText(str(toplam_won) + " won " + str(toplam_yang) + " m")

    def costume_price(self):
        full_time_day = self.full_time_costume_day.text()
        full_time_price = self.full_time_costume_price.text()
        current_day = self.current_day.text()
        current_hour = self.current_hour.text()
        current_min = self.current_min.text()
        costume = CostumeInfo(full_time_price, full_time_day, current_day, current_hour, current_min)
        price = CostumeInfo.price_for_random_day(costume)
        self.label_19.setText(str(format(price, '.2f')) + " Won")

    def path_finder(self):
        self.selected_path = path()

    def run_metin2(self):
        current_path = self.selected_path
        if self.selected_path[:2] == "D:":
            os.system("D: & CD {} & START Rohan2Global.exe".format(current_path))
        else:
            os.system("CD {} & dir".format(self.selected_path))

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 201, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.item_combo = QtWidgets.QComboBox(self.centralwidget)
        self.item_combo.setGeometry(QtCore.QRect(10, 60, 91, 22))
        self.item_combo.setObjectName("item_combo")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 15, 211, 31))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 39, 61, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(110, 40, 111, 21))
        self.label_3.setObjectName("label_3")
        self.won_line_1 = QtWidgets.QLineEdit(self.centralwidget)
        self.won_line_1.setGeometry(QtCore.QRect(110, 60, 101, 21))
        self.won_line_1.setObjectName("won_line_1")
        self.item_combo_2 = QtWidgets.QComboBox(self.centralwidget)
        self.item_combo_2.setGeometry(QtCore.QRect(10, 90, 91, 22))
        self.item_combo_2.setObjectName("item_combo_2")
        self.won_line_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.won_line_2.setGeometry(QtCore.QRect(110, 90, 101, 21))
        self.won_line_2.setObjectName("won_line_2")
        self.item_combo_3 = QtWidgets.QComboBox(self.centralwidget)
        self.item_combo_3.setGeometry(QtCore.QRect(10, 120, 91, 22))
        self.item_combo_3.setObjectName("item_combo_3")
        self.won_line_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.won_line_3.setGeometry(QtCore.QRect(110, 120, 101, 21))
        self.won_line_3.setObjectName("won_line_3")
        self.item_combo_4 = QtWidgets.QComboBox(self.centralwidget)
        self.item_combo_4.setGeometry(QtCore.QRect(10, 150, 91, 22))
        self.item_combo_4.setObjectName("item_combo_4")
        self.won_line_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.won_line_4.setGeometry(QtCore.QRect(110, 150, 101, 21))
        self.won_line_4.setObjectName("won_line_4")
        self.won_line_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.won_line_5.setGeometry(QtCore.QRect(110, 180, 101, 21))
        self.won_line_5.setObjectName("won_line_5")
        self.item_combo_5 = QtWidgets.QComboBox(self.centralwidget)
        self.item_combo_5.setGeometry(QtCore.QRect(10, 180, 91, 22))
        self.item_combo_5.setObjectName("item_combo_5")
        self.item_combo_6 = QtWidgets.QComboBox(self.centralwidget)
        self.item_combo_6.setGeometry(QtCore.QRect(10, 210, 91, 22))
        self.item_combo_6.setObjectName("item_combo_6")
        self.won_line_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.won_line_6.setGeometry(QtCore.QRect(110, 210, 101, 21))
        self.won_line_6.setObjectName("won_line_6")
        self.won_line_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.won_line_7.setGeometry(QtCore.QRect(110, 240, 101, 21))
        self.won_line_7.setObjectName("won_line_7")
        self.item_combo_7 = QtWidgets.QComboBox(self.centralwidget)
        self.item_combo_7.setGeometry(QtCore.QRect(10, 240, 91, 22))
        self.item_combo_7.setObjectName("item_combo_7")
        self.item_combo_8 = QtWidgets.QComboBox(self.centralwidget)
        self.item_combo_8.setGeometry(QtCore.QRect(10, 270, 91, 22))
        self.item_combo_8.setObjectName("item_combo_8")
        self.won_line_8 = QtWidgets.QLineEdit(self.centralwidget)
        self.won_line_8.setGeometry(QtCore.QRect(110, 270, 101, 21))
        self.won_line_8.setObjectName("won_line_8")
        self.won_line_9 = QtWidgets.QLineEdit(self.centralwidget)
        self.won_line_9.setGeometry(QtCore.QRect(110, 300, 101, 21))
        self.won_line_9.setObjectName("won_line_9")
        self.item_combo_9 = QtWidgets.QComboBox(self.centralwidget)
        self.item_combo_9.setGeometry(QtCore.QRect(10, 300, 91, 22))
        self.item_combo_9.setObjectName("item_combo_9")
        self.item_combo_10 = QtWidgets.QComboBox(self.centralwidget)
        self.item_combo_10.setGeometry(QtCore.QRect(10, 330, 91, 22))
        self.item_combo_10.setObjectName("item_combo_10")
        self.won_line_10 = QtWidgets.QLineEdit(self.centralwidget)
        self.won_line_10.setGeometry(QtCore.QRect(110, 330, 101, 21))
        self.won_line_10.setObjectName("won_line_10")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(70, 360, 71, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(10, 370, 201, 21))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.min_text = QtWidgets.QLabel(self.centralwidget)
        self.min_text.setGeometry(QtCore.QRect(10, 390, 47, 21))
        self.min_text.setObjectName("min_text")
        self.min_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.min_edit.setGeometry(QtCore.QRect(60, 390, 31, 20))
        self.min_edit.setObjectName("min_edit")
        self.metin_text = QtWidgets.QLabel(self.centralwidget)
        self.metin_text.setGeometry(QtCore.QRect(100, 390, 71, 21))
        self.metin_text.setObjectName("metin_text")
        self.number_of_metinstones = QtWidgets.QLineEdit(self.centralwidget)
        self.number_of_metinstones.setGeometry(QtCore.QRect(170, 390, 31, 20))
        self.number_of_metinstones.setObjectName("number_of_metinstones")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(10, 440, 211, 21))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(10, 460, 81, 21))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(10, 490, 111, 21))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(10, 520, 111, 21))
        self.label_10.setObjectName("label_10")
        self.revenue_sum = QtWidgets.QLabel(self.centralwidget)
        self.revenue_sum.setGeometry(QtCore.QRect(130, 460, 81, 21))
        self.revenue_sum.setObjectName("revenue_sum")
        self.revenue_per_min = QtWidgets.QLabel(self.centralwidget)
        self.revenue_per_min.setGeometry(QtCore.QRect(130, 490, 81, 21))
        self.revenue_per_min.setObjectName("revenue_per_min")
        self.revenue_per_metinstone = QtWidgets.QLabel(self.centralwidget)
        self.revenue_per_metinstone.setGeometry(QtCore.QRect(130, 520, 81, 21))
        self.revenue_per_metinstone.setObjectName("revenue_per_metinstone")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(210, 30, 20, 521))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.calculate_button = QtWidgets.QPushButton(self.centralwidget)
        self.calculate_button.setGeometry(QtCore.QRect(30, 420, 161, 23))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.calculate_button.setFont(font)
        self.calculate_button.setObjectName("calculate_button")
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(220, 10, 211, 41))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(250, 10, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(230, 60, 61, 21))
        self.label_6.setObjectName("label_6")
        self.toplu_won = QtWidgets.QLineEdit(self.centralwidget)
        self.toplu_won.setGeometry(QtCore.QRect(290, 60, 41, 20))
        self.toplu_won.setObjectName("toplu_won")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(300, 40, 51, 20))
        self.label_7.setObjectName("label_7")
        self.toplu_yang = QtWidgets.QLineEdit(self.centralwidget)
        self.toplu_yang.setGeometry(QtCore.QRect(340, 60, 81, 20))
        self.toplu_yang.setObjectName("toplu_yang")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(350, 40, 81, 20))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(230, 90, 61, 21))
        self.label_12.setObjectName("label_12")
        self.miktar = QtWidgets.QLineEdit(self.centralwidget)
        self.miktar.setGeometry(QtCore.QRect(290, 90, 41, 20))
        self.miktar.setObjectName("miktar")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(230, 120, 71, 21))
        self.label_13.setObjectName("label_13")
        self.toplam_fiyat = QtWidgets.QLabel(self.centralwidget)
        self.toplam_fiyat.setGeometry(QtCore.QRect(310, 120, 111, 21))
        self.toplam_fiyat.setObjectName("toplam_fiyat")
        self.line_7 = QtWidgets.QFrame(self.centralwidget)
        self.line_7.setGeometry(QtCore.QRect(420, 30, 20, 521))
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.line_8 = QtWidgets.QFrame(self.centralwidget)
        self.line_8.setGeometry(QtCore.QRect(220, 540, 211, 21))
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.line_9 = QtWidgets.QFrame(self.centralwidget)
        self.line_9.setGeometry(QtCore.QRect(220, 140, 211, 21))
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.toplu_calculate_button = QtWidgets.QPushButton(self.centralwidget)
        self.toplu_calculate_button.setGeometry(QtCore.QRect(340, 90, 81, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.toplu_calculate_button.setFont(font)
        self.toplu_calculate_button.setObjectName("toplu_calculate_button")
        self.line_10 = QtWidgets.QFrame(self.centralwidget)
        self.line_10.setGeometry(QtCore.QRect(-11, 30, 41, 521))
        self.line_10.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(10, 530, 211, 41))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_11 = QtWidgets.QFrame(self.centralwidget)
        self.line_11.setGeometry(QtCore.QRect(220, 440, 211, 21))
        self.line_11.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.text1 = QtWidgets.QLabel(self.centralwidget)
        self.text1.setGeometry(QtCore.QRect(230, 456, 191, 20))
        self.text1.setObjectName("text1")
        self.text2 = QtWidgets.QLabel(self.centralwidget)
        self.text2.setGeometry(QtCore.QRect(230, 480, 191, 20))
        self.text2.setObjectName("text2")
        self.text3 = QtWidgets.QLabel(self.centralwidget)
        self.text3.setGeometry(QtCore.QRect(230, 500, 191, 20))
        self.text3.setObjectName("text3")
        self.text4 = QtWidgets.QLabel(self.centralwidget)
        self.text4.setGeometry(QtCore.QRect(230, 520, 191, 20))
        self.text4.setObjectName("text4")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(240, 150, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.line_12 = QtWidgets.QFrame(self.centralwidget)
        self.line_12.setGeometry(QtCore.QRect(220, 160, 211, 31))
        self.line_12.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_12.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_12.setObjectName("line_12")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(230, 180, 81, 21))
        self.label_15.setObjectName("label_15")
        self.full_time_costume_day = QtWidgets.QLineEdit(self.centralwidget)
        self.full_time_costume_day.setGeometry(QtCore.QRect(310, 180, 31, 20))
        self.full_time_costume_day.setObjectName("full_time_costume_day")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(350, 180, 31, 21))
        self.label_16.setObjectName("label_16")
        self.full_time_costume_price = QtWidgets.QLineEdit(self.centralwidget)
        self.full_time_costume_price.setGeometry(QtCore.QRect(380, 180, 41, 20))
        self.full_time_costume_price.setObjectName("full_time_costume_price")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(230, 200, 121, 31))
        font = QtGui.QFont()
        font.setUnderline(True)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(230, 230, 91, 21))
        self.label_18.setObjectName("label_18")
        self.current_day = QtWidgets.QLineEdit(self.centralwidget)
        self.current_day.setGeometry(QtCore.QRect(320, 230, 21, 20))
        self.current_day.setObjectName("current_day")
        self.current_hour = QtWidgets.QLineEdit(self.centralwidget)
        self.current_hour.setGeometry(QtCore.QRect(360, 230, 21, 20))
        self.current_hour.setObjectName("current_hour")
        self.current_min = QtWidgets.QLineEdit(self.centralwidget)
        self.current_min.setGeometry(QtCore.QRect(400, 230, 21, 20))
        self.current_min.setObjectName("current_min")
        self.costume_button = QtWidgets.QPushButton(self.centralwidget)
        self.costume_button.setGeometry(QtCore.QRect(230, 260, 81, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.costume_button.setFont(font)
        self.costume_button.setObjectName("costume_button")
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(320, 260, 101, 21))
        self.label_19.setText("")
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(680, 450, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.path_select_button = QtWidgets.QPushButton(self.centralwidget)
        self.path_select_button.setGeometry(QtCore.QRect(690, 482, 75, 31))
        self.path_select_button.setObjectName("path_select_button")
        self.run_client_button = QtWidgets.QPushButton(self.centralwidget)
        self.run_client_button.setGeometry(QtCore.QRect(690, 512, 75, 31))
        self.run_client_button.setObjectName("run_client_button")
        self.line_13 = QtWidgets.QFrame(self.centralwidget)
        self.line_13.setGeometry(QtCore.QRect(430, 440, 351, 21))
        self.line_13.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_13.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_13.setObjectName("line_13")
        self.line_14 = QtWidgets.QFrame(self.centralwidget)
        self.line_14.setGeometry(QtCore.QRect(770, 30, 20, 521))
        self.line_14.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_14.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_14.setObjectName("line_14")
        self.line_15 = QtWidgets.QFrame(self.centralwidget)
        self.line_15.setGeometry(QtCore.QRect(430, 540, 351, 21))
        self.line_15.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_15.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_15.setObjectName("line_15")
        self.line_16 = QtWidgets.QFrame(self.centralwidget)
        self.line_16.setGeometry(QtCore.QRect(660, 450, 20, 101))
        self.line_16.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_16.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_16.setObjectName("line_16")
        self.line_17 = QtWidgets.QFrame(self.centralwidget)
        self.line_17.setGeometry(QtCore.QRect(430, 10, 351, 41))
        self.line_17.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_17.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_17.setObjectName("line_17")
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setGeometry(QtCore.QRect(260, 290, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.line_18 = QtWidgets.QFrame(self.centralwidget)
        self.line_18.setGeometry(QtCore.QRect(220, 270, 211, 41))
        self.line_18.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_18.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_18.setObjectName("line_18")
        self.line_19 = QtWidgets.QFrame(self.centralwidget)
        self.line_19.setGeometry(QtCore.QRect(220, 301, 211, 31))
        self.line_19.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_19.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_19.setObjectName("line_19")
        self.label_22 = QtWidgets.QLabel(self.centralwidget)
        self.label_22.setGeometry(QtCore.QRect(230, 320, 81, 21))
        self.label_22.setObjectName("label_22")
        self.item_combo_11 = QtWidgets.QComboBox(self.centralwidget)
        self.item_combo_11.setGeometry(QtCore.QRect(300, 320, 121, 22))
        self.item_combo_11.setObjectName("item_combo_11")
        self.label_23 = QtWidgets.QLabel(self.centralwidget)
        self.label_23.setGeometry(QtCore.QRect(230, 350, 71, 21))
        self.label_23.setObjectName("label_23")
        self.hasar_line = QtWidgets.QLineEdit(self.centralwidget)
        self.hasar_line.setGeometry(QtCore.QRect(300, 350, 121, 21))
        self.hasar_line.setObjectName("hasar_line")
        self.estimated_metin_value = QtWidgets.QLabel(self.centralwidget)
        self.estimated_metin_value.setGeometry(QtCore.QRect(230, 401, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.estimated_metin_value.setFont(font)
        self.estimated_metin_value.setObjectName("estimated_metin_value")
        self.estimated_revenue = QtWidgets.QLabel(self.centralwidget)
        self.estimated_revenue.setGeometry(QtCore.QRect(230, 420, 111, 31))
        self.estimated_revenue.setObjectName("estimated_revenue")
        self.estimated_farm_button = QtWidgets.QPushButton(self.centralwidget)
        self.estimated_farm_button.setGeometry(QtCore.QRect(360, 380, 61, 23))
        self.estimated_farm_button.setObjectName("estimated_farm_button")
        self.line_20 = QtWidgets.QFrame(self.centralwidget)
        self.line_20.setGeometry(QtCore.QRect(230, 392, 121, 20))
        self.line_20.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_20.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_20.setObjectName("line_20")
        self.label_24 = QtWidgets.QLabel(self.centralwidget)
        self.label_24.setGeometry(QtCore.QRect(230, 380, 71, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.line_19.raise_()
        self.line_18.raise_()
        self.line_12.raise_()
        self.line_9.raise_()
        self.line_7.raise_()
        self.line_11.raise_()
        self.line_8.raise_()
        self.label.raise_()
        self.item_combo.raise_()
        self.line.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.won_line_1.raise_()
        self.item_combo_2.raise_()
        self.won_line_2.raise_()
        self.item_combo_3.raise_()
        self.won_line_3.raise_()
        self.item_combo_4.raise_()
        self.won_line_4.raise_()
        self.won_line_5.raise_()
        self.item_combo_5.raise_()
        self.item_combo_6.raise_()
        self.won_line_6.raise_()
        self.won_line_7.raise_()
        self.item_combo_7.raise_()
        self.item_combo_8.raise_()
        self.won_line_8.raise_()
        self.won_line_9.raise_()
        self.item_combo_9.raise_()
        self.item_combo_10.raise_()
        self.won_line_10.raise_()
        self.label_4.raise_()
        self.line_2.raise_()
        self.min_text.raise_()
        self.min_edit.raise_()
        self.metin_text.raise_()
        self.number_of_metinstones.raise_()
        self.line_3.raise_()
        self.label_8.raise_()
        self.label_9.raise_()
        self.label_10.raise_()
        self.revenue_sum.raise_()
        self.revenue_per_min.raise_()
        self.revenue_per_metinstone.raise_()
        self.line_4.raise_()
        self.calculate_button.raise_()
        self.line_6.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.toplu_won.raise_()
        self.label_7.raise_()
        self.toplu_yang.raise_()
        self.label_11.raise_()
        self.label_12.raise_()
        self.miktar.raise_()
        self.label_13.raise_()
        self.toplam_fiyat.raise_()
        self.toplu_calculate_button.raise_()
        self.line_10.raise_()
        self.line_5.raise_()
        self.text1.raise_()
        self.text2.raise_()
        self.text3.raise_()
        self.text4.raise_()
        self.label_14.raise_()
        self.label_15.raise_()
        self.full_time_costume_day.raise_()
        self.label_16.raise_()
        self.full_time_costume_price.raise_()
        self.label_17.raise_()
        self.label_18.raise_()
        self.current_day.raise_()
        self.current_hour.raise_()
        self.current_min.raise_()
        self.costume_button.raise_()
        self.label_19.raise_()
        self.label_20.raise_()
        self.path_select_button.raise_()
        self.run_client_button.raise_()
        self.line_13.raise_()
        self.line_14.raise_()
        self.line_15.raise_()
        self.line_16.raise_()
        self.line_17.raise_()
        self.label_21.raise_()
        self.label_22.raise_()
        self.item_combo_11.raise_()
        self.label_23.raise_()
        self.hasar_line.raise_()
        self.estimated_metin_value.raise_()
        self.estimated_revenue.raise_()
        self.estimated_farm_button.raise_()
        self.line_20.raise_()
        self.label_24.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Metin2 Kar Hesaplama By SCA Game"))
        self.label.setText(_translate("MainWindow", "METIN FARMI KAR HESAPLAMA"))
        self.label_2.setText(_translate("MainWindow", "İTEM İSMİ"))
        self.label_3.setText(_translate("MainWindow", "TOPLAM FİYAT(won)"))
        self.label_4.setText(_translate("MainWindow", "İsteğe Bağlı"))
        self.min_text.setText(_translate("MainWindow", "Süre(dk) :"))
        self.metin_text.setText(_translate("MainWindow", "Metin Sayısı :"))
        self.label_8.setText(_translate("MainWindow", "Toplam Kazanç:"))
        self.label_9.setText(_translate("MainWindow", "Dakika Başına Kazanç :"))
        self.label_10.setText(_translate("MainWindow", "Metin Başına Kazanç :"))
        self.revenue_sum.setText(_translate("MainWindow", "0"))
        self.revenue_per_min.setText(_translate("MainWindow", "0"))
        self.revenue_per_metinstone.setText(_translate("MainWindow", "0"))
        self.calculate_button.setText(_translate("MainWindow", "HESAPLA"))
        self.label_5.setText(_translate("MainWindow", "TOPLU İTEM FİYATI"))
        self.label_6.setText(_translate("MainWindow", "Tane Fiyatı:"))
        self.label_7.setText(_translate("MainWindow", "Won"))
        self.label_11.setText(_translate("MainWindow", "Yang(milyon)"))
        self.label_12.setText(_translate("MainWindow", "Miktar:"))
        self.label_13.setText(_translate("MainWindow", "Toplam Fiyat:"))
        self.toplam_fiyat.setText(_translate("MainWindow", "0"))
        self.toplu_calculate_button.setText(_translate("MainWindow", "HESAPLA"))
        self.text1.setText(_translate("MainWindow", "............"))
        self.text2.setText(_translate("MainWindow", "............"))
        self.text3.setText(_translate("MainWindow", "............"))
        self.text4.setText(_translate("MainWindow", "............"))
        self.label_14.setText(_translate("MainWindow", "Güne Göre Nesne Fiyatı Hesaplama"))
        self.label_15.setText(_translate("MainWindow", "Tam Gün Sayısı :"))
        self.label_16.setText(_translate("MainWindow", "Fiyatı:"))
        self.label_17.setText(_translate("MainWindow", "Güncel Değerleri Giriniz.."))
        self.label_18.setText(_translate("MainWindow", "Gün/Saat/Dakika :"))
        self.costume_button.setText(_translate("MainWindow", "HESAPLA"))
        self.label_20.setText(_translate("MainWindow", "CLİENT BAŞLAT"))
        self.path_select_button.setText(_translate("MainWindow", "YOL SEÇ"))
        self.run_client_button.setText(_translate("MainWindow", "BAŞLAT"))
        self.label_21.setText(_translate("MainWindow", "Hasara Göre Tahmini Farm"))
        self.label_22.setText(_translate("MainWindow", "Map Seçiniz :"))
        self.label_23.setText(_translate("MainWindow", "Hasarınız :"))
        self.estimated_metin_value.setText(_translate("MainWindow", "Tahmini Metin Sayısı :"))
        self.estimated_revenue.setText(_translate("MainWindow", "Tahmini Kazanç(won) :"))
        self.estimated_farm_button.setText(_translate("MainWindow", "HESAPLA"))
        self.label_24.setText(_translate("MainWindow", "SONUÇLAR"))
        self.calculate_button.clicked.connect(self.price_calculate)
        self.toplu_calculate_button.clicked.connect(self.multi_item_price_calculate)
        self.costume_button.clicked.connect(self.costume_price)
        self.path_select_button.clicked.connect(self.path_finder)
        self.run_client_button.clicked.connect(self.run_metin2)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.call_combo()
    ui.call_make_zero()
    MainWindow.show()
    sys.exit(app.exec_())
