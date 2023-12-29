# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ConfiguracaoInicial.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)
import assets.icons_alt_regras_rc

class Ui_ConfigurarInicial(object):
    def setupUi(self, ConfigurarInicial):
        if not ConfigurarInicial.objectName():
            ConfigurarInicial.setObjectName(u"ConfigurarInicial")
        ConfigurarInicial.resize(922, 240)
        ConfigurarInicial.setMinimumSize(QSize(922, 240))
        ConfigurarInicial.setMaximumSize(QSize(16777215, 16777215))
        ConfigurarInicial.setStyleSheet(u"QWidget{	\n"
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
        self.verticalLayout = QVBoxLayout(ConfigurarInicial)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(4, 4, 4, 4)
        self.frame_3 = QFrame(ConfigurarInicial)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(10, 10, 10, 20)
        self.frame = QFrame(self.frame_3)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QSize(890, 145))
        self.frame.setMaximumSize(QSize(890, 145))
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
        self.gridLayout.setHorizontalSpacing(2)
        self.gridLayout.setVerticalSpacing(1)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.btn_ajuda_email_login = QPushButton(self.frame)
        self.btn_ajuda_email_login.setObjectName(u"btn_ajuda_email_login")
        self.btn_ajuda_email_login.setMinimumSize(QSize(30, 30))
        self.btn_ajuda_email_login.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_ajuda_email_login.setLayoutDirection(Qt.RightToLeft)
        self.btn_ajuda_email_login.setStyleSheet(u"QPushButton{	\n"
"	background-color: rgb(225, 225, 225);\n"
"    border-style: ridge;\n"
"    border-width: 3px;\n"
" 	border-color: rgb(234, 234, 234);\n"
"    font: bold 12px;\n"
"}\n"
"")
        icon = QIcon()
        icon.addFile(u":/assets.icons_alt_regras/ajuda-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_ajuda_email_login.setIcon(icon)
        self.btn_ajuda_email_login.setIconSize(QSize(25, 25))
        self.btn_ajuda_email_login.setCheckable(True)

        self.gridLayout.addWidget(self.btn_ajuda_email_login, 1, 5, 1, 1, Qt.AlignRight)

        self.txt_email_login = QLineEdit(self.frame)
        self.txt_email_login.setObjectName(u"txt_email_login")
        self.txt_email_login.setMinimumSize(QSize(0, 35))
        self.txt_email_login.setMaximumSize(QSize(16777215, 35))

        self.gridLayout.addWidget(self.txt_email_login, 1, 1, 1, 4)

        self.btn_visivel = QPushButton(self.frame)
        self.btn_visivel.setObjectName(u"btn_visivel")
        self.btn_visivel.setMinimumSize(QSize(35, 35))
        self.btn_visivel.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_visivel.setLayoutDirection(Qt.RightToLeft)
        self.btn_visivel.setStyleSheet(u"QPushButton{	\n"
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
        icon1.addFile(u":/assets.icons_alt_regras/ocultar-60.png", QSize(), QIcon.Normal, QIcon.Off)
        icon1.addFile(u":/assets.icons_alt_regras/vis\u00edvel.png", QSize(), QIcon.Normal, QIcon.On)
        self.btn_visivel.setIcon(icon1)
        self.btn_visivel.setIconSize(QSize(20, 20))
        self.btn_visivel.setCheckable(True)

        self.gridLayout.addWidget(self.btn_visivel, 3, 2, 1, 1)

        self.label_9 = QLabel(self.frame)
        self.label_9.setObjectName(u"label_9")
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setMinimumSize(QSize(120, 35))
        self.label_9.setMaximumSize(QSize(120, 35))
        self.label_9.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_9, 1, 0, 1, 1)

        self.txt_email_envio = QLineEdit(self.frame)
        self.txt_email_envio.setObjectName(u"txt_email_envio")
        self.txt_email_envio.setMinimumSize(QSize(0, 35))
        self.txt_email_envio.setMaximumSize(QSize(16777215, 35))

        self.gridLayout.addWidget(self.txt_email_envio, 2, 1, 1, 4)

        self.txt_senha = QLineEdit(self.frame)
        self.txt_senha.setObjectName(u"txt_senha")
        self.txt_senha.setMinimumSize(QSize(0, 35))
        self.txt_senha.setMaximumSize(QSize(16777215, 35))
        self.txt_senha.setEchoMode(QLineEdit.Password)

        self.gridLayout.addWidget(self.txt_senha, 3, 1, 1, 1)

        self.label_11 = QLabel(self.frame)
        self.label_11.setObjectName(u"label_11")
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setMinimumSize(QSize(120, 35))
        self.label_11.setMaximumSize(QSize(120, 35))
        self.label_11.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_11, 3, 0, 1, 1)

        self.label_10 = QLabel(self.frame)
        self.label_10.setObjectName(u"label_10")
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setMinimumSize(QSize(120, 35))
        self.label_10.setMaximumSize(QSize(120, 35))
        self.label_10.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_10, 2, 0, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(41, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 3, 3, 1, 1)

        self.btn_ajuda_email_envio = QPushButton(self.frame)
        self.btn_ajuda_email_envio.setObjectName(u"btn_ajuda_email_envio")
        self.btn_ajuda_email_envio.setMinimumSize(QSize(30, 30))
        self.btn_ajuda_email_envio.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_ajuda_email_envio.setLayoutDirection(Qt.RightToLeft)
        self.btn_ajuda_email_envio.setStyleSheet(u"QPushButton{	\n"
"	background-color: rgb(225, 225, 225);\n"
"    border-style: ridge;\n"
"    border-width: 3px;\n"
" 	border-color: rgb(234, 234, 234);\n"
"    font: bold 12px;\n"
"\n"
"}\n"
"")
        self.btn_ajuda_email_envio.setIcon(icon)
        self.btn_ajuda_email_envio.setIconSize(QSize(25, 25))
        self.btn_ajuda_email_envio.setCheckable(True)

        self.gridLayout.addWidget(self.btn_ajuda_email_envio, 2, 5, 1, 1, Qt.AlignRight)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 5, 1, 1, 1)

        self.label_12 = QLabel(self.frame)
        self.label_12.setObjectName(u"label_12")
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        self.label_12.setMinimumSize(QSize(120, 35))
        self.label_12.setMaximumSize(QSize(120, 35))
        self.label_12.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_12, 4, 0, 1, 1)

        self.txt_porta = QLineEdit(self.frame)
        self.txt_porta.setObjectName(u"txt_porta")
        self.txt_porta.setMinimumSize(QSize(0, 35))
        self.txt_porta.setMaximumSize(QSize(16777215, 35))
        self.txt_porta.setEchoMode(QLineEdit.Normal)

        self.gridLayout.addWidget(self.txt_porta, 4, 1, 1, 1)


        self.gridLayout_2.addWidget(self.frame, 1, 0, 1, 1)

        self.frame_2 = QFrame(self.frame_3)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(890, 0))
        self.frame_2.setMaximumSize(QSize(890, 40))
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
        self.horizontalLayout.setSpacing(22)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(5, 0, 0, 10)
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 50))
        self.label.setStyleSheet(u"background-color: rgb(200, 200, 200);\n"
"\n"
"font: bold 12pt \"Segoe UI\";\n"
"border: 0px;")
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label.setWordWrap(True)

        self.horizontalLayout.addWidget(self.label, 0, Qt.AlignTop)

        self.btn_ok = QPushButton(self.frame_2)
        self.btn_ok.setObjectName(u"btn_ok")
        self.btn_ok.setMinimumSize(QSize(50, 40))
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
        icon2 = QIcon()
        icon2.addFile(u":/assets.icons_alt_regras/salvar-e-fechar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_ok.setIcon(icon2)
        self.btn_ok.setIconSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.btn_ok)

        self.btn_cancelar = QPushButton(self.frame_2)
        self.btn_cancelar.setObjectName(u"btn_cancelar")
        self.btn_cancelar.setMinimumSize(QSize(50, 40))
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
        icon3 = QIcon()
        icon3.addFile(u":/assets.icons_alt_regras/fechar-janela.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_cancelar.setIcon(icon3)
        self.btn_cancelar.setIconSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.btn_cancelar)


        self.gridLayout_2.addWidget(self.frame_2, 0, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 2, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 1, 1, 1, 1)


        self.verticalLayout.addWidget(self.frame_3)

        QWidget.setTabOrder(self.txt_email_login, self.txt_email_envio)
        QWidget.setTabOrder(self.txt_email_envio, self.txt_senha)
        QWidget.setTabOrder(self.txt_senha, self.btn_visivel)
        QWidget.setTabOrder(self.btn_visivel, self.btn_ok)
        QWidget.setTabOrder(self.btn_ok, self.btn_cancelar)
        QWidget.setTabOrder(self.btn_cancelar, self.btn_ajuda_email_login)
        QWidget.setTabOrder(self.btn_ajuda_email_login, self.btn_ajuda_email_envio)

        self.retranslateUi(ConfigurarInicial)

        QMetaObject.connectSlotsByName(ConfigurarInicial)
    # setupUi

    def retranslateUi(self, ConfigurarInicial):
        ConfigurarInicial.setWindowTitle(QCoreApplication.translate("ConfigurarInicial", u"Form", None))
#if QT_CONFIG(tooltip)
        self.btn_ajuda_email_login.setToolTip(QCoreApplication.translate("ConfigurarInicial", u"<html><head/><body><p>Informar o usu\u00e1rio rede + @berneck.com.br, ex: </p><p>xxx00000@berneck.com.br</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_ajuda_email_login.setText("")
        self.txt_email_login.setInputMask("")
        self.txt_email_login.setPlaceholderText(QCoreApplication.translate("ConfigurarInicial", u"xxxx000000@berneck.com.br", None))
        self.btn_visivel.setText("")
        self.label_9.setText(QCoreApplication.translate("ConfigurarInicial", u"E-mail login:", None))
        self.txt_email_envio.setPlaceholderText(QCoreApplication.translate("ConfigurarInicial", u"xxxxxxxx@berneck.com.br", None))
        self.txt_senha.setPlaceholderText(QCoreApplication.translate("ConfigurarInicial", u"***********************", None))
        self.label_11.setText(QCoreApplication.translate("ConfigurarInicial", u"Senha e-mail:", None))
        self.label_10.setText(QCoreApplication.translate("ConfigurarInicial", u"E-mail envio:", None))
#if QT_CONFIG(tooltip)
        self.btn_ajuda_email_envio.setToolTip(QCoreApplication.translate("ConfigurarInicial", u"<html><head/><body><p>E-mail utilizado, ex: xxxxxx@berneck.com.br</p><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_ajuda_email_envio.setText("")
        self.label_12.setText(QCoreApplication.translate("ConfigurarInicial", u"Port:", None))
        self.txt_porta.setText(QCoreApplication.translate("ConfigurarInicial", u"587", None))
        self.txt_porta.setPlaceholderText(QCoreApplication.translate("ConfigurarInicial", u"***********************", None))
        self.label.setText(QCoreApplication.translate("ConfigurarInicial", u"Configura\u00e7\u00f5es iniciais:", None))
#if QT_CONFIG(tooltip)
        self.btn_ok.setToolTip(QCoreApplication.translate("ConfigurarInicial", u"<html><head/><body><p>Salvar e Sair</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_ok.setText("")
#if QT_CONFIG(tooltip)
        self.btn_cancelar.setToolTip(QCoreApplication.translate("ConfigurarInicial", u"<html><head/><body><p>Cancelar</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_cancelar.setText("")
    # retranslateUi

