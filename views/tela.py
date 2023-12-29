# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tela.ui'
##
## Created by: Qt User Interface Compiler version 6.2.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QCheckBox,
    QFrame, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QProgressBar, QPushButton,
    QSizePolicy, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)
import assets.icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(705, 540)
        MainWindow.setMinimumSize(QSize(657, 540))
        MainWindow.setStyleSheet(u"QWidget{\n"
"background-color: rgb(0, 98, 98);\n"
"border-color: rgb(194, 194, 194);\n"
"}\n"
"\n"
"QMessageBox{\n"
"	color: rgb(255, 255, 255);\n"
"	text: bold 12px:\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(630, 200))
        self.frame.setMaximumSize(QSize(16777215, 16777215))
        self.frame.setStyleSheet(u"QFrame#frame{\n"
"	border: 1px solid rgb(255, 255, 255);\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 0))
        self.frame_2.setMaximumSize(QSize(16777215, 16777215))
        self.frame_2.setStyleSheet(u"QLineEdit{\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-color:rgb(0, 0, 108);\n"
"	border-radius: 10px;\n"
"	font: 75 10pt \"Cambria\";\n"
"	color: rgb(0, 0, 0);\n"
"	border: 2px solid rgb(170, 255, 255);\n"
"	text-align: left;\n"
"}\n"
"\n"
"QFrame{\n"
"	border: 1px solid rgb(255, 255, 255);\n"
"}\n"
"\n"
"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.txt_sku = QLineEdit(self.frame_2)
        self.txt_sku.setObjectName(u"txt_sku")
        self.txt_sku.setMinimumSize(QSize(0, 30))
        font = QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.txt_sku.setFont(font)
        self.txt_sku.setStyleSheet(u"")
        self.txt_sku.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.txt_sku)

        self.txt_centro = QLineEdit(self.frame_2)
        self.txt_centro.setObjectName(u"txt_centro")
        self.txt_centro.setMinimumSize(QSize(0, 30))
        self.txt_centro.setFont(font)
        self.txt_centro.setStyleSheet(u"")
        self.txt_centro.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.txt_centro)

        self.txt_deposito = QLineEdit(self.frame_2)
        self.txt_deposito.setObjectName(u"txt_deposito")
        self.txt_deposito.setMinimumSize(QSize(0, 30))
        self.txt_deposito.setStyleSheet(u"")
        self.txt_deposito.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.txt_deposito)

        self.txt_local = QLineEdit(self.frame_2)
        self.txt_local.setObjectName(u"txt_local")
        self.txt_local.setMinimumSize(QSize(0, 30))
        self.txt_local.setFont(font)
        self.txt_local.setStyleSheet(u"")
        self.txt_local.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.txt_local)


        self.horizontalLayout.addWidget(self.frame_2)

        self.frame_7 = QFrame(self.frame)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(385, 0))
        self.frame_7.setMaximumSize(QSize(385, 16777215))
        self.frame_7.setStyleSheet(u"QFrame#frame_7{\n"
"	border: 1px solid rgb(255, 255, 255);\n"
"}\n"
"QFrame#frame_10{\n"
"	border: 1px solid rgb(255, 255, 255);\n"
"}\n"
"\n"
"\n"
"")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.frame_7)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(200, 0))
        self.frame_3.setMaximumSize(QSize(200, 16777215))
        self.frame_3.setStyleSheet(u"QLineEdit{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-color:rgb(0, 0, 108);\n"
"	border-radius: 10px;\n"
"	font: 75 10pt \"Cambria\";\n"
"	color: rgb(0, 0, 0);\n"
"	border: 2px solid rgb(170, 255, 255);\n"
"}\n"
"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius:4px;\n"
"    border-color: rgb(234, 234, 234);\n"
"    font: bold 14px;\n"
"	padding-right: 5px;\n"
"	padding-left: 5px;\n"
"	text-align: left;\n"
"}\n"
"QPushButton:hover#btn_alterar{\n"
"	background-color:rgb(0, 130, 0);\n"
"}\n"
"QPushButton#btn_alterar{\n"
"	background-color: rgb(0, 195, 0);\n"
"}\n"
"QPushButton:hover#btn_lista{\n"
"	background-color:rgb(127, 127, 63);\n"
"}\n"
"QPushButton#btn_lista{\n"
"	background-color:rgb(218, 145, 0);\n"
"}\n"
"\n"
"\n"
"")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(9, 9, 9, 9)
        self.btn_alterar = QPushButton(self.frame_3)
        self.btn_alterar.setObjectName(u"btn_alterar")
        self.btn_alterar.setMinimumSize(QSize(150, 40))
        self.btn_alterar.setMaximumSize(QSize(150, 40))
        font1 = QFont()
        font1.setBold(True)
        font1.setItalic(False)
        self.btn_alterar.setFont(font1)
        self.btn_alterar.setLayoutDirection(Qt.RightToLeft)
        self.btn_alterar.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/icons/play.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_alterar.setIcon(icon)
        self.btn_alterar.setIconSize(QSize(25, 25))

        self.verticalLayout_5.addWidget(self.btn_alterar, 0, Qt.AlignHCenter)

        self.btn_lista = QPushButton(self.frame_3)
        self.btn_lista.setObjectName(u"btn_lista")
        self.btn_lista.setMinimumSize(QSize(150, 40))
        self.btn_lista.setMaximumSize(QSize(150, 40))
        self.btn_lista.setFont(font1)
        self.btn_lista.setLayoutDirection(Qt.RightToLeft)
        self.btn_lista.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/icons/plus-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_lista.setIcon(icon1)
        self.btn_lista.setIconSize(QSize(25, 25))

        self.verticalLayout_5.addWidget(self.btn_lista, 0, Qt.AlignHCenter)

        self.txt_se = QLineEdit(self.frame_3)
        self.txt_se.setObjectName(u"txt_se")
        self.txt_se.setMinimumSize(QSize(0, 0))
        self.txt_se.setMaximumSize(QSize(0, 0))
        self.txt_se.setFont(font)
        self.txt_se.setStyleSheet(u"")
        self.txt_se.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.txt_se)

        self.check_alterar = QCheckBox(self.frame_3)
        self.check_alterar.setObjectName(u"check_alterar")
        self.check_alterar.setMinimumSize(QSize(0, 0))
        self.check_alterar.setMaximumSize(QSize(16777215, 16777215))
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(True)
        self.check_alterar.setFont(font2)
        self.check_alterar.setStyleSheet(u"\n"
"color: rgb(255, 255, 255);\n"
"")

        self.verticalLayout_5.addWidget(self.check_alterar, 0, Qt.AlignHCenter)


        self.horizontalLayout_3.addWidget(self.frame_3)

        self.frame_10 = QFrame(self.frame_7)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMinimumSize(QSize(180, 0))
        self.frame_10.setMaximumSize(QSize(180, 16777215))
        self.frame_10.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 85, 0);\n"
"	color: rgb(255, 255, 255);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius:4px;\n"
"    border-color: rgb(234, 234, 234);\n"
"    font: bold 14px;\n"
"	padding-right: 5px;\n"
"	padding-left: 5px;\n"
"	text-align: left;\n"
"}\n"
"\n"
"QPushButton#btn_excluir_linha{\n"
"	background-color: rgb(255, 85, 0);	\n"
"}\n"
"\n"
"QPushButton:hover#btn_excluir_linha{\n"
"	background-color:rgb(173, 57, 0);\n"
"}\n"
"\n"
"QPushButton#btn_limpar_list{\n"
"	background-color: rgb(255, 0, 0);\n"
"}\n"
"\n"
"QPushButton:hover#btn_limpar_list{\n"
"	background-color:rgb(144, 0, 0);\n"
"}\n"
"\n"
"\n"
"QPushButton:hover#btn_gerar_excel{\n"
"	background-color:rgb(0, 0, 127);\n"
"}\n"
"\n"
"QPushButton#btn_gerar_excel{\n"
"	background-color:rgb(0, 0, 255);\n"
"}\n"
"\n"
"QPushButton:hover#btn_export_excel{\n"
"	background-color:rgb(0, 0, 127);\n"
"}\n"
"\n"
"QPushButton#btn_export_excel{\n"
"	background-color:rgb(0, 0, 255);\n"
"}")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_10)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(9, 9, -1, -1)
        self.btn_limpar_list = QPushButton(self.frame_10)
        self.btn_limpar_list.setObjectName(u"btn_limpar_list")
        self.btn_limpar_list.setMinimumSize(QSize(160, 30))
        self.btn_limpar_list.setMaximumSize(QSize(140, 30))
        self.btn_limpar_list.setFont(font1)
        self.btn_limpar_list.setLayoutDirection(Qt.RightToLeft)
        self.btn_limpar_list.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u":/icons/delete.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_limpar_list.setIcon(icon2)
        self.btn_limpar_list.setIconSize(QSize(20, 20))

        self.verticalLayout_4.addWidget(self.btn_limpar_list, 0, Qt.AlignHCenter)

        self.btn_excluir_linha = QPushButton(self.frame_10)
        self.btn_excluir_linha.setObjectName(u"btn_excluir_linha")
        self.btn_excluir_linha.setMinimumSize(QSize(160, 30))
        self.btn_excluir_linha.setMaximumSize(QSize(140, 30))
        self.btn_excluir_linha.setFont(font1)
        self.btn_excluir_linha.setLayoutDirection(Qt.RightToLeft)
        self.btn_excluir_linha.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u":/icons/trash-2.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_excluir_linha.setIcon(icon3)
        self.btn_excluir_linha.setIconSize(QSize(20, 20))

        self.verticalLayout_4.addWidget(self.btn_excluir_linha, 0, Qt.AlignHCenter)

        self.btn_export_excel = QPushButton(self.frame_10)
        self.btn_export_excel.setObjectName(u"btn_export_excel")
        self.btn_export_excel.setMinimumSize(QSize(160, 30))
        self.btn_export_excel.setMaximumSize(QSize(140, 30))
        self.btn_export_excel.setFont(font1)
        self.btn_export_excel.setLayoutDirection(Qt.RightToLeft)
        self.btn_export_excel.setStyleSheet(u"")
        icon4 = QIcon()
        icon4.addFile(u":/icons/upload.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_export_excel.setIcon(icon4)
        self.btn_export_excel.setIconSize(QSize(20, 20))

        self.verticalLayout_4.addWidget(self.btn_export_excel, 0, Qt.AlignHCenter)

        self.btn_gerar_excel = QPushButton(self.frame_10)
        self.btn_gerar_excel.setObjectName(u"btn_gerar_excel")
        self.btn_gerar_excel.setMinimumSize(QSize(160, 30))
        self.btn_gerar_excel.setMaximumSize(QSize(140, 30))
        self.btn_gerar_excel.setFont(font1)
        self.btn_gerar_excel.setLayoutDirection(Qt.RightToLeft)
        self.btn_gerar_excel.setStyleSheet(u"")
        icon5 = QIcon()
        icon5.addFile(u":/icons/download.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_gerar_excel.setIcon(icon5)
        self.btn_gerar_excel.setIconSize(QSize(20, 20))

        self.verticalLayout_4.addWidget(self.btn_gerar_excel, 0, Qt.AlignHCenter)


        self.horizontalLayout_3.addWidget(self.frame_10)


        self.horizontalLayout.addWidget(self.frame_7)


        self.verticalLayout_3.addWidget(self.frame)

        self.frame_6 = QFrame(self.centralwidget)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(630, 305))
        self.frame_6.setStyleSheet(u"QFrame#frame_6{\n"
"	border: 1px solid rgb(255, 255, 255);\n"
"}\n"
"")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_6)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(3, 0, 3, 0)
        self.label = QLabel(self.frame_6)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QSize(0, 40))
        self.label.setMaximumSize(QSize(16777215, 40))
        font3 = QFont()
        font3.setPointSize(14)
        font3.setBold(True)
        font3.setItalic(False)
        self.label.setFont(font3)
        self.label.setLayoutDirection(Qt.RightToLeft)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"\n"
"")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)

        self.tb_alt_massa = QTableWidget(self.frame_6)
        if (self.tb_alt_massa.columnCount() < 7):
            self.tb_alt_massa.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.tb_alt_massa.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tb_alt_massa.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tb_alt_massa.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tb_alt_massa.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tb_alt_massa.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tb_alt_massa.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tb_alt_massa.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.tb_alt_massa.setObjectName(u"tb_alt_massa")
        font4 = QFont()
        font4.setPointSize(11)
        font4.setBold(True)
        font4.setStyleStrategy(QFont.PreferDefault)
        self.tb_alt_massa.setFont(font4)
        self.tb_alt_massa.setLayoutDirection(Qt.LeftToRight)
        self.tb_alt_massa.setAutoFillBackground(False)
        self.tb_alt_massa.setStyleSheet(u"QHeaderView::section{\n"
"	background-color:rgb(0, 76, 76);\n"
"	color: rgb(255, 255, 255);\n"
"	font: 75 11pt \"Cambria\";\n"
"}\n"
"\n"
"\n"
"QTableWidget{\n"
"	\n"
"	background-color: rgb(221, 221, 221);\n"
"}\n"
"")
        self.tb_alt_massa.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.tb_alt_massa.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.tb_alt_massa.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.tb_alt_massa.setAutoScroll(True)
        self.tb_alt_massa.setAutoScrollMargin(21)
        self.tb_alt_massa.setAlternatingRowColors(False)
        self.tb_alt_massa.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.tb_alt_massa.setGridStyle(Qt.SolidLine)
        self.tb_alt_massa.setSortingEnabled(False)
        self.tb_alt_massa.setRowCount(0)
        self.tb_alt_massa.horizontalHeader().setVisible(True)
        self.tb_alt_massa.horizontalHeader().setCascadingSectionResizes(False)
        self.tb_alt_massa.horizontalHeader().setDefaultSectionSize(150)
        self.tb_alt_massa.horizontalHeader().setHighlightSections(True)
        self.tb_alt_massa.horizontalHeader().setProperty("showSortIndicator", False)
        self.tb_alt_massa.horizontalHeader().setStretchLastSection(False)
        self.tb_alt_massa.verticalHeader().setCascadingSectionResizes(False)

        self.verticalLayout_2.addWidget(self.tb_alt_massa)

        self.prog_bar_pos = QProgressBar(self.frame_6)
        self.prog_bar_pos.setObjectName(u"prog_bar_pos")
        self.prog_bar_pos.setMaximumSize(QSize(16777215, 22))
        font5 = QFont()
        font5.setPointSize(12)
        font5.setBold(True)
        self.prog_bar_pos.setFont(font5)
        self.prog_bar_pos.setStyleSheet(u"background-color: rgb(112, 112, 112);\n"
"color: rgb(255, 255, 255);")
        self.prog_bar_pos.setValue(24)
        self.prog_bar_pos.setAlignment(Qt.AlignCenter)
        self.prog_bar_pos.setOrientation(Qt.Horizontal)

        self.verticalLayout_2.addWidget(self.prog_bar_pos)


        self.verticalLayout_3.addWidget(self.frame_6)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.txt_sku.setPlaceholderText(QCoreApplication.translate("MainWindow", u"SKU", None))
        self.txt_centro.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CENTRO", None))
        self.txt_deposito.setPlaceholderText(QCoreApplication.translate("MainWindow", u"DEP\u00d3SITO", None))
        self.txt_local.setPlaceholderText(QCoreApplication.translate("MainWindow", u"NOVA LOCALIZA\u00c7\u00c3O", None))
        self.btn_alterar.setText(QCoreApplication.translate("MainWindow", u"ALTERAR SAP", None))
        self.btn_lista.setText(QCoreApplication.translate("MainWindow", u"ADD LISTA", None))
        self.txt_se.setPlaceholderText(QCoreApplication.translate("MainWindow", u"N\u00b0 SE", None))
        self.check_alterar.setText(QCoreApplication.translate("MainWindow", u"ALTERA\u00c7\u00c3O MASSIVA", None))
        self.btn_limpar_list.setText(QCoreApplication.translate("MainWindow", u"LIMPAR LISTA", None))
        self.btn_excluir_linha.setText(QCoreApplication.translate("MainWindow", u"EXCLUIR LINHA", None))
#if QT_CONFIG(tooltip)
        self.btn_export_excel.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:400;\">Utilizar est\u00e1 op\u00e7\u00e3o para carregar uma lista em excel.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.btn_export_excel.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.btn_export_excel.setText(QCoreApplication.translate("MainWindow", u"CARREGAR EXCEL", None))
#if QT_CONFIG(tooltip)
        self.btn_gerar_excel.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:400;\">Utilizar est\u00e1 op\u00e7\u00e3o para gerar um arquivo em excel das altera\u00e7\u00f5es realizadas.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_gerar_excel.setText(QCoreApplication.translate("MainWindow", u"GERAR EXCEL", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Lista para Altera\u00e7\u00e3o em Massa", None))
        ___qtablewidgetitem = self.tb_alt_massa.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"SKU", None));
        ___qtablewidgetitem1 = self.tb_alt_massa.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"CENTRO", None));
        ___qtablewidgetitem2 = self.tb_alt_massa.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"DEP\u00d3SITO", None));
        ___qtablewidgetitem3 = self.tb_alt_massa.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"NOVA LOCALIZA\u00c7\u00c3O", None));
        ___qtablewidgetitem4 = self.tb_alt_massa.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"LOCAL ANTIGO", None));
        ___qtablewidgetitem5 = self.tb_alt_massa.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"STATUS", None));
        ___qtablewidgetitem6 = self.tb_alt_massa.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"ERRO", None));
    # retranslateUi

