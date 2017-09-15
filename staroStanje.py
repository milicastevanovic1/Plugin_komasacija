# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'staroStanje.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_staroStanje(object):
    def setupUi(self, staroStanje):
        staroStanje.setObjectName(_fromUtf8("staroStanje"))
        staroStanje.resize(603, 280)
        staroStanje.setMinimumSize(QtCore.QSize(603, 280))
        font = QtGui.QFont()
        font.setItalic(True)
        staroStanje.setFont(font)
        self.tableStaroStanje = QtGui.QTableWidget(staroStanje)
        self.tableStaroStanje.setGeometry(QtCore.QRect(10, 40, 581, 231))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(58)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableStaroStanje.sizePolicy().hasHeightForWidth())
        self.tableStaroStanje.setSizePolicy(sizePolicy)
        self.tableStaroStanje.setMinimumSize(QtCore.QSize(581, 231))
        self.tableStaroStanje.setObjectName(_fromUtf8("tableStaroStanje"))
        self.tableStaroStanje.setColumnCount(3)
        self.tableStaroStanje.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableStaroStanje.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableStaroStanje.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableStaroStanje.setHorizontalHeaderItem(2, item)
        self.label = QtGui.QLabel(staroStanje)
        self.label.setGeometry(QtCore.QRect(10, 10, 581, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Calibri"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(staroStanje)
        QtCore.QMetaObject.connectSlotsByName(staroStanje)

    def retranslateUi(self, staroStanje):
        staroStanje.setWindowTitle(_translate("staroStanje", "Staro Stanje", None))
        item = self.tableStaroStanje.horizontalHeaderItem(0)
        item.setText(_translate("staroStanje", "vlasnik", None))
        item = self.tableStaroStanje.horizontalHeaderItem(1)
        item.setText(_translate("staroStanje", "vrednost", None))
        item = self.tableStaroStanje.horizontalHeaderItem(2)
        item.setText(_translate("staroStanje", "[vrednost * koeficijentUmanjenja]", None))
        self.label.setText(_translate("staroStanje", "STARO STANJE", None))

