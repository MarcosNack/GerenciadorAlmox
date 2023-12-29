# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'HistoricoNaoAtendidos.ui'
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
    QHBoxLayout, QHeaderView, QLabel, QPushButton,
    QRadioButton, QScrollArea, QSizePolicy, QSpacerItem,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QAbstractItemView)
import assets.icons_alt_regras_rc

class Ui_Historico(object):
    def setupUi(self, Historico):
        if not Historico.objectName():
            Historico.setObjectName(u"Historico")
        Historico.resize(930, 600)
        Historico.setMinimumSize(QSize(930, 600))
        Historico.setMaximumSize(QSize(16777215, 16777215))
        Historico.setStyleSheet(u"QWidget{	\n"
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
"QComboBox{	\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-style: ridge;\n"
"	border-width: 3px;\n"
"    border-color: rgb(150, 150, 150);    \n"
"	font: bold 10pt \"Segoe UI\";\n"
"	}\n"
"QComboBox::focus{\n"
"    background-color: rgb(170, 255, 255);\n"
"    border-style: inset;\n"
"	}\n"
"QComboBox QListView {\n"
"	background-color: white; \n"
"	}\n"
"QLabel{	\n"
"	background-color: rgb(225, 225, 225);\n"
"	border-style: ridge ;\n"
"	border-width: 3px;\n"
"    border-color: rgb(170, 170, 170);\n"
"    font: bold 12px;\n"
"	text-align: left;\n"
"}\n"
"QRadioButton{	\n"
"	background-color: rgb(225, 225, 225);\n"
"	border: 0px;\n"
"    font: bold 12px;\n"
"	text-align: left;\n"
"}\n"
"QLineEdit{	"
                        "	\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-style: double;\n"
"	border-width: 3px;\n"
"    border-color: rgb(170, 170, 170);\n"
"    font: bold 12px;\n"
"}\n"
"QLineEdit::focus{\n"
"    background-color: rgb(170, 255, 255);\n"
"    border-style: inset;\n"
"}")
        self.verticalLayout = QVBoxLayout(Historico)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(4, 4, 4, 4)
        self.frame_3 = QFrame(Historico)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_3)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(4, 2, 4, 2)
        self.frame_2 = QFrame(self.frame_3)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 40))
        self.frame_2.setMaximumSize(QSize(16777215, 40))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setSpacing(24)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 5, 5, 5)
        self.rb_ano = QRadioButton(self.frame_2)
        self.rb_ano.setObjectName(u"rb_ano")

        self.horizontalLayout.addWidget(self.rb_ano)

        self.rb_mes = QRadioButton(self.frame_2)
        self.rb_mes.setObjectName(u"rb_mes")

        self.horizontalLayout.addWidget(self.rb_mes)

        self.cmb_mes_ano = QComboBox(self.frame_2)
        self.cmb_mes_ano.setObjectName(u"cmb_mes_ano")
        self.cmb_mes_ano.setMinimumSize(QSize(200, 25))
        self.cmb_mes_ano.setMaximumSize(QSize(16777215, 30))
        self.cmb_mes_ano.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.cmb_mes_ano)


        self.gridLayout_2.addWidget(self.frame_2, 1, 1, 1, 1)

        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 50))
        self.label.setStyleSheet(u"font: bold 12pt \"Segoe UI\";\n"
"border: 0px;")
        self.label.setWordWrap(True)

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 1, 2, 1, 1)

        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(250, 40))
        self.label_2.setMaximumSize(QSize(16777215, 40))
        self.label_2.setStyleSheet(u"font: 700 12pt \"Segoe UI\";")

        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)

        self.btn_cancelar = QPushButton(self.frame_3)
        self.btn_cancelar.setObjectName(u"btn_cancelar")
        self.btn_cancelar.setMinimumSize(QSize(50, 40))
        self.btn_cancelar.setMaximumSize(QSize(60, 40))
        self.btn_cancelar.setStyleSheet(u"#btn_cancelar{	\n"
"	background-color: rgb(204, 0, 0);\n"
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
        icon = QIcon()
        icon.addFile(u":/assets.icons_alt_regras/fechar-janela.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_cancelar.setIcon(icon)
        self.btn_cancelar.setIconSize(QSize(30, 30))

        self.gridLayout_2.addWidget(self.btn_cancelar, 0, 3, 1, 1)

        self.scrollArea = QScrollArea(self.frame_3)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 889, 542))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.scrollAreaWidgetContents)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMaximumSize(QSize(16777215, 350))
        self.frame.setStyleSheet(u"#frame{\n"
" border: 0px;\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.tb_top_ocorren = QTableWidget(self.frame)
        if (self.tb_top_ocorren.columnCount() < 3):
            self.tb_top_ocorren.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tb_top_ocorren.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tb_top_ocorren.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tb_top_ocorren.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tb_top_ocorren.setObjectName(u"tb_top_ocorren")
        self.tb_top_ocorren.setMinimumSize(QSize(300, 100))
        self.tb_top_ocorren.setMaximumSize(QSize(300, 16777215))
        self.tb_top_ocorren.setStyleSheet(u"QTableWidget{\n"
"	background-color: rgb(255, 255, 255);\n"
"	font: 8pt \"Segoe UI\";\n"
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
"	font: bold 8pt \"Segoe UI\";\n"
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
"  	background-color: rgb(100, 100, 100);\n"
"	border-style: ridge;\n"
"   	border-width: 2px;\n"
"    border-color: rgb(170, 170, 170);\n"
"	border-radius: 2px;\n"
"	}")
        self.tb_top_ocorren.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tb_top_ocorren.setWordWrap(False)
        self.tb_top_ocorren.setRowCount(0)
        self.tb_top_ocorren.setColumnCount(3)
        self.tb_top_ocorren.horizontalHeader().setCascadingSectionResizes(True)
        self.tb_top_ocorren.horizontalHeader().setMinimumSectionSize(30)
        self.tb_top_ocorren.horizontalHeader().setDefaultSectionSize(30)
        self.tb_top_ocorren.horizontalHeader().setProperty("showSortIndicator", False)
        self.tb_top_ocorren.horizontalHeader().setStretchLastSection(False)
        self.tb_top_ocorren.verticalHeader().setCascadingSectionResizes(False)
        self.tb_top_ocorren.verticalHeader().setDefaultSectionSize(30)

        self.gridLayout.addWidget(self.tb_top_ocorren, 2, 0, 1, 1)

        self.label_11 = QLabel(self.frame)
        self.label_11.setObjectName(u"label_11")
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setMinimumSize(QSize(300, 25))
        self.label_11.setMaximumSize(QSize(300, 25))
        self.label_11.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_11, 1, 0, 1, 1)

        self.label_12 = QLabel(self.frame)
        self.label_12.setObjectName(u"label_12")
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        self.label_12.setMinimumSize(QSize(0, 25))
        self.label_12.setMaximumSize(QSize(16777215, 25))
        self.label_12.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_12, 1, 1, 1, 1)

        self.label_13 = QLabel(self.frame)
        self.label_13.setObjectName(u"label_13")
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)
        self.label_13.setMinimumSize(QSize(0, 25))
        self.label_13.setMaximumSize(QSize(16777215, 25))
        self.label_13.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_13, 1, 2, 1, 1)

        self.fr_gr_total = QFrame(self.frame)
        self.fr_gr_total.setObjectName(u"fr_gr_total")
        self.fr_gr_total.setMinimumSize(QSize(0, 0))
        self.fr_gr_total.setMaximumSize(QSize(16777215, 16777215))
        self.fr_gr_total.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.fr_gr_total.setFrameShape(QFrame.StyledPanel)
        self.fr_gr_total.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.fr_gr_total, 2, 1, 1, 1)

        self.fr_gr_cod_sit = QFrame(self.frame)
        self.fr_gr_cod_sit.setObjectName(u"fr_gr_cod_sit")
        self.fr_gr_cod_sit.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.fr_gr_cod_sit.setFrameShape(QFrame.StyledPanel)
        self.fr_gr_cod_sit.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.fr_gr_cod_sit, 2, 2, 1, 1)


        self.verticalLayout_2.addWidget(self.frame)

        self.lb_geral = QLabel(self.scrollAreaWidgetContents)
        self.lb_geral.setObjectName(u"lb_geral")
        sizePolicy.setHeightForWidth(self.lb_geral.sizePolicy().hasHeightForWidth())
        self.lb_geral.setSizePolicy(sizePolicy)
        self.lb_geral.setMinimumSize(QSize(0, 25))
        self.lb_geral.setMaximumSize(QSize(16777215, 25))
        self.lb_geral.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.lb_geral)

        self.fr_gr_geral = QFrame(self.scrollAreaWidgetContents)
        self.fr_gr_geral.setObjectName(u"fr_gr_geral")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.fr_gr_geral.sizePolicy().hasHeightForWidth())
        self.fr_gr_geral.setSizePolicy(sizePolicy1)
        self.fr_gr_geral.setMinimumSize(QSize(72, 300))
        self.fr_gr_geral.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.fr_gr_geral.setFrameShape(QFrame.StyledPanel)
        self.fr_gr_geral.setFrameShadow(QFrame.Raised)

        self.verticalLayout_2.addWidget(self.fr_gr_geral)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_2.addWidget(self.scrollArea, 2, 0, 1, 4)


        self.verticalLayout.addWidget(self.frame_3)


        self.retranslateUi(Historico)

        QMetaObject.connectSlotsByName(Historico)
    # setupUi

    def retranslateUi(self, Historico):
        Historico.setWindowTitle(QCoreApplication.translate("Historico", u"Form", None))
        self.rb_ano.setText(QCoreApplication.translate("Historico", u"Anual", None))
        self.rb_mes.setText(QCoreApplication.translate("Historico", u"Mensal", None))
        self.label.setText(QCoreApplication.translate("Historico", u" HIST\u00d3RICO N\u00c3O ATENDIDOS - CENTRO 1001", None))
        self.label_2.setText(QCoreApplication.translate("Historico", u"Filtro:", None))
#if QT_CONFIG(tooltip)
        self.btn_cancelar.setToolTip(QCoreApplication.translate("Historico", u"<html><head/><body><p>Cancelar</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_cancelar.setText("")
        ___qtablewidgetitem = self.tb_top_ocorren.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Historico", u"Total", None));
        ___qtablewidgetitem1 = self.tb_top_ocorren.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Historico", u"Material", None));
        ___qtablewidgetitem2 = self.tb_top_ocorren.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Historico", u"Descri\u00e7\u00e3o", None));
        self.label_11.setText(QCoreApplication.translate("Historico", u"Top 15 Itens", None))
        self.label_12.setText(QCoreApplication.translate("Historico", u"Total Ocorrencia/Itens", None))
#if QT_CONFIG(tooltip)
        self.label_13.setToolTip(QCoreApplication.translate("Historico", u"<html><head/><body><table border=\"0\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px;\" cellspacing=\"2\" cellpadding=\"0\"><tr><td width=\"256\"><p>AI - Armazenado Incorretamente</p></td></tr><tr><td><p>DD - Outros</p></td></tr><tr><td><p>EI - Entrega Incorreta Fornecedor</p></td></tr><tr><td><p>FE - Furo de Estoque</p></td></tr><tr><td><p>FN - Falta Entrada Nota Fiscal</p></td></tr><tr><td><p>IO - Material Obsoleto</p></td></tr><tr><td><p>IR - Material Reservado</p></td></tr><tr><td><p>MC - Material de Conserto</p></td></tr><tr><td><p>MR - Movimentado Recentemente</p></td></tr><tr><td><p>NA - N\u00e3o Armazenado</p></td></tr><tr><td><p>NS - N\u00e3o Subiu para o SAP</p></td></tr><tr><td><p>ND - Material ND</p></td></tr><tr><td><p>OM - Outro Material</p></td></tr><tr><td><p>OC - Material de Outro Centro</p></td></tr><tr><td><p>PP - Pedido Pendente</p></td></tr><tr><td><p>RP - RC Pendente</p></td></tr><tr><td><p>SR - Sem Reposi\u00e7\u00e3o</p></td></tr><tr><td><p>SP - Sem Padro"
                        "niza\u00e7\u00e3o</p></td></tr></table></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_13.setText(QCoreApplication.translate("Historico", u"C\u00f3d. Situa\u00e7\u00e3o", None))
#if QT_CONFIG(tooltip)
        self.fr_gr_cod_sit.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.lb_geral.setText(QCoreApplication.translate("Historico", u"Geral", None))
    # retranslateUi

