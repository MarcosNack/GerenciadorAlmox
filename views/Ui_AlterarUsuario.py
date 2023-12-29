# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AlterarUsuario.ui'
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
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget, QAbstractItemView)
import assets.icons_alt_regras_rc

class Ui_AlterarUsuario(object):
    def setupUi(self, AlterarUsuario):
        if not AlterarUsuario.objectName():
            AlterarUsuario.setObjectName(u"AlterarUsuario")
        AlterarUsuario.resize(930, 230)
        AlterarUsuario.setMinimumSize(QSize(930, 230))
        AlterarUsuario.setMaximumSize(QSize(16777215, 16777215))
        AlterarUsuario.setStyleSheet(u"QWidget{	\n"
"	border-style: ridge;\n"
"    border-width: 2px;\n"
"    border-color: rgb(255, 255, 255);\n"
"	background-color:rgb(220, 220, 220);\n"
"}\n"
"\n"
"QFrame{\n"
"	background-color:rgb(200, 200, 200);\n"
"}\n"
"\n"
"QComboBox{	\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-style: double;\n"
"	border-width: 3px;\n"
"    border-color: rgb(150, 150, 150);\n"
"    font: bold 12px;\n"
"}\n"
"\n"
"QComboBox::QAbstractItemView{\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QComboBox::focus{\n"
"    background-color: rgb(170, 255, 255);\n"
"    border-style: inset;\n"
"}\n"
"\n"
"QLabel{	\n"
"	background-color: rgb(225, 225, 225);\n"
"	border-style: double;\n"
"	border-width: 3px;\n"
"    border-color: rgb(170, 170, 170);\n"
"    font: bold 12px;\n"
"	text-align: left;\n"
"    font: bold 12px;\n"
"}\n"
"QLineEdit{		\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-style: double;\n"
"	border-width: 3px;\n"
"    border-color: rgb(170, 170, 170);\n"
"    font: bold 12px;\n"
"}\n"
""
                        "QLineEdit::focus{\n"
"    background-color: rgb(170, 255, 255);\n"
"    border-style: inset;\n"
"}\n"
"\n"
"")
        self.verticalLayout = QVBoxLayout(AlterarUsuario)
        self.verticalLayout.setSpacing(4)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(4, 4, 4, 4)
        self.frame_3 = QFrame(AlterarUsuario)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(16777215, 16777215))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(10, 10, 10, 15)
        self.frame_2 = QFrame(self.frame_3)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(16777215, 50))
        self.frame_2.setStyleSheet(u"QFrame{\n"
"	border: 0px;\n"
"}\n"
"QPushButton {\n"
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
"\n"
"QPushButton::pressed {\n"
"    background-color: rgb(190, 190, 190);\n"
"    border-style: inset;\n"
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setSpacing(15)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(5, 0, 8, 0)
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 0))
        self.label.setStyleSheet(u"background-color: rgb(200, 200, 200);\n"
"\n"
"font: bold 12pt \"Segoe UI\";\n"
"border: 0px;")
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label.setWordWrap(True)

        self.horizontalLayout.addWidget(self.label)

        self.btn_ok = QPushButton(self.frame_2)
        self.btn_ok.setObjectName(u"btn_ok")
        self.btn_ok.setMinimumSize(QSize(60, 40))
        self.btn_ok.setMaximumSize(QSize(60, 40))
        self.btn_ok.setStyleSheet(u"#btn_ok{	\n"
"	background-color: rgb(0, 220, 0);\n"
"    border-style: outset;\n"
"    border-width: 3px;\n"
"    border-radius: 5px; \n"
"    border-color: rgb(0, 158, 0);\n"
"    font: bold 14px;		\n"
"	text-align: center;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#btn_ok::hover {\n"
"    background-color: rgb(0, 195, 0);\n"
"    border-style: inset;\n"
"}\n"
"#btn_ok::pressed {\n"
"    background-color: rgb(0, 195, 0);\n"
"    border-style: inset;\n"
"}\n"
"")
        icon = QIcon()
        icon.addFile(u":/assets.icons_alt_regras/salvar-e-fechar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_ok.setIcon(icon)
        self.btn_ok.setIconSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.btn_ok)

        self.btn_cancelar = QPushButton(self.frame_2)
        self.btn_cancelar.setObjectName(u"btn_cancelar")
        self.btn_cancelar.setMinimumSize(QSize(60, 40))
        self.btn_cancelar.setMaximumSize(QSize(60, 40))
        self.btn_cancelar.setStyleSheet(u"#btn_cancelar{	\n"
"	background-color: rgb(248, 0, 0);\n"
"    border-style: outset;\n"
"    border-width: 3px;\n"
"    border-radius: 5px; \n"
"    border-color: rgb(227, 0, 0);\n"
"    font: bold 14px;		\n"
"	text-align: center;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#btn_cancelar::hover {\n"
"    background-color: rgb(165, 0, 0);\n"
"    border-style: inset;\n"
"}\n"
"#btn_cancelar::pressed {\n"
"    background-color: rgb(165, 0, 0);\n"
"    border-style: inset;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/assets.icons_alt_regras/fechar-janela.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_cancelar.setIcon(icon1)
        self.btn_cancelar.setIconSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.btn_cancelar)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.frame = QFrame(self.frame_3)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMaximumSize(QSize(16777215, 145))
        self.frame.setStyleSheet(u"QAbstractItemView {\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"#frame{\n"
" border: 0px;\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setVerticalSpacing(2)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.lb_acesso = QLabel(self.frame)
        self.lb_acesso.setObjectName(u"lb_acesso")
        sizePolicy.setHeightForWidth(self.lb_acesso.sizePolicy().hasHeightForWidth())
        self.lb_acesso.setSizePolicy(sizePolicy)
        self.lb_acesso.setMinimumSize(QSize(120, 35))
        self.lb_acesso.setMaximumSize(QSize(120, 35))

        self.gridLayout.addWidget(self.lb_acesso, 3, 6, 1, 1)

        self.label_9 = QLabel(self.frame)
        self.label_9.setObjectName(u"label_9")
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setMinimumSize(QSize(120, 35))
        self.label_9.setMaximumSize(QSize(120, 35))
        self.label_9.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_9, 2, 1, 1, 1, Qt.AlignLeft)

        self.txt_nome = QLineEdit(self.frame)
        self.txt_nome.setObjectName(u"txt_nome")
        self.txt_nome.setMinimumSize(QSize(0, 35))
        self.txt_nome.setMaximumSize(QSize(16777215, 35))

        self.gridLayout.addWidget(self.txt_nome, 5, 2, 1, 2)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QSize(70, 35))
        self.label_2.setMaximumSize(QSize(70, 35))

        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)

        self.txt_user = QLineEdit(self.frame)
        self.txt_user.setObjectName(u"txt_user")
        self.txt_user.setMinimumSize(QSize(120, 35))
        self.txt_user.setMaximumSize(QSize(120, 35))

        self.gridLayout.addWidget(self.txt_user, 5, 1, 1, 1, Qt.AlignVCenter)

        self.label_14 = QLabel(self.frame)
        self.label_14.setObjectName(u"label_14")
        sizePolicy.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy)
        self.label_14.setMinimumSize(QSize(120, 35))
        self.label_14.setMaximumSize(QSize(120, 35))
        self.label_14.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_14, 2, 6, 1, 1)

        self.txt_nome_ant = QLineEdit(self.frame)
        self.txt_nome_ant.setObjectName(u"txt_nome_ant")
        self.txt_nome_ant.setMinimumSize(QSize(0, 35))
        self.txt_nome_ant.setMaximumSize(QSize(16777215, 35))
        self.txt_nome_ant.setStyleSheet(u"background-color: rgb(220, 220, 220);")
        self.txt_nome_ant.setReadOnly(True)

        self.gridLayout.addWidget(self.txt_nome_ant, 3, 2, 1, 2)

        self.label_13 = QLabel(self.frame)
        self.label_13.setObjectName(u"label_13")
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)
        self.label_13.setMinimumSize(QSize(120, 35))
        self.label_13.setMaximumSize(QSize(120, 35))
        self.label_13.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_13, 2, 5, 1, 1)

        self.cmb_cen = QComboBox(self.frame)
        self.cmb_cen.setObjectName(u"cmb_cen")
        sizePolicy.setHeightForWidth(self.cmb_cen.sizePolicy().hasHeightForWidth())
        self.cmb_cen.setSizePolicy(sizePolicy)
        self.cmb_cen.setMinimumSize(QSize(120, 35))
        self.cmb_cen.setMaximumSize(QSize(120, 35))

        self.gridLayout.addWidget(self.cmb_cen, 5, 5, 1, 1)

        self.lb_id = QLabel(self.frame)
        self.lb_id.setObjectName(u"lb_id")
        self.lb_id.setEnabled(True)
        sizePolicy.setHeightForWidth(self.lb_id.sizePolicy().hasHeightForWidth())
        self.lb_id.setSizePolicy(sizePolicy)
        self.lb_id.setMinimumSize(QSize(120, 35))
        self.lb_id.setMaximumSize(QSize(120, 35))

        self.gridLayout.addWidget(self.lb_id, 0, 2, 1, 1)

        self.txt_user_ant = QLineEdit(self.frame)
        self.txt_user_ant.setObjectName(u"txt_user_ant")
        self.txt_user_ant.setMinimumSize(QSize(120, 35))
        self.txt_user_ant.setMaximumSize(QSize(120, 35))
        self.txt_user_ant.setStyleSheet(u"background-color: rgb(220, 220, 220);")
        self.txt_user_ant.setReadOnly(True)

        self.gridLayout.addWidget(self.txt_user_ant, 3, 1, 1, 1)

        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setMinimumSize(QSize(120, 35))
        self.label_6.setMaximumSize(QSize(120, 35))

        self.gridLayout.addWidget(self.label_6, 0, 1, 1, 1)

        self.label_11 = QLabel(self.frame)
        self.label_11.setObjectName(u"label_11")
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setMinimumSize(QSize(0, 35))
        self.label_11.setMaximumSize(QSize(16777215, 35))
        self.label_11.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_11, 2, 2, 1, 2)

        self.label_8 = QLabel(self.frame)
        self.label_8.setObjectName(u"label_8")
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setMinimumSize(QSize(70, 35))
        self.label_8.setMaximumSize(QSize(70, 35))

        self.gridLayout.addWidget(self.label_8, 5, 0, 1, 1)

        self.lb_cen = QLabel(self.frame)
        self.lb_cen.setObjectName(u"lb_cen")
        sizePolicy.setHeightForWidth(self.lb_cen.sizePolicy().hasHeightForWidth())
        self.lb_cen.setSizePolicy(sizePolicy)
        self.lb_cen.setMinimumSize(QSize(120, 35))
        self.lb_cen.setMaximumSize(QSize(120, 35))

        self.gridLayout.addWidget(self.lb_cen, 3, 5, 1, 1)

        self.cmb_acesso = QComboBox(self.frame)
        self.cmb_acesso.addItem("")
        self.cmb_acesso.addItem("")
        self.cmb_acesso.addItem("")
        self.cmb_acesso.setObjectName(u"cmb_acesso")
        sizePolicy.setHeightForWidth(self.cmb_acesso.sizePolicy().hasHeightForWidth())
        self.cmb_acesso.setSizePolicy(sizePolicy)
        self.cmb_acesso.setMinimumSize(QSize(120, 35))
        self.cmb_acesso.setMaximumSize(QSize(120, 35))

        self.gridLayout.addWidget(self.cmb_acesso, 5, 6, 1, 1)


        self.verticalLayout_2.addWidget(self.frame)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.verticalLayout.addWidget(self.frame_3)

        QWidget.setTabOrder(self.txt_user, self.txt_nome)
        QWidget.setTabOrder(self.txt_nome, self.cmb_cen)
        QWidget.setTabOrder(self.cmb_cen, self.btn_ok)
        QWidget.setTabOrder(self.btn_ok, self.btn_cancelar)

        self.retranslateUi(AlterarUsuario)

        QMetaObject.connectSlotsByName(AlterarUsuario)
    # setupUi

    def retranslateUi(self, AlterarUsuario):
        AlterarUsuario.setWindowTitle(QCoreApplication.translate("AlterarUsuario", u"Form", None))
        self.label.setText(QCoreApplication.translate("AlterarUsuario", u"Alterar Usu\u00e1rio:", None))
#if QT_CONFIG(tooltip)
        self.btn_ok.setToolTip(QCoreApplication.translate("AlterarUsuario", u"<html><head/><body><p>Salvar e Sair</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_ok.setText("")
#if QT_CONFIG(tooltip)
        self.btn_cancelar.setToolTip(QCoreApplication.translate("AlterarUsuario", u"<html><head/><body><p>Cancelar</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_cancelar.setText("")
        self.lb_acesso.setText("")
        self.label_9.setText(QCoreApplication.translate("AlterarUsuario", u"Usu\u00e1rio", None))
        self.label_2.setText(QCoreApplication.translate("AlterarUsuario", u"Antigo", None))
        self.txt_user.setText("")
        self.label_14.setText(QCoreApplication.translate("AlterarUsuario", u"Acesso", None))
        self.label_13.setText(QCoreApplication.translate("AlterarUsuario", u"Centro", None))
        self.lb_id.setText("")
        self.txt_user_ant.setText("")
        self.label_6.setText(QCoreApplication.translate("AlterarUsuario", u"ID", None))
        self.label_11.setText(QCoreApplication.translate("AlterarUsuario", u"Nome", None))
        self.label_8.setText(QCoreApplication.translate("AlterarUsuario", u"Novo", None))
        self.lb_cen.setText("")
        self.cmb_acesso.setItemText(0, "")
        self.cmb_acesso.setItemText(1, QCoreApplication.translate("AlterarUsuario", u"ALMOX", None))
        self.cmb_acesso.setItemText(2, QCoreApplication.translate("AlterarUsuario", u"RECEB", None))

    # retranslateUi

