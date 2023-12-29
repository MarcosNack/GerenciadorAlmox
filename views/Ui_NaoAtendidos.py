# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'NaoAtendidosoegtVM.ui'
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
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QPlainTextEdit, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget, QAbstractItemView)
import assets.icons_alt_regras_rc

class Ui_NaoAtendidos(object):
    def setupUi(self, NaoAtendidos):
        if not NaoAtendidos.objectName():
            NaoAtendidos.setObjectName(u"NaoAtendidos")
        NaoAtendidos.resize(930, 600)
        NaoAtendidos.setMinimumSize(QSize(930, 600))
        NaoAtendidos.setMaximumSize(QSize(16777215, 16777215))
        NaoAtendidos.setStyleSheet(u"QWidget{	\n"
"	border-style: ridge;\n"
"    border-width: 2px;\n"
"    border-color: rgb(255, 255, 255);\n"
"	background-color: rgb(159, 159, 159);\n"
"	}\n"
"QFrame{\n"
"	background-color:rgb(225, 225, 225)\n"
"	}\n"
"QComboBox{	\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-style: ridge;\n"
"	border-width: 4px;\n"
"    border-color: rgb(180, 180, 180);    \n"
"	font: bold 11pt \"Calibri\";\n"
"	color: rgb(0, 0, 190);\n"
"	}\n"
"QComboBox::focus{\n"
"    background-color: rgb(170, 255, 255);\n"
"    border-style: ridge;\n"
"	}\n"
"QComboBox QListView {\n"
"	background-color: white;\n"
"	}\n"
"QLabel{	\n"
"	border-style: solid;\n"
"	border-width: 1px 1px 0px 1px;\n"
"    border-color: rgb(170, 170, 170);\n"
"	text-align: left;\n"
"	font: bold 9pt \"Calibri\";\n"
"	}\n"
"QLineEdit{		\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-style: ridge;\n"
"	border-width: 3px;\n"
"    border-color: rgb(180, 180, 180);\n"
"	font: bold 11pt \"Calibri\";\n"
"	color: rgb(0, 0, 190);\n"
"	}\n"
"QLineEdit::foc"
                        "us{\n"
"    background-color: rgb(170, 255, 255);\n"
"    border-style: inset;\n"
"	}\n"
"QPlainTextEdit{		\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-style: ridge;\n"
"	border-width: 3px;\n"
"    border-color: rgb(170, 170, 170);\n"
"	font: bold 11pt \"Calibri\";\n"
"	color: rgb(0, 0, 190);\n"
"	}\n"
"QTableWidget{\n"
"	background-color: rgb(255, 255, 255);\n"
"	font: bold 9pt  \"Calibri\";\n"
"	}\n"
"QTableWidget QLineEdit::focus{\n"
"	background-color: rgb(170, 255, 255);\n"
"    border-style: ridge;\n"
"	border-width: 2px;\n"
"	color: rgb(0, 0, 0);\n"
"	}\n"
"QTableWidget QWidget {\n"
"	background-color: rgb(100, 100, 100);\n"
"    color: #fffff8;\n"
"	font: bold 9pt \"Calibri\";\n"
"	}\n"
"QTableWidget QHeaderView::section {\n"
"	background-color : rgb(100, 100, 100);\n"
"	border-style: ridge;\n"
"   	border-width: 2px;\n"
"    border-color: rgb(170, 170, 170);\n"
"	border-radius: 2px;\n"
" 	padding-left: 2px;\n"
"  }\n"
"QTableWidget QTableCornerButton::section {\n"
"  	background-color: rgb("
                        "100, 100, 100);\n"
"	border-style: ridge;\n"
"   	border-width: 2px;\n"
"    border-color: rgb(170, 170, 170);\n"
"	border-radius: 2px;\n"
"	}")
        self.verticalLayout = QVBoxLayout(NaoAtendidos)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(4, 4, 4, 4)
        self.scrollArea = QScrollArea(NaoAtendidos)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 918, 588))
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.scrollAreaWidgetContents)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 0))
        self.frame_3.setMaximumSize(QSize(16777215, 16777215))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(4, 2, 4, 2)
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
        self.horizontalLayout.setContentsMargins(5, 6, 8, 6)
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 30))
        self.label.setStyleSheet(u"\n"
"font: bold 14pt \"Segoe UI\";\n"
"border: 0px;")
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label.setWordWrap(True)

        self.horizontalLayout.addWidget(self.label)

        self.btn_salvar_novo = QPushButton(self.frame_2)
        self.btn_salvar_novo.setObjectName(u"btn_salvar_novo")
        self.btn_salvar_novo.setMinimumSize(QSize(60, 40))
        self.btn_salvar_novo.setMaximumSize(QSize(60, 40))
        self.btn_salvar_novo.setStyleSheet(u"#btn_salvar_novo{	\n"
"	background-color: rgb(0, 220, 0);\n"
"    border-style: outset;\n"
"    border-width: 3px;\n"
"    border-radius: 5px; \n"
"    border-color: rgb(0, 158, 0);\n"
"    font: bold 14px;		\n"
"	text-align: center;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#btn_salvar_novo::hover {\n"
"    background-color: rgb(0, 195, 0);\n"
"    border-style: inset;\n"
"}\n"
"#btn_salvar_novo::pressed {\n"
"    background-color: rgb(0, 195, 0);\n"
"    border-style: inset;\n"
"}\n"
"")
        icon = QIcon()
        icon.addFile(u":/assets.icons_alt_regras/salvar-novo50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_salvar_novo.setIcon(icon)
        self.btn_salvar_novo.setIconSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.btn_salvar_novo)

        self.btn_salvar_sair = QPushButton(self.frame_2)
        self.btn_salvar_sair.setObjectName(u"btn_salvar_sair")
        self.btn_salvar_sair.setMinimumSize(QSize(60, 40))
        self.btn_salvar_sair.setMaximumSize(QSize(60, 40))
        self.btn_salvar_sair.setStyleSheet(u"#btn_salvar_sair{	\n"
"	background-color: rgb(0, 240, 240);\n"
"    border-style: outset;\n"
"    border-width: 3px;\n"
"    border-radius: 5px; \n"
"    border-color: rgb(0, 210, 210);\n"
"    font: bold 14px;		\n"
"	text-align: center;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#btn_salvar_sair::hover {\n"
"    background-color: rgb(0, 180, 180);\n"
"    border-style: inset;\n"
"}\n"
"#btn_salvar_sair::pressed {\n"
"    background-color: rgb(0, 180, 180);\n"
"    border-style: inset;\n"
"}\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/assets.icons_alt_regras/salvar-e-fechar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_salvar_sair.setIcon(icon1)
        self.btn_salvar_sair.setIconSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.btn_salvar_sair)

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
        icon2 = QIcon()
        icon2.addFile(u":/assets.icons_alt_regras/fechar-janela.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_cancelar.setIcon(icon2)
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
        self.frame.setMaximumSize(QSize(16777215, 530))
        self.frame.setStyleSheet(u"#frame{\n"
" border: 0px;\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(1)
        self.gridLayout.setVerticalSpacing(2)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_38 = QLabel(self.frame)
        self.label_38.setObjectName(u"label_38")
        sizePolicy.setHeightForWidth(self.label_38.sizePolicy().hasHeightForWidth())
        self.label_38.setSizePolicy(sizePolicy)
        self.label_38.setMinimumSize(QSize(0, 20))
        self.label_38.setMaximumSize(QSize(16777215, 20))
        self.label_38.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_38, 16, 8, 1, 3)

        self.label_21 = QLabel(self.frame)
        self.label_21.setObjectName(u"label_21")
        sizePolicy.setHeightForWidth(self.label_21.sizePolicy().hasHeightForWidth())
        self.label_21.setSizePolicy(sizePolicy)
        self.label_21.setMinimumSize(QSize(0, 20))
        self.label_21.setMaximumSize(QSize(16777215, 20))
        self.label_21.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_21, 7, 0, 1, 1)

        self.label_34 = QLabel(self.frame)
        self.label_34.setObjectName(u"label_34")
        sizePolicy.setHeightForWidth(self.label_34.sizePolicy().hasHeightForWidth())
        self.label_34.setSizePolicy(sizePolicy)
        self.label_34.setMinimumSize(QSize(0, 20))
        self.label_34.setMaximumSize(QSize(16777215, 20))
        self.label_34.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_34, 12, 2, 1, 1)

        self.txt_bloqueado = QLineEdit(self.frame)
        self.txt_bloqueado.setObjectName(u"txt_bloqueado")
        self.txt_bloqueado.setMinimumSize(QSize(0, 35))
        self.txt_bloqueado.setMaximumSize(QSize(16777215, 35))
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        self.txt_bloqueado.setFont(font)
        self.txt_bloqueado.setStyleSheet(u"background-color: rgb(225, 225, 225);\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(170, 170, 170);\n"
"")
        self.txt_bloqueado.setMaxLength(20)
        self.txt_bloqueado.setAlignment(Qt.AlignCenter)
        self.txt_bloqueado.setReadOnly(True)

        self.gridLayout.addWidget(self.txt_bloqueado, 11, 10, 1, 1)

        self.label_13 = QLabel(self.frame)
        self.label_13.setObjectName(u"label_13")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy1)
        self.label_13.setMinimumSize(QSize(0, 20))
        self.label_13.setMaximumSize(QSize(16777215, 20))
        self.label_13.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_13, 0, 2, 1, 1)

        self.txt_minimo = QLineEdit(self.frame)
        self.txt_minimo.setObjectName(u"txt_minimo")
        self.txt_minimo.setMinimumSize(QSize(0, 35))
        self.txt_minimo.setMaximumSize(QSize(110, 35))
        self.txt_minimo.setFont(font)
        self.txt_minimo.setStyleSheet(u"background-color: rgb(225, 225, 225);\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(170, 170, 170);\n"
"")
        self.txt_minimo.setMaxLength(20)
        self.txt_minimo.setAlignment(Qt.AlignCenter)
        self.txt_minimo.setReadOnly(True)

        self.gridLayout.addWidget(self.txt_minimo, 8, 3, 1, 2)

        self.cmb_setor = QComboBox(self.frame)
        self.cmb_setor.setObjectName(u"cmb_setor")
        self.cmb_setor.setMinimumSize(QSize(0, 35))
        self.cmb_setor.setMaximumSize(QSize(213, 16777215))
        self.cmb_setor.setEditable(True)

        self.gridLayout.addWidget(self.cmb_setor, 4, 3, 1, 4)

        self.txt_comprador = QLineEdit(self.frame)
        self.txt_comprador.setObjectName(u"txt_comprador")
        self.txt_comprador.setMinimumSize(QSize(0, 35))
        self.txt_comprador.setMaximumSize(QSize(16777215, 35))
        self.txt_comprador.setFont(font)
        self.txt_comprador.setStyleSheet(u"background-color: rgb(225, 225, 225);\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(170, 170, 170);\n"
"")
        self.txt_comprador.setMaxLength(100)
        self.txt_comprador.setAlignment(Qt.AlignCenter)
        self.txt_comprador.setReadOnly(True)

        self.gridLayout.addWidget(self.txt_comprador, 14, 9, 1, 2)

        self.txt_grp_comp = QLineEdit(self.frame)
        self.txt_grp_comp.setObjectName(u"txt_grp_comp")
        self.txt_grp_comp.setMinimumSize(QSize(0, 35))
        self.txt_grp_comp.setMaximumSize(QSize(110, 35))
        self.txt_grp_comp.setFont(font)
        self.txt_grp_comp.setStyleSheet(u"background-color: rgb(225, 225, 225);\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(170, 170, 170);\n"
"")
        self.txt_grp_comp.setMaxLength(4)
        self.txt_grp_comp.setAlignment(Qt.AlignCenter)
        self.txt_grp_comp.setReadOnly(True)

        self.gridLayout.addWidget(self.txt_grp_comp, 14, 8, 1, 1)

        self.txt_status_erp_geral = QLineEdit(self.frame)
        self.txt_status_erp_geral.setObjectName(u"txt_status_erp_geral")
        self.txt_status_erp_geral.setMinimumSize(QSize(0, 35))
        self.txt_status_erp_geral.setMaximumSize(QSize(50, 35))
        self.txt_status_erp_geral.setFont(font)
        self.txt_status_erp_geral.setStyleSheet(u"background-color: rgb(225, 225, 225);\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(170, 170, 170);\n"
"")
        self.txt_status_erp_geral.setMaxLength(4)
        self.txt_status_erp_geral.setAlignment(Qt.AlignCenter)
        self.txt_status_erp_geral.setReadOnly(True)

        self.gridLayout.addWidget(self.txt_status_erp_geral, 11, 3, 1, 1)

        self.txt_saldo_fisico = QLineEdit(self.frame)
        self.txt_saldo_fisico.setObjectName(u"txt_saldo_fisico")
        self.txt_saldo_fisico.setMinimumSize(QSize(0, 35))
        self.txt_saldo_fisico.setMaximumSize(QSize(110, 35))
        self.txt_saldo_fisico.setMaxLength(20)
        self.txt_saldo_fisico.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_saldo_fisico, 11, 8, 1, 1)

        self.label_33 = QLabel(self.frame)
        self.label_33.setObjectName(u"label_33")
        sizePolicy.setHeightForWidth(self.label_33.sizePolicy().hasHeightForWidth())
        self.label_33.setSizePolicy(sizePolicy)
        self.label_33.setMinimumSize(QSize(0, 20))
        self.label_33.setMaximumSize(QSize(16777215, 20))
        self.label_33.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_33, 12, 0, 1, 1)

        self.label_43 = QLabel(self.frame)
        self.label_43.setObjectName(u"label_43")
        sizePolicy.setHeightForWidth(self.label_43.sizePolicy().hasHeightForWidth())
        self.label_43.setSizePolicy(sizePolicy)
        self.label_43.setMinimumSize(QSize(0, 20))
        self.label_43.setMaximumSize(QSize(16777215, 20))
        self.label_43.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_43, 12, 9, 1, 2)

        self.txt_critico = QLineEdit(self.frame)
        self.txt_critico.setObjectName(u"txt_critico")
        self.txt_critico.setMinimumSize(QSize(0, 35))
        self.txt_critico.setMaximumSize(QSize(16777215, 35))
        self.txt_critico.setFont(font)
        self.txt_critico.setStyleSheet(u"background-color: rgb(225, 225, 225);\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(170, 170, 170);\n"
"")
        self.txt_critico.setMaxLength(4)
        self.txt_critico.setAlignment(Qt.AlignCenter)
        self.txt_critico.setReadOnly(True)

        self.gridLayout.addWidget(self.txt_critico, 11, 0, 1, 1)

        self.cmb_sit_ped = QComboBox(self.frame)
        self.cmb_sit_ped.addItem("")
        self.cmb_sit_ped.addItem("")
        self.cmb_sit_ped.addItem("")
        self.cmb_sit_ped.addItem("")
        self.cmb_sit_ped.addItem("")
        self.cmb_sit_ped.setObjectName(u"cmb_sit_ped")
        self.cmb_sit_ped.setMinimumSize(QSize(0, 35))

        self.gridLayout.addWidget(self.cmb_sit_ped, 19, 0, 1, 3)

        self.txt_mat = QLineEdit(self.frame)
        self.txt_mat.setObjectName(u"txt_mat")
        self.txt_mat.setMinimumSize(QSize(0, 35))
        self.txt_mat.setMaximumSize(QSize(999999, 35))
        self.txt_mat.setMaxLength(8)
        self.txt_mat.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_mat, 2, 3, 1, 2)

        self.txt_plan = QLineEdit(self.frame)
        self.txt_plan.setObjectName(u"txt_plan")
        self.txt_plan.setMinimumSize(QSize(0, 35))
        self.txt_plan.setMaximumSize(QSize(16777215, 35))
        self.txt_plan.setFont(font)
        self.txt_plan.setStyleSheet(u"background-color: rgb(225, 225, 225);\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(170, 170, 170);\n"
"")
        self.txt_plan.setMaxLength(100)
        self.txt_plan.setAlignment(Qt.AlignCenter)
        self.txt_plan.setReadOnly(True)

        self.gridLayout.addWidget(self.txt_plan, 8, 9, 1, 2)

        self.txt_devergencia = QLineEdit(self.frame)
        self.txt_devergencia.setObjectName(u"txt_devergencia")
        self.txt_devergencia.setMinimumSize(QSize(0, 35))
        self.txt_devergencia.setMaximumSize(QSize(16777215, 35))
        self.txt_devergencia.setFont(font)
        self.txt_devergencia.setStyleSheet(u"background-color: rgb(225, 225, 225);\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(170, 170, 170);\n"
"")
        self.txt_devergencia.setMaxLength(20)
        self.txt_devergencia.setAlignment(Qt.AlignCenter)
        self.txt_devergencia.setReadOnly(True)

        self.gridLayout.addWidget(self.txt_devergencia, 14, 2, 1, 1)

        self.label_31 = QLabel(self.frame)
        self.label_31.setObjectName(u"label_31")
        sizePolicy.setHeightForWidth(self.label_31.sizePolicy().hasHeightForWidth())
        self.label_31.setSizePolicy(sizePolicy)
        self.label_31.setMinimumSize(QSize(0, 20))
        self.label_31.setMaximumSize(QSize(16777215, 20))
        self.label_31.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_31, 10, 9, 1, 1)

        self.ptxt_nota_mat = QPlainTextEdit(self.frame)
        self.ptxt_nota_mat.setObjectName(u"ptxt_nota_mat")
        self.ptxt_nota_mat.setMaximumSize(QSize(213, 16777215))
        self.ptxt_nota_mat.setFont(font)
        self.ptxt_nota_mat.setStyleSheet(u"background-color: rgb(225, 225, 225);\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(170, 170, 170);\n"
"")
        self.ptxt_nota_mat.setReadOnly(True)

        self.gridLayout.addWidget(self.ptxt_nota_mat, 17, 3, 5, 4)

        self.txt_valor_unit = QLineEdit(self.frame)
        self.txt_valor_unit.setObjectName(u"txt_valor_unit")
        self.txt_valor_unit.setMinimumSize(QSize(0, 35))
        self.txt_valor_unit.setMaximumSize(QSize(110, 35))
        self.txt_valor_unit.setFont(font)
        self.txt_valor_unit.setStyleSheet(u"background-color: rgb(225, 225, 225);\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(170, 170, 170);\n"
"")
        self.txt_valor_unit.setMaxLength(20)
        self.txt_valor_unit.setAlignment(Qt.AlignCenter)
        self.txt_valor_unit.setReadOnly(True)

        self.gridLayout.addWidget(self.txt_valor_unit, 14, 6, 1, 1)

        self.txt_saldo_sistema = QLineEdit(self.frame)
        self.txt_saldo_sistema.setObjectName(u"txt_saldo_sistema")
        self.txt_saldo_sistema.setMinimumSize(QSize(0, 35))
        self.txt_saldo_sistema.setMaximumSize(QSize(110, 35))
        self.txt_saldo_sistema.setFont(font)
        self.txt_saldo_sistema.setStyleSheet(u"background-color: rgb(225, 225, 225);\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(170, 170, 170);\n"
"")
        self.txt_saldo_sistema.setMaxLength(20)
        self.txt_saldo_sistema.setAlignment(Qt.AlignCenter)
        self.txt_saldo_sistema.setReadOnly(True)

        self.gridLayout.addWidget(self.txt_saldo_sistema, 11, 6, 1, 1)

        self.label_19 = QLabel(self.frame)
        self.label_19.setObjectName(u"label_19")
        sizePolicy.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
        self.label_19.setSizePolicy(sizePolicy)
        self.label_19.setMinimumSize(QSize(0, 20))
        self.label_19.setMaximumSize(QSize(16777215, 20))
        self.label_19.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_19, 3, 8, 1, 3)

        self.label_42 = QLabel(self.frame)
        self.label_42.setObjectName(u"label_42")
        sizePolicy.setHeightForWidth(self.label_42.sizePolicy().hasHeightForWidth())
        self.label_42.setSizePolicy(sizePolicy)
        self.label_42.setMinimumSize(QSize(0, 20))
        self.label_42.setMaximumSize(QSize(16777215, 20))
        self.label_42.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_42, 7, 9, 1, 2)

        self.txt_obs_almox = QLineEdit(self.frame)
        self.txt_obs_almox.setObjectName(u"txt_obs_almox")
        self.txt_obs_almox.setMinimumSize(QSize(0, 35))
        self.txt_obs_almox.setMaximumSize(QSize(16777215, 35))
        self.txt_obs_almox.setMaxLength(100)
        self.txt_obs_almox.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_obs_almox, 4, 8, 1, 3)

        self.label_29 = QLabel(self.frame)
        self.label_29.setObjectName(u"label_29")
        sizePolicy.setHeightForWidth(self.label_29.sizePolicy().hasHeightForWidth())
        self.label_29.setSizePolicy(sizePolicy)
        self.label_29.setMinimumSize(QSize(0, 20))
        self.label_29.setMaximumSize(QSize(110, 20))
        self.label_29.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_29, 10, 6, 1, 1)

        self.label_16 = QLabel(self.frame)
        self.label_16.setObjectName(u"label_16")
        sizePolicy.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy)
        self.label_16.setMinimumSize(QSize(0, 20))
        self.label_16.setMaximumSize(QSize(16777215, 20))
        self.label_16.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_16, 3, 2, 1, 1)

        self.txt_hora = QLineEdit(self.frame)
        self.txt_hora.setObjectName(u"txt_hora")
        self.txt_hora.setMinimumSize(QSize(0, 35))
        self.txt_hora.setMaximumSize(QSize(16777215, 35))
        self.txt_hora.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_hora, 2, 2, 1, 1)

        self.txt_solicitante = QLineEdit(self.frame)
        self.txt_solicitante.setObjectName(u"txt_solicitante")
        self.txt_solicitante.setMinimumSize(QSize(0, 35))
        self.txt_solicitante.setMaximumSize(QSize(16777215, 35))
        self.txt_solicitante.setMaxLength(30)
        self.txt_solicitante.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_solicitante, 4, 0, 1, 1)

        self.txt_decricao = QLineEdit(self.frame)
        self.txt_decricao.setObjectName(u"txt_decricao")
        self.txt_decricao.setMinimumSize(QSize(280, 35))
        self.txt_decricao.setMaximumSize(QSize(16777215, 35))
        self.txt_decricao.setFont(font)
        self.txt_decricao.setStyleSheet(u"background-color: rgb(225, 225, 225);\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(170, 170, 170);\n"
"")
        self.txt_decricao.setMaxLength(41)
        self.txt_decricao.setAlignment(Qt.AlignCenter)
        self.txt_decricao.setReadOnly(True)

        self.gridLayout.addWidget(self.txt_decricao, 2, 5, 1, 5)

        self.label_20 = QLabel(self.frame)
        self.label_20.setObjectName(u"label_20")
        sizePolicy.setHeightForWidth(self.label_20.sizePolicy().hasHeightForWidth())
        self.label_20.setSizePolicy(sizePolicy)
        self.label_20.setMinimumSize(QSize(0, 20))
        self.label_20.setMaximumSize(QSize(110, 20))
        self.label_20.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_20, 7, 3, 1, 2)

        self.label_27 = QLabel(self.frame)
        self.label_27.setObjectName(u"label_27")
        sizePolicy.setHeightForWidth(self.label_27.sizePolicy().hasHeightForWidth())
        self.label_27.setSizePolicy(sizePolicy)
        self.label_27.setMinimumSize(QSize(0, 20))
        self.label_27.setMaximumSize(QSize(16777215, 20))
        self.label_27.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_27, 10, 2, 1, 1)

        self.label_35 = QLabel(self.frame)
        self.label_35.setObjectName(u"label_35")
        sizePolicy.setHeightForWidth(self.label_35.sizePolicy().hasHeightForWidth())
        self.label_35.setSizePolicy(sizePolicy)
        self.label_35.setMinimumSize(QSize(0, 20))
        self.label_35.setMaximumSize(QSize(110, 20))
        self.label_35.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_35, 12, 6, 1, 1)

        self.label_14 = QLabel(self.frame)
        self.label_14.setObjectName(u"label_14")
        sizePolicy1.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy1)
        self.label_14.setMinimumSize(QSize(0, 20))
        self.label_14.setMaximumSize(QSize(999999, 20))
        self.label_14.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_14, 0, 3, 1, 2)

        self.label_9 = QLabel(self.frame)
        self.label_9.setObjectName(u"label_9")
        sizePolicy1.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy1)
        self.label_9.setMinimumSize(QSize(0, 20))
        self.label_9.setMaximumSize(QSize(16777215, 20))
        font1 = QFont()
        font1.setPointSize(9)
        font1.setBold(True)
        font1.setItalic(False)
        self.label_9.setFont(font1)
        self.label_9.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_9, 0, 0, 1, 1)

        self.txt_req_manual = QLineEdit(self.frame)
        self.txt_req_manual.setObjectName(u"txt_req_manual")
        self.txt_req_manual.setMinimumSize(QSize(0, 35))
        self.txt_req_manual.setMaximumSize(QSize(16777215, 35))
        self.txt_req_manual.setMaxLength(20)
        self.txt_req_manual.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_req_manual, 14, 0, 1, 1)

        self.txt_status_erp_cen = QLineEdit(self.frame)
        self.txt_status_erp_cen.setObjectName(u"txt_status_erp_cen")
        self.txt_status_erp_cen.setMinimumSize(QSize(0, 35))
        self.txt_status_erp_cen.setMaximumSize(QSize(50, 35))
        self.txt_status_erp_cen.setFont(font)
        self.txt_status_erp_cen.setStyleSheet(u"background-color: rgb(225, 225, 225);\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(170, 170, 170);\n"
"")
        self.txt_status_erp_cen.setMaxLength(4)
        self.txt_status_erp_cen.setAlignment(Qt.AlignCenter)
        self.txt_status_erp_cen.setReadOnly(True)

        self.gridLayout.addWidget(self.txt_status_erp_cen, 11, 4, 1, 1)

        self.label_15 = QLabel(self.frame)
        self.label_15.setObjectName(u"label_15")
        sizePolicy1.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy1)
        self.label_15.setMinimumSize(QSize(0, 20))
        self.label_15.setMaximumSize(QSize(16777215, 20))
        self.label_15.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_15, 0, 5, 1, 5)

        self.label_18 = QLabel(self.frame)
        self.label_18.setObjectName(u"label_18")
        sizePolicy.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy)
        self.label_18.setMinimumSize(QSize(0, 20))
        self.label_18.setMaximumSize(QSize(213, 20))
        self.label_18.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_18, 3, 3, 1, 4)

        self.txt_ramal = QLineEdit(self.frame)
        self.txt_ramal.setObjectName(u"txt_ramal")
        self.txt_ramal.setMinimumSize(QSize(0, 35))
        self.txt_ramal.setMaximumSize(QSize(16777215, 35))
        self.txt_ramal.setMaxLength(4)
        self.txt_ramal.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_ramal, 4, 2, 1, 1)

        self.label_26 = QLabel(self.frame)
        self.label_26.setObjectName(u"label_26")
        sizePolicy.setHeightForWidth(self.label_26.sizePolicy().hasHeightForWidth())
        self.label_26.setSizePolicy(sizePolicy)
        self.label_26.setMinimumSize(QSize(0, 20))
        self.label_26.setMaximumSize(QSize(16777215, 20))
        self.label_26.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_26, 10, 0, 1, 1)

        self.label_10 = QLabel(self.frame)
        self.label_10.setObjectName(u"label_10")
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setMinimumSize(QSize(0, 20))
        self.label_10.setMaximumSize(QSize(16777215, 20))
        self.label_10.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_10, 3, 0, 1, 1)

        self.txt_maximo = QLineEdit(self.frame)
        self.txt_maximo.setObjectName(u"txt_maximo")
        self.txt_maximo.setMinimumSize(QSize(0, 35))
        self.txt_maximo.setMaximumSize(QSize(110, 35))
        self.txt_maximo.setFont(font)
        self.txt_maximo.setStyleSheet(u"background-color: rgb(225, 225, 225);\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(170, 170, 170);\n"
"")
        self.txt_maximo.setMaxLength(20)
        self.txt_maximo.setAlignment(Qt.AlignCenter)
        self.txt_maximo.setReadOnly(True)

        self.gridLayout.addWidget(self.txt_maximo, 8, 6, 1, 1)

        self.txt_total_proc = QLineEdit(self.frame)
        self.txt_total_proc.setObjectName(u"txt_total_proc")
        self.txt_total_proc.setMinimumSize(QSize(0, 35))
        self.txt_total_proc.setMaximumSize(QSize(110, 35))
        self.txt_total_proc.setFont(font)
        self.txt_total_proc.setStyleSheet(u"background-color: rgb(225, 225, 225);\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(170, 170, 170);\n"
"")
        self.txt_total_proc.setMaxLength(20)
        self.txt_total_proc.setAlignment(Qt.AlignCenter)
        self.txt_total_proc.setReadOnly(True)

        self.gridLayout.addWidget(self.txt_total_proc, 14, 3, 1, 2)

        self.txt_und_med = QLineEdit(self.frame)
        self.txt_und_med.setObjectName(u"txt_und_med")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.txt_und_med.sizePolicy().hasHeightForWidth())
        self.txt_und_med.setSizePolicy(sizePolicy2)
        self.txt_und_med.setMinimumSize(QSize(0, 35))
        self.txt_und_med.setMaximumSize(QSize(16777215, 35))
        self.txt_und_med.setFont(font)
        self.txt_und_med.setStyleSheet(u"background-color: rgb(225, 225, 225);\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(170, 170, 170);\n"
"")
        self.txt_und_med.setMaxLength(4)
        self.txt_und_med.setAlignment(Qt.AlignCenter)
        self.txt_und_med.setReadOnly(True)

        self.gridLayout.addWidget(self.txt_und_med, 2, 10, 1, 1)

        self.label_17 = QLabel(self.frame)
        self.label_17.setObjectName(u"label_17")
        sizePolicy.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy)
        self.label_17.setMinimumSize(QSize(0, 20))
        self.label_17.setMaximumSize(QSize(16777215, 20))
        self.label_17.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_17, 0, 10, 1, 1)

        self.txt_grp_plan = QLineEdit(self.frame)
        self.txt_grp_plan.setObjectName(u"txt_grp_plan")
        self.txt_grp_plan.setMinimumSize(QSize(0, 35))
        self.txt_grp_plan.setMaximumSize(QSize(110, 35))
        self.txt_grp_plan.setFont(font)
        self.txt_grp_plan.setStyleSheet(u"background-color: rgb(225, 225, 225);\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(170, 170, 170);\n"
"")
        self.txt_grp_plan.setMaxLength(4)
        self.txt_grp_plan.setAlignment(Qt.AlignCenter)
        self.txt_grp_plan.setReadOnly(True)

        self.gridLayout.addWidget(self.txt_grp_plan, 8, 8, 1, 1)

        self.txt_data = QLineEdit(self.frame)
        self.txt_data.setObjectName(u"txt_data")
        sizePolicy2.setHeightForWidth(self.txt_data.sizePolicy().hasHeightForWidth())
        self.txt_data.setSizePolicy(sizePolicy2)
        self.txt_data.setMinimumSize(QSize(0, 35))
        self.txt_data.setMaximumSize(QSize(16777215, 35))
        self.txt_data.setLayoutDirection(Qt.LeftToRight)
        self.txt_data.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_data, 2, 0, 1, 1)

        self.txt_tp_mrp = QLineEdit(self.frame)
        self.txt_tp_mrp.setObjectName(u"txt_tp_mrp")
        self.txt_tp_mrp.setMinimumSize(QSize(0, 35))
        self.txt_tp_mrp.setMaximumSize(QSize(16777215, 35))
        self.txt_tp_mrp.setFont(font)
        self.txt_tp_mrp.setStyleSheet(u"background-color: rgb(225, 225, 225);\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(170, 170, 170);\n"
"")
        self.txt_tp_mrp.setMaxLength(2)
        self.txt_tp_mrp.setAlignment(Qt.AlignCenter)
        self.txt_tp_mrp.setReadOnly(True)

        self.gridLayout.addWidget(self.txt_tp_mrp, 8, 2, 1, 1)

        self.tb_proc_comp = QTableWidget(self.frame)
        if (self.tb_proc_comp.columnCount() < 4):
            self.tb_proc_comp.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tb_proc_comp.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tb_proc_comp.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tb_proc_comp.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tb_proc_comp.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tb_proc_comp.setObjectName(u"tb_proc_comp")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.tb_proc_comp.sizePolicy().hasHeightForWidth())
        self.tb_proc_comp.setSizePolicy(sizePolicy3)
        self.tb_proc_comp.setFont(font1)
        self.tb_proc_comp.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tb_proc_comp.setTabKeyNavigation(False)
        self.tb_proc_comp.setProperty("showDropIndicator", False)
        self.tb_proc_comp.setDragEnabled(False)
        self.tb_proc_comp.setDragDropOverwriteMode(False)
        self.tb_proc_comp.setRowCount(0)
        self.tb_proc_comp.setColumnCount(4)
        self.tb_proc_comp.horizontalHeader().setCascadingSectionResizes(False)
        self.tb_proc_comp.horizontalHeader().setProperty("showSortIndicator", False)
        self.tb_proc_comp.horizontalHeader().setStretchLastSection(True)

        self.gridLayout.addWidget(self.tb_proc_comp, 17, 8, 5, 3)

        self.label_39 = QLabel(self.frame)
        self.label_39.setObjectName(u"label_39")
        sizePolicy.setHeightForWidth(self.label_39.sizePolicy().hasHeightForWidth())
        self.label_39.setSizePolicy(sizePolicy)
        self.label_39.setMinimumSize(QSize(0, 20))
        self.label_39.setMaximumSize(QSize(213, 20))
        self.label_39.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_39, 16, 3, 1, 4)

        self.label_36 = QLabel(self.frame)
        self.label_36.setObjectName(u"label_36")
        sizePolicy.setHeightForWidth(self.label_36.sizePolicy().hasHeightForWidth())
        self.label_36.setSizePolicy(sizePolicy)
        self.label_36.setMinimumSize(QSize(0, 20))
        self.label_36.setMaximumSize(QSize(16777215, 20))
        self.label_36.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_36, 16, 0, 1, 3)

        self.label_32 = QLabel(self.frame)
        self.label_32.setObjectName(u"label_32")
        sizePolicy.setHeightForWidth(self.label_32.sizePolicy().hasHeightForWidth())
        self.label_32.setSizePolicy(sizePolicy)
        self.label_32.setMinimumSize(QSize(0, 20))
        self.label_32.setMaximumSize(QSize(16777215, 20))
        self.label_32.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_32, 10, 10, 1, 1)

        self.label_25 = QLabel(self.frame)
        self.label_25.setObjectName(u"label_25")
        sizePolicy.setHeightForWidth(self.label_25.sizePolicy().hasHeightForWidth())
        self.label_25.setSizePolicy(sizePolicy)
        self.label_25.setMinimumSize(QSize(0, 20))
        self.label_25.setMaximumSize(QSize(110, 20))
        self.label_25.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_25, 7, 8, 1, 1)

        self.label_40 = QLabel(self.frame)
        self.label_40.setObjectName(u"label_40")
        sizePolicy.setHeightForWidth(self.label_40.sizePolicy().hasHeightForWidth())
        self.label_40.setSizePolicy(sizePolicy)
        self.label_40.setMinimumSize(QSize(0, 20))
        self.label_40.setMaximumSize(QSize(110, 20))
        self.label_40.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_40, 12, 3, 1, 2)

        self.txt_cons_fint = QLineEdit(self.frame)
        self.txt_cons_fint.setObjectName(u"txt_cons_fint")
        self.txt_cons_fint.setMinimumSize(QSize(0, 35))
        self.txt_cons_fint.setMaximumSize(QSize(16777215, 35))
        self.txt_cons_fint.setFont(font)
        self.txt_cons_fint.setStyleSheet(u"background-color: rgb(225, 225, 225);\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: rgb(170, 170, 170);\n"
"")
        self.txt_cons_fint.setMaxLength(4)
        self.txt_cons_fint.setAlignment(Qt.AlignCenter)
        self.txt_cons_fint.setReadOnly(True)

        self.gridLayout.addWidget(self.txt_cons_fint, 11, 2, 1, 1)

        self.label_37 = QLabel(self.frame)
        self.label_37.setObjectName(u"label_37")
        sizePolicy.setHeightForWidth(self.label_37.sizePolicy().hasHeightForWidth())
        self.label_37.setSizePolicy(sizePolicy)
        self.label_37.setMinimumSize(QSize(0, 20))
        self.label_37.setMaximumSize(QSize(16777215, 20))
        self.label_37.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_37, 18, 0, 1, 3)

        self.label_30 = QLabel(self.frame)
        self.label_30.setObjectName(u"label_30")
        sizePolicy.setHeightForWidth(self.label_30.sizePolicy().hasHeightForWidth())
        self.label_30.setSizePolicy(sizePolicy)
        self.label_30.setMinimumSize(QSize(0, 20))
        self.label_30.setMaximumSize(QSize(110, 20))
        self.label_30.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_30, 10, 8, 1, 1)

        self.txt_segunda_cont = QLineEdit(self.frame)
        self.txt_segunda_cont.setObjectName(u"txt_segunda_cont")
        self.txt_segunda_cont.setMinimumSize(QSize(0, 35))
        self.txt_segunda_cont.setMaximumSize(QSize(16777215, 35))
        self.txt_segunda_cont.setInputMask(u"")
        self.txt_segunda_cont.setMaxLength(32767)
        self.txt_segunda_cont.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_segunda_cont, 11, 9, 1, 1)

        self.txt_qt_solicitada = QLineEdit(self.frame)
        self.txt_qt_solicitada.setObjectName(u"txt_qt_solicitada")
        self.txt_qt_solicitada.setMinimumSize(QSize(0, 35))
        self.txt_qt_solicitada.setMaximumSize(QSize(16777215, 35))
        self.txt_qt_solicitada.setMaxLength(20)
        self.txt_qt_solicitada.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.txt_qt_solicitada, 8, 0, 1, 1)

        self.label_22 = QLabel(self.frame)
        self.label_22.setObjectName(u"label_22")
        sizePolicy.setHeightForWidth(self.label_22.sizePolicy().hasHeightForWidth())
        self.label_22.setSizePolicy(sizePolicy)
        self.label_22.setMinimumSize(QSize(0, 20))
        self.label_22.setMaximumSize(QSize(110, 20))
        self.label_22.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_22, 7, 6, 1, 1)

        self.label_24 = QLabel(self.frame)
        self.label_24.setObjectName(u"label_24")
        sizePolicy.setHeightForWidth(self.label_24.sizePolicy().hasHeightForWidth())
        self.label_24.setSizePolicy(sizePolicy)
        self.label_24.setMinimumSize(QSize(0, 20))
        self.label_24.setMaximumSize(QSize(16777215, 20))
        self.label_24.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_24, 7, 2, 1, 1)

        self.label_41 = QLabel(self.frame)
        self.label_41.setObjectName(u"label_41")
        sizePolicy.setHeightForWidth(self.label_41.sizePolicy().hasHeightForWidth())
        self.label_41.setSizePolicy(sizePolicy)
        self.label_41.setMinimumSize(QSize(0, 20))
        self.label_41.setMaximumSize(QSize(110, 20))
        self.label_41.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_41, 12, 8, 1, 1)

        self.cmb_cod_sit = QComboBox(self.frame)
        self.cmb_cod_sit.addItem("")
        self.cmb_cod_sit.addItem("")
        self.cmb_cod_sit.addItem("")
        self.cmb_cod_sit.addItem("")
        self.cmb_cod_sit.addItem("")
        self.cmb_cod_sit.addItem("")
        self.cmb_cod_sit.addItem("")
        self.cmb_cod_sit.addItem("")
        self.cmb_cod_sit.addItem("")
        self.cmb_cod_sit.addItem("")
        self.cmb_cod_sit.addItem("")
        self.cmb_cod_sit.addItem("")
        self.cmb_cod_sit.addItem("")
        self.cmb_cod_sit.addItem("")
        self.cmb_cod_sit.addItem("")
        self.cmb_cod_sit.addItem("")
        self.cmb_cod_sit.addItem("")
        self.cmb_cod_sit.addItem("")
        self.cmb_cod_sit.addItem("")
        self.cmb_cod_sit.setObjectName(u"cmb_cod_sit")
        self.cmb_cod_sit.setMinimumSize(QSize(0, 35))

        self.gridLayout.addWidget(self.cmb_cod_sit, 17, 0, 1, 3)

        self.label_28 = QLabel(self.frame)
        self.label_28.setObjectName(u"label_28")
        sizePolicy.setHeightForWidth(self.label_28.sizePolicy().hasHeightForWidth())
        self.label_28.setSizePolicy(sizePolicy)
        self.label_28.setMinimumSize(QSize(0, 20))
        self.label_28.setMaximumSize(QSize(110, 20))
        self.label_28.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_28, 10, 3, 1, 2)

        self.lb_info = QLabel(self.frame)
        self.lb_info.setObjectName(u"lb_info")
        sizePolicy.setHeightForWidth(self.lb_info.sizePolicy().hasHeightForWidth())
        self.lb_info.setSizePolicy(sizePolicy)
        self.lb_info.setMinimumSize(QSize(0, 0))
        self.lb_info.setMaximumSize(QSize(16777215, 16777215))
        self.lb_info.setStyleSheet(u"background-color: rgb(255, 0, 0);\n"
"border-width: 1px;\n"
"font: bold 9pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);\n"
"")
        self.lb_info.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lb_info, 20, 0, 1, 3)


        self.verticalLayout_2.addWidget(self.frame)

        self.verticalSpacer_2 = QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)


        self.verticalLayout_3.addWidget(self.frame_3)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)

#if QT_CONFIG(shortcut)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.txt_data, self.txt_hora)
        QWidget.setTabOrder(self.txt_hora, self.txt_mat)
        QWidget.setTabOrder(self.txt_mat, self.txt_solicitante)
        QWidget.setTabOrder(self.txt_solicitante, self.txt_ramal)
        QWidget.setTabOrder(self.txt_ramal, self.cmb_setor)
        QWidget.setTabOrder(self.cmb_setor, self.txt_obs_almox)
        QWidget.setTabOrder(self.txt_obs_almox, self.txt_qt_solicitada)
        QWidget.setTabOrder(self.txt_qt_solicitada, self.txt_saldo_fisico)
        QWidget.setTabOrder(self.txt_saldo_fisico, self.txt_segunda_cont)
        QWidget.setTabOrder(self.txt_segunda_cont, self.txt_req_manual)
        QWidget.setTabOrder(self.txt_req_manual, self.cmb_cod_sit)
        QWidget.setTabOrder(self.cmb_cod_sit, self.cmb_sit_ped)
        QWidget.setTabOrder(self.cmb_sit_ped, self.btn_salvar_novo)
        QWidget.setTabOrder(self.btn_salvar_novo, self.btn_salvar_sair)
        QWidget.setTabOrder(self.btn_salvar_sair, self.btn_cancelar)
        QWidget.setTabOrder(self.btn_cancelar, self.txt_saldo_sistema)
        QWidget.setTabOrder(self.txt_saldo_sistema, self.txt_bloqueado)
        QWidget.setTabOrder(self.txt_bloqueado, self.scrollArea)
        QWidget.setTabOrder(self.scrollArea, self.txt_und_med)
        QWidget.setTabOrder(self.txt_und_med, self.txt_decricao)
        QWidget.setTabOrder(self.txt_decricao, self.txt_devergencia)
        QWidget.setTabOrder(self.txt_devergencia, self.txt_total_proc)
        QWidget.setTabOrder(self.txt_total_proc, self.txt_valor_unit)
        QWidget.setTabOrder(self.txt_valor_unit, self.ptxt_nota_mat)
        QWidget.setTabOrder(self.ptxt_nota_mat, self.txt_critico)
        QWidget.setTabOrder(self.txt_critico, self.txt_status_erp_geral)
        QWidget.setTabOrder(self.txt_status_erp_geral, self.txt_cons_fint)
        QWidget.setTabOrder(self.txt_cons_fint, self.txt_grp_plan)
        QWidget.setTabOrder(self.txt_grp_plan, self.txt_grp_comp)
        QWidget.setTabOrder(self.txt_grp_comp, self.txt_plan)
        QWidget.setTabOrder(self.txt_plan, self.txt_comprador)

        self.retranslateUi(NaoAtendidos)

        QMetaObject.connectSlotsByName(NaoAtendidos)
    # setupUi

    def retranslateUi(self, NaoAtendidos):
        NaoAtendidos.setWindowTitle(QCoreApplication.translate("NaoAtendidos", u"Form", None))
        self.label.setText(QCoreApplication.translate("NaoAtendidos", u"  Formul\u00e1rio N\u00e3o Atendidos", None))
#if QT_CONFIG(tooltip)
        self.btn_salvar_novo.setToolTip(QCoreApplication.translate("NaoAtendidos", u"<html><head/><body><p>Salvar e Novo</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_salvar_novo.setText("")
#if QT_CONFIG(tooltip)
        self.btn_salvar_sair.setToolTip(QCoreApplication.translate("NaoAtendidos", u"<html><head/><body><p>Salvar e Sair</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_salvar_sair.setText("")
#if QT_CONFIG(tooltip)
        self.btn_cancelar.setToolTip(QCoreApplication.translate("NaoAtendidos", u"<html><head/><body><p>Cancelar</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_cancelar.setText("")
        self.label_38.setText(QCoreApplication.translate("NaoAtendidos", u"Situa\u00e7\u00e3o Processo Compras", None))
        self.label_21.setText(QCoreApplication.translate("NaoAtendidos", u"Qt. Solic.", None))
        self.label_34.setText(QCoreApplication.translate("NaoAtendidos", u"Diverg.", None))
        self.txt_bloqueado.setInputMask("")
        self.txt_bloqueado.setPlaceholderText("")
        self.label_13.setText(QCoreApplication.translate("NaoAtendidos", u"Hora", None))
        self.txt_minimo.setInputMask("")
        self.txt_minimo.setText("")
        self.txt_minimo.setPlaceholderText("")
        self.txt_comprador.setInputMask("")
        self.txt_comprador.setText("")
        self.txt_comprador.setPlaceholderText("")
        self.txt_grp_comp.setInputMask("")
        self.txt_grp_comp.setText("")
        self.txt_grp_comp.setPlaceholderText("")
        self.txt_status_erp_geral.setInputMask("")
        self.txt_status_erp_geral.setText("")
        self.txt_status_erp_geral.setPlaceholderText("")
        self.txt_saldo_fisico.setInputMask("")
        self.txt_saldo_fisico.setPlaceholderText("")
        self.label_33.setText(QCoreApplication.translate("NaoAtendidos", u"Req. Man.", None))
        self.label_43.setText(QCoreApplication.translate("NaoAtendidos", u"Comprador", None))
        self.txt_critico.setInputMask("")
        self.txt_critico.setText("")
        self.txt_critico.setPlaceholderText("")
        self.cmb_sit_ped.setItemText(0, "")
        self.cmb_sit_ped.setItemText(1, QCoreApplication.translate("NaoAtendidos", u"PA - Pedido Atrasado", None))
        self.cmb_sit_ped.setItemText(2, QCoreApplication.translate("NaoAtendidos", u"SP - Sem Pedido", None))
        self.cmb_sit_ped.setItemText(3, QCoreApplication.translate("NaoAtendidos", u"EF - Entrega Futura", None))
        self.cmb_sit_ped.setItemText(4, QCoreApplication.translate("NaoAtendidos", u"EH - Entrega Hoje", None))

        self.txt_mat.setInputMask("")
        self.txt_mat.setText("")
        self.txt_mat.setPlaceholderText("")
        self.txt_plan.setInputMask("")
        self.txt_plan.setText("")
        self.txt_plan.setPlaceholderText("")
        self.txt_devergencia.setInputMask("")
        self.txt_devergencia.setText("")
        self.txt_devergencia.setPlaceholderText("")
        self.label_31.setText(QCoreApplication.translate("NaoAtendidos", u"2\u00aa Cont.", None))
        self.ptxt_nota_mat.setPlainText("")
        self.txt_valor_unit.setInputMask("")
        self.txt_valor_unit.setText("")
        self.txt_valor_unit.setPlaceholderText("")
        self.txt_saldo_sistema.setInputMask("")
        self.txt_saldo_sistema.setText("")
        self.txt_saldo_sistema.setPlaceholderText("")
        self.label_19.setText(QCoreApplication.translate("NaoAtendidos", u"Observa\u00e7\u00e3o do Almoxarife", None))
        self.label_42.setText(QCoreApplication.translate("NaoAtendidos", u"Planejador", None))
        self.txt_obs_almox.setInputMask("")
        self.txt_obs_almox.setPlaceholderText("")
        self.label_29.setText(QCoreApplication.translate("NaoAtendidos", u"Saldo Sist.", None))
        self.label_16.setText(QCoreApplication.translate("NaoAtendidos", u"Ramal", None))
        self.txt_hora.setInputMask(QCoreApplication.translate("NaoAtendidos", u"00:00", None))
        self.txt_hora.setText(QCoreApplication.translate("NaoAtendidos", u":", None))
        self.txt_hora.setPlaceholderText("")
        self.txt_solicitante.setInputMask("")
        self.txt_solicitante.setText("")
        self.txt_solicitante.setPlaceholderText("")
        self.txt_decricao.setInputMask("")
        self.txt_decricao.setText("")
        self.txt_decricao.setPlaceholderText("")
        self.label_20.setText(QCoreApplication.translate("NaoAtendidos", u"M\u00ednimo", None))
        self.label_27.setText(QCoreApplication.translate("NaoAtendidos", u"Cons./FINT", None))
        self.label_35.setText(QCoreApplication.translate("NaoAtendidos", u"Valor Unit.", None))
        self.label_14.setText(QCoreApplication.translate("NaoAtendidos", u"C\u00f3digo Mat.", None))
        self.label_9.setText(QCoreApplication.translate("NaoAtendidos", u"Data", None))
        self.txt_req_manual.setInputMask("")
        self.txt_req_manual.setPlaceholderText("")
        self.txt_status_erp_cen.setInputMask("")
        self.txt_status_erp_cen.setText("")
        self.txt_status_erp_cen.setPlaceholderText("")
        self.label_15.setText(QCoreApplication.translate("NaoAtendidos", u"Descri\u00e7\u00e3o", None))
        self.label_18.setText(QCoreApplication.translate("NaoAtendidos", u"Setor", None))
        self.txt_ramal.setInputMask("")
        self.txt_ramal.setText("")
        self.txt_ramal.setPlaceholderText("")
        self.label_26.setText(QCoreApplication.translate("NaoAtendidos", u"Cr\u00edtico", None))
        self.label_10.setText(QCoreApplication.translate("NaoAtendidos", u"Solicitante", None))
        self.txt_maximo.setInputMask("")
        self.txt_maximo.setText("")
        self.txt_maximo.setPlaceholderText("")
        self.txt_total_proc.setInputMask("")
        self.txt_total_proc.setText("")
        self.txt_total_proc.setPlaceholderText("")
        self.txt_und_med.setInputMask("")
        self.txt_und_med.setText("")
        self.txt_und_med.setPlaceholderText("")
        self.label_17.setText(QCoreApplication.translate("NaoAtendidos", u"UnMed", None))
        self.txt_grp_plan.setInputMask("")
        self.txt_grp_plan.setText("")
        self.txt_grp_plan.setPlaceholderText("")
        self.txt_data.setInputMask(QCoreApplication.translate("NaoAtendidos", u"00.00.0000", None))
        self.txt_data.setText(QCoreApplication.translate("NaoAtendidos", u"..", None))
        self.txt_data.setPlaceholderText("")
        self.txt_tp_mrp.setInputMask("")
        self.txt_tp_mrp.setText("")
        self.txt_tp_mrp.setPlaceholderText("")
        ___qtablewidgetitem = self.tb_proc_comp.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("NaoAtendidos", u"Data Prevista", None));
        ___qtablewidgetitem1 = self.tb_proc_comp.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("NaoAtendidos", u"Status", None));
        ___qtablewidgetitem2 = self.tb_proc_comp.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("NaoAtendidos", u"Tp.Proc.", None));
        ___qtablewidgetitem3 = self.tb_proc_comp.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("NaoAtendidos", u"Proc.Comp.", None));
        self.label_39.setText(QCoreApplication.translate("NaoAtendidos", u"Nota Mat.", None))
        self.label_36.setText(QCoreApplication.translate("NaoAtendidos", u"C\u00f3d. Sit.", None))
        self.label_32.setText(QCoreApplication.translate("NaoAtendidos", u"Bloqueado", None))
        self.label_25.setText(QCoreApplication.translate("NaoAtendidos", u"Grp. Plan.", None))
        self.label_40.setText(QCoreApplication.translate("NaoAtendidos", u"N\u00b0. Proc. Comp.", None))
        self.txt_cons_fint.setInputMask("")
        self.txt_cons_fint.setText("")
        self.txt_cons_fint.setPlaceholderText("")
        self.label_37.setText(QCoreApplication.translate("NaoAtendidos", u"Sit. Pedido", None))
        self.label_30.setText(QCoreApplication.translate("NaoAtendidos", u"Saldo F\u00edsico", None))
        self.txt_segunda_cont.setText("")
        self.txt_segunda_cont.setPlaceholderText("")
        self.txt_qt_solicitada.setInputMask("")
        self.txt_qt_solicitada.setPlaceholderText("")
        self.label_22.setText(QCoreApplication.translate("NaoAtendidos", u"M\u00e1ximo", None))
        self.label_24.setText(QCoreApplication.translate("NaoAtendidos", u"Tp. MRP", None))
        self.label_41.setText(QCoreApplication.translate("NaoAtendidos", u"Grp.Comp.", None))
        self.cmb_cod_sit.setItemText(0, "")
        self.cmb_cod_sit.setItemText(1, QCoreApplication.translate("NaoAtendidos", u"AI - Armazenado Incorretamente", None))
        self.cmb_cod_sit.setItemText(2, QCoreApplication.translate("NaoAtendidos", u"DD - Outros", None))
        self.cmb_cod_sit.setItemText(3, QCoreApplication.translate("NaoAtendidos", u"EI - Entrega Incorreta Fornecedor", None))
        self.cmb_cod_sit.setItemText(4, QCoreApplication.translate("NaoAtendidos", u"FE - Furo de Estoque", None))
        self.cmb_cod_sit.setItemText(5, QCoreApplication.translate("NaoAtendidos", u"FN - Falta Entrada Nota Fiscal", None))
        self.cmb_cod_sit.setItemText(6, QCoreApplication.translate("NaoAtendidos", u"IO - Material Obsoleto", None))
        self.cmb_cod_sit.setItemText(7, QCoreApplication.translate("NaoAtendidos", u"IR - Material Reservado", None))
        self.cmb_cod_sit.setItemText(8, QCoreApplication.translate("NaoAtendidos", u"MC - Material de Conserto", None))
        self.cmb_cod_sit.setItemText(9, QCoreApplication.translate("NaoAtendidos", u"MR - Movimentado Recentemente", None))
        self.cmb_cod_sit.setItemText(10, QCoreApplication.translate("NaoAtendidos", u"NA - N\u00e3o Armazenado", None))
        self.cmb_cod_sit.setItemText(11, QCoreApplication.translate("NaoAtendidos", u"NS - N\u00e3o Subiu para o SAP", None))
        self.cmb_cod_sit.setItemText(12, QCoreApplication.translate("NaoAtendidos", u"ND - Material ND", None))
        self.cmb_cod_sit.setItemText(13, QCoreApplication.translate("NaoAtendidos", u"OM - Outro Material", None))
        self.cmb_cod_sit.setItemText(14, QCoreApplication.translate("NaoAtendidos", u"OC - Material de Outro Centro", None))
        self.cmb_cod_sit.setItemText(15, QCoreApplication.translate("NaoAtendidos", u"PP - Pedido Pendente", None))
        self.cmb_cod_sit.setItemText(16, QCoreApplication.translate("NaoAtendidos", u"RP - RC Pendente", None))
        self.cmb_cod_sit.setItemText(17, QCoreApplication.translate("NaoAtendidos", u"SR - Sem Reposi\u00e7\u00e3o", None))
        self.cmb_cod_sit.setItemText(18, QCoreApplication.translate("NaoAtendidos", u"SP - Sem Padroniza\u00e7\u00e3o", None))

        self.label_28.setText(QCoreApplication.translate("NaoAtendidos", u"Status ERP", None))
        self.lb_info.setText("")
    # retranslateUi

