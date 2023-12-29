# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SelectColumns.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_AtribuirCampos(object):
    def setupUi(self, AtribuirCampos):
        if not AtribuirCampos.objectName():
            AtribuirCampos.setObjectName(u"AtribuirCampos")
        AtribuirCampos.resize(450, 228)
        AtribuirCampos.setMinimumSize(QSize(450, 228))
        AtribuirCampos.setMaximumSize(QSize(450, 228))
        AtribuirCampos.setStyleSheet(u"QWidget{	\n"
"	border-style: ridge;\n"
"    border-width: 2px;\n"
"    border-color: rgb(255, 255, 255);\n"
"	background-color: rgb(159, 159, 159);\n"
"	}\n"
"QFrame{\n"
"	background-color:rgb(225, 225, 225);\n"
"	border-style: ridge;\n"
"    border-width: 2px;\n"
"	border-color: rgb(170, 170, 170);\n"
"	}\n"
"QLabel{	\n"
"	background-color: rgb(225, 225, 225);\n"
"	border-style: ridge;\n"
"	border-width: 2px;\n"
"    border-color: rgb(250, 250, 250);\n"
"    font: bold 12px;\n"
"}\n"
"QComboBox{	\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-style: ridge;\n"
"	border-width: 2px;\n"
"    border-color: rgb(250, 250, 250);\n"
"    font: bold 12px;\n"
"}\n"
"QComboBox::focus{\n"
"    background-color: rgb(170, 255, 255);\n"
"    border-style: inset;\n"
"}\n"
"QComboBox QListView {\n"
"	background-color: white; \n"
"}\n"
"")
        self.verticalLayout = QVBoxLayout(AtribuirCampos)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(4, 4, 4, 4)
        self.frame_3 = QFrame(AtribuirCampos)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setSpacing(2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 34))
        self.label.setStyleSheet(u"font: bold 12pt \"Segoe UI\";\n"
"border: 0px;")
        self.label.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.label)

        self.frame = QFrame(self.frame_3)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMaximumSize(QSize(548, 16777215))
        self.frame.setStyleSheet(u"QAbstractItemView {\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setSpacing(2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMinimumSize(QSize(0, 24))
        self.label_4.setMaximumSize(QSize(120, 16777215))

        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)

        self.cmb_dep = QComboBox(self.frame)
        self.cmb_dep.setObjectName(u"cmb_dep")
        sizePolicy.setHeightForWidth(self.cmb_dep.sizePolicy().hasHeightForWidth())
        self.cmb_dep.setSizePolicy(sizePolicy)
        self.cmb_dep.setMinimumSize(QSize(173, 24))

        self.gridLayout.addWidget(self.cmb_dep, 2, 1, 1, 1)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QSize(0, 24))
        self.label_3.setMaximumSize(QSize(120, 16777215))

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)

        self.cmb_mat = QComboBox(self.frame)
        self.cmb_mat.addItem("")
        self.cmb_mat.addItem("")
        self.cmb_mat.addItem("")
        self.cmb_mat.setObjectName(u"cmb_mat")
        sizePolicy.setHeightForWidth(self.cmb_mat.sizePolicy().hasHeightForWidth())
        self.cmb_mat.setSizePolicy(sizePolicy)
        self.cmb_mat.setMinimumSize(QSize(173, 24))
        self.cmb_mat.setStyleSheet(u"")

        self.gridLayout.addWidget(self.cmb_mat, 0, 1, 1, 1)

        self.cmb_cen = QComboBox(self.frame)
        self.cmb_cen.setObjectName(u"cmb_cen")
        sizePolicy.setHeightForWidth(self.cmb_cen.sizePolicy().hasHeightForWidth())
        self.cmb_cen.setSizePolicy(sizePolicy)
        self.cmb_cen.setMinimumSize(QSize(173, 24))

        self.gridLayout.addWidget(self.cmb_cen, 1, 1, 1, 1)

        self.cmb_loc = QComboBox(self.frame)
        self.cmb_loc.setObjectName(u"cmb_loc")
        sizePolicy.setHeightForWidth(self.cmb_loc.sizePolicy().hasHeightForWidth())
        self.cmb_loc.setSizePolicy(sizePolicy)
        self.cmb_loc.setMinimumSize(QSize(173, 24))

        self.gridLayout.addWidget(self.cmb_loc, 3, 1, 1, 1)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QSize(0, 24))
        self.label_2.setMaximumSize(QSize(120, 16777215))

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setMinimumSize(QSize(0, 24))
        self.label_5.setMaximumSize(QSize(120, 16777215))

        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.frame)

        self.frame_2 = QFrame(self.frame_3)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(207, 207, 207);\n"
"	border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 5px; \n"
"    border-color: rgb(238, 238, 238);\n"
"    font: bold 14px;		\n"
"	text-align: center;\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background-color: rgb(190, 190, 190);\n"
"    border-style: inset;\n"
"}\n"
"QPushButton::pressed {\n"
"    background-color: rgb(190, 190, 190);\n"
"    border-style: inset;\n"
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.btn_ok = QPushButton(self.frame_2)
        self.btn_ok.setObjectName(u"btn_ok")
        self.btn_ok.setMinimumSize(QSize(50, 35))
        self.btn_ok.setMaximumSize(QSize(46, 16777215))
        self.btn_ok.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.btn_ok)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btn_cancelar = QPushButton(self.frame_2)
        self.btn_cancelar.setObjectName(u"btn_cancelar")
        self.btn_cancelar.setMinimumSize(QSize(80, 35))
        self.btn_cancelar.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout.addWidget(self.btn_cancelar)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)


        self.verticalLayout_2.addWidget(self.frame_2)


        self.verticalLayout.addWidget(self.frame_3)

        QWidget.setTabOrder(self.cmb_mat, self.cmb_cen)
        QWidget.setTabOrder(self.cmb_cen, self.cmb_dep)
        QWidget.setTabOrder(self.cmb_dep, self.cmb_loc)
        QWidget.setTabOrder(self.cmb_loc, self.btn_ok)
        QWidget.setTabOrder(self.btn_ok, self.btn_cancelar)

        self.retranslateUi(AtribuirCampos)

        QMetaObject.connectSlotsByName(AtribuirCampos)
    # setupUi

    def retranslateUi(self, AtribuirCampos):
        AtribuirCampos.setWindowTitle(QCoreApplication.translate("AtribuirCampos", u"Form", None))
        self.label.setText(QCoreApplication.translate("AtribuirCampos", u" Atribuir campos:", None))
        self.label_4.setText(QCoreApplication.translate("AtribuirCampos", u"Dep\u00f3sito:", None))
        self.label_3.setText(QCoreApplication.translate("AtribuirCampos", u"Centro:", None))
        self.cmb_mat.setItemText(0, QCoreApplication.translate("AtribuirCampos", u"New Item", None))
        self.cmb_mat.setItemText(1, QCoreApplication.translate("AtribuirCampos", u"New Item", None))
        self.cmb_mat.setItemText(2, QCoreApplication.translate("AtribuirCampos", u"New Item", None))

        self.label_2.setText(QCoreApplication.translate("AtribuirCampos", u"Material:", None))
        self.label_5.setText(QCoreApplication.translate("AtribuirCampos", u"Nova Localiza\u00e7\u00e3o:", None))
        self.btn_ok.setText(QCoreApplication.translate("AtribuirCampos", u"OK", None))
        self.btn_cancelar.setText(QCoreApplication.translate("AtribuirCampos", u"Cancelar", None))
    # retranslateUi

