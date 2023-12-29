from PySide6.QtWidgets import (QWidget, QMainWindow, QHeaderView, QTableWidget, QVBoxLayout, QAbstractItemView)
from PySide6.QtGui import (QShortcut, QKeySequence, QIntValidator, QDoubleValidator, QIcon)

from controllers.funcoes import *

from views.Ui_AlterarUsuario import Ui_AlterarUsuario
from views.Ui_HistoricoNaoAtendidos import Ui_Historico
from views.Ui_MainGerenciadorAlmox import Ui_MainGerenciadorAlmox
from views.Ui_NaoAtendidos import Ui_NaoAtendidos
from views.Ui_NaoAtendidosVisual import Ui_NaoAtendidosVisual
from views.Ui_SelectColumns import Ui_AtribuirCampos

from msgbox.msgbox import MsgQuestion

from datetime import datetime

import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

# Classe controle interface principal
class MainWindow(QMainWindow, Ui_MainGerenciadorAlmox):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Gerenciador Almoxarifado')

        appIcon = QIcon(u"caminho_icone")
        self.setWindowIcon(appIcon)
        
        self.porta = ""
        #--> Barra de progresso
        self.prog_bar_pos.setVisible(False)
        # configuracao_inicial(self)
        self.home_btn_config.setVisible(False)
        self.home_btn_cont_acesso.setVisible(False)
        self.home_btn_alt_local.setVisible(False)
        self.home_btn_nao_atendidos.setVisible(False)
        self.home_btn_recebimento.setVisible(False)
        self.pgs_principal.setCurrentWidget(self.pg_notificacao)
        self.lb_titulo.setText("Gerenciador Almoxarifado")
        self.lb_notificacao.setText(f"Seja bem vindo, por gentileza selecionar a função desejado no menu!")



        ############### Configurações HOME ###############
        #--> Ocultar a guia HOME
        self.qf_home.setVisible(False)
        #--> Botão exibir a guia home
        self.btn_home.toggled.connect(self.qf_home.setVisible)
        #--> Botão Home Alterar Poseção Depósito
        self.home_btn_alt_local.toggled.connect(self.abrir_interface_alt_pos_dep)
        self.home_btn_alt_local.clicked.connect(lambda: self.pgs_principal.setCurrentWidget(self.pg_alt_dep))
        #--> Botão Home Monitor não atendidos
        self.home_btn_nao_atendidos.toggled.connect(self.abrir_interface_nao_atendidos)
        self.home_btn_nao_atendidos.toggled.connect(lambda: self.pgs_principal.setCurrentWidget(self.pg_nao_atendidos))
        self.home_btn_nao_atendidos.toggled.connect(lambda: iniciar_pg_nao_atendidos(self))
        #--> Botão Home Controle Entrada almox
        self.home_btn_cont_entrada_almox.setVisible(False)
        #--> Botão Home Controle Acesso
        self.home_btn_cont_acesso.toggled.connect(self.abrir_interface_controle_acesso)
        self.home_btn_cont_acesso.toggled.connect(lambda: self.pgs_principal.setCurrentWidget(self.pg_controle_acesso))
        ##############################################################################



        ##################### Configuração alteração localização #####################
        #--> Alterar dados SAP
        self.alt_loc_btn_alt_dados.clicked.connect(lambda: alterar_btn(self))
        #--> Adicionar item alteração em massa 
        self.alt_loc_btn_incluir.clicked.connect(lambda: add_item_alt_massiva(self))
        #--> Limpar lista alteração em massa
        self.alt_loc_btn_limpar_dados.clicked.connect(lambda: limpar_tabela_alt_massiva(self))
        #--> Importar dados para alteração do arquivo excel
        self.alt_loc_btn_imp_excel.clicked.connect(lambda: importar_excel(self))
        #--> Exportar dados alteração para Excel
        self.alt_loc_btn_exp_excel.clicked.connect(lambda: exportar_excel(self))
        #--> Excluir linha
        self.alt_loc_btn_excluir_linha.clicked.connect(lambda: excluir_linha(self))
        # Configuração QLineEdit
        #--> Txt Material
        self.alt_loc_txt_mat.setValidator(QIntValidator())
        #--> Txt Material
        self.alt_loc_txt_cen.setValidator(QIntValidator())
        #--> Txt Material
        self.alt_loc_txt_dep.setValidator(QIntValidator())
        # Dimensionar tabela
        alt_loc_tb_alt_massa = self.alt_loc_tb_alt_massa.horizontalHeader()
        alt_loc_tb_alt_massa.setSectionResizeMode(QHeaderView.ResizeToContents)        
        #----------Comandos teclado
        #--> Deletar dados tabela alteração 'Delete'
        QShortcut(QKeySequence('del'),self.pg_alt_dep).activated.connect(lambda: deletar_linha_selecionada(self))
        #--> Colar Dados tabela alteração 'CTRL+V'
        QShortcut(QKeySequence('Ctrl+v'),self.pg_alt_dep).activated.connect(lambda: colar_dados_tabela(self))
        #--> Add linha tabela alteração 'CTRL++'
        QShortcut(QKeySequence('Ctrl++'),self.pg_alt_dep).activated.connect(lambda: add_Linha_tabela_low(self))
        #--> Add linha tabela alteração 'CTRL+Shift++'
        QShortcut(QKeySequence('Ctrl+Shift++'),self.pg_alt_dep).activated.connect(lambda: add_linha_tabela_top(self))
        #--> Replicar dados tabela alteração 'Ctrl+d'
        QShortcut(QKeySequence('Ctrl+d'),self.pg_alt_dep).activated.connect(lambda: replicar_dados(self))
        #--> Excluir linha tabela alteração 'Ctrl+-'
        QShortcut(QKeySequence('Ctrl+-'),self.pg_alt_dep).activated.connect(lambda: excluir_linha(self))
        #--> Limpar tabela alteração 'Ctrl+del'
        QShortcut(QKeySequence('Ctrl+del'),self.pg_alt_dep).activated.connect(lambda: limpar_tabela_alt_massiva(self))
        #--> Importar dados para alteração do arquivo excel 'Ctrl+e'
        QShortcut(QKeySequence('Ctrl+e'),self.pg_alt_dep).activated.connect(lambda: importar_excel(self))
        #--> Exportar dados alteração para Excel 'Ctrl+Alt+e'
        QShortcut(QKeySequence('Ctrl+Alt+e'),self.pg_alt_dep).activated.connect(lambda: exportar_excel(self))
        ##############################################################################



        ##################### Configuração Controle Acesso #####################
        #--> Botão alterar usuário
        self.cont_aces_btn_alt_user.clicked.connect(lambda: abrir_form_alt_user(self, "ALT"))
        #--> Botão incluir usuário
        self.cont_aces_btn_inc_user.clicked.connect(lambda: abrir_form_alt_user(self, "CAD"))
        self.cont_aces_btn_exc_user.clicked.connect(lambda: exluir_usuario(self))
        ##############################################################################



        ##################### Configuração não atendidos #####################
        #--> Botão incluir registro
        self.nao_atend_btn_inc_regist.clicked.connect(lambda: abrir_form_nao_atendidos(self, "NOVO"))
        #--> Botão alterar registro
        self.nao_atend_btn_alt_regist.clicked.connect(lambda: abrir_form_nao_atendidos(self, "ALT"))
        #--> Botão alterar excluir
        self.nao_atend_btn_excluir.clicked.connect(lambda: excluir_registrar_nao_atendidos(self))
        #--> Botão pesquisar
        self.nao_atend_btn_pesquisar.clicked.connect(lambda: consulta_db_nao_atendidos(self))
        #--> Configuração ações filtros
        self.nao_atend_cmb_ano_mes.currentIndexChanged.connect(lambda: consulta_db_nao_atendidos(self))
        self.nao_atend_cmb_acao_plan.currentIndexChanged.connect(lambda: consulta_db_nao_atendidos(self))
        self.nao_atend_cmb_email.currentIndexChanged.connect(lambda: consulta_db_nao_atendidos(self))
        self.nao_atend_txt_material.returnPressed.connect(lambda: consulta_db_nao_atendidos(self))        
        #--> Botão alterar registro
        self.nao_atend_btn_enviar_email.clicked.connect(lambda: enviar_email(self))
        #--> Botão alterar registro
        self.nao_atend_btn_visualizar.clicked.connect(lambda: visualisar_nao_atendidos(self))
        #--> Botão Abrir histórico não atendidos
        self.nao_atend_btn_historico.clicked.connect(self.nao_atendidos_historico)        
        # Dimensionar tabela
        nao_atend_tb_registros = self.nao_atend_tb_registros.horizontalHeader()
        nao_atend_tb_registros.setSectionResizeMode(QHeaderView.ResizeToContents)
        # Bloquear tabela não atendidos
        self.nao_atend_tb_registros.setEditTriggers(QTableWidget.NoEditTriggers)        
        ##############################################################################
        validar_acesso(self)

    # Configuração inicial Alteração localização
    def abrir_interface_alt_pos_dep(self):
        ################ Configuração Pagina Alteração Posição Depósito ###############
        # Validar se o SAP Gui esta aberto
        status_sap = validar_sap()
        if status_sap[0] == "Erro":
            MsgErro(status_sap[1])
        # Alterar o título
        self.lb_titulo.setText("Alteração Localização")

        # Ocultar o menu home
        self.btn_home.click()
        
    # Configuração inicial Controle Acesso    
    def abrir_interface_controle_acesso(self):
        ################ Configuração Pagina Controle Acesso ###############
        # Alterar o título
        self.lb_titulo.setText("Controle Acesso")
        # Validar o Acesso
        validar_acesso(self)
        # Ocultar o menu home
        self.btn_home.click()        
        
    # Configuração inicial Não Atendidos
    def abrir_interface_nao_atendidos(self):
        ################ Configuração Pagina Monitor Não Atendidos ###############
        consulta_db_nao_atendidos(self)
        # Alterar o título
        self.lb_titulo.setText("Monitor Não Atendidos")
        # Ocultar o menu home
        self.btn_home.click()
       
    # Configuração inicial Não Atendidos Histórico
    def nao_atendidos_historico(self):
        if len(self.status_consulta["DADOS"]) > 0:
            from controllers.interface import NaoAtendidosHistorico
            self.nao_atendidos = NaoAtendidosHistorico(self)
            self.nao_atendidos.show()
        else:
            MsgInformation("", f"Não foi encontrado nenhum registro para o centro {', '.join(self.cen_user)}!")

    # Validação para fechar o aplicativo
    def closeEvent(self, event):
        if self.acesso == "OK": 
            msg_info = 'Deseja realmente fechar o App?'
            resp = MsgQuestion(msg_info)
            if resp == 16384:
                event.accept()
            else:
                event.ignore()
        else:
            event.accept()


# Classe controle QWidget atribuição colunas
class SelectColunms(QWidget, Ui_AtribuirCampos):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent  
        self.setupUi(self)

        #----------Congiguração botões----------
        #--> Botão cancelar
        self.btn_cancelar.clicked.connect(lambda: self.close())
        #--> Botão OK confirme
        self.btn_ok.clicked.connect(lambda: atualizar_tabela(self))
        
        #----------Congiguração ComboBox----------
        #--> Carregar as ComboBox
        self.cmb_mat.addItem('')
        self.cmb_cen.addItem('')
        self.cmb_dep.addItem('')
        self.cmb_loc.addItem('')
        self.cmb_mat.addItems(self.parent.df.columns)
        self.cmb_cen.addItems(self.parent.df.columns)
        self.cmb_dep.addItems(self.parent.df.columns)
        self.cmb_loc.addItems(self.parent.df.columns)


# Classe controle QWidget Alterar usuários
class AlterarUsuario(QWidget, Ui_AlterarUsuario):
    def __init__(self, parent=None, tp=None, id=None, user=None, nome=None, centro=None, cen_adm=None, acesso=None):
        super().__init__(parent)
        self.setupUi(self)
        self.parent = parent

        self.resize(self.parent.size())
        
        self.tp = tp

        self.label_2.setVisible(False)
        self.label_6.setVisible(False)
        self.lb_id.setVisible(False)
        self.txt_user_ant.setVisible(False)
        self.txt_nome_ant.setVisible(False)
        self.lb_cen.setVisible(False)
        self.lb_acesso.setVisible(False)

        self.cmb_cen.addItems(cen_adm)
        if self.tp == "ALT":
            self.label.setText("Alterar Usuário:")
            self.label_2.setVisible(True)
            self.label_6.setVisible(True)
            self.lb_id.setVisible(True)
            self.txt_user_ant.setVisible(True)
            self.txt_nome_ant.setVisible(True)
            self.lb_cen.setVisible(True)
            self.lb_acesso.setVisible(True)

            self.lb_id.setText(str(id))
            self.txt_user_ant.setText(str(user))
            self.txt_nome_ant.setText(str(nome))
            self.txt_user.setText(str(user))
            self.txt_nome.setText(str(nome))
            self.lb_cen.setText(str(centro))
            self.lb_acesso.setText(str(acesso))

        elif self.tp == "CAD":
            self.label.setText("Cadastrar Usuário:")
        
        #--> Opção cancelar fechar formulário Alterar Usuário
        self.btn_cancelar.clicked.connect(lambda: self.close())
        #--> Opção OK atutalizar usuário
        self.btn_ok.clicked.connect(lambda: alterar_usuario(self))

        self.parent.resizeEvent = self.auto_resized

    def auto_resized(self, event):
        self.resize(self.parent.size())


# # Classe controle QWidget configuração inicial
# class ConfiguracaoInical(QWidget, Ui_ConfigurarInicial):
#     def __init__(self, parent=None, tp=None):
#         super().__init__(parent)
#         self.setupUi(self)
       
#         self.parent = parent

#         self.resize(self.parent.size())

#         self.btn_visivel.clicked.connect(lambda: exibir_ocultar_senha(self))
#         self.btn_ok.clicked.connect(lambda: criar_arquivo_configuracao(self))

#         self.btn_cancelar.clicked.connect(lambda: self.close())

#         if tp == "ALT":
#             with open(self.parent.caminho_arquivo_json, 'r') as arquivo:
#                 dados_carregados = json.load(arquivo)
          
#             self.txt_email_login.setText(dados_carregados["EmailLogin"])
#             self.txt_email_envio.setText(dados_carregados["EmailSend"])
#             self.txt_senha.setText(dados_carregados["Senha"])
        
#         self.parent.resizeEvent = self.auto_resized

#     def auto_resized(self, event):
#         self.resize(self.parent.size())


# Classe controle QWidget interface não atendidos
class NaoAtendidos(QWidget, Ui_NaoAtendidos):
    def __init__(self, parent=None, tp=None, tb_dados=None, id_alt=None):
        super().__init__(parent)
        self.setupUi(self)
        self.parent = parent 
        self.cen_user = self.parent.cen_user
        # Dimensionar tabela
        tb_proc_comp = self.tb_proc_comp.horizontalHeader()
        tb_proc_comp.setSectionResizeMode(QHeaderView.ResizeToContents) 
        self.tb_proc_comp.setEditTriggers(QTableWidget.NoEditTriggers)
        
        self.resize(self.parent.size())
        
        status_sap = validar_sap()
        if status_sap[0] == "Erro":
            MsgErro(status_sap[1])
         
        self.tp = tp
        self.tb_dados = tb_dados
        self.id = id_alt
        self.txt_mat.setValidator(QDoubleValidator())
        self.txt_ramal.setValidator(QDoubleValidator())
        self.txt_qt_solicitada.setValidator(QDoubleValidator())
        self.txt_saldo_sistema.setValidator(QDoubleValidator())
        self.txt_saldo_fisico.setValidator(QDoubleValidator())
        self.txt_segunda_cont.setValidator(QDoubleValidator())
        self.txt_bloqueado.setValidator(QDoubleValidator())
        self.txt_req_manual.setValidator(QDoubleValidator())
        
        self.lb_info.setVisible(False)

        self.btn_cancelar.clicked.connect(lambda: self.close())
        self.btn_salvar_novo.clicked.connect(lambda: incluir_registrar_nao_atendidos(self))

        self.btn_salvar_sair.clicked.connect(self.validar_btn_salvar_sair)

        self.txt_mat.returnPressed.connect(lambda: consulta_dados_sap(self))
        self.txt_saldo_fisico.editingFinished.connect(lambda: campo_divergencia(self))
        self.txt_segunda_cont.editingFinished.connect(lambda: campo_divergencia(self))
        self.txt_req_manual.editingFinished.connect(lambda: campo_divergencia(self))
        self.cmb_setor.addItem("")
        if len(self.parent.status_consulta["DADOS"]) > 0:
            self.cmb_setor.addItems(self.parent.status_consulta["DADOS"]["SETOR"].unique())

        data_atual = datetime.now()
        # Obtém apenas a parte da data com hora zero (00:00:00)
        self.txt_data.setText(datetime.strftime(data_atual, "%d/%m/%Y"))
        self.txt_hora.setText(datetime.strftime(data_atual, "%H:%M"))
    
        self.parent.resizeEvent = self.auto_resized

    def auto_resized(self, event):
        self.resize(self.parent.size())


    def validar_btn_salvar_sair(self):
        if self.tp == "ALT":
            alterar_registrar_nao_atendidos(self, "SALVAR_SAIR")
        else:
            incluir_registrar_nao_atendidos(self, "SALVAR_SAIR")
        

# Classe controle QWidget interface não atendidos
class NaoAtendidosVisualisar(QWidget, Ui_NaoAtendidosVisual):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.parent = parent
        
        # Dimensionar tabela
        tb_proc_comp = self.tb_proc_comp.horizontalHeader()
        tb_proc_comp.setSectionResizeMode(QHeaderView.ResizeToContents) 

        self.resize(self.parent.size())

        self.btn_cancelar.clicked.connect(lambda: self.close())
        
        self.parent.resizeEvent = self.auto_resized

    def auto_resized(self, event):
        self.resize(self.parent.size())


# Classe controle QWidget interface Histórico
class NaoAtendidosHistorico(QWidget, Ui_Historico):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.cen_user = self.parent.cen_user
        self.resize(self.parent.size())

        self.parent.resizeEvent = self.auto_resized

        self.btn_cancelar.clicked.connect(lambda: self.close())

        self.cmb_mes_ano.setVisible(False)
        self.cmb_mes_ano.addItems(self.parent.lista_mes_ano)
        self.cmb_mes_ano.currentIndexChanged.connect(lambda: tratar_base_graficos(self))

        self.valida_gr_geral = ""
        self.valida_gr_ocor_iten = ""
        self.valida_gr_cod_sit = ""
        self.figures = []

        self.layout_gr_geral = QVBoxLayout(self.fr_gr_geral)
        self.layout_gr_ocor_iten = QVBoxLayout(self.fr_gr_total)
        self.layout_gr_cod_sit = QVBoxLayout(self.fr_gr_cod_sit)

        self.label.setText(str(f"HISTÓRICO NÃO ATENDIDOS - CENTRO {', '.join(self.cen_user)}"))

        self.rb_ano.setChecked(True)
        self.rb_ano.toggled.connect(lambda: self.cmb_mes_ano.setVisible(False))

        self.rb_mes.toggled.connect(lambda: tratar_base_graficos(self))
        self.rb_mes.toggled.connect(lambda: self.cmb_mes_ano.setVisible(True))
        self.rb_mes.toggled.connect(lambda: self.cmb_mes_ano.setCurrentText(self.parent.lista_mes_ano[0]))

        # Dimensionar tabela
        tb_top_ocorren = self.tb_top_ocorren.horizontalHeader()
        tb_top_ocorren.setSectionResizeMode(QHeaderView.ResizeToContents) 
        self.tb_top_ocorren.setEditTriggers(QAbstractItemView.NoEditTriggers)

        tratar_base_graficos(self)

    def auto_resized(self, event):
        self.resize(self.parent.size())

