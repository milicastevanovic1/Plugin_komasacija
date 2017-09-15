# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Komasacija_dialog_base.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

import os
from PyQt4 import QtCore, QtGui, uic
import csv
from PyQt4.QtGui import QMessageBox
from qgis.core import QgsVectorLayer, QgsMapLayerRegistry
from qgis.analysis import QgsOverlayAnalyzer



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

FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'Komasacija_dialog_base.ui'))

class Ui_Komasacija(QtGui.QDialog, FORM_CLASS):
    def __init__(self, parent=None, iface=None):
        """Constructor."""
        super(Ui_Komasacija, self).__init__(parent)
        self.setupUi(self)
        self.iface = iface

        self.staroStanje = dict()
        self.novoStanje = dict()
        self.parcele_klase = None

        QtCore.QObject.connect(self.btnRacunaj, QtCore.SIGNAL('clicked()'), self.calculate)
        QtCore.QObject.connect(self.sracunajStanje, QtCore.SIGNAL('clicked()'), self.sracunaj_fond_mase)
        QtCore.QObject.connect(self.btnPregledKnjigeFonda, QtCore.SIGNAL('clicked()'), self.tabela_fond_mase)



    def setupUi(self, Komasacija):
        Komasacija.setObjectName(_fromUtf8("Komasacija"))
        Komasacija.setEnabled(True)
        Komasacija.resize(583, 462)
        Komasacija.setMinimumSize(QtCore.QSize(583, 462))
        Komasacija.setMaximumSize(QtCore.QSize(583, 462))
        self.label_2 = QtGui.QLabel(Komasacija)
        self.label_2.setGeometry(QtCore.QRect(70, 180, 111, 31))
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Komasacija)
        self.label_3.setGeometry(QtCore.QRect(70, 220, 111, 31))
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(Komasacija)
        self.label_4.setGeometry(QtCore.QRect(290, 180, 111, 31))
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_6 = QtGui.QLabel(Komasacija)
        self.label_6.setGeometry(QtCore.QRect(290, 220, 111, 31))
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.klasa1 = QtGui.QLineEdit(Komasacija)
        self.klasa1.setGeometry(QtCore.QRect(190, 180, 91, 31))
        self.klasa1.setInputMask(_fromUtf8(""))
        self.klasa1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.klasa1.setObjectName(_fromUtf8("klasa1"))
        self.klasa2 = QtGui.QLineEdit(Komasacija)
        self.klasa2.setGeometry(QtCore.QRect(190, 220, 91, 31))
        self.klasa2.setInputMask(_fromUtf8(""))
        self.klasa2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.klasa2.setObjectName(_fromUtf8("klasa2"))
        self.klasa3 = QtGui.QLineEdit(Komasacija)
        self.klasa3.setGeometry(QtCore.QRect(410, 180, 91, 31))
        self.klasa3.setInputMask(_fromUtf8(""))
        self.klasa3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.klasa3.setObjectName(_fromUtf8("klasa3"))
        self.klasa4 = QtGui.QLineEdit(Komasacija)
        self.klasa4.setGeometry(QtCore.QRect(410, 220, 91, 31))
        self.klasa4.setInputMask(_fromUtf8(""))
        self.klasa4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.klasa4.setObjectName(_fromUtf8("klasa4"))



        self.groupBox = QtGui.QGroupBox(Komasacija)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 561, 151))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.shpPlodno = QtGui.QComboBox(self.groupBox)
        self.shpPlodno.setGeometry(QtCore.QRect(180, 21, 361, 31))
        self.shpPlodno.setObjectName(_fromUtf8("shpPlodno"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(0, 20, 171, 31))
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(0, 60, 171, 31))
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.shpNeplodno = QtGui.QComboBox(self.groupBox)
        self.shpNeplodno.setGeometry(QtCore.QRect(180, 60, 361, 31))
        self.shpNeplodno.setObjectName(_fromUtf8("shpNeplodno"))
        self.shpKlase = QtGui.QComboBox(self.groupBox)
        self.shpKlase.setGeometry(QtCore.QRect(180, 100, 361, 31))
        self.shpKlase.setObjectName(_fromUtf8("shpKlase"))
        self.label_11 = QtGui.QLabel(self.groupBox)
        self.label_11.setGeometry(QtCore.QRect(0, 100, 171, 31))
        self.label_11.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.groupBox_2 = QtGui.QGroupBox(Komasacija)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 260, 561, 151))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.btnRacunaj = QtGui.QPushButton(self.groupBox_2)
        self.btnRacunaj.setGeometry(QtCore.QRect(50, 20, 100, 40))
        self.btnRacunaj.setObjectName(_fromUtf8("btnRacunaj"))
        self.chooseValueAttributeParceleKlase = QtGui.QComboBox(self.groupBox_2)
        self.chooseValueAttributeParceleKlase.setGeometry(QtCore.QRect(160, 20, 100, 40))
        self.chooseValueAttributeParceleKlase.setObjectName(_fromUtf8("chooseValueAttributeParceleKlase"))
        self.chooseGroupBy = QtGui.QComboBox(self.groupBox_2)
        self.chooseGroupBy.setGeometry(QtCore.QRect(270, 20, 100, 40))
        self.chooseGroupBy.setObjectName(_fromUtf8("chooseGroupBy"))
        self.sracunajStanje = QtGui.QPushButton(self.groupBox_2)
        self.sracunajStanje.setGeometry(QtCore.QRect(380, 20, 100, 40))
        self.sracunajStanje.setObjectName(_fromUtf8("sracunajStanje"))
        self.label_koeficijentUmanjenja = QtGui.QLabel(self.groupBox_2)
        self.label_koeficijentUmanjenja.setGeometry(QtCore.QRect(390, 220, 111, 31))
        self.label_koeficijentUmanjenja.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_koeficijentUmanjenja.setObjectName(_fromUtf8("label_koeficijentUmanjenja"))
        self.btnPregledKnjigeFonda = QtGui.QPushButton(self.groupBox_2)
        self.btnPregledKnjigeFonda.setGeometry(QtCore.QRect(210, 70, 131, 31))
        self.btnPregledKnjigeFonda.setObjectName(_fromUtf8("btnPregledKnjigeFonda"))
        self.label_8 = QtGui.QLabel(self.groupBox_2)
        self.label_8.setGeometry(QtCore.QRect(30, 70, 171, 31))
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName(_fromUtf8("label_8"))


        self.retranslateUi(Komasacija)
        QtCore.QMetaObject.connectSlotsByName(Komasacija)
        Komasacija.setTabOrder(self.shpPlodno, self.shpNeplodno)
        Komasacija.setTabOrder(self.shpNeplodno, self.shpKlase)
        Komasacija.setTabOrder(self.shpKlase, self.klasa1)
        Komasacija.setTabOrder(self.klasa1, self.klasa3)
        Komasacija.setTabOrder(self.klasa3, self.klasa2)
        Komasacija.setTabOrder(self.klasa2, self.klasa4)


        Komasacija.setTabOrder(self.klasa4, self.btnRacunaj)
        Komasacija.setTabOrder(self.btnRacunaj, self.btnPregledKnjigeFonda)



    def retranslateUi(self, Komasacija):
        Komasacija.setWindowTitle(_translate("Komasacija", "Komasacija", None))
        self.label_2.setText(_translate("Komasacija", "Klasa 1 vrednost:", None))
        self.label_3.setText(_translate("Komasacija", "Klasa 2 vrednost:", None))
        self.label_4.setText(_translate("Komasacija", "Klasa 3 vrednost:", None))
        self.label_6.setText(_translate("Komasacija", "Klasa 4 vrednost:", None))
        self.klasa1.setText(_translate("Komasacija", "1", None))
        self.klasa2.setText(_translate("Komasacija", "2", None))
        self.klasa3.setText(_translate("Komasacija", "3", None))
        self.klasa4.setText(_translate("Komasacija", "4", None))

        self.label_koeficijentUmanjenja.setText(_translate("Komasacija", "Ovde ce biti sracunat koef umanjenja", None))

        self.groupBox.setTitle(_translate("Komasacija", "Ulazni podaci", None))
        self.label.setText(_translate("Komasacija", "Parcele Shape file:", None))
        self.label_5.setText(_translate("Komasacija", "Neplodno zemljiste Shape file:", None))
        self.label_11.setText(_translate("Komasacija", "Klase Shape file:", None))
        self.groupBox_2.setTitle(_translate("Komasacija", "Kalkulacije", None))
        self.btnRacunaj.setText(_translate("Komasacija", "Preklopi lejere", None))
        self.btnPregledKnjigeFonda.setText(_translate("Komasacija", "Pregled", None))
        self.label_8.setText(_translate("Komasacija", "Knjiga fonda komasacione mase:", None))
        self.sracunajStanje.setText(_translate("Komasacija", "Staro i novo stanje", None))

    def calculate(self):

        k1 = float(self.klasa1.text())
        k2 = float(self.klasa2.text())
        k3 = float(self.klasa3.text())
        k4 = float(self.klasa4.text())

        # Inicijalizacija lejera iz drop down menija
        layer_name_plodno = self.shpPlodno.currentText()
        layer_name_neplodno = self.shpNeplodno.currentText()
        layer_name_klase = self.shpKlase.currentText()
        layer_plodno, layer_neplodno, layer_klase = None, None, None
        for layer in self.iface.mapCanvas().layers():
          if layer.name () == layer_name_plodno:
              layer_plodno = layer
          elif layer.name() == layer_name_neplodno:
              layer_neplodno = layer
          elif layer.name() == layer_name_klase:
              layer_klase = layer

        # kontrola ucitavanja lejera
        if layer_neplodno is None or layer_klase is None or layer_plodno is None:
            QMessageBox.about(self, "Error", "Neki lejer nije lepo ucitan.")
            return

        # Pretpostavka da su svi u istom koordinatnom sistemu
        overlayAnalyzer = QgsOverlayAnalyzer()

        # Presek lejera plodnog i lejera klase
        # Klik na dugme za biranje direktorijuma u kome ce biti kreirani shp fajlovi. Otvara se Dialog i bira se direktorijum.
        directory = QtGui.QFileDialog.getExistingDirectory(self, 'Select file directory')

        overlayAnalyzer.intersection(layer_plodno, layer_klase, os.path.join(directory, 'layer_plodno_klase.shp'))
        parcele_klase = self.iface.addVectorLayer(os.path.join(directory, 'layer_plodno_klase.shp'), 'layer_plodno_klase', 'ogr')
        dp_parcele_klase = parcele_klase.dataProvider()
        for field in dp_parcele_klase.fields():
            self.chooseValueAttributeParceleKlase.addItem(field.name())
            self.chooseGroupBy.addItem(field.name())

        self.parcele_klase = parcele_klase
#
        overlayAnalyzer.intersection(parcele_klase, layer_neplodno, os.path.join(directory, 'layer_plodno_klase_neplodno.shp'))
        parcele_klase_neplodno = self.iface.addVectorLayer(os.path.join(directory, 'layer_plodno_klase_neplodno.shp'), 'layer_plodno_klase_neplodno', 'ogr')

        self.parcele_klase_neplodno = parcele_klase_neplodno


    def sracunaj_fond_mase(self):
        if self.parcele_klase is None:
            QMessageBox.about(self, "Error", "Niste preklopili pracele")
            return
        k1 = float(self.klasa1.text())
        k2 = float(self.klasa2.text())
        k3 = float(self.klasa3.text())
        k4 = float(self.klasa4.text())
        niz_koeficijenata = [k1, k2, k3, k4]
        staroStanje = dict()
        atribut_klase = self.chooseValueAttributeParceleKlase.currentText()
        atribut_group_by = self.chooseGroupBy.currentText()
        staroStanjeVrednost = 0
        for feature in self.parcele_klase.getFeatures():
            povrsina = feature.geometry().area()
            vlasnik = feature[atribut_group_by]
            klasa = feature[atribut_klase]

            koef_klase = niz_koeficijenata[klasa - 1]
            vrednost_featura = povrsina * koef_klase
            staroStanjeVrednost += vrednost_featura
            # QMessageBox.about(self, "msg1", str(vlasnik) + str(klasa))
            vrednost_vlasnika = staroStanje.get(vlasnik, None)
            if vrednost_vlasnika is None:
                staroStanje[vlasnik] = vrednost_featura
                # QMessageBox.about(self, "msg2", str(vlasnik) + str(klasa))
            else:
                # QMessageBox.about(self, "msg3", str(vlasnik) + str(klasa))
                vrednost_vlasnika += vrednost_featura
                staroStanje[vlasnik] = vrednost_featura

        self.staroStanje = staroStanje
        self.staroStanjeVrednost = staroStanjeVrednost
        oduzetaVrednost = 0
        for feature in self.parcele_klase_neplodno.getFeatures():
            povrsina = feature.geometry().area()
            vlasnik = feature[atribut_group_by]
            klasa = feature[atribut_klase]

            koef_klase = niz_koeficijenata[klasa - 1]
            vrednost_featura = povrsina * koef_klase
            oduzetaVrednost += vrednost_featura

        self.koeficijentUmanjenja = (self.staroStanjeVrednost - oduzetaVrednost) / self.staroStanjeVrednost
        self.label_koeficijentUmanjenja.setText(str(self.koeficijentUmanjenja))

        CSVdirectory = QtGui.QFileDialog.getExistingDirectory(self, 'Select csv directory')
        self.putanja_csv = os.path.join(CSVdirectory, 'staro_stanje_novostanje.csv')
        with open(self.putanja_csv, 'w') as f:  # Just use 'w' mode in 3.x
            fieldnames = ['Ime Vlasnika', 'Staro Stanje', "Novo Stanje"]
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for vlasnik, vrednost in self.staroStanje.items():
                writer.writerow({'Ime Vlasnika': vlasnik,
                                 'Staro Stanje': vrednost,
                                 'Novo Stanje': vrednost * self.koeficijentUmanjenja})

        QMessageBox.about(self, "Info", "Racunanje starog i novog stanja je keirano uspesno")

    def tabela_fond_mase(self):
        d = QtGui.QDialog()
        d.setWindowTitle("Fond Mase")
        model = QtGui.QStandardItemModel(d)

        tableView = QtGui.QTableView(d)
        tableView.setModel(model)
        tableView.horizontalHeader().setResizeMode(QtGui.QHeaderView.Stretch)

        with open(self.putanja_csv, 'r') as f:
            header = True
            for row in csv.reader(f):
                if header:
                    model.setHorizontalHeaderLabels(row)
                    header = False
                    continue
                items = [
                    QtGui.QStandardItem(field)
                    for field in row
                    ]
                model.appendRow(items)
        d.exec_()