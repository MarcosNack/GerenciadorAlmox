# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainGerenciadorAlmox.ui'
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
    QComboBox, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QProgressBar, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QStackedWidget, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)
import assets.icons_alt_regras_rc

class Ui_MainGerenciadorAlmox(object):
    def setupUi(self, MainGerenciadorAlmox):
        if not MainGerenciadorAlmox.objectName():
            MainGerenciadorAlmox.setObjectName(u"MainGerenciadorAlmox")
        MainGerenciadorAlmox.resize(930, 600)
        MainGerenciadorAlmox.setMinimumSize(QSize(930, 600))
        MainGerenciadorAlmox.setStyleSheet(u"#centralwidget{\n"
"	background-color: rgb(0, 98, 98);\n"
"	border-style: ridge;\n"
"	border-width: 4px;\n"
"    border-radius: 0px;\n"
"    border-color: rgb(234, 234, 234);\n"
"	padding-left: 5px;\n"
"	}\n"
"QWidget{\n"
"	background-color: rgb(0, 98, 98);\n"
"	}\n"
"QTableWidget{\n"
"	background-color: rgb(255, 255, 255);\n"
"	font: 9pt \"Segoe UI\";\n"
"	}\n"
"QTableWidget QLineEdit::focus{\n"
"	background-color: rgb(170, 255, 255);\n"
"    border-style: ridge;\n"
"	border-width: 2px;\n"
"	color: rgb(0, 0, 0);\n"
"	}\n"
"QTableWidget QWidget {\n"
"	background-color: rgb(0, 108, 108);\n"
"    color: #fffff8;\n"
"	font: bold 9pt \"Segoe UI\";\n"
"	}\n"
"QTableWidget QHeaderView::section {\n"
"	background-color :rgb(0, 98, 98);\n"
"	border-style: ridge;\n"
"   	border-width: 2px;\n"
"    border-color: rgb(170, 170, 170);\n"
"	border-radius: 2px;\n"
" 	padding-left: 2px;\n"
"  }\n"
"QTableWidget QTableCornerButton::section {\n"
"  	background-color: rgb(0, 98, 98);\n"
"	border-style: ridge;\n"
"   	border-width"
                        ": 2px;\n"
"    border-color: rgb(170, 170, 170);\n"
"	border-radius: 2px;\n"
"	}\n"
"QLabel{	\n"
"	background-color: rgb(225, 225, 225);\n"
"	border-style: ridge ;\n"
"	border-width: 3px;\n"
"    border-color: rgb(170, 170, 170);\n"
"    font: bold 12px;\n"
"	text-align: left;\n"
"	}\n"
"QLineEdit{		\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-style: double;\n"
"	border-width: 3px;\n"
"    border-color: rgb(170, 170, 170);\n"
"    font: bold 12px;\n"
"	}\n"
"QLineEdit::focus{\n"
"    background-color: rgb(170, 255, 255);\n"
"    border-style: inset;\n"
"	}\n"
"")
        self.centralwidget = QWidget(MainGerenciadorAlmox)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.gridLayout_20 = QGridLayout(self.centralwidget)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.gridLayout_20.setHorizontalSpacing(6)
        self.gridLayout_20.setVerticalSpacing(0)
        self.qf_home = QFrame(self.centralwidget)
        self.qf_home.setObjectName(u"qf_home")
        self.qf_home.setMinimumSize(QSize(240, 0))
        self.qf_home.setStyleSheet(u"#frame_3{\n"
"    border-style: ridge;\n"
"    border-width: 3px;\n"
"    border-radius: 5px;\n"
"    border-color: rgb(234, 234, 234);\n"
"}\n"
"#qf_home_button{\n"
"    border-style: ridge;\n"
"    border-width: 3px;\n"
"    border-radius: 5px;\n"
"    border-color: rgb(234, 234, 234);\n"
"}")
        self.qf_home.setFrameShape(QFrame.StyledPanel)
        self.qf_home.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.qf_home)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.qf_home)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(16777215, 50))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 0))
        self.label_2.setStyleSheet(u"border: 0px;\n"
"color: rgb(255, 255, 255);\n"
"font: bold 14pt;\n"
"background-color: rgb(0, 98, 98)")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_2)


        self.verticalLayout.addWidget(self.frame_3)

        self.qf_home_button = QFrame(self.qf_home)
        self.qf_home_button.setObjectName(u"qf_home_button")
        self.qf_home_button.setStyleSheet(u"#qw_home_btn{\n"
"    border-style: outset;\n"
"    border-width: 3px;\n"
"    border-radius: 0px;\n"
"    border-color: rgb(234, 234, 234);\n"
"\n"
"}\n"
"\n"
"QPushButton{	\n"
"	background-color: rgb(225, 225, 225);\n"
"    border-style: ridge;\n"
"    border-width: 3px;\n"
"    border-color: rgb(234, 234, 234);\n"
"    font: bold 12px;\n"
"	padding-right: 5px;		\n"
"	text-align: left;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background-color: rgb(150, 150, 150);\n"
"    border-style: inset;\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"    background-color: rgb(150, 150, 150);\n"
"    border-style: inset;\n"
"}")
        self.qf_home_button.setFrameShape(QFrame.StyledPanel)
        self.qf_home_button.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.qf_home_button)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(3, 10, 0, 5)
        self.home_btn_alt_local = QPushButton(self.qf_home_button)
        self.home_btn_alt_local.setObjectName(u"home_btn_alt_local")
        self.home_btn_alt_local.setMinimumSize(QSize(0, 35))
        self.home_btn_alt_local.setCursor(QCursor(Qt.PointingHandCursor))
        self.home_btn_alt_local.setLayoutDirection(Qt.RightToLeft)
        self.home_btn_alt_local.setCheckable(True)

        self.verticalLayout_3.addWidget(self.home_btn_alt_local)

        self.home_btn_cont_entrada_almox = QPushButton(self.qf_home_button)
        self.home_btn_cont_entrada_almox.setObjectName(u"home_btn_cont_entrada_almox")
        self.home_btn_cont_entrada_almox.setMinimumSize(QSize(0, 35))
        self.home_btn_cont_entrada_almox.setCursor(QCursor(Qt.PointingHandCursor))
        self.home_btn_cont_entrada_almox.setLayoutDirection(Qt.RightToLeft)
        self.home_btn_cont_entrada_almox.setCheckable(True)

        self.verticalLayout_3.addWidget(self.home_btn_cont_entrada_almox)

        self.home_btn_nao_atendidos = QPushButton(self.qf_home_button)
        self.home_btn_nao_atendidos.setObjectName(u"home_btn_nao_atendidos")
        self.home_btn_nao_atendidos.setMinimumSize(QSize(0, 35))
        self.home_btn_nao_atendidos.setCursor(QCursor(Qt.PointingHandCursor))
        self.home_btn_nao_atendidos.setLayoutDirection(Qt.RightToLeft)
        self.home_btn_nao_atendidos.setCheckable(True)

        self.verticalLayout_3.addWidget(self.home_btn_nao_atendidos)

        self.home_btn_recebimento = QPushButton(self.qf_home_button)
        self.home_btn_recebimento.setObjectName(u"home_btn_recebimento")
        self.home_btn_recebimento.setMinimumSize(QSize(0, 35))
        self.home_btn_recebimento.setCursor(QCursor(Qt.PointingHandCursor))
        self.home_btn_recebimento.setLayoutDirection(Qt.RightToLeft)
        self.home_btn_recebimento.setCheckable(True)

        self.verticalLayout_3.addWidget(self.home_btn_recebimento)

        self.home_btn_cont_acesso = QPushButton(self.qf_home_button)
        self.home_btn_cont_acesso.setObjectName(u"home_btn_cont_acesso")
        self.home_btn_cont_acesso.setMinimumSize(QSize(0, 35))
        self.home_btn_cont_acesso.setCursor(QCursor(Qt.PointingHandCursor))
        self.home_btn_cont_acesso.setLayoutDirection(Qt.RightToLeft)
        self.home_btn_cont_acesso.setCheckable(True)

        self.verticalLayout_3.addWidget(self.home_btn_cont_acesso)

        self.verticalSpacer = QSpacerItem(178, 336, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.home_btn_config = QPushButton(self.qf_home_button)
        self.home_btn_config.setObjectName(u"home_btn_config")
        self.home_btn_config.setMinimumSize(QSize(0, 41))
        self.home_btn_config.setStyleSheet(u"QPushButton{	\n"
"	background-color: rgb(225, 225, 225);\n"
"    border-style: ridge;\n"
"    border-width: 3px;\n"
"    border-color: rgb(234, 234, 234);\n"
"	border-radius: 5px;\n"
"    font: bold 12px;\n"
"	padding: 0px;		\n"
"	text-align: center;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background-color: rgb(150, 150, 150);\n"
"    border-style: inset;\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"    background-color: rgb(150, 150, 150);\n"
"    border-style: inset;\n"
"}")
        icon = QIcon()
        icon.addFile(u":/assets.icons_alt_regras/configura\u00e7\u00f5es.png", QSize(), QIcon.Normal, QIcon.Off)
        self.home_btn_config.setIcon(icon)
        self.home_btn_config.setIconSize(QSize(30, 30))

        self.verticalLayout_3.addWidget(self.home_btn_config, 0, Qt.AlignLeft|Qt.AlignTop)


        self.verticalLayout.addWidget(self.qf_home_button)


        self.gridLayout_20.addWidget(self.qf_home, 0, 0, 1, 1)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 0))
        self.frame_2.setStyleSheet(u"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(0, 50))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_5)
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.btn_home = QPushButton(self.frame_5)
        self.btn_home.setObjectName(u"btn_home")
        self.btn_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_home.setLayoutDirection(Qt.RightToLeft)
        self.btn_home.setStyleSheet(u"QPushButton{	\n"
"	background-color: rgb(225, 225, 225);\n"
"    border-style: ridge;\n"
"    border-width: 3px;\n"
"\n"
" 	border-color: rgb(234, 234, 234);\n"
"    font: bold 12px;\n"
"\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"    background-color: rgb(150, 150, 150);\n"
"    border-style: inset;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/assets.icons_alt_regras/menu-arredondado.png", QSize(), QIcon.Normal, QIcon.Off)
        icon1.addFile(u":/assets.icons_alt_regras/duplo-para-a-esquerda.png", QSize(), QIcon.Normal, QIcon.On)
        self.btn_home.setIcon(icon1)
        self.btn_home.setIconSize(QSize(41, 41))
        self.btn_home.setCheckable(True)

        self.horizontalLayout.addWidget(self.btn_home)

        self.lb_logo = QLabel(self.frame_5)
        self.lb_logo.setObjectName(u"lb_logo")
        self.lb_logo.setMaximumSize(QSize(16777215, 49))
        self.lb_logo.setStyleSheet(u"background-color: rgb(234, 234, 234);\n"
"border-radius: 3px;")
        self.lb_logo.setPixmap(QPixmap(u":/assets.icons_alt_regras/logo.png"))
        self.lb_logo.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.lb_logo.setMargin(1)
        self.lb_logo.setIndent(-1)

        self.horizontalLayout.addWidget(self.lb_logo)

        self.lb_titulo = QLabel(self.frame_5)
        self.lb_titulo.setObjectName(u"lb_titulo")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lb_titulo.sizePolicy().hasHeightForWidth())
        self.lb_titulo.setSizePolicy(sizePolicy)
        self.lb_titulo.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: bold 20pt;\n"
"background-color: rgb(0, 98, 98);\n"
"border-radius: 3px;")
        self.lb_titulo.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.lb_titulo)


        self.verticalLayout_2.addWidget(self.frame_5, 0, Qt.AlignTop)

        self.frame_6 = QFrame(self.frame_2)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy1)
        self.frame_6.setStyleSheet(u"#scrollArea {\n"
"	background-color: rgb(0, 108, 108);\n"
"	border-width: 5px;\n"
"    border-radius: 5px;\n"
"    border-color: rgb(0, 161, 161);\n"
"}\n"
"")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_78 = QVBoxLayout(self.frame_6)
        self.verticalLayout_78.setSpacing(0)
        self.verticalLayout_78.setObjectName(u"verticalLayout_78")
        self.verticalLayout_78.setContentsMargins(0, 0, 0, 0)
        self.pgs_principal = QStackedWidget(self.frame_6)
        self.pgs_principal.setObjectName(u"pgs_principal")
        sizePolicy2 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pgs_principal.sizePolicy().hasHeightForWidth())
        self.pgs_principal.setSizePolicy(sizePolicy2)
        self.pgs_principal.setStyleSheet(u"QScrollArea{	\n"
" 	border: 3px solid;\n"
"    border-color: rgb(234, 234, 234);\n"
"}\n"
"QPushButton {\n"
"	border-width: 5px;\n"
"    border-radius: 5px;\n"
"    border-color: rgb(0, 161, 161);\n"
"}\n"
"QComboBox::focus{\n"
"    border-style: inset;\n"
"	border-color: rgb(0, 179, 179);\n"
"}\n"
"\n"
"")
        self.pg_alt_dep = QWidget()
        self.pg_alt_dep.setObjectName(u"pg_alt_dep")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.pg_alt_dep.sizePolicy().hasHeightForWidth())
        self.pg_alt_dep.setSizePolicy(sizePolicy3)
        self.pg_alt_dep.setMinimumSize(QSize(0, 0))
        self.pg_alt_dep.setStyleSheet(u"#frame_4{	\n"
"    background-color: rgb(200, 200, 200);\n"
"}\n"
"\n"
"#frame_19{	\n"
"    background-color: rgb(200, 200, 200);\n"
"}\n"
"#widget{	\n"
"    background-color: rgb(200, 200, 200);\n"
"}\n"
"QLabel{	\n"
"	border-style: ridge;\n"
"	border-width: 2px;\n"
"    border-color: rgb(170, 170, 170);\n"
"	text-align: left;\n"
"	font: bold 9pt \"Segoe UI\";\n"
"}\n"
"QLineEdit{		\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-style: ridge;\n"
"	border-width: 2px;\n"
"    border-color: rgb(170, 170, 170);\n"
"	font: bold 10pt \"Segoe UI\";\n"
"}\n"
"QLineEdit::focus{\n"
"    background-color: rgb(170, 255, 255);\n"
"    border-style: inset;\n"
"}")
        self.verticalLayout_77 = QVBoxLayout(self.pg_alt_dep)
        self.verticalLayout_77.setSpacing(0)
        self.verticalLayout_77.setObjectName(u"verticalLayout_77")
        self.verticalLayout_77.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.pg_alt_dep)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy3.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy3)
        self.scrollArea.setMinimumSize(QSize(0, 0))
        self.scrollArea.setMaximumSize(QSize(16777215, 16777215))
        self.scrollArea.setStyleSheet(u"")
        self.scrollArea.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 736, 481))
        sizePolicy3.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy3)
        self.scrollAreaWidgetContents.setStyleSheet(u"")
        self.verticalLayout_8 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.qw_dados_com = QWidget(self.scrollAreaWidgetContents)
        self.qw_dados_com.setObjectName(u"qw_dados_com")
        self.qw_dados_com.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.qw_dados_com.sizePolicy().hasHeightForWidth())
        self.qw_dados_com.setSizePolicy(sizePolicy3)
        self.qw_dados_com.setMinimumSize(QSize(0, 0))
        self.qw_dados_com.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setPointSize(11)
        font.setBold(False)
        self.qw_dados_com.setFont(font)
        self.qw_dados_com.setStyleSheet(u"")
        self.verticalLayout_12 = QVBoxLayout(self.qw_dados_com)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.alt_loc_lb_dados_user = QLabel(self.qw_dados_com)
        self.alt_loc_lb_dados_user.setObjectName(u"alt_loc_lb_dados_user")
        self.alt_loc_lb_dados_user.setMinimumSize(QSize(0, 50))

        self.verticalLayout_12.addWidget(self.alt_loc_lb_dados_user)

        self.label_19 = QLabel(self.qw_dados_com)
        self.label_19.setObjectName(u"label_19")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
        self.label_19.setSizePolicy(sizePolicy4)
        self.label_19.setMinimumSize(QSize(0, 30))
        self.label_19.setMaximumSize(QSize(16777215, 30))
        self.label_19.setStyleSheet(u"QLabel{	\n"
"	background-color: rgb(180, 180, 180);\n"
"    border-style: outset;\n"
"    border-width: 3px;\n"
"   /* border-radius: 5px;*/\n"
"    border-color: rgb(234, 234, 234);\n"
"    font: bold 12px;\n"
"\n"
"}")
        self.label_19.setAlignment(Qt.AlignCenter)
        self.label_19.setWordWrap(False)

        self.verticalLayout_12.addWidget(self.label_19)

        self.widget_11 = QWidget(self.qw_dados_com)
        self.widget_11.setObjectName(u"widget_11")
        sizePolicy1.setHeightForWidth(self.widget_11.sizePolicy().hasHeightForWidth())
        self.widget_11.setSizePolicy(sizePolicy1)
        self.widget_11.setMinimumSize(QSize(0, 150))
        self.widget_11.setMaximumSize(QSize(16777215, 150))
        self.widget_11.setStyleSheet(u"")
        self.gridLayout_4 = QGridLayout(self.widget_11)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_19 = QFrame(self.widget_11)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_19)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(10)
        self.gridLayout.setVerticalSpacing(16)
        self.gridLayout.setContentsMargins(15, 4, 10, 41)
        self.alt_loc_btn_exp_excel = QPushButton(self.frame_19)
        self.alt_loc_btn_exp_excel.setObjectName(u"alt_loc_btn_exp_excel")
        sizePolicy3.setHeightForWidth(self.alt_loc_btn_exp_excel.sizePolicy().hasHeightForWidth())
        self.alt_loc_btn_exp_excel.setSizePolicy(sizePolicy3)
        self.alt_loc_btn_exp_excel.setMinimumSize(QSize(50, 40))
        self.alt_loc_btn_exp_excel.setMaximumSize(QSize(50, 40))
        font1 = QFont()
        font1.setBold(True)
        font1.setItalic(False)
        self.alt_loc_btn_exp_excel.setFont(font1)
        self.alt_loc_btn_exp_excel.setCursor(QCursor(Qt.PointingHandCursor))
        self.alt_loc_btn_exp_excel.setLayoutDirection(Qt.RightToLeft)
        self.alt_loc_btn_exp_excel.setStyleSheet(u"#alt_loc_btn_exp_excel{	\n"
"	background-color: rgb(91, 182, 0);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 5px; \n"
"    border-color: rgb(105, 209, 0);\n"
"    font: bold 14px;		\n"
"	text-align: center;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#alt_loc_btn_exp_excel::hover {\n"
"    background-color: rgb(105, 209, 0);\n"
"    border-style: inset;\n"
"}\n"
"#alt_loc_btn_exp_excel::pressed {\n"
"    background-color: rgb(105, 209, 0);\n"
"    border-style: inset;\n"
"}\n"
"\n"
"")
        icon2 = QIcon()
        icon2.addFile(u":/assets.icons_alt_regras/export-excel.png", QSize(), QIcon.Normal, QIcon.Off)
        self.alt_loc_btn_exp_excel.setIcon(icon2)
        self.alt_loc_btn_exp_excel.setIconSize(QSize(30, 30))

        self.gridLayout.addWidget(self.alt_loc_btn_exp_excel, 2, 1, 1, 1)

        self.alt_loc_btn_imp_excel = QPushButton(self.frame_19)
        self.alt_loc_btn_imp_excel.setObjectName(u"alt_loc_btn_imp_excel")
        self.alt_loc_btn_imp_excel.setMinimumSize(QSize(50, 40))
        self.alt_loc_btn_imp_excel.setMaximumSize(QSize(50, 40))
        self.alt_loc_btn_imp_excel.setFont(font1)
        self.alt_loc_btn_imp_excel.setCursor(QCursor(Qt.PointingHandCursor))
        self.alt_loc_btn_imp_excel.setStyleSheet(u"#alt_loc_btn_imp_excel{	\n"
"	background-color: rgb(91, 182, 0);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 5px; \n"
"    border-color: rgb(105, 209, 0);\n"
"    font: bold 14px;		\n"
"	text-align: center;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#alt_loc_btn_imp_excel::hover {\n"
"    background-color: rgb(105, 209, 0);\n"
"    border-style: inset;\n"
"}\n"
"#alt_loc_btn_imp_excel::pressed {\n"
"    background-color: rgb(105, 209, 0);\n"
"    border-style: inset;\n"
"}\n"
"\n"
"")
        icon3 = QIcon()
        icon3.addFile(u":/assets.icons_alt_regras/ms-excel.png", QSize(), QIcon.Normal, QIcon.Off)
        self.alt_loc_btn_imp_excel.setIcon(icon3)
        self.alt_loc_btn_imp_excel.setIconSize(QSize(30, 30))

        self.gridLayout.addWidget(self.alt_loc_btn_imp_excel, 2, 0, 1, 1)

        self.alt_loc_btn_excluir_linha = QPushButton(self.frame_19)
        self.alt_loc_btn_excluir_linha.setObjectName(u"alt_loc_btn_excluir_linha")
        self.alt_loc_btn_excluir_linha.setMinimumSize(QSize(50, 40))
        self.alt_loc_btn_excluir_linha.setMaximumSize(QSize(50, 40))
        self.alt_loc_btn_excluir_linha.setFont(font1)
        self.alt_loc_btn_excluir_linha.setCursor(QCursor(Qt.PointingHandCursor))
        self.alt_loc_btn_excluir_linha.setStyleSheet(u"#alt_loc_btn_excluir_linha{	\n"
"	background-color: rgb(204, 0, 0);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 5px; \n"
"    border-color: rgb(227, 0, 0);\n"
"    font: bold 14px;		\n"
"	text-align: center;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#alt_loc_btn_excluir_linha::hover {\n"
"    background-color: rgb(165, 0, 0);\n"
"    border-style: inset;\n"
"}\n"
"#alt_loc_btn_excluir_linha::pressed {\n"
"    background-color: rgb(165, 0, 0);\n"
"    border-style: inset;\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/assets.icons_alt_regras/limpar-s\u00edmbolo-60.png", QSize(), QIcon.Normal, QIcon.Off)
        self.alt_loc_btn_excluir_linha.setIcon(icon4)
        self.alt_loc_btn_excluir_linha.setIconSize(QSize(30, 30))

        self.gridLayout.addWidget(self.alt_loc_btn_excluir_linha, 0, 0, 1, 1)

        self.alt_loc_btn_limpar_dados = QPushButton(self.frame_19)
        self.alt_loc_btn_limpar_dados.setObjectName(u"alt_loc_btn_limpar_dados")
        self.alt_loc_btn_limpar_dados.setMinimumSize(QSize(50, 40))
        self.alt_loc_btn_limpar_dados.setMaximumSize(QSize(50, 40))
        self.alt_loc_btn_limpar_dados.setFont(font1)
        self.alt_loc_btn_limpar_dados.setCursor(QCursor(Qt.PointingHandCursor))
        self.alt_loc_btn_limpar_dados.setStyleSheet(u"#alt_loc_btn_limpar_dados{	\n"
"	background-color: rgb(204, 0, 0);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 5px; \n"
"    border-color: rgb(227, 0, 0);\n"
"    font: bold 14px;		\n"
"	text-align: center;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#alt_loc_btn_limpar_dados::hover {\n"
"    background-color: rgb(165, 0, 0);\n"
"    border-style: inset;\n"
"}\n"
"#alt_loc_btn_limpar_dados::pressed {\n"
"    background-color: rgb(165, 0, 0);\n"
"    border-style: inset;\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/assets.icons_alt_regras/icons8-apagar-para-sempre-64.png", QSize(), QIcon.Normal, QIcon.Off)
        self.alt_loc_btn_limpar_dados.setIcon(icon5)
        self.alt_loc_btn_limpar_dados.setIconSize(QSize(30, 30))

        self.gridLayout.addWidget(self.alt_loc_btn_limpar_dados, 0, 1, 1, 1)


        self.gridLayout_4.addWidget(self.frame_19, 0, 2, 1, 1, Qt.AlignHCenter)

        self.widget = QWidget(self.widget_11)
        self.widget.setObjectName(u"widget")
        sizePolicy1.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy1)
        self.widget.setMinimumSize(QSize(0, 0))
        self.widget.setMaximumSize(QSize(16777215, 16777215))
        self.widget.setStyleSheet(u"")
        self.gridLayout_2 = QGridLayout(self.widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(4)
        self.gridLayout_2.setVerticalSpacing(2)
        self.gridLayout_2.setContentsMargins(2, 2, 2, 2)
        self.label_7 = QLabel(self.widget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(0, 30))
        self.label_7.setAlignment(Qt.AlignCenter)
        self.label_7.setWordWrap(False)

        self.gridLayout_2.addWidget(self.label_7, 0, 1, 1, 1)

        self.label_12 = QLabel(self.widget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(0, 30))
        self.label_12.setAlignment(Qt.AlignCenter)
        self.label_12.setWordWrap(False)

        self.gridLayout_2.addWidget(self.label_12, 2, 0, 1, 1)

        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(0, 30))
        self.label_4.setAlignment(Qt.AlignCenter)
        self.label_4.setWordWrap(False)

        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)

        self.alt_loc_txt_cen = QLineEdit(self.widget)
        self.alt_loc_txt_cen.setObjectName(u"alt_loc_txt_cen")
        self.alt_loc_txt_cen.setMinimumSize(QSize(80, 35))
        self.alt_loc_txt_cen.setMaximumSize(QSize(16777215, 35))
        self.alt_loc_txt_cen.setMaxLength(4)

        self.gridLayout_2.addWidget(self.alt_loc_txt_cen, 1, 1, 1, 1, Qt.AlignTop)

        self.alt_loc_txt_mat = QLineEdit(self.widget)
        self.alt_loc_txt_mat.setObjectName(u"alt_loc_txt_mat")
        self.alt_loc_txt_mat.setMinimumSize(QSize(80, 35))
        self.alt_loc_txt_mat.setMaximumSize(QSize(16777215, 35))
        self.alt_loc_txt_mat.setMaxLength(8)

        self.gridLayout_2.addWidget(self.alt_loc_txt_mat, 1, 0, 1, 1, Qt.AlignTop)

        self.label_10 = QLabel(self.widget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(0, 30))
        self.label_10.setAlignment(Qt.AlignCenter)
        self.label_10.setWordWrap(False)

        self.gridLayout_2.addWidget(self.label_10, 2, 1, 1, 1)

        self.alt_loc_txt_pos_local = QLineEdit(self.widget)
        self.alt_loc_txt_pos_local.setObjectName(u"alt_loc_txt_pos_local")
        self.alt_loc_txt_pos_local.setMinimumSize(QSize(80, 35))
        self.alt_loc_txt_pos_local.setMaximumSize(QSize(16777215, 35))
        self.alt_loc_txt_pos_local.setMaxLength(10)

        self.gridLayout_2.addWidget(self.alt_loc_txt_pos_local, 7, 1, 1, 1)

        self.alt_loc_txt_dep = QLineEdit(self.widget)
        self.alt_loc_txt_dep.setObjectName(u"alt_loc_txt_dep")
        self.alt_loc_txt_dep.setMinimumSize(QSize(80, 35))
        self.alt_loc_txt_dep.setMaximumSize(QSize(16777215, 35))
        self.alt_loc_txt_dep.setMaxLength(4)

        self.gridLayout_2.addWidget(self.alt_loc_txt_dep, 7, 0, 1, 1)


        self.gridLayout_4.addWidget(self.widget, 0, 0, 1, 1)

        self.frame_4 = QFrame(self.widget_11)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(170, 0))
        self.frame_4.setStyleSheet(u"")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_4)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setVerticalSpacing(10)
        self.gridLayout_6.setContentsMargins(0, 4, 0, 0)
        self.alt_loc_btn_alt_dados = QPushButton(self.frame_4)
        self.alt_loc_btn_alt_dados.setObjectName(u"alt_loc_btn_alt_dados")
        sizePolicy3.setHeightForWidth(self.alt_loc_btn_alt_dados.sizePolicy().hasHeightForWidth())
        self.alt_loc_btn_alt_dados.setSizePolicy(sizePolicy3)
        self.alt_loc_btn_alt_dados.setMinimumSize(QSize(80, 45))
        self.alt_loc_btn_alt_dados.setMaximumSize(QSize(45, 16777215))
        self.alt_loc_btn_alt_dados.setFont(font1)
        self.alt_loc_btn_alt_dados.setCursor(QCursor(Qt.PointingHandCursor))
        self.alt_loc_btn_alt_dados.setLayoutDirection(Qt.RightToLeft)
        self.alt_loc_btn_alt_dados.setStyleSheet(u"#alt_loc_btn_alt_dados{	\n"
"	background-color: rgb(0, 195, 0);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 5px; \n"
"    border-color: rgb(0, 158, 0);\n"
"    font: bold 14px;		\n"
"	text-align: center;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#alt_loc_btn_alt_dados::hover {\n"
"    background-color: rgb(0, 220, 0);\n"
"    border-style: inset;\n"
"}\n"
"#alt_loc_btn_alt_dados::pressed {\n"
"    background-color: rgb(0, 220, 0);\n"
"    border-style: inset;\n"
"}\n"
"\n"
"")
        icon6 = QIcon()
        icon6.addFile(u":/assets.icons_alt_regras/sap_color.png", QSize(), QIcon.Normal, QIcon.Off)
        self.alt_loc_btn_alt_dados.setIcon(icon6)
        self.alt_loc_btn_alt_dados.setIconSize(QSize(40, 40))

        self.gridLayout_6.addWidget(self.alt_loc_btn_alt_dados, 0, 1, 1, 1, Qt.AlignHCenter|Qt.AlignBottom)

        self.alt_loc_btn_incluir = QPushButton(self.frame_4)
        self.alt_loc_btn_incluir.setObjectName(u"alt_loc_btn_incluir")
        self.alt_loc_btn_incluir.setMinimumSize(QSize(80, 45))
        self.alt_loc_btn_incluir.setMaximumSize(QSize(45, 16777215))
        self.alt_loc_btn_incluir.setFont(font1)
        self.alt_loc_btn_incluir.setCursor(QCursor(Qt.PointingHandCursor))
        self.alt_loc_btn_incluir.setStyleSheet(u"#alt_loc_btn_incluir{	\n"
"	background-color: rgb(218, 145, 0);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 5px; \n"
"    border-color: rgb(235, 153, 0);\n"
"    font: bold 14px;		\n"
"	text-align: center;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#alt_loc_btn_incluir::hover {\n"
"    background-color: rgb(186, 121, 0);\n"
"    border-style: inset;\n"
"}\n"
"#alt_loc_btn_incluir::pressed {\n"
"    background-color: rgb(186, 121, 0);\n"
"    border-style: inset;\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u":/assets.icons_alt_regras/inserir-tabela-60.png", QSize(), QIcon.Normal, QIcon.Off)
        self.alt_loc_btn_incluir.setIcon(icon7)
        self.alt_loc_btn_incluir.setIconSize(QSize(30, 30))
        self.alt_loc_btn_incluir.setCheckable(True)

        self.gridLayout_6.addWidget(self.alt_loc_btn_incluir, 1, 1, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        self.alt_loc_chcb_alt_massiva = QCheckBox(self.frame_4)
        self.alt_loc_chcb_alt_massiva.setObjectName(u"alt_loc_chcb_alt_massiva")
        self.alt_loc_chcb_alt_massiva.setCursor(QCursor(Qt.PointingHandCursor))
        self.alt_loc_chcb_alt_massiva.setAutoFillBackground(False)
        self.alt_loc_chcb_alt_massiva.setStyleSheet(u"background-color: rgb(200, 200, 200);\n"
"font: bold 12px;")
        self.alt_loc_chcb_alt_massiva.setChecked(False)

        self.gridLayout_6.addWidget(self.alt_loc_chcb_alt_massiva, 2, 1, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)


        self.gridLayout_4.addWidget(self.frame_4, 0, 1, 1, 1)


        self.verticalLayout_12.addWidget(self.widget_11)

        self.label_20 = QLabel(self.qw_dados_com)
        self.label_20.setObjectName(u"label_20")
        sizePolicy4.setHeightForWidth(self.label_20.sizePolicy().hasHeightForWidth())
        self.label_20.setSizePolicy(sizePolicy4)
        self.label_20.setMinimumSize(QSize(0, 30))
        self.label_20.setMaximumSize(QSize(16777215, 30))
        self.label_20.setStyleSheet(u"QLabel{	\n"
"	background-color: rgb(180, 180, 180);\n"
"    border-style: outset;\n"
"    border-width: 3px;\n"
"   /* border-radius: 5px;*/\n"
"    border-color: rgb(234, 234, 234);\n"
"    font: bold 12px;\n"
"\n"
"}")
        self.label_20.setAlignment(Qt.AlignCenter)
        self.label_20.setWordWrap(False)

        self.verticalLayout_12.addWidget(self.label_20)


        self.verticalLayout_8.addWidget(self.qw_dados_com, 0, Qt.AlignTop)

        self.alt_loc_tb_alt_massa = QTableWidget(self.scrollAreaWidgetContents)
        if (self.alt_loc_tb_alt_massa.columnCount() < 7):
            self.alt_loc_tb_alt_massa.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.alt_loc_tb_alt_massa.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.alt_loc_tb_alt_massa.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.alt_loc_tb_alt_massa.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.alt_loc_tb_alt_massa.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.alt_loc_tb_alt_massa.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.alt_loc_tb_alt_massa.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.alt_loc_tb_alt_massa.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        if (self.alt_loc_tb_alt_massa.rowCount() < 1):
            self.alt_loc_tb_alt_massa.setRowCount(1)
        self.alt_loc_tb_alt_massa.setObjectName(u"alt_loc_tb_alt_massa")
        sizePolicy3.setHeightForWidth(self.alt_loc_tb_alt_massa.sizePolicy().hasHeightForWidth())
        self.alt_loc_tb_alt_massa.setSizePolicy(sizePolicy3)
        self.alt_loc_tb_alt_massa.setMinimumSize(QSize(0, 0))
        self.alt_loc_tb_alt_massa.setMaximumSize(QSize(16777215, 16777215))
        self.alt_loc_tb_alt_massa.viewport().setProperty("cursor", QCursor(Qt.ArrowCursor))
        self.alt_loc_tb_alt_massa.setStyleSheet(u"")
        self.alt_loc_tb_alt_massa.setFrameShape(QFrame.StyledPanel)
        self.alt_loc_tb_alt_massa.setFrameShadow(QFrame.Sunken)
        self.alt_loc_tb_alt_massa.setLineWidth(1)
        self.alt_loc_tb_alt_massa.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.alt_loc_tb_alt_massa.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.alt_loc_tb_alt_massa.setAutoScroll(True)
        self.alt_loc_tb_alt_massa.setProperty("showDropIndicator", True)
        self.alt_loc_tb_alt_massa.setDragEnabled(False)
        self.alt_loc_tb_alt_massa.setAlternatingRowColors(True)
        self.alt_loc_tb_alt_massa.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.alt_loc_tb_alt_massa.setTextElideMode(Qt.ElideRight)
        self.alt_loc_tb_alt_massa.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.alt_loc_tb_alt_massa.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.alt_loc_tb_alt_massa.setShowGrid(True)
        self.alt_loc_tb_alt_massa.setGridStyle(Qt.SolidLine)
        self.alt_loc_tb_alt_massa.setSortingEnabled(False)
        self.alt_loc_tb_alt_massa.setWordWrap(True)
        self.alt_loc_tb_alt_massa.setCornerButtonEnabled(True)
        self.alt_loc_tb_alt_massa.setRowCount(1)
        self.alt_loc_tb_alt_massa.setColumnCount(7)
        self.alt_loc_tb_alt_massa.horizontalHeader().setVisible(True)
        self.alt_loc_tb_alt_massa.horizontalHeader().setCascadingSectionResizes(False)
        self.alt_loc_tb_alt_massa.horizontalHeader().setMinimumSectionSize(42)
        self.alt_loc_tb_alt_massa.horizontalHeader().setDefaultSectionSize(120)
        self.alt_loc_tb_alt_massa.horizontalHeader().setHighlightSections(True)
        self.alt_loc_tb_alt_massa.horizontalHeader().setProperty("showSortIndicator", False)
        self.alt_loc_tb_alt_massa.horizontalHeader().setStretchLastSection(True)
        self.alt_loc_tb_alt_massa.verticalHeader().setCascadingSectionResizes(True)
        self.alt_loc_tb_alt_massa.verticalHeader().setDefaultSectionSize(30)
        self.alt_loc_tb_alt_massa.verticalHeader().setHighlightSections(True)
        self.alt_loc_tb_alt_massa.verticalHeader().setProperty("showSortIndicator", False)
        self.alt_loc_tb_alt_massa.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_8.addWidget(self.alt_loc_tb_alt_massa)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_77.addWidget(self.scrollArea)

        self.pgs_principal.addWidget(self.pg_alt_dep)
        self.pg_cont_entrada_almox = QWidget()
        self.pg_cont_entrada_almox.setObjectName(u"pg_cont_entrada_almox")
        self.pg_cont_entrada_almox.setStyleSheet(u"QWidget{	\n"
"	border-style: ridge;\n"
"    border-width: 2px;\n"
"    border-color: rgb(234, 234, 234);\n"
"	background-color: rgb(225, 225, 225);\n"
"}\n"
"QComboBox{	\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-style: ridge;\n"
"	border-width: 3px;\n"
"    border-color: rgb(150, 150, 150);    \n"
"	font: bold 10pt \"Segoe UI\";\n"
"}\n"
"QComboBox QListView{	\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"QComboBox::focus{\n"
"    background-color: rgb(170, 255, 255);\n"
"    border-style: inset;\n"
"}\n"
"QLabel{	\n"
"	border-style: ridge;\n"
"	border-width: 2px;\n"
"    border-color: rgb(170, 170, 170);\n"
"	text-align: left;\n"
"	font: bold 9pt \"Segoe UI\";\n"
"}\n"
"QLineEdit{		\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-style: ridge;\n"
"	border-width: 2px;\n"
"    border-color: rgb(170, 170, 170);\n"
"	font: bold 10pt \"Segoe UI\";\n"
"}\n"
"QLineEdit::focus{\n"
"    background-color: rgb(170, 255, 255);\n"
"    border-style: inset;\n"
"}")
        self.verticalLayout_5 = QVBoxLayout(self.pg_cont_entrada_almox)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_4 = QScrollArea(self.pg_cont_entrada_almox)
        self.scrollArea_4.setObjectName(u"scrollArea_4")
        sizePolicy3.setHeightForWidth(self.scrollArea_4.sizePolicy().hasHeightForWidth())
        self.scrollArea_4.setSizePolicy(sizePolicy3)
        self.scrollArea_4.setMinimumSize(QSize(0, 0))
        self.scrollArea_4.setMaximumSize(QSize(16777215, 16777215))
        self.scrollArea_4.setStyleSheet(u"")
        self.scrollArea_4.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollArea_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 738, 483))
        sizePolicy3.setHeightForWidth(self.scrollAreaWidgetContents_4.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents_4.setSizePolicy(sizePolicy3)
        self.scrollAreaWidgetContents_4.setStyleSheet(u"")
        self.verticalLayout_11 = QVBoxLayout(self.scrollAreaWidgetContents_4)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(self.scrollAreaWidgetContents_4)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy3)
        self.widget_2.setMinimumSize(QSize(0, 0))
        self.widget_2.setMaximumSize(QSize(16777215, 16777215))
        self.widget_2.setFont(font)
        self.widget_2.setStyleSheet(u"")
        self.verticalLayout_15 = QVBoxLayout(self.widget_2)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.cont_ent_almox_lb_dec_cen_mes = QLabel(self.widget_2)
        self.cont_ent_almox_lb_dec_cen_mes.setObjectName(u"cont_ent_almox_lb_dec_cen_mes")
        sizePolicy4.setHeightForWidth(self.cont_ent_almox_lb_dec_cen_mes.sizePolicy().hasHeightForWidth())
        self.cont_ent_almox_lb_dec_cen_mes.setSizePolicy(sizePolicy4)
        self.cont_ent_almox_lb_dec_cen_mes.setMinimumSize(QSize(0, 30))
        self.cont_ent_almox_lb_dec_cen_mes.setMaximumSize(QSize(16777215, 30))
        self.cont_ent_almox_lb_dec_cen_mes.setStyleSheet(u"QLabel{	\n"
"	background-color: rgb(180, 180, 180);\n"
"    border-style: outset;\n"
"    border-width: 3px;\n"
"   /* border-radius: 5px;*/\n"
"    border-color: rgb(234, 234, 234);\n"
"    font: bold 12px;\n"
"\n"
"}")
        self.cont_ent_almox_lb_dec_cen_mes.setAlignment(Qt.AlignCenter)
        self.cont_ent_almox_lb_dec_cen_mes.setWordWrap(False)

        self.verticalLayout_15.addWidget(self.cont_ent_almox_lb_dec_cen_mes)

        self.widget_16 = QWidget(self.widget_2)
        self.widget_16.setObjectName(u"widget_16")
        sizePolicy1.setHeightForWidth(self.widget_16.sizePolicy().hasHeightForWidth())
        self.widget_16.setSizePolicy(sizePolicy1)
        self.widget_16.setMinimumSize(QSize(0, 0))
        self.widget_16.setMaximumSize(QSize(16777215, 150))
        self.widget_16.setStyleSheet(u"")
        self.gridLayout_12 = QGridLayout(self.widget_16)
        self.gridLayout_12.setSpacing(0)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setContentsMargins(0, 0, 0, 0)
        self.widget_17 = QWidget(self.widget_16)
        self.widget_17.setObjectName(u"widget_17")
        sizePolicy1.setHeightForWidth(self.widget_17.sizePolicy().hasHeightForWidth())
        self.widget_17.setSizePolicy(sizePolicy1)
        self.widget_17.setMinimumSize(QSize(0, 0))
        self.widget_17.setMaximumSize(QSize(16777215, 149))
        self.widget_17.setStyleSheet(u"")
        self.gridLayout_13 = QGridLayout(self.widget_17)
        self.gridLayout_13.setSpacing(0)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_13.setContentsMargins(0, 0, 0, 0)
        self.frame_13 = QFrame(self.widget_17)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setStyleSheet(u"")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.gridLayout_15 = QGridLayout(self.frame_13)
        self.gridLayout_15.setSpacing(0)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.gridLayout_15.setContentsMargins(0, 0, 0, 2)
        self.label_36 = QLabel(self.frame_13)
        self.label_36.setObjectName(u"label_36")
        sizePolicy4.setHeightForWidth(self.label_36.sizePolicy().hasHeightForWidth())
        self.label_36.setSizePolicy(sizePolicy4)
        self.label_36.setMinimumSize(QSize(85, 30))
        self.label_36.setMaximumSize(QSize(85, 30))
        self.label_36.setStyleSheet(u"")
        self.label_36.setAlignment(Qt.AlignCenter)
        self.label_36.setWordWrap(False)

        self.gridLayout_15.addWidget(self.label_36, 5, 0, 1, 2)

        self.nao_atend_cmb_acao_plan_2 = QComboBox(self.frame_13)
        self.nao_atend_cmb_acao_plan_2.addItem("")
        self.nao_atend_cmb_acao_plan_2.addItem("")
        self.nao_atend_cmb_acao_plan_2.addItem("")
        self.nao_atend_cmb_acao_plan_2.setObjectName(u"nao_atend_cmb_acao_plan_2")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.nao_atend_cmb_acao_plan_2.sizePolicy().hasHeightForWidth())
        self.nao_atend_cmb_acao_plan_2.setSizePolicy(sizePolicy5)
        self.nao_atend_cmb_acao_plan_2.setMinimumSize(QSize(86, 30))
        self.nao_atend_cmb_acao_plan_2.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_15.addWidget(self.nao_atend_cmb_acao_plan_2, 3, 2, 1, 1)

        self.label_37 = QLabel(self.frame_13)
        self.label_37.setObjectName(u"label_37")
        sizePolicy4.setHeightForWidth(self.label_37.sizePolicy().hasHeightForWidth())
        self.label_37.setSizePolicy(sizePolicy4)
        self.label_37.setMinimumSize(QSize(140, 30))
        self.label_37.setMaximumSize(QSize(16777215, 30))
        self.label_37.setStyleSheet(u"")
        self.label_37.setAlignment(Qt.AlignCenter)
        self.label_37.setWordWrap(False)

        self.gridLayout_15.addWidget(self.label_37, 0, 0, 1, 5)

        self.label_38 = QLabel(self.frame_13)
        self.label_38.setObjectName(u"label_38")
        sizePolicy4.setHeightForWidth(self.label_38.sizePolicy().hasHeightForWidth())
        self.label_38.setSizePolicy(sizePolicy4)
        self.label_38.setMinimumSize(QSize(85, 30))
        self.label_38.setMaximumSize(QSize(85, 30))
        self.label_38.setStyleSheet(u"")
        self.label_38.setAlignment(Qt.AlignCenter)
        self.label_38.setWordWrap(False)

        self.gridLayout_15.addWidget(self.label_38, 3, 0, 1, 2)

        self.frame_14 = QFrame(self.frame_13)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setStyleSheet(u"border: 0px;")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)

        self.gridLayout_15.addWidget(self.frame_14, 5, 3, 3, 1)

        self.label_39 = QLabel(self.frame_13)
        self.label_39.setObjectName(u"label_39")
        sizePolicy4.setHeightForWidth(self.label_39.sizePolicy().hasHeightForWidth())
        self.label_39.setSizePolicy(sizePolicy4)
        self.label_39.setMinimumSize(QSize(85, 30))
        self.label_39.setMaximumSize(QSize(85, 30))
        self.label_39.setStyleSheet(u"")
        self.label_39.setAlignment(Qt.AlignCenter)
        self.label_39.setWordWrap(False)

        self.gridLayout_15.addWidget(self.label_39, 1, 0, 1, 2)

        self.nao_atend_cmb_ano_mes_2 = QComboBox(self.frame_13)
        self.nao_atend_cmb_ano_mes_2.addItem("")
        self.nao_atend_cmb_ano_mes_2.setObjectName(u"nao_atend_cmb_ano_mes_2")
        sizePolicy5.setHeightForWidth(self.nao_atend_cmb_ano_mes_2.sizePolicy().hasHeightForWidth())
        self.nao_atend_cmb_ano_mes_2.setSizePolicy(sizePolicy5)
        self.nao_atend_cmb_ano_mes_2.setMinimumSize(QSize(86, 30))
        self.nao_atend_cmb_ano_mes_2.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_15.addWidget(self.nao_atend_cmb_ano_mes_2, 1, 2, 1, 1)

        self.nao_atend_txt_material_2 = QLineEdit(self.frame_13)
        self.nao_atend_txt_material_2.setObjectName(u"nao_atend_txt_material_2")
        self.nao_atend_txt_material_2.setMinimumSize(QSize(86, 30))
        self.nao_atend_txt_material_2.setMaximumSize(QSize(16777215, 30))
        self.nao_atend_txt_material_2.setMaxLength(8)

        self.gridLayout_15.addWidget(self.nao_atend_txt_material_2, 5, 2, 1, 1)

        self.label_40 = QLabel(self.frame_13)
        self.label_40.setObjectName(u"label_40")
        sizePolicy4.setHeightForWidth(self.label_40.sizePolicy().hasHeightForWidth())
        self.label_40.setSizePolicy(sizePolicy4)
        self.label_40.setMinimumSize(QSize(85, 30))
        self.label_40.setMaximumSize(QSize(85, 30))
        self.label_40.setStyleSheet(u"")
        self.label_40.setAlignment(Qt.AlignCenter)
        self.label_40.setWordWrap(False)

        self.gridLayout_15.addWidget(self.label_40, 4, 0, 1, 1)

        self.nao_atend_cmb_cod_sit_2 = QComboBox(self.frame_13)
        self.nao_atend_cmb_cod_sit_2.addItem("")
        self.nao_atend_cmb_cod_sit_2.addItem("")
        self.nao_atend_cmb_cod_sit_2.addItem("")
        self.nao_atend_cmb_cod_sit_2.addItem("")
        self.nao_atend_cmb_cod_sit_2.addItem("")
        self.nao_atend_cmb_cod_sit_2.addItem("")
        self.nao_atend_cmb_cod_sit_2.addItem("")
        self.nao_atend_cmb_cod_sit_2.addItem("")
        self.nao_atend_cmb_cod_sit_2.addItem("")
        self.nao_atend_cmb_cod_sit_2.addItem("")
        self.nao_atend_cmb_cod_sit_2.addItem("")
        self.nao_atend_cmb_cod_sit_2.addItem("")
        self.nao_atend_cmb_cod_sit_2.addItem("")
        self.nao_atend_cmb_cod_sit_2.addItem("")
        self.nao_atend_cmb_cod_sit_2.addItem("")
        self.nao_atend_cmb_cod_sit_2.addItem("")
        self.nao_atend_cmb_cod_sit_2.addItem("")
        self.nao_atend_cmb_cod_sit_2.addItem("")
        self.nao_atend_cmb_cod_sit_2.addItem("")
        self.nao_atend_cmb_cod_sit_2.setObjectName(u"nao_atend_cmb_cod_sit_2")
        self.nao_atend_cmb_cod_sit_2.setMinimumSize(QSize(0, 30))
        self.nao_atend_cmb_cod_sit_2.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_15.addWidget(self.nao_atend_cmb_cod_sit_2, 4, 1, 1, 2)


        self.gridLayout_13.addWidget(self.frame_13, 1, 4, 1, 1)

        self.frame_15 = QFrame(self.widget_17)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setStyleSheet(u"")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.gridLayout_16 = QGridLayout(self.frame_15)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.gridLayout_16.setHorizontalSpacing(20)
        self.gridLayout_16.setVerticalSpacing(2)
        self.gridLayout_16.setContentsMargins(20, 0, 20, 0)
        self.cont_ent_almox_btn_alt_regist = QPushButton(self.frame_15)
        self.cont_ent_almox_btn_alt_regist.setObjectName(u"cont_ent_almox_btn_alt_regist")
        sizePolicy3.setHeightForWidth(self.cont_ent_almox_btn_alt_regist.sizePolicy().hasHeightForWidth())
        self.cont_ent_almox_btn_alt_regist.setSizePolicy(sizePolicy3)
        self.cont_ent_almox_btn_alt_regist.setMinimumSize(QSize(60, 40))
        self.cont_ent_almox_btn_alt_regist.setMaximumSize(QSize(60, 40))
        self.cont_ent_almox_btn_alt_regist.setFont(font1)
        self.cont_ent_almox_btn_alt_regist.setCursor(QCursor(Qt.PointingHandCursor))
        self.cont_ent_almox_btn_alt_regist.setLayoutDirection(Qt.RightToLeft)
        self.cont_ent_almox_btn_alt_regist.setStyleSheet(u"#nao_atend_btn_alt_regist{	\n"
"	background-color: rgb(218, 145, 0);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 5px; \n"
"    border-color: rgb(235, 153, 0);\n"
"    font: bold 14px;		\n"
"	text-align: center;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#nao_atend_btn_alt_regist::hover {\n"
"    background-color: rgb(186, 121, 0);\n"
"    border-style: inset;\n"
"}\n"
"#nao_atend_btn_alt_regist::pressed {\n"
"    background-color: rgb(186, 121, 0);\n"
"    border-style: inset;\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u":/assets.icons_alt_regras/editar-60.png", QSize(), QIcon.Normal, QIcon.Off)
        self.cont_ent_almox_btn_alt_regist.setIcon(icon8)
        self.cont_ent_almox_btn_alt_regist.setIconSize(QSize(30, 30))

        self.gridLayout_16.addWidget(self.cont_ent_almox_btn_alt_regist, 2, 1, 1, 1)

        self.cont_ent_almox_btn_inc_regist = QPushButton(self.frame_15)
        self.cont_ent_almox_btn_inc_regist.setObjectName(u"cont_ent_almox_btn_inc_regist")
        sizePolicy3.setHeightForWidth(self.cont_ent_almox_btn_inc_regist.sizePolicy().hasHeightForWidth())
        self.cont_ent_almox_btn_inc_regist.setSizePolicy(sizePolicy3)
        self.cont_ent_almox_btn_inc_regist.setMinimumSize(QSize(60, 40))
        self.cont_ent_almox_btn_inc_regist.setMaximumSize(QSize(60, 40))
        self.cont_ent_almox_btn_inc_regist.setFont(font1)
        self.cont_ent_almox_btn_inc_regist.setCursor(QCursor(Qt.PointingHandCursor))
        self.cont_ent_almox_btn_inc_regist.setLayoutDirection(Qt.RightToLeft)
        self.cont_ent_almox_btn_inc_regist.setStyleSheet(u"#nao_atend_btn_inc_regist{	\n"
"	background-color: rgb(0, 195, 0);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 5px; \n"
"    border-color: rgb(0, 212, 0);\n"
"    font: bold 14px;		\n"
"	text-align: center;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#nao_atend_btn_inc_regist::hover {\n"
"    background-color: rgb(0, 144, 0);\n"
"    border-style: inset;\n"
"}\n"
"#nao_atend_btn_inc_regist::pressed {\n"
"    background-color:  rgb(0, 144, 0);\n"
"    border-style: inset;\n"
"}")
        icon9 = QIcon()
        icon9.addFile(u":/assets.icons_alt_regras/icons8-macos-maximize-60.png", QSize(), QIcon.Normal, QIcon.Off)
        self.cont_ent_almox_btn_inc_regist.setIcon(icon9)
        self.cont_ent_almox_btn_inc_regist.setIconSize(QSize(30, 30))

        self.gridLayout_16.addWidget(self.cont_ent_almox_btn_inc_regist, 0, 1, 1, 1)

        self.cont_ent_almox_btn_pesquisar = QPushButton(self.frame_15)
        self.cont_ent_almox_btn_pesquisar.setObjectName(u"cont_ent_almox_btn_pesquisar")
        sizePolicy3.setHeightForWidth(self.cont_ent_almox_btn_pesquisar.sizePolicy().hasHeightForWidth())
        self.cont_ent_almox_btn_pesquisar.setSizePolicy(sizePolicy3)
        self.cont_ent_almox_btn_pesquisar.setMinimumSize(QSize(60, 40))
        self.cont_ent_almox_btn_pesquisar.setMaximumSize(QSize(60, 40))
        self.cont_ent_almox_btn_pesquisar.setFont(font1)
        self.cont_ent_almox_btn_pesquisar.setCursor(QCursor(Qt.PointingHandCursor))
        self.cont_ent_almox_btn_pesquisar.setLayoutDirection(Qt.RightToLeft)
        self.cont_ent_almox_btn_pesquisar.setStyleSheet(u"#nao_atend_btn_pesquisar{	\n"
"	background-color: rgb(170, 255, 255);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 5px; \n"
"    border-color: rgb(180, 255, 255);\n"
"    font: bold 14px;		\n"
"	text-align: center;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#nao_atend_btn_pesquisar::hover {\n"
"    background-color: rgb(150, 255, 255);\n"
"    border-style: inset;\n"
"}\n"
"#nao_atend_btn_pesquisar::pressed {\n"
"    background-color: rgb(150, 255, 255);\n"
"    border-style: inset;\n"
"}")
        icon10 = QIcon()
        icon10.addFile(u":/assets.icons_alt_regras/pesquisar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.cont_ent_almox_btn_pesquisar.setIcon(icon10)
        self.cont_ent_almox_btn_pesquisar.setIconSize(QSize(30, 30))

        self.gridLayout_16.addWidget(self.cont_ent_almox_btn_pesquisar, 0, 2, 1, 1)


        self.gridLayout_13.addWidget(self.frame_15, 0, 5, 3, 1, Qt.AlignRight)

        self.frame_12 = QFrame(self.widget_17)
        self.frame_12.setObjectName(u"frame_12")
        sizePolicy2.setHeightForWidth(self.frame_12.sizePolicy().hasHeightForWidth())
        self.frame_12.setSizePolicy(sizePolicy2)
        self.frame_12.setMinimumSize(QSize(200, 0))
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.gridLayout_14 = QGridLayout(self.frame_12)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.gridLayout_14.setHorizontalSpacing(2)
        self.gridLayout_14.setVerticalSpacing(0)
        self.gridLayout_14.setContentsMargins(4, 0, 2, 0)
        self.nao_atend_lb_itens_na_2 = QLabel(self.frame_12)
        self.nao_atend_lb_itens_na_2.setObjectName(u"nao_atend_lb_itens_na_2")
        self.nao_atend_lb_itens_na_2.setMinimumSize(QSize(80, 30))
        self.nao_atend_lb_itens_na_2.setMaximumSize(QSize(16777215, 30))
        self.nao_atend_lb_itens_na_2.setStyleSheet(u"background-color: rgb(255, 255, 255);color: rgb(227, 0, 0);")
        self.nao_atend_lb_itens_na_2.setAlignment(Qt.AlignCenter)
        self.nao_atend_lb_itens_na_2.setWordWrap(False)

        self.gridLayout_14.addWidget(self.nao_atend_lb_itens_na_2, 3, 0, 1, 1)

        self.nao_atend_lb_total_ocor_2 = QLabel(self.frame_12)
        self.nao_atend_lb_total_ocor_2.setObjectName(u"nao_atend_lb_total_ocor_2")
        self.nao_atend_lb_total_ocor_2.setMinimumSize(QSize(80, 30))
        self.nao_atend_lb_total_ocor_2.setMaximumSize(QSize(16777215, 30))
        self.nao_atend_lb_total_ocor_2.setStyleSheet(u"background-color: rgb(255, 255, 255);color: rgb(227, 0, 0);")
        self.nao_atend_lb_total_ocor_2.setAlignment(Qt.AlignCenter)
        self.nao_atend_lb_total_ocor_2.setWordWrap(False)

        self.gridLayout_14.addWidget(self.nao_atend_lb_total_ocor_2, 1, 0, 1, 1)

        self.label_34 = QLabel(self.frame_12)
        self.label_34.setObjectName(u"label_34")
        sizePolicy4.setHeightForWidth(self.label_34.sizePolicy().hasHeightForWidth())
        self.label_34.setSizePolicy(sizePolicy4)
        self.label_34.setMinimumSize(QSize(0, 30))
        self.label_34.setMaximumSize(QSize(16777215, 30))
        self.label_34.setStyleSheet(u"")
        self.label_34.setAlignment(Qt.AlignCenter)
        self.label_34.setWordWrap(False)

        self.gridLayout_14.addWidget(self.label_34, 2, 0, 1, 1)

        self.label_35 = QLabel(self.frame_12)
        self.label_35.setObjectName(u"label_35")
        sizePolicy6 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.label_35.sizePolicy().hasHeightForWidth())
        self.label_35.setSizePolicy(sizePolicy6)
        self.label_35.setMinimumSize(QSize(0, 30))
        self.label_35.setMaximumSize(QSize(16777215, 30))
        self.label_35.setStyleSheet(u"")
        self.label_35.setAlignment(Qt.AlignCenter)
        self.label_35.setWordWrap(False)

        self.gridLayout_14.addWidget(self.label_35, 0, 0, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_14.addItem(self.verticalSpacer_5, 4, 0, 1, 1)


        self.gridLayout_13.addWidget(self.frame_12, 0, 2, 3, 1, Qt.AlignLeft)


        self.gridLayout_12.addWidget(self.widget_17, 0, 0, 1, 1, Qt.AlignTop)


        self.verticalLayout_15.addWidget(self.widget_16, 0, Qt.AlignTop)

        self.label_41 = QLabel(self.widget_2)
        self.label_41.setObjectName(u"label_41")
        sizePolicy4.setHeightForWidth(self.label_41.sizePolicy().hasHeightForWidth())
        self.label_41.setSizePolicy(sizePolicy4)
        self.label_41.setMinimumSize(QSize(0, 30))
        self.label_41.setMaximumSize(QSize(16777215, 30))
        self.label_41.setStyleSheet(u"QLabel{	\n"
"	background-color: rgb(180, 180, 180);\n"
"    border-style: outset;\n"
"    border-width: 3px;\n"
"   /* border-radius: 5px;*/\n"
"    border-color: rgb(234, 234, 234);\n"
"    font: bold 12px;\n"
"\n"
"}")
        self.label_41.setAlignment(Qt.AlignCenter)
        self.label_41.setWordWrap(False)

        self.verticalLayout_15.addWidget(self.label_41)


        self.verticalLayout_11.addWidget(self.widget_2, 0, Qt.AlignTop)

        self.cont_ent_almox_tb_entradas = QTableWidget(self.scrollAreaWidgetContents_4)
        if (self.cont_ent_almox_tb_entradas.columnCount() < 33):
            self.cont_ent_almox_tb_entradas.setColumnCount(33)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.cont_ent_almox_tb_entradas.setHorizontalHeaderItem(0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.cont_ent_almox_tb_entradas.setHorizontalHeaderItem(1, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.cont_ent_almox_tb_entradas.setHorizontalHeaderItem(2, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.cont_ent_almox_tb_entradas.setHorizontalHeaderItem(3, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.cont_ent_almox_tb_entradas.setHorizontalHeaderItem(4, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.cont_ent_almox_tb_entradas.setHorizontalHeaderItem(5, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.cont_ent_almox_tb_entradas.setHorizontalHeaderItem(6, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.cont_ent_almox_tb_entradas.setHorizontalHeaderItem(7, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.cont_ent_almox_tb_entradas.setHorizontalHeaderItem(8, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.cont_ent_almox_tb_entradas.setHorizontalHeaderItem(9, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.cont_ent_almox_tb_entradas.setHorizontalHeaderItem(10, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.cont_ent_almox_tb_entradas.setHorizontalHeaderItem(11, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.cont_ent_almox_tb_entradas.setHorizontalHeaderItem(12, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.cont_ent_almox_tb_entradas.setHorizontalHeaderItem(13, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.cont_ent_almox_tb_entradas.setHorizontalHeaderItem(14, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.cont_ent_almox_tb_entradas.setHorizontalHeaderItem(15, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.cont_ent_almox_tb_entradas.setHorizontalHeaderItem(16, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.cont_ent_almox_tb_entradas.setHorizontalHeaderItem(17, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.cont_ent_almox_tb_entradas.setHorizontalHeaderItem(18, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.cont_ent_almox_tb_entradas.setHorizontalHeaderItem(19, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.cont_ent_almox_tb_entradas.setHorizontalHeaderItem(20, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.cont_ent_almox_tb_entradas.setHorizontalHeaderItem(21, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.cont_ent_almox_tb_entradas.setHorizontalHeaderItem(22, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.cont_ent_almox_tb_entradas.setHorizontalHeaderItem(23, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.cont_ent_almox_tb_entradas.setHorizontalHeaderItem(24, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.cont_ent_almox_tb_entradas.setHorizontalHeaderItem(25, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.cont_ent_almox_tb_entradas.setHorizontalHeaderItem(26, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.cont_ent_almox_tb_entradas.setHorizontalHeaderItem(27, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.cont_ent_almox_tb_entradas.setHorizontalHeaderItem(28, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.cont_ent_almox_tb_entradas.setHorizontalHeaderItem(29, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.cont_ent_almox_tb_entradas.setHorizontalHeaderItem(30, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.cont_ent_almox_tb_entradas.setHorizontalHeaderItem(31, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.cont_ent_almox_tb_entradas.setHorizontalHeaderItem(32, __qtablewidgetitem39)
        self.cont_ent_almox_tb_entradas.setObjectName(u"cont_ent_almox_tb_entradas")
        sizePolicy3.setHeightForWidth(self.cont_ent_almox_tb_entradas.sizePolicy().hasHeightForWidth())
        self.cont_ent_almox_tb_entradas.setSizePolicy(sizePolicy3)
        self.cont_ent_almox_tb_entradas.setMinimumSize(QSize(0, 0))
        self.cont_ent_almox_tb_entradas.setMaximumSize(QSize(16777215, 16777215))
        self.cont_ent_almox_tb_entradas.setStyleSheet(u"")
        self.cont_ent_almox_tb_entradas.setFrameShape(QFrame.StyledPanel)
        self.cont_ent_almox_tb_entradas.setFrameShadow(QFrame.Sunken)
        self.cont_ent_almox_tb_entradas.setLineWidth(1)
        self.cont_ent_almox_tb_entradas.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.cont_ent_almox_tb_entradas.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.cont_ent_almox_tb_entradas.setAutoScroll(True)
        self.cont_ent_almox_tb_entradas.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.cont_ent_almox_tb_entradas.setProperty("showDropIndicator", True)
        self.cont_ent_almox_tb_entradas.setDragEnabled(False)
        self.cont_ent_almox_tb_entradas.setAlternatingRowColors(True)
        self.cont_ent_almox_tb_entradas.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.cont_ent_almox_tb_entradas.setTextElideMode(Qt.ElideRight)
        self.cont_ent_almox_tb_entradas.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.cont_ent_almox_tb_entradas.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.cont_ent_almox_tb_entradas.setShowGrid(True)
        self.cont_ent_almox_tb_entradas.setGridStyle(Qt.SolidLine)
        self.cont_ent_almox_tb_entradas.setSortingEnabled(False)
        self.cont_ent_almox_tb_entradas.setWordWrap(True)
        self.cont_ent_almox_tb_entradas.setCornerButtonEnabled(True)
        self.cont_ent_almox_tb_entradas.setRowCount(0)
        self.cont_ent_almox_tb_entradas.setColumnCount(33)
        self.cont_ent_almox_tb_entradas.horizontalHeader().setVisible(True)
        self.cont_ent_almox_tb_entradas.horizontalHeader().setCascadingSectionResizes(False)
        self.cont_ent_almox_tb_entradas.horizontalHeader().setMinimumSectionSize(42)
        self.cont_ent_almox_tb_entradas.horizontalHeader().setDefaultSectionSize(120)
        self.cont_ent_almox_tb_entradas.horizontalHeader().setHighlightSections(True)
        self.cont_ent_almox_tb_entradas.horizontalHeader().setProperty("showSortIndicator", False)
        self.cont_ent_almox_tb_entradas.horizontalHeader().setStretchLastSection(True)
        self.cont_ent_almox_tb_entradas.verticalHeader().setCascadingSectionResizes(True)
        self.cont_ent_almox_tb_entradas.verticalHeader().setDefaultSectionSize(30)
        self.cont_ent_almox_tb_entradas.verticalHeader().setHighlightSections(True)
        self.cont_ent_almox_tb_entradas.verticalHeader().setProperty("showSortIndicator", False)
        self.cont_ent_almox_tb_entradas.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_11.addWidget(self.cont_ent_almox_tb_entradas)

        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_4)

        self.verticalLayout_5.addWidget(self.scrollArea_4)

        self.pgs_principal.addWidget(self.pg_cont_entrada_almox)
        self.pg_nao_atendidos = QWidget()
        self.pg_nao_atendidos.setObjectName(u"pg_nao_atendidos")
        self.pg_nao_atendidos.setStyleSheet(u"QWidget{	\n"
"	border-style: ridge;\n"
"    border-width: 2px;\n"
"    border-color: rgb(234, 234, 234);\n"
"	background-color: rgb(225, 225, 225);\n"
"}\n"
"QComboBox{	\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-style: ridge;\n"
"	border-width: 3px;\n"
"    border-color: rgb(150, 150, 150);    \n"
"	font: bold 10pt \"Segoe UI\";\n"
"}\n"
"QComboBox QListView{	\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"QComboBox::focus{\n"
"    background-color: rgb(170, 255, 255);\n"
"    border-style: inset;\n"
"}\n"
"QLabel{	\n"
"	border-style: ridge;\n"
"	border-width: 2px;\n"
"    border-color: rgb(170, 170, 170);\n"
"	text-align: left;\n"
"	font: bold 9pt \"Segoe UI\";\n"
"}\n"
"QLineEdit{		\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-style: ridge;\n"
"	border-width: 2px;\n"
"    border-color: rgb(170, 170, 170);\n"
"	font: bold 10pt \"Segoe UI\";\n"
"}\n"
"QLineEdit::focus{\n"
"    background-color: rgb(170, 255, 255);\n"
"    border-style: inset;\n"
"}")
        self.horizontalLayout_4 = QHBoxLayout(self.pg_nao_atendidos)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_3 = QScrollArea(self.pg_nao_atendidos)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        sizePolicy3.setHeightForWidth(self.scrollArea_3.sizePolicy().hasHeightForWidth())
        self.scrollArea_3.setSizePolicy(sizePolicy3)
        self.scrollArea_3.setMinimumSize(QSize(0, 0))
        self.scrollArea_3.setMaximumSize(QSize(16777215, 16777215))
        self.scrollArea_3.setStyleSheet(u"")
        self.scrollArea_3.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 898, 466))
        sizePolicy3.setHeightForWidth(self.scrollAreaWidgetContents_3.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents_3.setSizePolicy(sizePolicy3)
        self.scrollAreaWidgetContents_3.setStyleSheet(u"")
        self.verticalLayout_10 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.qw_dados_com_3 = QWidget(self.scrollAreaWidgetContents_3)
        self.qw_dados_com_3.setObjectName(u"qw_dados_com_3")
        self.qw_dados_com_3.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.qw_dados_com_3.sizePolicy().hasHeightForWidth())
        self.qw_dados_com_3.setSizePolicy(sizePolicy3)
        self.qw_dados_com_3.setMinimumSize(QSize(0, 0))
        self.qw_dados_com_3.setMaximumSize(QSize(16777215, 16777215))
        self.qw_dados_com_3.setFont(font)
        self.qw_dados_com_3.setStyleSheet(u"")
        self.verticalLayout_14 = QVBoxLayout(self.qw_dados_com_3)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.nao_atend_lb_dec_cen_mes = QLabel(self.qw_dados_com_3)
        self.nao_atend_lb_dec_cen_mes.setObjectName(u"nao_atend_lb_dec_cen_mes")
        sizePolicy4.setHeightForWidth(self.nao_atend_lb_dec_cen_mes.sizePolicy().hasHeightForWidth())
        self.nao_atend_lb_dec_cen_mes.setSizePolicy(sizePolicy4)
        self.nao_atend_lb_dec_cen_mes.setMinimumSize(QSize(0, 30))
        self.nao_atend_lb_dec_cen_mes.setMaximumSize(QSize(16777215, 30))
        self.nao_atend_lb_dec_cen_mes.setStyleSheet(u"QLabel{	\n"
"	background-color: rgb(180, 180, 180);\n"
"    border-style: outset;\n"
"    border-width: 3px;\n"
"   /* border-radius: 5px;*/\n"
"    border-color: rgb(234, 234, 234);\n"
"    font: bold 12px;\n"
"\n"
"}")
        self.nao_atend_lb_dec_cen_mes.setAlignment(Qt.AlignCenter)
        self.nao_atend_lb_dec_cen_mes.setWordWrap(False)

        self.verticalLayout_14.addWidget(self.nao_atend_lb_dec_cen_mes)

        self.widget_14 = QWidget(self.qw_dados_com_3)
        self.widget_14.setObjectName(u"widget_14")
        sizePolicy1.setHeightForWidth(self.widget_14.sizePolicy().hasHeightForWidth())
        self.widget_14.setSizePolicy(sizePolicy1)
        self.widget_14.setMinimumSize(QSize(0, 0))
        self.widget_14.setMaximumSize(QSize(16777215, 170))
        self.widget_14.setStyleSheet(u"")
        self.gridLayout_8 = QGridLayout(self.widget_14)
        self.gridLayout_8.setSpacing(0)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.widget_15 = QWidget(self.widget_14)
        self.widget_15.setObjectName(u"widget_15")
        sizePolicy1.setHeightForWidth(self.widget_15.sizePolicy().hasHeightForWidth())
        self.widget_15.setSizePolicy(sizePolicy1)
        self.widget_15.setMinimumSize(QSize(0, 165))
        self.widget_15.setMaximumSize(QSize(16777215, 165))
        self.widget_15.setStyleSheet(u"")
        self.gridLayout_9 = QGridLayout(self.widget_15)
        self.gridLayout_9.setSpacing(0)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(0, 0, 6, 0)
        self.frame_10 = QFrame(self.widget_15)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setStyleSheet(u"")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.gridLayout_11 = QGridLayout(self.frame_10)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setHorizontalSpacing(0)
        self.gridLayout_11.setVerticalSpacing(1)
        self.gridLayout_11.setContentsMargins(0, 0, 0, 2)
        self.nao_atend_cmb_email = QComboBox(self.frame_10)
        self.nao_atend_cmb_email.addItem("")
        self.nao_atend_cmb_email.addItem("")
        self.nao_atend_cmb_email.addItem("")
        self.nao_atend_cmb_email.setObjectName(u"nao_atend_cmb_email")
        sizePolicy5.setHeightForWidth(self.nao_atend_cmb_email.sizePolicy().hasHeightForWidth())
        self.nao_atend_cmb_email.setSizePolicy(sizePolicy5)
        self.nao_atend_cmb_email.setMinimumSize(QSize(86, 30))
        self.nao_atend_cmb_email.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_11.addWidget(self.nao_atend_cmb_email, 4, 2, 1, 1)

        self.nao_atend_cmb_acao_plan = QComboBox(self.frame_10)
        self.nao_atend_cmb_acao_plan.addItem("")
        self.nao_atend_cmb_acao_plan.addItem("")
        self.nao_atend_cmb_acao_plan.addItem("")
        self.nao_atend_cmb_acao_plan.setObjectName(u"nao_atend_cmb_acao_plan")
        sizePolicy5.setHeightForWidth(self.nao_atend_cmb_acao_plan.sizePolicy().hasHeightForWidth())
        self.nao_atend_cmb_acao_plan.setSizePolicy(sizePolicy5)
        self.nao_atend_cmb_acao_plan.setMinimumSize(QSize(86, 30))
        self.nao_atend_cmb_acao_plan.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_11.addWidget(self.nao_atend_cmb_acao_plan, 3, 2, 1, 1)

        self.label_33 = QLabel(self.frame_10)
        self.label_33.setObjectName(u"label_33")
        sizePolicy4.setHeightForWidth(self.label_33.sizePolicy().hasHeightForWidth())
        self.label_33.setSizePolicy(sizePolicy4)
        self.label_33.setMinimumSize(QSize(85, 30))
        self.label_33.setMaximumSize(QSize(85, 30))
        self.label_33.setStyleSheet(u"")
        self.label_33.setAlignment(Qt.AlignCenter)
        self.label_33.setWordWrap(False)

        self.gridLayout_11.addWidget(self.label_33, 4, 0, 1, 1)

        self.nao_atend_txt_material = QLineEdit(self.frame_10)
        self.nao_atend_txt_material.setObjectName(u"nao_atend_txt_material")
        self.nao_atend_txt_material.setMinimumSize(QSize(86, 30))
        self.nao_atend_txt_material.setMaximumSize(QSize(16777215, 30))
        self.nao_atend_txt_material.setMaxLength(8)

        self.gridLayout_11.addWidget(self.nao_atend_txt_material, 5, 2, 1, 1)

        self.nao_atend_cmb_ano_mes = QComboBox(self.frame_10)
        self.nao_atend_cmb_ano_mes.addItem("")
        self.nao_atend_cmb_ano_mes.setObjectName(u"nao_atend_cmb_ano_mes")
        sizePolicy5.setHeightForWidth(self.nao_atend_cmb_ano_mes.sizePolicy().hasHeightForWidth())
        self.nao_atend_cmb_ano_mes.setSizePolicy(sizePolicy5)
        self.nao_atend_cmb_ano_mes.setMinimumSize(QSize(86, 30))
        self.nao_atend_cmb_ano_mes.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_11.addWidget(self.nao_atend_cmb_ano_mes, 1, 2, 1, 1)

        self.label_27 = QLabel(self.frame_10)
        self.label_27.setObjectName(u"label_27")
        sizePolicy7 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.label_27.sizePolicy().hasHeightForWidth())
        self.label_27.setSizePolicy(sizePolicy7)
        self.label_27.setMinimumSize(QSize(250, 30))
        self.label_27.setMaximumSize(QSize(16777215, 30))
        self.label_27.setStyleSheet(u"")
        self.label_27.setAlignment(Qt.AlignCenter)
        self.label_27.setWordWrap(False)

        self.gridLayout_11.addWidget(self.label_27, 0, 0, 1, 6)

        self.label_31 = QLabel(self.frame_10)
        self.label_31.setObjectName(u"label_31")
        sizePolicy4.setHeightForWidth(self.label_31.sizePolicy().hasHeightForWidth())
        self.label_31.setSizePolicy(sizePolicy4)
        self.label_31.setMinimumSize(QSize(85, 30))
        self.label_31.setMaximumSize(QSize(85, 30))
        self.label_31.setStyleSheet(u"")
        self.label_31.setAlignment(Qt.AlignCenter)
        self.label_31.setWordWrap(False)

        self.gridLayout_11.addWidget(self.label_31, 3, 0, 1, 2)

        self.label_32 = QLabel(self.frame_10)
        self.label_32.setObjectName(u"label_32")
        sizePolicy4.setHeightForWidth(self.label_32.sizePolicy().hasHeightForWidth())
        self.label_32.setSizePolicy(sizePolicy4)
        self.label_32.setMinimumSize(QSize(85, 30))
        self.label_32.setMaximumSize(QSize(85, 30))
        self.label_32.setStyleSheet(u"")
        self.label_32.setAlignment(Qt.AlignCenter)
        self.label_32.setWordWrap(False)

        self.gridLayout_11.addWidget(self.label_32, 5, 0, 1, 2)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_11.addItem(self.verticalSpacer_6, 6, 0, 1, 1)

        self.label_30 = QLabel(self.frame_10)
        self.label_30.setObjectName(u"label_30")
        sizePolicy4.setHeightForWidth(self.label_30.sizePolicy().hasHeightForWidth())
        self.label_30.setSizePolicy(sizePolicy4)
        self.label_30.setMinimumSize(QSize(85, 30))
        self.label_30.setMaximumSize(QSize(85, 30))
        self.label_30.setStyleSheet(u"")
        self.label_30.setAlignment(Qt.AlignCenter)
        self.label_30.setWordWrap(False)

        self.gridLayout_11.addWidget(self.label_30, 1, 0, 1, 2)

        self.frame_7 = QFrame(self.frame_10)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setStyleSheet(u"border: 0px;")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_7)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(10, 2, 5, 0)
        self.nao_atend_btn_pesquisar = QPushButton(self.frame_7)
        self.nao_atend_btn_pesquisar.setObjectName(u"nao_atend_btn_pesquisar")
        sizePolicy3.setHeightForWidth(self.nao_atend_btn_pesquisar.sizePolicy().hasHeightForWidth())
        self.nao_atend_btn_pesquisar.setSizePolicy(sizePolicy3)
        self.nao_atend_btn_pesquisar.setMinimumSize(QSize(50, 60))
        self.nao_atend_btn_pesquisar.setMaximumSize(QSize(50, 60))
        self.nao_atend_btn_pesquisar.setFont(font1)
        self.nao_atend_btn_pesquisar.setCursor(QCursor(Qt.PointingHandCursor))
        self.nao_atend_btn_pesquisar.setLayoutDirection(Qt.RightToLeft)
        self.nao_atend_btn_pesquisar.setStyleSheet(u"#nao_atend_btn_pesquisar{	\n"
"	background-color: rgb(170, 255, 255);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 5px; \n"
"    border-color: rgb(180, 255, 255);\n"
"    font: bold 14px;		\n"
"	text-align: center;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#nao_atend_btn_pesquisar::hover {\n"
"    background-color: rgb(150, 255, 255);\n"
"    border-style: inset;\n"
"}\n"
"#nao_atend_btn_pesquisar::pressed {\n"
"    background-color: rgb(150, 255, 255);\n"
"    border-style: inset;\n"
"}")
        icon11 = QIcon()
        icon11.addFile(u":/assets.icons_alt_regras/banco-de-dados-de-pesquisa.png", QSize(), QIcon.Normal, QIcon.Off)
        self.nao_atend_btn_pesquisar.setIcon(icon11)
        self.nao_atend_btn_pesquisar.setIconSize(QSize(25, 25))

        self.verticalLayout_7.addWidget(self.nao_atend_btn_pesquisar)


        self.gridLayout_11.addWidget(self.frame_7, 1, 3, 4, 2, Qt.AlignTop)


        self.gridLayout_9.addWidget(self.frame_10, 2, 5, 1, 1)

        self.frame_8 = QFrame(self.widget_15)
        self.frame_8.setObjectName(u"frame_8")
        sizePolicy2.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy2)
        self.frame_8.setMinimumSize(QSize(200, 0))
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.gridLayout_10 = QGridLayout(self.frame_8)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setHorizontalSpacing(2)
        self.gridLayout_10.setVerticalSpacing(0)
        self.gridLayout_10.setContentsMargins(4, 0, 2, 0)
        self.nao_atend_lb_itens_na = QLabel(self.frame_8)
        self.nao_atend_lb_itens_na.setObjectName(u"nao_atend_lb_itens_na")
        self.nao_atend_lb_itens_na.setMinimumSize(QSize(80, 30))
        self.nao_atend_lb_itens_na.setMaximumSize(QSize(16777215, 30))
        self.nao_atend_lb_itens_na.setStyleSheet(u"background-color: rgb(255, 255, 255);color: rgb(227, 0, 0);")
        self.nao_atend_lb_itens_na.setAlignment(Qt.AlignCenter)
        self.nao_atend_lb_itens_na.setWordWrap(False)

        self.gridLayout_10.addWidget(self.nao_atend_lb_itens_na, 3, 0, 1, 1)

        self.nao_atend_lb_total_ocor = QLabel(self.frame_8)
        self.nao_atend_lb_total_ocor.setObjectName(u"nao_atend_lb_total_ocor")
        self.nao_atend_lb_total_ocor.setMinimumSize(QSize(80, 30))
        self.nao_atend_lb_total_ocor.setMaximumSize(QSize(16777215, 30))
        self.nao_atend_lb_total_ocor.setStyleSheet(u"background-color: rgb(255, 255, 255);color: rgb(227, 0, 0);")
        self.nao_atend_lb_total_ocor.setAlignment(Qt.AlignCenter)
        self.nao_atend_lb_total_ocor.setWordWrap(False)

        self.gridLayout_10.addWidget(self.nao_atend_lb_total_ocor, 1, 0, 1, 1)

        self.label_29 = QLabel(self.frame_8)
        self.label_29.setObjectName(u"label_29")
        sizePolicy4.setHeightForWidth(self.label_29.sizePolicy().hasHeightForWidth())
        self.label_29.setSizePolicy(sizePolicy4)
        self.label_29.setMinimumSize(QSize(0, 30))
        self.label_29.setMaximumSize(QSize(16777215, 30))
        self.label_29.setStyleSheet(u"")
        self.label_29.setAlignment(Qt.AlignCenter)
        self.label_29.setWordWrap(False)

        self.gridLayout_10.addWidget(self.label_29, 2, 0, 1, 1)

        self.label_25 = QLabel(self.frame_8)
        self.label_25.setObjectName(u"label_25")
        sizePolicy6.setHeightForWidth(self.label_25.sizePolicy().hasHeightForWidth())
        self.label_25.setSizePolicy(sizePolicy6)
        self.label_25.setMinimumSize(QSize(0, 30))
        self.label_25.setMaximumSize(QSize(16777215, 30))
        self.label_25.setStyleSheet(u"")
        self.label_25.setAlignment(Qt.AlignCenter)
        self.label_25.setWordWrap(False)

        self.gridLayout_10.addWidget(self.label_25, 0, 0, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_10.addItem(self.verticalSpacer_4, 4, 0, 1, 1)


        self.gridLayout_9.addWidget(self.frame_8, 0, 2, 4, 1, Qt.AlignLeft)

        self.frame_9 = QFrame(self.widget_15)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMinimumSize(QSize(203, 0))
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_9)
        self.verticalLayout_6.setSpacing(2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(2, 2, 2, 2)
        self.label_26 = QLabel(self.frame_9)
        self.label_26.setObjectName(u"label_26")
        sizePolicy4.setHeightForWidth(self.label_26.sizePolicy().hasHeightForWidth())
        self.label_26.setSizePolicy(sizePolicy4)
        self.label_26.setMinimumSize(QSize(140, 30))
        self.label_26.setMaximumSize(QSize(16777215, 30))
        self.label_26.setStyleSheet(u"")
        self.label_26.setAlignment(Qt.AlignCenter)
        self.label_26.setWordWrap(False)

        self.verticalLayout_6.addWidget(self.label_26)

        self.nao_atend_lb_na_mes_ant = QLabel(self.frame_9)
        self.nao_atend_lb_na_mes_ant.setObjectName(u"nao_atend_lb_na_mes_ant")
        self.nao_atend_lb_na_mes_ant.setMinimumSize(QSize(0, 30))
        self.nao_atend_lb_na_mes_ant.setMaximumSize(QSize(16777215, 30))
        self.nao_atend_lb_na_mes_ant.setStyleSheet(u"background-color: rgb(255, 255, 255);color: rgb(227, 0, 0);")
        self.nao_atend_lb_na_mes_ant.setAlignment(Qt.AlignCenter)
        self.nao_atend_lb_na_mes_ant.setWordWrap(False)

        self.verticalLayout_6.addWidget(self.nao_atend_lb_na_mes_ant)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_2)


        self.gridLayout_9.addWidget(self.frame_9, 0, 3, 4, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_2, 2, 6, 1, 1)

        self.frame = QFrame(self.widget_15)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"border:0px")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(20)
        self.gridLayout_3.setVerticalSpacing(19)
        self.gridLayout_3.setContentsMargins(20, 0, 10, 0)
        self.nao_atend_btn_alt_regist = QPushButton(self.frame)
        self.nao_atend_btn_alt_regist.setObjectName(u"nao_atend_btn_alt_regist")
        sizePolicy3.setHeightForWidth(self.nao_atend_btn_alt_regist.sizePolicy().hasHeightForWidth())
        self.nao_atend_btn_alt_regist.setSizePolicy(sizePolicy3)
        self.nao_atend_btn_alt_regist.setMinimumSize(QSize(60, 35))
        self.nao_atend_btn_alt_regist.setMaximumSize(QSize(60, 35))
        self.nao_atend_btn_alt_regist.setFont(font1)
        self.nao_atend_btn_alt_regist.setCursor(QCursor(Qt.PointingHandCursor))
        self.nao_atend_btn_alt_regist.setLayoutDirection(Qt.RightToLeft)
        self.nao_atend_btn_alt_regist.setStyleSheet(u"#nao_atend_btn_alt_regist{	\n"
"	background-color: rgb(218, 145, 0);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 5px; \n"
"    border-color: rgb(235, 153, 0);\n"
"    font: bold 14px;		\n"
"	text-align: center;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#nao_atend_btn_alt_regist::hover {\n"
"    background-color: rgb(186, 121, 0);\n"
"    border-style: inset;\n"
"}\n"
"#nao_atend_btn_alt_regist::pressed {\n"
"    background-color: rgb(186, 121, 0);\n"
"    border-style: inset;\n"
"}")
        self.nao_atend_btn_alt_regist.setIcon(icon8)
        self.nao_atend_btn_alt_regist.setIconSize(QSize(25, 25))

        self.gridLayout_3.addWidget(self.nao_atend_btn_alt_regist, 2, 1, 1, 1)

        self.nao_atend_btn_inc_regist = QPushButton(self.frame)
        self.nao_atend_btn_inc_regist.setObjectName(u"nao_atend_btn_inc_regist")
        sizePolicy3.setHeightForWidth(self.nao_atend_btn_inc_regist.sizePolicy().hasHeightForWidth())
        self.nao_atend_btn_inc_regist.setSizePolicy(sizePolicy3)
        self.nao_atend_btn_inc_regist.setMinimumSize(QSize(60, 35))
        self.nao_atend_btn_inc_regist.setMaximumSize(QSize(60, 35))
        self.nao_atend_btn_inc_regist.setFont(font1)
        self.nao_atend_btn_inc_regist.setCursor(QCursor(Qt.PointingHandCursor))
        self.nao_atend_btn_inc_regist.setLayoutDirection(Qt.RightToLeft)
        self.nao_atend_btn_inc_regist.setStyleSheet(u"#nao_atend_btn_inc_regist{	\n"
"	background-color: rgb(0, 195, 0);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 5px; \n"
"    border-color: rgb(0, 212, 0);\n"
"    font: bold 14px;		\n"
"	text-align: center;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#nao_atend_btn_inc_regist::hover {\n"
"    background-color: rgb(0, 144, 0);\n"
"    border-style: inset;\n"
"}\n"
"#nao_atend_btn_inc_regist::pressed {\n"
"    background-color:  rgb(0, 144, 0);\n"
"    border-style: inset;\n"
"}")
        self.nao_atend_btn_inc_regist.setIcon(icon9)
        self.nao_atend_btn_inc_regist.setIconSize(QSize(25, 25))

        self.gridLayout_3.addWidget(self.nao_atend_btn_inc_regist, 0, 1, 1, 1)

        self.nao_atend_btn_visualizar = QPushButton(self.frame)
        self.nao_atend_btn_visualizar.setObjectName(u"nao_atend_btn_visualizar")
        sizePolicy3.setHeightForWidth(self.nao_atend_btn_visualizar.sizePolicy().hasHeightForWidth())
        self.nao_atend_btn_visualizar.setSizePolicy(sizePolicy3)
        self.nao_atend_btn_visualizar.setMinimumSize(QSize(60, 35))
        self.nao_atend_btn_visualizar.setMaximumSize(QSize(60, 35))
        self.nao_atend_btn_visualizar.setFont(font1)
        self.nao_atend_btn_visualizar.setCursor(QCursor(Qt.PointingHandCursor))
        self.nao_atend_btn_visualizar.setLayoutDirection(Qt.RightToLeft)
        self.nao_atend_btn_visualizar.setStyleSheet(u"#nao_atend_btn_visualizar{	\n"
"	background-color: rgb(170, 255, 255);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 5px; \n"
"    border-color: rgb(180, 255, 255);\n"
"    font: bold 14px;		\n"
"	text-align: center;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#nao_atend_btn_visualizar::hover {\n"
"    background-color: rgb(150, 255, 255);\n"
"    border-style: inset;\n"
"}\n"
"#nao_atend_btn_visualizar::pressed {\n"
"    background-color: rgb(150, 255, 255);\n"
"    border-style: inset;\n"
"}")
        icon12 = QIcon()
        icon12.addFile(u":/assets.icons_alt_regras/vis\u00edvel.png", QSize(), QIcon.Normal, QIcon.Off)
        self.nao_atend_btn_visualizar.setIcon(icon12)
        self.nao_atend_btn_visualizar.setIconSize(QSize(25, 25))

        self.gridLayout_3.addWidget(self.nao_atend_btn_visualizar, 2, 2, 1, 1)

        self.nao_atend_btn_historico = QPushButton(self.frame)
        self.nao_atend_btn_historico.setObjectName(u"nao_atend_btn_historico")
        sizePolicy3.setHeightForWidth(self.nao_atend_btn_historico.sizePolicy().hasHeightForWidth())
        self.nao_atend_btn_historico.setSizePolicy(sizePolicy3)
        self.nao_atend_btn_historico.setMinimumSize(QSize(60, 35))
        self.nao_atend_btn_historico.setMaximumSize(QSize(60, 35))
        self.nao_atend_btn_historico.setFont(font1)
        self.nao_atend_btn_historico.setCursor(QCursor(Qt.PointingHandCursor))
        self.nao_atend_btn_historico.setLayoutDirection(Qt.RightToLeft)
        self.nao_atend_btn_historico.setStyleSheet(u"#nao_atend_btn_historico{	\n"
"	background-color: rgb(0, 200, 200);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 5px; \n"
"    border-color: rgb(0, 230, 230);\n"
"    font: bold 14px;		\n"
"	text-align: center;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#nao_atend_btn_historico::hover {\n"
"    background-color: rgb(0, 180, 180);\n"
"    border-style: inset;\n"
"}\n"
"#nao_atend_btn_historico::pressed {\n"
"    background-color: rgb(0, 180, 180);\n"
"    border-style: inset;\n"
"}")
        icon13 = QIcon()
        icon13.addFile(u":/assets.icons_alt_regras/hist\u00f3rico-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.nao_atend_btn_historico.setIcon(icon13)
        self.nao_atend_btn_historico.setIconSize(QSize(25, 25))

        self.gridLayout_3.addWidget(self.nao_atend_btn_historico, 3, 2, 1, 1)

        self.nao_atend_btn_excluir = QPushButton(self.frame)
        self.nao_atend_btn_excluir.setObjectName(u"nao_atend_btn_excluir")
        sizePolicy3.setHeightForWidth(self.nao_atend_btn_excluir.sizePolicy().hasHeightForWidth())
        self.nao_atend_btn_excluir.setSizePolicy(sizePolicy3)
        self.nao_atend_btn_excluir.setMinimumSize(QSize(60, 35))
        self.nao_atend_btn_excluir.setMaximumSize(QSize(60, 35))
        self.nao_atend_btn_excluir.setFont(font1)
        self.nao_atend_btn_excluir.setCursor(QCursor(Qt.PointingHandCursor))
        self.nao_atend_btn_excluir.setLayoutDirection(Qt.RightToLeft)
        self.nao_atend_btn_excluir.setStyleSheet(u"#nao_atend_btn_excluir{	\n"
"	background-color: rgb(255, 0, 0);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 5px; \n"
"    border-color: rgb(255, 0, 0);\n"
"    font: bold 14px;		\n"
"	text-align: center;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#nao_atend_btn_excluir::hover {\n"
"    background-color: rgb(230, 0, 0);\n"
"    border-style: inset;\n"
"}\n"
"#nao_atend_btn_excluir::pressed {\n"
"    background-color: rgb(230, 0, 0);\n"
"    border-style: inset;\n"
"}")
        self.nao_atend_btn_excluir.setIcon(icon5)
        self.nao_atend_btn_excluir.setIconSize(QSize(25, 25))

        self.gridLayout_3.addWidget(self.nao_atend_btn_excluir, 3, 1, 1, 1)

        self.nao_atend_btn_enviar_email = QPushButton(self.frame)
        self.nao_atend_btn_enviar_email.setObjectName(u"nao_atend_btn_enviar_email")
        sizePolicy3.setHeightForWidth(self.nao_atend_btn_enviar_email.sizePolicy().hasHeightForWidth())
        self.nao_atend_btn_enviar_email.setSizePolicy(sizePolicy3)
        self.nao_atend_btn_enviar_email.setMinimumSize(QSize(60, 35))
        self.nao_atend_btn_enviar_email.setMaximumSize(QSize(60, 35))
        self.nao_atend_btn_enviar_email.setFont(font1)
        self.nao_atend_btn_enviar_email.setCursor(QCursor(Qt.PointingHandCursor))
        self.nao_atend_btn_enviar_email.setLayoutDirection(Qt.RightToLeft)
        self.nao_atend_btn_enviar_email.setStyleSheet(u"#nao_atend_btn_enviar_email{	\n"
"	background-color: rgb(0, 230, 230);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 5px; \n"
"    border-color: rgb(0, 255, 255);\n"
"    font: bold 14px;		\n"
"	text-align: center;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#nao_atend_btn_enviar_email::hover {\n"
"    background-color: rgb(0, 200, 200);\n"
"    border-style: inset;\n"
"}\n"
"#nao_atend_btn_enviar_email::pressed {\n"
"    background-color: rgb(0, 200, 200);\n"
"    border-style: inset;\n"
"}")
        icon14 = QIcon()
        icon14.addFile(u":/assets.icons_alt_regras/enviar-60.png", QSize(), QIcon.Normal, QIcon.Off)
        self.nao_atend_btn_enviar_email.setIcon(icon14)
        self.nao_atend_btn_enviar_email.setIconSize(QSize(25, 25))

        self.gridLayout_3.addWidget(self.nao_atend_btn_enviar_email, 0, 2, 1, 1)


        self.gridLayout_9.addWidget(self.frame, 2, 7, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)


        self.gridLayout_8.addWidget(self.widget_15, 0, 0, 1, 1, Qt.AlignTop)


        self.verticalLayout_14.addWidget(self.widget_14, 0, Qt.AlignTop)

        self.label_24 = QLabel(self.qw_dados_com_3)
        self.label_24.setObjectName(u"label_24")
        sizePolicy4.setHeightForWidth(self.label_24.sizePolicy().hasHeightForWidth())
        self.label_24.setSizePolicy(sizePolicy4)
        self.label_24.setMinimumSize(QSize(0, 30))
        self.label_24.setMaximumSize(QSize(16777215, 30))
        self.label_24.setStyleSheet(u"QLabel{	\n"
"	background-color: rgb(180, 180, 180);\n"
"    border-style: outset;\n"
"    border-width: 3px;\n"
"   /* border-radius: 5px;*/\n"
"    border-color: rgb(234, 234, 234);\n"
"    font: bold 12px;\n"
"\n"
"}")
        self.label_24.setAlignment(Qt.AlignCenter)
        self.label_24.setWordWrap(False)

        self.verticalLayout_14.addWidget(self.label_24)


        self.verticalLayout_10.addWidget(self.qw_dados_com_3, 0, Qt.AlignTop)

        self.nao_atend_tb_registros = QTableWidget(self.scrollAreaWidgetContents_3)
        if (self.nao_atend_tb_registros.columnCount() < 39):
            self.nao_atend_tb_registros.setColumnCount(39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.nao_atend_tb_registros.setHorizontalHeaderItem(0, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.nao_atend_tb_registros.setHorizontalHeaderItem(1, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.nao_atend_tb_registros.setHorizontalHeaderItem(2, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        self.nao_atend_tb_registros.setHorizontalHeaderItem(3, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        self.nao_atend_tb_registros.setHorizontalHeaderItem(4, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        self.nao_atend_tb_registros.setHorizontalHeaderItem(5, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        self.nao_atend_tb_registros.setHorizontalHeaderItem(6, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        self.nao_atend_tb_registros.setHorizontalHeaderItem(7, __qtablewidgetitem47)
        __qtablewidgetitem48 = QTableWidgetItem()
        self.nao_atend_tb_registros.setHorizontalHeaderItem(8, __qtablewidgetitem48)
        __qtablewidgetitem49 = QTableWidgetItem()
        self.nao_atend_tb_registros.setHorizontalHeaderItem(9, __qtablewidgetitem49)
        __qtablewidgetitem50 = QTableWidgetItem()
        self.nao_atend_tb_registros.setHorizontalHeaderItem(10, __qtablewidgetitem50)
        __qtablewidgetitem51 = QTableWidgetItem()
        self.nao_atend_tb_registros.setHorizontalHeaderItem(11, __qtablewidgetitem51)
        __qtablewidgetitem52 = QTableWidgetItem()
        self.nao_atend_tb_registros.setHorizontalHeaderItem(12, __qtablewidgetitem52)
        __qtablewidgetitem53 = QTableWidgetItem()
        self.nao_atend_tb_registros.setHorizontalHeaderItem(13, __qtablewidgetitem53)
        __qtablewidgetitem54 = QTableWidgetItem()
        self.nao_atend_tb_registros.setHorizontalHeaderItem(14, __qtablewidgetitem54)
        __qtablewidgetitem55 = QTableWidgetItem()
        self.nao_atend_tb_registros.setHorizontalHeaderItem(15, __qtablewidgetitem55)
        __qtablewidgetitem56 = QTableWidgetItem()
        self.nao_atend_tb_registros.setHorizontalHeaderItem(16, __qtablewidgetitem56)
        __qtablewidgetitem57 = QTableWidgetItem()
        self.nao_atend_tb_registros.setHorizontalHeaderItem(17, __qtablewidgetitem57)
        __qtablewidgetitem58 = QTableWidgetItem()
        self.nao_atend_tb_registros.setHorizontalHeaderItem(18, __qtablewidgetitem58)
        __qtablewidgetitem59 = QTableWidgetItem()
        self.nao_atend_tb_registros.setHorizontalHeaderItem(19, __qtablewidgetitem59)
        __qtablewidgetitem60 = QTableWidgetItem()
        self.nao_atend_tb_registros.setHorizontalHeaderItem(20, __qtablewidgetitem60)
        __qtablewidgetitem61 = QTableWidgetItem()
        self.nao_atend_tb_registros.setHorizontalHeaderItem(21, __qtablewidgetitem61)
        __qtablewidgetitem62 = QTableWidgetItem()
        self.nao_atend_tb_registros.setHorizontalHeaderItem(22, __qtablewidgetitem62)
        __qtablewidgetitem63 = QTableWidgetItem()
        self.nao_atend_tb_registros.setHorizontalHeaderItem(23, __qtablewidgetitem63)
        __qtablewidgetitem64 = QTableWidgetItem()
        self.nao_atend_tb_registros.setHorizontalHeaderItem(24, __qtablewidgetitem64)
        __qtablewidgetitem65 = QTableWidgetItem()
        self.nao_atend_tb_registros.setHorizontalHeaderItem(25, __qtablewidgetitem65)
        __qtablewidgetitem66 = QTableWidgetItem()
        self.nao_atend_tb_registros.setHorizontalHeaderItem(26, __qtablewidgetitem66)
        __qtablewidgetitem67 = QTableWidgetItem()
        self.nao_atend_tb_registros.setHorizontalHeaderItem(27, __qtablewidgetitem67)
        __qtablewidgetitem68 = QTableWidgetItem()
        self.nao_atend_tb_registros.setHorizontalHeaderItem(28, __qtablewidgetitem68)
        __qtablewidgetitem69 = QTableWidgetItem()
        self.nao_atend_tb_registros.setHorizontalHeaderItem(29, __qtablewidgetitem69)
        __qtablewidgetitem70 = QTableWidgetItem()
        self.nao_atend_tb_registros.setHorizontalHeaderItem(30, __qtablewidgetitem70)
        __qtablewidgetitem71 = QTableWidgetItem()
        self.nao_atend_tb_registros.setHorizontalHeaderItem(31, __qtablewidgetitem71)
        __qtablewidgetitem72 = QTableWidgetItem()
        self.nao_atend_tb_registros.setHorizontalHeaderItem(32, __qtablewidgetitem72)
        __qtablewidgetitem73 = QTableWidgetItem()
        self.nao_atend_tb_registros.setHorizontalHeaderItem(33, __qtablewidgetitem73)
        __qtablewidgetitem74 = QTableWidgetItem()
        self.nao_atend_tb_registros.setHorizontalHeaderItem(34, __qtablewidgetitem74)
        __qtablewidgetitem75 = QTableWidgetItem()
        self.nao_atend_tb_registros.setHorizontalHeaderItem(35, __qtablewidgetitem75)
        __qtablewidgetitem76 = QTableWidgetItem()
        self.nao_atend_tb_registros.setHorizontalHeaderItem(36, __qtablewidgetitem76)
        __qtablewidgetitem77 = QTableWidgetItem()
        self.nao_atend_tb_registros.setHorizontalHeaderItem(37, __qtablewidgetitem77)
        __qtablewidgetitem78 = QTableWidgetItem()
        self.nao_atend_tb_registros.setHorizontalHeaderItem(38, __qtablewidgetitem78)
        self.nao_atend_tb_registros.setObjectName(u"nao_atend_tb_registros")
        sizePolicy3.setHeightForWidth(self.nao_atend_tb_registros.sizePolicy().hasHeightForWidth())
        self.nao_atend_tb_registros.setSizePolicy(sizePolicy3)
        self.nao_atend_tb_registros.setMinimumSize(QSize(0, 0))
        self.nao_atend_tb_registros.setMaximumSize(QSize(16777215, 16777215))
        self.nao_atend_tb_registros.setStyleSheet(u"")
        self.nao_atend_tb_registros.setFrameShape(QFrame.StyledPanel)
        self.nao_atend_tb_registros.setFrameShadow(QFrame.Sunken)
        self.nao_atend_tb_registros.setLineWidth(1)
        self.nao_atend_tb_registros.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.nao_atend_tb_registros.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.nao_atend_tb_registros.setAutoScroll(True)
        self.nao_atend_tb_registros.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.nao_atend_tb_registros.setProperty("showDropIndicator", True)
        self.nao_atend_tb_registros.setDragEnabled(False)
        self.nao_atend_tb_registros.setAlternatingRowColors(True)
        self.nao_atend_tb_registros.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.nao_atend_tb_registros.setTextElideMode(Qt.ElideRight)
        self.nao_atend_tb_registros.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.nao_atend_tb_registros.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.nao_atend_tb_registros.setShowGrid(True)
        self.nao_atend_tb_registros.setGridStyle(Qt.SolidLine)
        self.nao_atend_tb_registros.setSortingEnabled(False)
        self.nao_atend_tb_registros.setWordWrap(True)
        self.nao_atend_tb_registros.setCornerButtonEnabled(True)
        self.nao_atend_tb_registros.setRowCount(0)
        self.nao_atend_tb_registros.setColumnCount(39)
        self.nao_atend_tb_registros.horizontalHeader().setVisible(True)
        self.nao_atend_tb_registros.horizontalHeader().setCascadingSectionResizes(False)
        self.nao_atend_tb_registros.horizontalHeader().setMinimumSectionSize(42)
        self.nao_atend_tb_registros.horizontalHeader().setDefaultSectionSize(120)
        self.nao_atend_tb_registros.horizontalHeader().setHighlightSections(True)
        self.nao_atend_tb_registros.horizontalHeader().setProperty("showSortIndicator", False)
        self.nao_atend_tb_registros.horizontalHeader().setStretchLastSection(True)
        self.nao_atend_tb_registros.verticalHeader().setCascadingSectionResizes(True)
        self.nao_atend_tb_registros.verticalHeader().setDefaultSectionSize(30)
        self.nao_atend_tb_registros.verticalHeader().setHighlightSections(True)
        self.nao_atend_tb_registros.verticalHeader().setProperty("showSortIndicator", False)
        self.nao_atend_tb_registros.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_10.addWidget(self.nao_atend_tb_registros)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)

        self.horizontalLayout_4.addWidget(self.scrollArea_3)

        self.pgs_principal.addWidget(self.pg_nao_atendidos)
        self.pg_notificacao = QWidget()
        self.pg_notificacao.setObjectName(u"pg_notificacao")
        self.verticalLayout_4 = QVBoxLayout(self.pg_notificacao)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.lb_notificacao = QLabel(self.pg_notificacao)
        self.lb_notificacao.setObjectName(u"lb_notificacao")
        sizePolicy.setHeightForWidth(self.lb_notificacao.sizePolicy().hasHeightForWidth())
        self.lb_notificacao.setSizePolicy(sizePolicy)
        self.lb_notificacao.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: bold 12pt;\n"
"background-color: rgb(0, 98, 98);\n"
"border-radius: 3px;")
        self.lb_notificacao.setAlignment(Qt.AlignCenter)
        self.lb_notificacao.setWordWrap(True)

        self.verticalLayout_4.addWidget(self.lb_notificacao)

        self.pgs_principal.addWidget(self.pg_notificacao)
        self.pg_controle_acesso = QWidget()
        self.pg_controle_acesso.setObjectName(u"pg_controle_acesso")
        self.pg_controle_acesso.setStyleSheet(u"QLabel{	\n"
"	border-style: ridge;\n"
"	border-width: 2px;\n"
"    border-color: rgb(170, 170, 170);\n"
"	text-align: left;\n"
"	font: bold 9pt \"Segoe UI\";\n"
"}")
        self.horizontalLayout_3 = QHBoxLayout(self.pg_controle_acesso)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_2 = QScrollArea(self.pg_controle_acesso)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        sizePolicy3.setHeightForWidth(self.scrollArea_2.sizePolicy().hasHeightForWidth())
        self.scrollArea_2.setSizePolicy(sizePolicy3)
        self.scrollArea_2.setMinimumSize(QSize(0, 0))
        self.scrollArea_2.setMaximumSize(QSize(16777215, 16777215))
        self.scrollArea_2.setStyleSheet(u"")
        self.scrollArea_2.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 656, 481))
        sizePolicy3.setHeightForWidth(self.scrollAreaWidgetContents_2.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents_2.setSizePolicy(sizePolicy3)
        self.scrollAreaWidgetContents_2.setStyleSheet(u"")
        self.verticalLayout_9 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.qw_dados_com_2 = QWidget(self.scrollAreaWidgetContents_2)
        self.qw_dados_com_2.setObjectName(u"qw_dados_com_2")
        self.qw_dados_com_2.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.qw_dados_com_2.sizePolicy().hasHeightForWidth())
        self.qw_dados_com_2.setSizePolicy(sizePolicy3)
        self.qw_dados_com_2.setMinimumSize(QSize(0, 0))
        self.qw_dados_com_2.setMaximumSize(QSize(16777215, 16777215))
        self.qw_dados_com_2.setFont(font)
        self.qw_dados_com_2.setStyleSheet(u"")
        self.verticalLayout_13 = QVBoxLayout(self.qw_dados_com_2)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.label_21 = QLabel(self.qw_dados_com_2)
        self.label_21.setObjectName(u"label_21")
        sizePolicy4.setHeightForWidth(self.label_21.sizePolicy().hasHeightForWidth())
        self.label_21.setSizePolicy(sizePolicy4)
        self.label_21.setMinimumSize(QSize(0, 30))
        self.label_21.setMaximumSize(QSize(16777215, 30))
        self.label_21.setStyleSheet(u"QLabel{	\n"
"	background-color: rgb(180, 180, 180);\n"
"    border-style: outset;\n"
"    border-width: 3px;\n"
"   /* border-radius: 5px;*/\n"
"    border-color: rgb(234, 234, 234);\n"
"    font: bold 12px;\n"
"\n"
"}")
        self.label_21.setAlignment(Qt.AlignCenter)
        self.label_21.setWordWrap(False)

        self.verticalLayout_13.addWidget(self.label_21)

        self.widget_12 = QWidget(self.qw_dados_com_2)
        self.widget_12.setObjectName(u"widget_12")
        sizePolicy1.setHeightForWidth(self.widget_12.sizePolicy().hasHeightForWidth())
        self.widget_12.setSizePolicy(sizePolicy1)
        self.widget_12.setMinimumSize(QSize(0, 0))
        self.widget_12.setMaximumSize(QSize(16777215, 150))
        self.widget_12.setStyleSheet(u"#widget_11{	\n"
"    border-top: 2px solid;\n"
" 	border: 2px solid;\n"
"	/*border-right: 2px solid;\n"
"    border-color: rgb(100, 100, 100);*/\n"
"    border-color: rgb(234, 234, 234);\n"
"background-color: rgb(225, 225, 225);\n"
"}\n"
"#frame_4{	\n"
"    border-top: 2px solid;\n"
" 	border: 2px solid;\n"
"    border-color: rgb(234, 234, 234);\n"
"}\n"
"QFrame{\n"
"	background-color: rgb(225, 225, 225);\n"
"}\n"
"/*\n"
"QTableWidget QWidget {\n"
"    color: #fffff8;\n"
"}\n"
"QTableWidget QHeaderView::section {\n"
"    background-color: rgb(0, 108, 108);;   \n"
"  }\n"
"QTableWidget QTableCornerButton::section {\n"
"   background-color: rgb(0, 108, 108);;\n"
"   border: 1px solid #006b6b;\n"
"}*/\n"
"")
        self.gridLayout_5 = QGridLayout(self.widget_12)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.widget_13 = QWidget(self.widget_12)
        self.widget_13.setObjectName(u"widget_13")
        sizePolicy1.setHeightForWidth(self.widget_13.sizePolicy().hasHeightForWidth())
        self.widget_13.setSizePolicy(sizePolicy1)
        self.widget_13.setMinimumSize(QSize(0, 0))
        self.widget_13.setMaximumSize(QSize(16777215, 16777215))
        self.widget_13.setStyleSheet(u"QWidget{	\n"
"	border-style: ridge;\n"
"    border-width: 2px;\n"
"    border-color: rgb(234, 234, 234);\n"
"	background-color: rgb(225, 225, 225);\n"
"}\n"
"\n"
"QLabel{	\n"
"	background-color: rgb(225, 225, 225);\n"
"	border-style: ridge;\n"
"	border-width: 2px;\n"
"    border-color: rgb(250, 250, 250);\n"
"    font: bold 12px;\n"
"}\n"
"\n"
"QLineEdit{		\n"
"	background-color: rgb(255, 255, 255);\n"
"\n"
"	border-style: inset;\n"
"	border-width: 3px;\n"
"    border-color: rgb(180, 180, 180);\n"
"\n"
"    font: bold 12px;\n"
"}\n"
"QLineEdit::focus{\n"
"    background-color: rgb(170, 255, 255);\n"
"    border-style: inset;\n"
"}\n"
"\n"
"\n"
"")
        self.gridLayout_7 = QGridLayout(self.widget_13)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setHorizontalSpacing(30)
        self.gridLayout_7.setVerticalSpacing(2)
        self.gridLayout_7.setContentsMargins(9, 6, 9, 7)
        self.cont_aces_btn_inc_user = QPushButton(self.widget_13)
        self.cont_aces_btn_inc_user.setObjectName(u"cont_aces_btn_inc_user")
        sizePolicy3.setHeightForWidth(self.cont_aces_btn_inc_user.sizePolicy().hasHeightForWidth())
        self.cont_aces_btn_inc_user.setSizePolicy(sizePolicy3)
        self.cont_aces_btn_inc_user.setMinimumSize(QSize(80, 50))
        self.cont_aces_btn_inc_user.setMaximumSize(QSize(80, 50))
        self.cont_aces_btn_inc_user.setFont(font1)
        self.cont_aces_btn_inc_user.setCursor(QCursor(Qt.PointingHandCursor))
        self.cont_aces_btn_inc_user.setLayoutDirection(Qt.RightToLeft)
        self.cont_aces_btn_inc_user.setStyleSheet(u"#cont_aces_btn_inc_user{	\n"
"	background-color: rgb(0, 195, 0);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 5px; \n"
"    border-color: rgb(0, 212, 0);\n"
"    font: bold 14px;		\n"
"	text-align: center;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#cont_aces_btn_inc_user::hover {\n"
"    background-color: rgb(0, 144, 0);\n"
"    border-style: inset;\n"
"}\n"
"#cont_aces_btn_inc_user::pressed {\n"
"    background-color:  rgb(0, 144, 0);\n"
"    border-style: inset;\n"
"}")
        icon15 = QIcon()
        icon15.addFile(u":/assets.icons_alt_regras/usu\u00e1rio-adicionar-60.png", QSize(), QIcon.Normal, QIcon.Off)
        self.cont_aces_btn_inc_user.setIcon(icon15)
        self.cont_aces_btn_inc_user.setIconSize(QSize(40, 40))

        self.gridLayout_7.addWidget(self.cont_aces_btn_inc_user, 0, 1, 1, 1)

        self.cont_aces_btn_alt_user = QPushButton(self.widget_13)
        self.cont_aces_btn_alt_user.setObjectName(u"cont_aces_btn_alt_user")
        sizePolicy3.setHeightForWidth(self.cont_aces_btn_alt_user.sizePolicy().hasHeightForWidth())
        self.cont_aces_btn_alt_user.setSizePolicy(sizePolicy3)
        self.cont_aces_btn_alt_user.setMinimumSize(QSize(80, 50))
        self.cont_aces_btn_alt_user.setMaximumSize(QSize(80, 50))
        self.cont_aces_btn_alt_user.setFont(font1)
        self.cont_aces_btn_alt_user.setCursor(QCursor(Qt.PointingHandCursor))
        self.cont_aces_btn_alt_user.setLayoutDirection(Qt.RightToLeft)
        self.cont_aces_btn_alt_user.setStyleSheet(u"#cont_aces_btn_alt_user{	\n"
"	background-color: rgb(218, 145, 0);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 5px; \n"
"    border-color: rgb(235, 153, 0);\n"
"    font: bold 14px;		\n"
"	text-align: center;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#cont_aces_btn_alt_user::hover {\n"
"    background-color: rgb(186, 121, 0);\n"
"    border-style: inset;\n"
"}\n"
"#cont_aces_btn_alt_user::pressed {\n"
"    background-color: rgb(186, 121, 0);\n"
"    border-style: inset;\n"
"}")
        icon16 = QIcon()
        icon16.addFile(u":/assets.icons_alt_regras/usu\u00e1rio-alterar-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.cont_aces_btn_alt_user.setIcon(icon16)
        self.cont_aces_btn_alt_user.setIconSize(QSize(40, 40))

        self.gridLayout_7.addWidget(self.cont_aces_btn_alt_user, 0, 2, 1, 1)

        self.cont_aces_lb_user_resp = QLabel(self.widget_13)
        self.cont_aces_lb_user_resp.setObjectName(u"cont_aces_lb_user_resp")
        self.cont_aces_lb_user_resp.setMinimumSize(QSize(0, 39))
        self.cont_aces_lb_user_resp.setMaximumSize(QSize(16777215, 100))
        self.cont_aces_lb_user_resp.setStyleSheet(u"border: 0px;")
        self.cont_aces_lb_user_resp.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.cont_aces_lb_user_resp.setWordWrap(False)

        self.gridLayout_7.addWidget(self.cont_aces_lb_user_resp, 0, 0, 1, 1)

        self.cont_aces_btn_exc_user = QPushButton(self.widget_13)
        self.cont_aces_btn_exc_user.setObjectName(u"cont_aces_btn_exc_user")
        sizePolicy3.setHeightForWidth(self.cont_aces_btn_exc_user.sizePolicy().hasHeightForWidth())
        self.cont_aces_btn_exc_user.setSizePolicy(sizePolicy3)
        self.cont_aces_btn_exc_user.setMinimumSize(QSize(80, 50))
        self.cont_aces_btn_exc_user.setMaximumSize(QSize(80, 50))
        self.cont_aces_btn_exc_user.setFont(font1)
        self.cont_aces_btn_exc_user.setCursor(QCursor(Qt.PointingHandCursor))
        self.cont_aces_btn_exc_user.setLayoutDirection(Qt.RightToLeft)
        self.cont_aces_btn_exc_user.setStyleSheet(u"#cont_aces_btn_exc_user{	\n"
"	background-color: rgb(204, 0, 0);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 5px; \n"
"    border-color: rgb(227, 0, 0);\n"
"    font: bold 14px;		\n"
"	text-align: center;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#cont_aces_btn_exc_user::hover {\n"
"    background-color: rgb(165, 0, 0);\n"
"    border-style: inset;\n"
"}\n"
"#cont_aces_btn_exc_user::pressed {\n"
"    background-color: rgb(165, 0, 0);\n"
"    border-style: inset;\n"
"}")
        icon17 = QIcon()
        icon17.addFile(u":/assets.icons_alt_regras/icons8-usu\u00e1rio-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.cont_aces_btn_exc_user.setIcon(icon17)
        self.cont_aces_btn_exc_user.setIconSize(QSize(40, 40))

        self.gridLayout_7.addWidget(self.cont_aces_btn_exc_user, 0, 3, 1, 1)


        self.gridLayout_5.addWidget(self.widget_13, 0, 0, 1, 1, Qt.AlignTop)


        self.verticalLayout_13.addWidget(self.widget_12, 0, Qt.AlignTop)

        self.label_22 = QLabel(self.qw_dados_com_2)
        self.label_22.setObjectName(u"label_22")
        sizePolicy4.setHeightForWidth(self.label_22.sizePolicy().hasHeightForWidth())
        self.label_22.setSizePolicy(sizePolicy4)
        self.label_22.setMinimumSize(QSize(0, 30))
        self.label_22.setMaximumSize(QSize(16777215, 30))
        self.label_22.setStyleSheet(u"QLabel{	\n"
"	background-color: rgb(180, 180, 180);\n"
"    border-style: outset;\n"
"    border-width: 3px;\n"
"   /* border-radius: 5px;*/\n"
"    border-color: rgb(234, 234, 234);\n"
"    font: bold 12px;\n"
"\n"
"}")
        self.label_22.setAlignment(Qt.AlignCenter)
        self.label_22.setWordWrap(False)

        self.verticalLayout_13.addWidget(self.label_22)


        self.verticalLayout_9.addWidget(self.qw_dados_com_2, 0, Qt.AlignTop)

        self.cont_aces_tb_usuarios = QTableWidget(self.scrollAreaWidgetContents_2)
        if (self.cont_aces_tb_usuarios.columnCount() < 5):
            self.cont_aces_tb_usuarios.setColumnCount(5)
        __qtablewidgetitem79 = QTableWidgetItem()
        self.cont_aces_tb_usuarios.setHorizontalHeaderItem(0, __qtablewidgetitem79)
        __qtablewidgetitem80 = QTableWidgetItem()
        self.cont_aces_tb_usuarios.setHorizontalHeaderItem(1, __qtablewidgetitem80)
        __qtablewidgetitem81 = QTableWidgetItem()
        self.cont_aces_tb_usuarios.setHorizontalHeaderItem(2, __qtablewidgetitem81)
        __qtablewidgetitem82 = QTableWidgetItem()
        self.cont_aces_tb_usuarios.setHorizontalHeaderItem(3, __qtablewidgetitem82)
        __qtablewidgetitem83 = QTableWidgetItem()
        self.cont_aces_tb_usuarios.setHorizontalHeaderItem(4, __qtablewidgetitem83)
        self.cont_aces_tb_usuarios.setObjectName(u"cont_aces_tb_usuarios")
        sizePolicy3.setHeightForWidth(self.cont_aces_tb_usuarios.sizePolicy().hasHeightForWidth())
        self.cont_aces_tb_usuarios.setSizePolicy(sizePolicy3)
        self.cont_aces_tb_usuarios.setMinimumSize(QSize(0, 0))
        self.cont_aces_tb_usuarios.setMaximumSize(QSize(16777215, 16777215))
        self.cont_aces_tb_usuarios.setStyleSheet(u"")
        self.cont_aces_tb_usuarios.setFrameShape(QFrame.StyledPanel)
        self.cont_aces_tb_usuarios.setFrameShadow(QFrame.Sunken)
        self.cont_aces_tb_usuarios.setLineWidth(1)
        self.cont_aces_tb_usuarios.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.cont_aces_tb_usuarios.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.cont_aces_tb_usuarios.setAutoScroll(True)
        self.cont_aces_tb_usuarios.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.cont_aces_tb_usuarios.setProperty("showDropIndicator", True)
        self.cont_aces_tb_usuarios.setDragEnabled(False)
        self.cont_aces_tb_usuarios.setAlternatingRowColors(True)
        self.cont_aces_tb_usuarios.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.cont_aces_tb_usuarios.setTextElideMode(Qt.ElideRight)
        self.cont_aces_tb_usuarios.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.cont_aces_tb_usuarios.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.cont_aces_tb_usuarios.setShowGrid(True)
        self.cont_aces_tb_usuarios.setGridStyle(Qt.SolidLine)
        self.cont_aces_tb_usuarios.setSortingEnabled(False)
        self.cont_aces_tb_usuarios.setWordWrap(True)
        self.cont_aces_tb_usuarios.setCornerButtonEnabled(True)
        self.cont_aces_tb_usuarios.setRowCount(0)
        self.cont_aces_tb_usuarios.setColumnCount(5)
        self.cont_aces_tb_usuarios.horizontalHeader().setVisible(True)
        self.cont_aces_tb_usuarios.horizontalHeader().setCascadingSectionResizes(False)
        self.cont_aces_tb_usuarios.horizontalHeader().setMinimumSectionSize(42)
        self.cont_aces_tb_usuarios.horizontalHeader().setDefaultSectionSize(120)
        self.cont_aces_tb_usuarios.horizontalHeader().setHighlightSections(True)
        self.cont_aces_tb_usuarios.horizontalHeader().setProperty("showSortIndicator", False)
        self.cont_aces_tb_usuarios.horizontalHeader().setStretchLastSection(True)
        self.cont_aces_tb_usuarios.verticalHeader().setCascadingSectionResizes(True)
        self.cont_aces_tb_usuarios.verticalHeader().setDefaultSectionSize(30)
        self.cont_aces_tb_usuarios.verticalHeader().setHighlightSections(True)
        self.cont_aces_tb_usuarios.verticalHeader().setProperty("showSortIndicator", False)
        self.cont_aces_tb_usuarios.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_9.addWidget(self.cont_aces_tb_usuarios)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.horizontalLayout_3.addWidget(self.scrollArea_2)

        self.pgs_principal.addWidget(self.pg_controle_acesso)

        self.verticalLayout_78.addWidget(self.pgs_principal)


        self.verticalLayout_2.addWidget(self.frame_6)


        self.gridLayout_20.addWidget(self.frame_2, 0, 1, 1, 1)

        self.prog_bar_pos = QProgressBar(self.centralwidget)
        self.prog_bar_pos.setObjectName(u"prog_bar_pos")
        font2 = QFont()
        font2.setBold(True)
        font2.setItalic(False)
        font2.setStyleStrategy(QFont.PreferDefault)
        self.prog_bar_pos.setFont(font2)
        self.prog_bar_pos.setCursor(QCursor(Qt.WaitCursor))
        self.prog_bar_pos.setFocusPolicy(Qt.NoFocus)
        self.prog_bar_pos.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.prog_bar_pos.setStyleSheet(u"border-style: ridge ;\n"
"background-color: rgb(255, 255, 255);\n"
"border-width: 4px;\n"
"border-radius: 5px;\n"
"border-color: rgb(200, 200, 200);\n"
"font: bold 18px;\n"
"color: rgb(0, 0, 0);")
        self.prog_bar_pos.setInputMethodHints(Qt.ImhNone)
        self.prog_bar_pos.setMaximum(500)
        self.prog_bar_pos.setValue(462)
        self.prog_bar_pos.setAlignment(Qt.AlignCenter)
        self.prog_bar_pos.setTextDirection(QProgressBar.TopToBottom)

        self.gridLayout_20.addWidget(self.prog_bar_pos, 1, 1, 1, 1)

        MainGerenciadorAlmox.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.alt_loc_txt_mat, self.alt_loc_txt_cen)
        QWidget.setTabOrder(self.alt_loc_txt_cen, self.alt_loc_txt_dep)
        QWidget.setTabOrder(self.alt_loc_txt_dep, self.alt_loc_txt_pos_local)
        QWidget.setTabOrder(self.alt_loc_txt_pos_local, self.alt_loc_chcb_alt_massiva)
        QWidget.setTabOrder(self.alt_loc_chcb_alt_massiva, self.alt_loc_btn_alt_dados)
        QWidget.setTabOrder(self.alt_loc_btn_alt_dados, self.alt_loc_btn_incluir)
        QWidget.setTabOrder(self.alt_loc_btn_incluir, self.alt_loc_btn_excluir_linha)
        QWidget.setTabOrder(self.alt_loc_btn_excluir_linha, self.alt_loc_btn_limpar_dados)
        QWidget.setTabOrder(self.alt_loc_btn_limpar_dados, self.alt_loc_btn_imp_excel)
        QWidget.setTabOrder(self.alt_loc_btn_imp_excel, self.alt_loc_btn_exp_excel)
        QWidget.setTabOrder(self.alt_loc_btn_exp_excel, self.scrollArea)

        self.retranslateUi(MainGerenciadorAlmox)
        self.btn_home.toggled.connect(self.qf_home.setVisible)

        self.pgs_principal.setCurrentIndex(4)


        QMetaObject.connectSlotsByName(MainGerenciadorAlmox)
    # setupUi

    def retranslateUi(self, MainGerenciadorAlmox):
        MainGerenciadorAlmox.setWindowTitle(QCoreApplication.translate("MainGerenciadorAlmox", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate("MainGerenciadorAlmox", u"HOME", None))
        self.home_btn_alt_local.setText(QCoreApplication.translate("MainGerenciadorAlmox", u"ALTERAR POSI\u00c7\u00c3O DEP\u00d3SITO", None))
        self.home_btn_cont_entrada_almox.setText(QCoreApplication.translate("MainGerenciadorAlmox", u"CONTROLE ENTRADA ALMOX", None))
        self.home_btn_nao_atendidos.setText(QCoreApplication.translate("MainGerenciadorAlmox", u"MONITOR N\u00c3O ATENDIDOS", None))
        self.home_btn_recebimento.setText(QCoreApplication.translate("MainGerenciadorAlmox", u"MONITOR RECEBIMENTO", None))
        self.home_btn_cont_acesso.setText(QCoreApplication.translate("MainGerenciadorAlmox", u"CONTROLE ACESSO APP", None))
#if QT_CONFIG(tooltip)
        self.home_btn_config.setToolTip(QCoreApplication.translate("MainGerenciadorAlmox", u"<html><head/><body><p>Alterar Configura\u00e7\u00f5es</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.home_btn_config.setText("")
        self.btn_home.setText("")
        self.lb_logo.setText("")
        self.lb_titulo.setText(QCoreApplication.translate("MainGerenciadorAlmox", u"Altera\u00e7\u00e3o Localiza\u00e7\u00e3o", None))
        self.alt_loc_lb_dados_user.setText(QCoreApplication.translate("MainGerenciadorAlmox", u"Usu\u00e1rio: Marcos Henrique Nack Camargo\n"
"Centro: 1001", None))
        self.label_19.setText(QCoreApplication.translate("MainGerenciadorAlmox", u"Dados Altera\u00e7\u00e3o", None))
#if QT_CONFIG(tooltip)
        self.alt_loc_btn_exp_excel.setToolTip(QCoreApplication.translate("MainGerenciadorAlmox", u"<html><head/><body><p>Exportar Excel <span style=\" color:#e30000;\">(Ctrl+Alt+e)</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.alt_loc_btn_exp_excel.setText("")
#if QT_CONFIG(tooltip)
        self.alt_loc_btn_imp_excel.setToolTip(QCoreApplication.translate("MainGerenciadorAlmox", u"<html><head/><body><p>Importar Excel<span style=\" color:#e30000;\"> (Ctrl+e)</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.alt_loc_btn_imp_excel.setText("")
#if QT_CONFIG(tooltip)
        self.alt_loc_btn_excluir_linha.setToolTip(QCoreApplication.translate("MainGerenciadorAlmox", u"<html><head/><body><p>Excluir Linha <span style=\" color:#e30000;\">(Ctrl+-)</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.alt_loc_btn_excluir_linha.setText("")
#if QT_CONFIG(tooltip)
        self.alt_loc_btn_limpar_dados.setToolTip(QCoreApplication.translate("MainGerenciadorAlmox", u"<html><head/><body><p>Limpar Lista Materiais <span style=\" color:#e30000;\">(Ctrl+del)</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.alt_loc_btn_limpar_dados.setText("")
        self.label_7.setText(QCoreApplication.translate("MainGerenciadorAlmox", u"Centro", None))
        self.label_12.setText(QCoreApplication.translate("MainGerenciadorAlmox", u"Dep\u00f3sito", None))
        self.label_4.setText(QCoreApplication.translate("MainGerenciadorAlmox", u"Material", None))
        self.label_10.setText(QCoreApplication.translate("MainGerenciadorAlmox", u"Posi\u00e7\u00e3o Deposito", None))
#if QT_CONFIG(tooltip)
        self.alt_loc_btn_alt_dados.setToolTip(QCoreApplication.translate("MainGerenciadorAlmox", u"<html><head/><body><p>Alterar Dados SAP</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.alt_loc_btn_alt_dados.setText("")
#if QT_CONFIG(tooltip)
        self.alt_loc_btn_incluir.setToolTip(QCoreApplication.translate("MainGerenciadorAlmox", u"<html><head/><body><p>Incluir Item Altera\u00e7\u00e3o Massiva</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.alt_loc_btn_incluir.setWhatsThis(QCoreApplication.translate("MainGerenciadorAlmox", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.alt_loc_btn_incluir.setText("")
        self.alt_loc_chcb_alt_massiva.setText(QCoreApplication.translate("MainGerenciadorAlmox", u"ALTERA\u00c7\u00c3O MASSIVA", None))
        self.label_20.setText(QCoreApplication.translate("MainGerenciadorAlmox", u"Lista Materiais", None))
        ___qtablewidgetitem = self.alt_loc_tb_alt_massa.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainGerenciadorAlmox", u"Material", None));
        ___qtablewidgetitem1 = self.alt_loc_tb_alt_massa.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainGerenciadorAlmox", u"Centro", None));
        ___qtablewidgetitem2 = self.alt_loc_tb_alt_massa.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainGerenciadorAlmox", u"Dep\u00f3sito", None));
        ___qtablewidgetitem3 = self.alt_loc_tb_alt_massa.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainGerenciadorAlmox", u"Nova Localiza\u00e7\u00e3o", None));
        ___qtablewidgetitem4 = self.alt_loc_tb_alt_massa.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainGerenciadorAlmox", u"Status", None));
        ___qtablewidgetitem5 = self.alt_loc_tb_alt_massa.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainGerenciadorAlmox", u"Local Antigo", None));
        ___qtablewidgetitem6 = self.alt_loc_tb_alt_massa.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainGerenciadorAlmox", u"MsgErro", None));
        self.cont_ent_almox_lb_dec_cen_mes.setText(QCoreApplication.translate("MainGerenciadorAlmox", u"CENTRO 1001 - ARAUC\u00c1RIA - CONTROLE DE MATERIAL N\u00c3O ATENDIDO - NOVEMBRO/2023", None))
        self.label_36.setText(QCoreApplication.translate("MainGerenciadorAlmox", u"Material", None))
        self.nao_atend_cmb_acao_plan_2.setItemText(0, "")
        self.nao_atend_cmb_acao_plan_2.setItemText(1, QCoreApplication.translate("MainGerenciadorAlmox", u"OK", None))
        self.nao_atend_cmb_acao_plan_2.setItemText(2, QCoreApplication.translate("MainGerenciadorAlmox", u"Pendente", None))

        self.label_37.setText(QCoreApplication.translate("MainGerenciadorAlmox", u"Consulta N\u00e3o Atendido", None))
        self.label_38.setText(QCoreApplication.translate("MainGerenciadorAlmox", u"A\u00e7\u00e3o Plan.", None))
        self.label_39.setText(QCoreApplication.translate("MainGerenciadorAlmox", u"Ano/M\u00eas", None))
        self.nao_atend_cmb_ano_mes_2.setItemText(0, "")

        self.nao_atend_txt_material_2.setText("")
        self.label_40.setText(QCoreApplication.translate("MainGerenciadorAlmox", u"C\u00f3d. Sit.", None))
        self.nao_atend_cmb_cod_sit_2.setItemText(0, "")
        self.nao_atend_cmb_cod_sit_2.setItemText(1, QCoreApplication.translate("MainGerenciadorAlmox", u"AI - Armazenado Incorretamente", None))
        self.nao_atend_cmb_cod_sit_2.setItemText(2, QCoreApplication.translate("MainGerenciadorAlmox", u"DD - Outros", None))
        self.nao_atend_cmb_cod_sit_2.setItemText(3, QCoreApplication.translate("MainGerenciadorAlmox", u"EI - Entrega Incorreta Fornecedor", None))
        self.nao_atend_cmb_cod_sit_2.setItemText(4, QCoreApplication.translate("MainGerenciadorAlmox", u"FE - Furo de Estoque", None))
        self.nao_atend_cmb_cod_sit_2.setItemText(5, QCoreApplication.translate("MainGerenciadorAlmox", u"FN - Falta Entrada Nota Fiscal", None))
        self.nao_atend_cmb_cod_sit_2.setItemText(6, QCoreApplication.translate("MainGerenciadorAlmox", u"IO - Material Obsoleto", None))
        self.nao_atend_cmb_cod_sit_2.setItemText(7, QCoreApplication.translate("MainGerenciadorAlmox", u"IR - Material Reservado", None))
        self.nao_atend_cmb_cod_sit_2.setItemText(8, QCoreApplication.translate("MainGerenciadorAlmox", u"MC - Material de Conserto", None))
        self.nao_atend_cmb_cod_sit_2.setItemText(9, QCoreApplication.translate("MainGerenciadorAlmox", u"MR - Movimentado Recentemente", None))
        self.nao_atend_cmb_cod_sit_2.setItemText(10, QCoreApplication.translate("MainGerenciadorAlmox", u"NA - N\u00e3o Armazenado", None))
        self.nao_atend_cmb_cod_sit_2.setItemText(11, QCoreApplication.translate("MainGerenciadorAlmox", u"NS - N\u00e3o Subiu para o SAP", None))
        self.nao_atend_cmb_cod_sit_2.setItemText(12, QCoreApplication.translate("MainGerenciadorAlmox", u"ND - Material ND", None))
        self.nao_atend_cmb_cod_sit_2.setItemText(13, QCoreApplication.translate("MainGerenciadorAlmox", u"OM - Outro Material", None))
        self.nao_atend_cmb_cod_sit_2.setItemText(14, QCoreApplication.translate("MainGerenciadorAlmox", u"OC - Material de Outro Centro", None))
        self.nao_atend_cmb_cod_sit_2.setItemText(15, QCoreApplication.translate("MainGerenciadorAlmox", u"PP - Pedido Pendente", None))
        self.nao_atend_cmb_cod_sit_2.setItemText(16, QCoreApplication.translate("MainGerenciadorAlmox", u"RP - RC Pendente", None))
        self.nao_atend_cmb_cod_sit_2.setItemText(17, QCoreApplication.translate("MainGerenciadorAlmox", u"SR - Sem Reposi\u00e7\u00e3o", None))
        self.nao_atend_cmb_cod_sit_2.setItemText(18, QCoreApplication.translate("MainGerenciadorAlmox", u"SP - Sem Padroniza\u00e7\u00e3o", None))

#if QT_CONFIG(tooltip)
        self.cont_ent_almox_btn_alt_regist.setToolTip(QCoreApplication.translate("MainGerenciadorAlmox", u"<html><head/><body><p>Alterar Registro</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.cont_ent_almox_btn_alt_regist.setText("")
#if QT_CONFIG(tooltip)
        self.cont_ent_almox_btn_inc_regist.setToolTip(QCoreApplication.translate("MainGerenciadorAlmox", u"<html><head/><body><p>Adicionar Registro</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.cont_ent_almox_btn_inc_regist.setText("")
#if QT_CONFIG(tooltip)
        self.cont_ent_almox_btn_pesquisar.setToolTip(QCoreApplication.translate("MainGerenciadorAlmox", u"<html><head/><body><p>Pesquisar</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.cont_ent_almox_btn_pesquisar.setText("")
        self.nao_atend_lb_itens_na_2.setText("")
        self.nao_atend_lb_total_ocor_2.setText("")
        self.label_34.setText(QCoreApplication.translate("MainGerenciadorAlmox", u"Tempo M\u00e9dio", None))
        self.label_35.setText(QCoreApplication.translate("MainGerenciadorAlmox", u"DATA", None))
        self.label_41.setText(QCoreApplication.translate("MainGerenciadorAlmox", u"Lista N\u00e3o Atendidos", None))
        ___qtablewidgetitem7 = self.cont_ent_almox_tb_entradas.horizontalHeaderItem(0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainGerenciadorAlmox", u"ID", None));
        ___qtablewidgetitem8 = self.cont_ent_almox_tb_entradas.horizontalHeaderItem(1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainGerenciadorAlmox", u"Data", None));
        ___qtablewidgetitem9 = self.cont_ent_almox_tb_entradas.horizontalHeaderItem(2)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainGerenciadorAlmox", u"Hora", None));
        ___qtablewidgetitem10 = self.cont_ent_almox_tb_entradas.horizontalHeaderItem(3)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainGerenciadorAlmox", u"C\u00f3digo Mat.", None));
        ___qtablewidgetitem11 = self.cont_ent_almox_tb_entradas.horizontalHeaderItem(4)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainGerenciadorAlmox", u"Descri\u00e7\u00e3o", None));
        ___qtablewidgetitem12 = self.cont_ent_almox_tb_entradas.horizontalHeaderItem(5)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainGerenciadorAlmox", u"Un.Med.", None));
        ___qtablewidgetitem13 = self.cont_ent_almox_tb_entradas.horizontalHeaderItem(6)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainGerenciadorAlmox", u"Solicitante", None));
        ___qtablewidgetitem14 = self.cont_ent_almox_tb_entradas.horizontalHeaderItem(7)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainGerenciadorAlmox", u"Ramal", None));
        ___qtablewidgetitem15 = self.cont_ent_almox_tb_entradas.horizontalHeaderItem(8)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainGerenciadorAlmox", u"Setor", None));
        ___qtablewidgetitem16 = self.cont_ent_almox_tb_entradas.horizontalHeaderItem(9)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainGerenciadorAlmox", u"Observa\u00e7\u00e3o do Almoxarife", None));
        ___qtablewidgetitem17 = self.cont_ent_almox_tb_entradas.horizontalHeaderItem(10)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainGerenciadorAlmox", u"Qt. Solic.", None));
        ___qtablewidgetitem18 = self.cont_ent_almox_tb_entradas.horizontalHeaderItem(11)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainGerenciadorAlmox", u"M\u00ednimo", None));
        ___qtablewidgetitem19 = self.cont_ent_almox_tb_entradas.horizontalHeaderItem(12)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainGerenciadorAlmox", u"M\u00e1ximo", None));
        ___qtablewidgetitem20 = self.cont_ent_almox_tb_entradas.horizontalHeaderItem(13)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainGerenciadorAlmox", u"Tp.MPR", None));
        ___qtablewidgetitem21 = self.cont_ent_almox_tb_entradas.horizontalHeaderItem(14)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainGerenciadorAlmox", u"Planejador", None));
        ___qtablewidgetitem22 = self.cont_ent_almox_tb_entradas.horizontalHeaderItem(15)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainGerenciadorAlmox", u"Cr\u00edtico", None));
        ___qtablewidgetitem23 = self.cont_ent_almox_tb_entradas.horizontalHeaderItem(16)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainGerenciadorAlmox", u"Cons./FINT", None));
        ___qtablewidgetitem24 = self.cont_ent_almox_tb_entradas.horizontalHeaderItem(17)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainGerenciadorAlmox", u"Status ERP", None));
        ___qtablewidgetitem25 = self.cont_ent_almox_tb_entradas.horizontalHeaderItem(18)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainGerenciadorAlmox", u"Saldo Sist.", None));
        ___qtablewidgetitem26 = self.cont_ent_almox_tb_entradas.horizontalHeaderItem(19)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainGerenciadorAlmox", u"Saldo F\u00edsico", None));
        ___qtablewidgetitem27 = self.cont_ent_almox_tb_entradas.horizontalHeaderItem(20)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainGerenciadorAlmox", u"2\u00aa Cont.", None));
        ___qtablewidgetitem28 = self.cont_ent_almox_tb_entradas.horizontalHeaderItem(21)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainGerenciadorAlmox", u"Bloqueado", None));
        ___qtablewidgetitem29 = self.cont_ent_almox_tb_entradas.horizontalHeaderItem(22)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainGerenciadorAlmox", u"Req. Man.", None));
        ___qtablewidgetitem30 = self.cont_ent_almox_tb_entradas.horizontalHeaderItem(23)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainGerenciadorAlmox", u"Diverg.", None));
        ___qtablewidgetitem31 = self.cont_ent_almox_tb_entradas.horizontalHeaderItem(24)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainGerenciadorAlmox", u"N\u00ba. Proc. Comp.", None));
        ___qtablewidgetitem32 = self.cont_ent_almox_tb_entradas.horizontalHeaderItem(25)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainGerenciadorAlmox", u"Valor Unit", None));
        ___qtablewidgetitem33 = self.cont_ent_almox_tb_entradas.horizontalHeaderItem(26)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainGerenciadorAlmox", u"C\u00f3d. Sit.", None));
        ___qtablewidgetitem34 = self.cont_ent_almox_tb_entradas.horizontalHeaderItem(27)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainGerenciadorAlmox", u"Sit. Pedido", None));
        ___qtablewidgetitem35 = self.cont_ent_almox_tb_entradas.horizontalHeaderItem(28)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainGerenciadorAlmox", u"Nota Mat.", None));
        ___qtablewidgetitem36 = self.cont_ent_almox_tb_entradas.horizontalHeaderItem(29)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainGerenciadorAlmox", u"Situa\u00e7\u00e3o Processo Compras", None));
        ___qtablewidgetitem37 = self.cont_ent_almox_tb_entradas.horizontalHeaderItem(30)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainGerenciadorAlmox", u"Usu\u00e1rio", None));
        ___qtablewidgetitem38 = self.cont_ent_almox_tb_entradas.horizontalHeaderItem(31)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainGerenciadorAlmox", u"Data Registro", None));
        ___qtablewidgetitem39 = self.cont_ent_almox_tb_entradas.horizontalHeaderItem(32)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("MainGerenciadorAlmox", u"EMAIL", None));
        self.nao_atend_lb_dec_cen_mes.setText(QCoreApplication.translate("MainGerenciadorAlmox", u"CENTRO 1001 - ARAUC\u00c1RIA - CONTROLE DE MATERIAL N\u00c3O ATENDIDO - NOVEMBRO/2023", None))
        self.nao_atend_cmb_email.setItemText(0, "")
        self.nao_atend_cmb_email.setItemText(1, QCoreApplication.translate("MainGerenciadorAlmox", u"Enviado", None))
        self.nao_atend_cmb_email.setItemText(2, QCoreApplication.translate("MainGerenciadorAlmox", u"Pendente", None))

        self.nao_atend_cmb_acao_plan.setItemText(0, "")
        self.nao_atend_cmb_acao_plan.setItemText(1, QCoreApplication.translate("MainGerenciadorAlmox", u"OK", None))
        self.nao_atend_cmb_acao_plan.setItemText(2, QCoreApplication.translate("MainGerenciadorAlmox", u"Pendente", None))

        self.label_33.setText(QCoreApplication.translate("MainGerenciadorAlmox", u"E-mail", None))
        self.nao_atend_txt_material.setText("")
        self.nao_atend_cmb_ano_mes.setItemText(0, "")

        self.label_27.setText(QCoreApplication.translate("MainGerenciadorAlmox", u"Consulta N\u00e3o Atendido", None))
        self.label_31.setText(QCoreApplication.translate("MainGerenciadorAlmox", u"A\u00e7\u00e3o Plan.", None))
        self.label_32.setText(QCoreApplication.translate("MainGerenciadorAlmox", u"Material", None))
        self.label_30.setText(QCoreApplication.translate("MainGerenciadorAlmox", u"Ano/M\u00eas", None))
#if QT_CONFIG(tooltip)
        self.nao_atend_btn_pesquisar.setToolTip(QCoreApplication.translate("MainGerenciadorAlmox", u"<html><head/><body><p>Pesquisar</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.nao_atend_btn_pesquisar.setText("")
        self.nao_atend_lb_itens_na.setText("")
        self.nao_atend_lb_total_ocor.setText("")
        self.label_29.setText(QCoreApplication.translate("MainGerenciadorAlmox", u" Total Itens N\u00e3o Atendidos: ", None))
        self.label_25.setText(QCoreApplication.translate("MainGerenciadorAlmox", u"Total de Ocorr\u00eancias:", None))
        self.label_26.setText(QCoreApplication.translate("MainGerenciadorAlmox", u"NA - M\u00caS ANTERIOR", None))
        self.nao_atend_lb_na_mes_ant.setText("")
#if QT_CONFIG(tooltip)
        self.nao_atend_btn_alt_regist.setToolTip(QCoreApplication.translate("MainGerenciadorAlmox", u"<html><head/><body><p>Alterar Registro</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.nao_atend_btn_alt_regist.setText("")
#if QT_CONFIG(tooltip)
        self.nao_atend_btn_inc_regist.setToolTip(QCoreApplication.translate("MainGerenciadorAlmox", u"<html><head/><body><p>Adicionar Registro</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.nao_atend_btn_inc_regist.setText("")
#if QT_CONFIG(tooltip)
        self.nao_atend_btn_visualizar.setToolTip(QCoreApplication.translate("MainGerenciadorAlmox", u"<html><head/><body><p>Visualizar</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.nao_atend_btn_visualizar.setText("")
#if QT_CONFIG(tooltip)
        self.nao_atend_btn_historico.setToolTip(QCoreApplication.translate("MainGerenciadorAlmox", u"<html><head/><body><p>Hist\u00f3rico</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.nao_atend_btn_historico.setText("")
#if QT_CONFIG(tooltip)
        self.nao_atend_btn_excluir.setToolTip(QCoreApplication.translate("MainGerenciadorAlmox", u"<html><head/><body><p>Eliminar Registro</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.nao_atend_btn_excluir.setText("")
#if QT_CONFIG(tooltip)
        self.nao_atend_btn_enviar_email.setToolTip(QCoreApplication.translate("MainGerenciadorAlmox", u"<html><head/><body><p>Enviar e-mail</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.nao_atend_btn_enviar_email.setText("")
        self.label_24.setText(QCoreApplication.translate("MainGerenciadorAlmox", u"Lista N\u00e3o Atendidos", None))
        ___qtablewidgetitem40 = self.nao_atend_tb_registros.horizontalHeaderItem(0)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("MainGerenciadorAlmox", u"ID", None));
        ___qtablewidgetitem41 = self.nao_atend_tb_registros.horizontalHeaderItem(1)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("MainGerenciadorAlmox", u"Data", None));
        ___qtablewidgetitem42 = self.nao_atend_tb_registros.horizontalHeaderItem(2)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("MainGerenciadorAlmox", u"Hora", None));
        ___qtablewidgetitem43 = self.nao_atend_tb_registros.horizontalHeaderItem(3)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("MainGerenciadorAlmox", u"C\u00f3digo Mat.", None));
        ___qtablewidgetitem44 = self.nao_atend_tb_registros.horizontalHeaderItem(4)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("MainGerenciadorAlmox", u"Descri\u00e7\u00e3o", None));
        ___qtablewidgetitem45 = self.nao_atend_tb_registros.horizontalHeaderItem(5)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("MainGerenciadorAlmox", u"Un.Med.", None));
        ___qtablewidgetitem46 = self.nao_atend_tb_registros.horizontalHeaderItem(6)
        ___qtablewidgetitem46.setText(QCoreApplication.translate("MainGerenciadorAlmox", u"Solicitante", None));
        ___qtablewidgetitem47 = self.nao_atend_tb_registros.horizontalHeaderItem(7)
        ___qtablewidgetitem47.setText(QCoreApplication.translate("MainGerenciadorAlmox", u"Ramal", None));
        ___qtablewidgetitem48 = self.nao_atend_tb_registros.horizontalHeaderItem(8)
        ___qtablewidgetitem48.setText(QCoreApplication.translate("MainGerenciadorAlmox", u"Setor", None));
        ___qtablewidgetitem49 = self.nao_atend_tb_registros.horizontalHeaderItem(9)
        ___qtablewidgetitem49.setText(QCoreApplication.translate("MainGerenciadorAlmox", u"Obs. Almox.", None));
        ___qtablewidgetitem50 = self.nao_atend_tb_registros.horizontalHeaderItem(10)
        ___qtablewidgetitem50.setText(QCoreApplication.translate("MainGerenciadorAlmox", u"Qt. Solic.", None));
        ___qtablewidgetitem51 = self.nao_atend_tb_registros.horizontalHeaderItem(11)
        ___qtablewidgetitem51.setText(QCoreApplication.translate("MainGerenciadorAlmox", u"Tp.MPR", None));
        ___qtablewidgetitem52 = self.nao_atend_tb_registros.horizontalHeaderItem(12)
        ___qtablewidgetitem52.setText(QCoreApplication.translate("MainGerenciadorAlmox", u"M\u00ednimo", None));
        ___qtablewidgetitem53 = self.nao_atend_tb_registros.horizontalHeaderItem(13)
        ___qtablewidgetitem53.setText(QCoreApplication.translate("MainGerenciadorAlmox", u"M\u00e1ximo", None));
        ___qtablewidgetitem54 = self.nao_atend_tb_registros.horizontalHeaderItem(14)
        ___qtablewidgetitem54.setText(QCoreApplication.translate("MainGerenciadorAlmox", u"Grp. Plan.", None));
        ___qtablewidgetitem55 = self.nao_atend_tb_registros.horizontalHeaderItem(15)
        ___qtablewidgetitem55.setText(QCoreApplication.translate("MainGerenciadorAlmox", u"Nome Plan.", None));
        ___qtablewidgetitem56 = self.nao_atend_tb_registros.horizontalHeaderItem(16)
        ___qtablewidgetitem56.setText(QCoreApplication.translate("MainGerenciadorAlmox", u"Cr\u00edtico", None));
        ___qtablewidgetitem57 = self.nao_atend_tb_registros.horizontalHeaderItem(17)
        ___qtablewidgetitem57.setText(QCoreApplication.translate("MainGerenciadorAlmox", u"Cons./FINT", None));
        ___qtablewidgetitem58 = self.nao_atend_tb_registros.horizontalHeaderItem(18)
        ___qtablewidgetitem58.setText(QCoreApplication.translate("MainGerenciadorAlmox", u"St. Geral", None));
        ___qtablewidgetitem59 = self.nao_atend_tb_registros.horizontalHeaderItem(19)
        ___qtablewidgetitem59.setText(QCoreApplication.translate("MainGerenciadorAlmox", u"St. Cen.", None));
        ___qtablewidgetitem60 = self.nao_atend_tb_registros.horizontalHeaderItem(20)
        ___qtablewidgetitem60.setText(QCoreApplication.translate("MainGerenciadorAlmox", u"Saldo Sist.", None));
        ___qtablewidgetitem61 = self.nao_atend_tb_registros.horizontalHeaderItem(21)
        ___qtablewidgetitem61.setText(QCoreApplication.translate("MainGerenciadorAlmox", u"Saldo F\u00edsico", None));
        ___qtablewidgetitem62 = self.nao_atend_tb_registros.horizontalHeaderItem(22)
        ___qtablewidgetitem62.setText(QCoreApplication.translate("MainGerenciadorAlmox", u"2\u00aa Cont.", None));
        ___qtablewidgetitem63 = self.nao_atend_tb_registros.horizontalHeaderItem(23)
        ___qtablewidgetitem63.setText(QCoreApplication.translate("MainGerenciadorAlmox", u"Bloqueado", None));
        ___qtablewidgetitem64 = self.nao_atend_tb_registros.horizontalHeaderItem(24)
        ___qtablewidgetitem64.setText(QCoreApplication.translate("MainGerenciadorAlmox", u"Req. Man.", None));
        ___qtablewidgetitem65 = self.nao_atend_tb_registros.horizontalHeaderItem(25)
        ___qtablewidgetitem65.setText(QCoreApplication.translate("MainGerenciadorAlmox", u"Diverg.", None));
        ___qtablewidgetitem66 = self.nao_atend_tb_registros.horizontalHeaderItem(26)
        ___qtablewidgetitem66.setText(QCoreApplication.translate("MainGerenciadorAlmox", u"N\u00ba. Proc. Comp.", None));
        ___qtablewidgetitem67 = self.nao_atend_tb_registros.horizontalHeaderItem(27)
        ___qtablewidgetitem67.setText(QCoreApplication.translate("MainGerenciadorAlmox", u"Valor Unit", None));
        ___qtablewidgetitem68 = self.nao_atend_tb_registros.horizontalHeaderItem(28)
        ___qtablewidgetitem68.setText(QCoreApplication.translate("MainGerenciadorAlmox", u"Grp. Comp.", None));
        ___qtablewidgetitem69 = self.nao_atend_tb_registros.horizontalHeaderItem(29)
        ___qtablewidgetitem69.setText(QCoreApplication.translate("MainGerenciadorAlmox", u"Comprador", None));
        ___qtablewidgetitem70 = self.nao_atend_tb_registros.horizontalHeaderItem(30)
        ___qtablewidgetitem70.setText(QCoreApplication.translate("MainGerenciadorAlmox", u"C\u00f3d. Sit.", None));
        ___qtablewidgetitem71 = self.nao_atend_tb_registros.horizontalHeaderItem(31)
        ___qtablewidgetitem71.setText(QCoreApplication.translate("MainGerenciadorAlmox", u"Sit. Pedido", None));
        ___qtablewidgetitem72 = self.nao_atend_tb_registros.horizontalHeaderItem(32)
        ___qtablewidgetitem72.setText(QCoreApplication.translate("MainGerenciadorAlmox", u"Nota Mat.", None));
        ___qtablewidgetitem73 = self.nao_atend_tb_registros.horizontalHeaderItem(33)
        ___qtablewidgetitem73.setText(QCoreApplication.translate("MainGerenciadorAlmox", u"Situa\u00e7\u00e3o Processo Compras", None));
        ___qtablewidgetitem74 = self.nao_atend_tb_registros.horizontalHeaderItem(34)
        ___qtablewidgetitem74.setText(QCoreApplication.translate("MainGerenciadorAlmox", u"A\u00e7\u00e3o Plan.", None));
        ___qtablewidgetitem75 = self.nao_atend_tb_registros.horizontalHeaderItem(35)
        ___qtablewidgetitem75.setText(QCoreApplication.translate("MainGerenciadorAlmox", u"Centro", None));
        ___qtablewidgetitem76 = self.nao_atend_tb_registros.horizontalHeaderItem(36)
        ___qtablewidgetitem76.setText(QCoreApplication.translate("MainGerenciadorAlmox", u"Usu\u00e1rio", None));
        ___qtablewidgetitem77 = self.nao_atend_tb_registros.horizontalHeaderItem(37)
        ___qtablewidgetitem77.setText(QCoreApplication.translate("MainGerenciadorAlmox", u"Data Registro", None));
        ___qtablewidgetitem78 = self.nao_atend_tb_registros.horizontalHeaderItem(38)
        ___qtablewidgetitem78.setText(QCoreApplication.translate("MainGerenciadorAlmox", u"EMAIL", None));
        self.lb_notificacao.setText("")
        self.label_21.setText(QCoreApplication.translate("MainGerenciadorAlmox", u"Dados Usu\u00e1rios Respons\u00e1vel", None))
#if QT_CONFIG(tooltip)
        self.cont_aces_btn_inc_user.setToolTip(QCoreApplication.translate("MainGerenciadorAlmox", u"<html><head/><body><p>Incluir Usu\u00e1rio</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.cont_aces_btn_inc_user.setText("")
#if QT_CONFIG(tooltip)
        self.cont_aces_btn_alt_user.setToolTip(QCoreApplication.translate("MainGerenciadorAlmox", u"<html><head/><body><p>Alterar Usu\u00e1rio</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.cont_aces_btn_alt_user.setText("")
        self.cont_aces_lb_user_resp.setText(QCoreApplication.translate("MainGerenciadorAlmox", u"Usu\u00e1rio: Marcos Henrique Nack Camargo\n"
"Centro: 1001", None))
#if QT_CONFIG(tooltip)
        self.cont_aces_btn_exc_user.setToolTip(QCoreApplication.translate("MainGerenciadorAlmox", u"<html><head/><body><p>Alterar Usu\u00e1rio</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.cont_aces_btn_exc_user.setText("")
        self.label_22.setText(QCoreApplication.translate("MainGerenciadorAlmox", u"Lista usu\u00e1rio", None))
        ___qtablewidgetitem79 = self.cont_aces_tb_usuarios.horizontalHeaderItem(0)
        ___qtablewidgetitem79.setText(QCoreApplication.translate("MainGerenciadorAlmox", u"ID", None));
        ___qtablewidgetitem80 = self.cont_aces_tb_usuarios.horizontalHeaderItem(1)
        ___qtablewidgetitem80.setText(QCoreApplication.translate("MainGerenciadorAlmox", u"Usu\u00e1rio", None));
        ___qtablewidgetitem81 = self.cont_aces_tb_usuarios.horizontalHeaderItem(2)
        ___qtablewidgetitem81.setText(QCoreApplication.translate("MainGerenciadorAlmox", u"Nome", None));
        ___qtablewidgetitem82 = self.cont_aces_tb_usuarios.horizontalHeaderItem(3)
        ___qtablewidgetitem82.setText(QCoreApplication.translate("MainGerenciadorAlmox", u"Centro", None));
        ___qtablewidgetitem83 = self.cont_aces_tb_usuarios.horizontalHeaderItem(4)
        ___qtablewidgetitem83.setText(QCoreApplication.translate("MainGerenciadorAlmox", u"Acesso", None));
    # retranslateUi

