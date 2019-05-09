# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HMI.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_HMI(object):
    def setupUi(self, HMI):
        HMI.setObjectName("HMI")
        HMI.resize(599, 512)
        HMI.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame = QtWidgets.QFrame(HMI)
        self.frame.setGeometry(QtCore.QRect(0, 0, 601, 521))
        self.frame.setStyleSheet("background-color: rgb(208, 208, 208);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_16 = QtWidgets.QLabel(self.frame)
        self.label_16.setGeometry(QtCore.QRect(130, 0, 361, 41))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("color: rgb(213, 0, 106);\n"
                                    "font: 18pt \"楷体\";\n"
                                    "")
        self.label_16.setObjectName("label_16")
        self.rst_key = QtWidgets.QPushButton(self.frame)
        self.rst_key.setGeometry(QtCore.QRect(30, 340, 93, 39))
        self.rst_key.setStyleSheet("color: rgb(0, 0, 0);\n"
                                   "background-color: rgb(255, 255, 127);\n"
                                   "font: 18pt \"隶书\";\n"
                                   "\n"
                                   "")
        self.rst_key.setCheckable(False)
        self.rst_key.setChecked(False)
        self.rst_key.setProperty("name", "")
        self.rst_key.setObjectName("rst_key")
        self.mes_lab3 = QtWidgets.QLabel(self.frame)
        self.mes_lab3.setGeometry(QtCore.QRect(30, 280, 411, 31))
        self.mes_lab3.setStyleSheet("font: 12pt \"楷体\";\n"
                                    "background-color: rgb(208, 208, 208);\n"
                                    "text-decoration: underline;")
        self.mes_lab3.setText("")
        self.mes_lab3.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.mes_lab3.setObjectName("mes_lab3")
        self.len_choose_key = QtWidgets.QPushButton(self.frame)
        self.len_choose_key.setGeometry(QtCore.QRect(20, 80, 161, 51))
        self.len_choose_key.setStyleSheet("color: rgb(0, 0, 0);\n"
                                          "\n"
                                          "font: 12pt \"楷体\";")
        self.len_choose_key.setCheckable(True)
        self.len_choose_key.setObjectName("len_choose_key")
        self.run_key = QtWidgets.QPushButton(self.frame)
        self.run_key.setGeometry(QtCore.QRect(200, 230, 141, 41))
        self.run_key.setStyleSheet("color: rgb(0, 0, 0);\n"
                                   "\n"
                                   "font: 12pt \"楷体\";")
        self.run_key.setCheckable(True)
        self.run_key.setObjectName("run_key")
        self.label_13 = QtWidgets.QLabel(self.frame)
        self.label_13.setGeometry(QtCore.QRect(210, 90, 121, 20))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.label_10 = QtWidgets.QLabel(self.frame)
        self.label_10.setGeometry(QtCore.QRect(210, 180, 121, 20))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.mes_lab1 = QtWidgets.QLabel(self.frame)
        self.mes_lab1.setGeometry(QtCore.QRect(340, 80, 101, 41))
        self.mes_lab1.setStyleSheet("background-color: rgb(159, 239, 239);")
        self.mes_lab1.setText("")
        self.mes_lab1.setAlignment(QtCore.Qt.AlignCenter)
        self.mes_lab1.setObjectName("mes_lab1")
        self.mes_lab2 = QtWidgets.QLabel(self.frame)
        self.mes_lab2.setGeometry(QtCore.QRect(340, 170, 101, 41))
        self.mes_lab2.setStyleSheet("background-color: rgb(159, 239, 239);")
        self.mes_lab2.setText("")
        self.mes_lab2.setAlignment(QtCore.Qt.AlignCenter)
        self.mes_lab2.setObjectName("mes_lab2")
        self.next_key = QtWidgets.QPushButton(self.frame)
        self.next_key.setGeometry(QtCore.QRect(170, 339, 93, 39))
        self.next_key.setStyleSheet("color: rgb(0, 0, 0);\n"
                                    "background-color: rgb(0, 170, 127);\n"
                                    "font: 14pt \"隶书\";\n"
                                    "\n"
                                    "")
        self.next_key.setCheckable(True)
        self.next_key.setChecked(False)
        self.next_key.setProperty("name", "")
        self.next_key.setObjectName("next_key")
        self.zrn_key = QtWidgets.QPushButton(self.frame)
        self.zrn_key.setGeometry(QtCore.QRect(310, 340, 93, 39))
        self.zrn_key.setStyleSheet("color: rgb(0, 0, 0);\n"
                                   "background-color: rgb(0, 170, 127);\n"
                                   "font: 18pt \"隶书\";\n"
                                   "\n"
                                   "")
        self.zrn_key.setCheckable(False)
        self.zrn_key.setChecked(False)
        self.zrn_key.setProperty("name", "")
        self.zrn_key.setObjectName("zrn_key")
        self.photo = QtWidgets.QLabel(self.frame)
        self.photo.setGeometry(QtCore.QRect(447, 60, 141, 191))
        self.photo.setObjectName("photo")
        self.auto_key = QtWidgets.QPushButton(self.frame)
        self.auto_key.setGeometry(QtCore.QRect(460, 270, 121, 61))
        self.auto_key.setStyleSheet("color: rgb(0, 0, 0);\n"
                                    "font: 18pt \"隶书\";\n"
                                    "background-color: rgb(0, 170, 127);\n"
                                    "\n"
                                    "")
        self.auto_key.setCheckable(True)
        self.auto_key.setChecked(False)
        self.auto_key.setProperty("name", "")
        self.auto_key.setObjectName("auto_key")
        self.mes_lab5 = QtWidgets.QLabel(self.frame)
        self.mes_lab5.setGeometry(QtCore.QRect(20, 230, 161, 31))
        self.mes_lab5.setStyleSheet("font: 12pt \"楷体\";\n"
                                    "background-color: rgb(208, 208, 208);\n"
                                    "text-decoration: underline;")
        self.mes_lab5.setText("")
        self.mes_lab5.setAlignment(QtCore.Qt.AlignCenter)
        self.mes_lab5.setObjectName("mes_lab5")
        self.mes_lab4 = QtWidgets.QLabel(self.frame)
        self.mes_lab4.setGeometry(QtCore.QRect(20, 140, 161, 31))
        self.mes_lab4.setStyleSheet("font: 12pt \"楷体\";\n"
                                    "background-color: rgb(208, 208, 208);\n"
                                    "text-decoration: underline;")
        self.mes_lab4.setText("")
        self.mes_lab4.setAlignment(QtCore.Qt.AlignCenter)
        self.mes_lab4.setObjectName("mes_lab4")
        self.hz_choose_key = QtWidgets.QPushButton(self.frame)
        self.hz_choose_key.setGeometry(QtCore.QRect(20, 170, 161, 51))
        self.hz_choose_key.setStyleSheet("color: rgb(0, 0, 0);\n"
                                         "\n"
                                         "font: 12pt \"楷体\";")
        self.hz_choose_key.setCheckable(True)
        self.hz_choose_key.setObjectName("hz_choose_key")
        self.hold_key = QtWidgets.QPushButton(self.frame)
        self.hold_key.setGeometry(QtCore.QRect(460, 350, 121, 61))
        self.hold_key.setStyleSheet("color: rgb(0, 0, 0);\n"
                                    "font: 18pt \"隶书\";\n"
                                    "background-color: rgb(218, 218, 0);\n"
                                    "\n"
                                    "")
        self.hold_key.setCheckable(True)
        self.hold_key.setChecked(False)
        self.hold_key.setProperty("name", "")
        self.hold_key.setObjectName("hold_key")
        self.mes_lab6 = QtWidgets.QLabel(self.frame)
        self.mes_lab6.setGeometry(QtCore.QRect(20, 390, 411, 31))
        self.mes_lab6.setStyleSheet("font: 12pt \"楷体\";\n"
                                    "background-color: rgb(208, 208, 208);\n"
                                    "text-decoration: underline;")
        self.mes_lab6.setText("")
        self.mes_lab6.setAlignment(QtCore.Qt.AlignCenter)
        self.mes_lab6.setObjectName("mes_lab6")
        self.groupBox = QtWidgets.QGroupBox(self.frame)
        self.groupBox.setGeometry(QtCore.QRect(30, 420, 561, 71))
        self.groupBox.setStyleSheet("background-color: rgb(234, 255, 255);")
        self.groupBox.setObjectName("groupBox")
        self.splitter = QtWidgets.QSplitter(self.groupBox)
        self.splitter.setGeometry(QtCore.QRect(20, 30, 501, 39))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.D_key1 = QtWidgets.QPushButton(self.splitter)
        self.D_key1.setStyleSheet("color: rgb(0, 0, 0);\n"
                                  "background-color: rgb(255, 25, 127);\n"
                                  "font: 12pt \"隶书\";\n"
                                  "\n"
                                  "")
        self.D_key1.setCheckable(False)
        self.D_key1.setChecked(False)
        self.D_key1.setProperty("name", "")
        self.D_key1.setObjectName("D_key1")
        self.D_key2 = QtWidgets.QPushButton(self.splitter)
        self.D_key2.setStyleSheet("color: rgb(0, 0, 0);\n"
                                  "background-color: rgb(255, 170, 127);\n"
                                  "font: 12pt \"隶书\";\n"
                                  "\n"
                                  "")
        self.D_key2.setCheckable(False)
        self.D_key2.setChecked(False)
        self.D_key2.setProperty("name", "")
        self.D_key2.setObjectName("D_key2")
        self.H_key1 = QtWidgets.QPushButton(self.splitter)
        self.H_key1.setStyleSheet("color: rgb(0, 0, 0);\n"
                                  "background-color: rgb(255, 25, 127);\n"
                                  "font: 12pt \"隶书\";\n"
                                  "\n"
                                  "")
        self.H_key1.setCheckable(False)
        self.H_key1.setChecked(False)
        self.H_key1.setProperty("name", "")
        self.H_key1.setObjectName("H_key1")
        self.H_key2 = QtWidgets.QPushButton(self.splitter)
        self.H_key2.setStyleSheet("color: rgb(0, 0, 0);\n"
                                  "background-color: rgb(255, 170, 127);\n"
                                  "font: 12pt \"隶书\";\n"
                                  "\n"
                                  "")
        self.H_key2.setCheckable(False)
        self.H_key2.setChecked(False)
        self.H_key2.setProperty("name", "")
        self.H_key2.setObjectName("H_key2")
        self.ok_key = QtWidgets.QPushButton(self.splitter)
        self.ok_key.setStyleSheet("color: rgb(0, 0, 0);\n"
                                  "background-color: rgb(170, 255, 255);\n"
                                  "font: 16pt \"隶书\";\n"
                                  "\n"
                                  "")
        self.ok_key.setCheckable(False)
        self.ok_key.setChecked(False)
        self.ok_key.setProperty("name", "")
        self.ok_key.setObjectName("ok_key")
        self.label_16.raise_()
        self.rst_key.raise_()
        self.mes_lab3.raise_()
        self.len_choose_key.raise_()
        self.run_key.raise_()
        self.label_13.raise_()
        self.label_10.raise_()
        self.mes_lab1.raise_()
        self.mes_lab2.raise_()
        self.zrn_key.raise_()
        self.next_key.raise_()
        self.photo.raise_()
        self.auto_key.raise_()
        self.mes_lab5.raise_()
        self.mes_lab4.raise_()
        self.hz_choose_key.raise_()
        self.hold_key.raise_()
        self.mes_lab6.raise_()
        self.groupBox.raise_()

        self.retranslateUi(HMI)
        QtCore.QMetaObject.connectSlotsByName(HMI)

    def retranslateUi(self, HMI):
        _translate = QtCore.QCoreApplication.translate
        HMI.setWindowTitle(_translate("HMI", "HMI"))
        self.label_16.setText(_translate("HMI", "AMC-control-interface"))
        self.rst_key.setText(_translate("HMI", "复位"))
        self.len_choose_key.setText(_translate("HMI", "长度选择"))
        self.run_key.setText(_translate("HMI", "运行状态"))
        self.label_13.setText(_translate("HMI", "当前生产序号"))
        self.label_10.setText(_translate("HMI", "当前检测序号"))
        self.next_key.setText(_translate("HMI", "NEXT"))
        self.zrn_key.setText(_translate("HMI", "回零"))
        self.photo.setText(_translate("HMI", "TextLabel"))
        self.auto_key.setText(_translate("HMI", "全自动"))
        self.hz_choose_key.setText(_translate("HMI", "检测频率"))
        self.hold_key.setText(_translate("HMI", "暂停"))
        self.groupBox.setTitle(_translate("HMI", "设置界面"))
        self.D_key1.setText(_translate("HMI", "直径下限"))
        self.D_key2.setText(_translate("HMI", "直径上限"))
        self.H_key1.setText(_translate("HMI", "高度下限"))
        self.H_key2.setText(_translate("HMI", "高度上限"))
        self.ok_key.setText(_translate("HMI", "尺寸确认"))
