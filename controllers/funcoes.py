import os
import pandas as pd
# import json
from datetime import datetime

import locale
import calendar

from controllers.conexao_sap import *
from controllers.conexao_db import *

from PySide6.QtWidgets import (QTableWidgetItem, QApplication, QFileDialog, QHeaderView, QLineEdit)

from msgbox.msgbox import MsgErro, MsgQuestion, MsgCancelado, MsgFinalizado, MsgInformation

import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.font_manager import FontProperties


################ Funções Controle Pagina Alteração Posição Depósito ###############
# Deletar dados
def deletar_linha_selecionada(self):
    linhaselecionada = self.alt_loc_tb_alt_massa.selectedIndexes()
    if linhaselecionada:                    
        for index in self.alt_loc_tb_alt_massa.selectedIndexes():
            self.alt_loc_tb_alt_massa.setItem(index.row(),index.column(), QTableWidgetItem(str('')))
                            
# Colar Dados
def colar_dados_tabela(self):
    cb = QApplication.clipboard()
    texto = cb.text(mode=cb.Clipboard)

    dados = []
    for row in texto.split('\n'):
        dados.append(row.split('\t'))     
    
    linhaselecionada = self.alt_loc_tb_alt_massa.selectedIndexes()
    if linhaselecionada:
        col = linhaselecionada[0].column()
        if col == 0:
            if len(dados) > 0:
                for i, row in enumerate(dados):
                    if len(row[0]) == 8:   
                        self.alt_loc_tb_alt_massa.insertRow(linhaselecionada[0].row()+i)                         
                        self.alt_loc_tb_alt_massa.setItem(linhaselecionada[0].row()+i, col, QTableWidgetItem(str(row[0])))
                        self.alt_loc_tb_alt_massa.setItem(linhaselecionada[0].row()+i, 6, QTableWidgetItem(str('')))

                    elif row[0] != '':
                        self.alt_loc_tb_alt_massa.insertRow(linhaselecionada[0].row()+i)
                        self.alt_loc_tb_alt_massa.setItem(linhaselecionada[0].row()+i, col, QTableWidgetItem(str(row[0])))
                        self.alt_loc_tb_alt_massa.setItem(linhaselecionada[0].row()+i, 6, QTableWidgetItem(str('Código SAP inválido')))

        elif col == 1:
            if len(dados) > 0:
                for i, row in enumerate(dados):
                    if len(row[0]) == 4:                           
                        self.alt_loc_tb_alt_massa.setItem(linhaselecionada[0].row()+i, col, QTableWidgetItem(str(row[0])))
                        self.alt_loc_tb_alt_massa.setItem(linhaselecionada[0].row()+i, 6, QTableWidgetItem(str('')))

                    elif row[0] != '':
                        self.alt_loc_tb_alt_massa.setItem(linhaselecionada[0].row()+i, col, QTableWidgetItem(str(row[0])))
                        self.alt_loc_tb_alt_massa.setItem(linhaselecionada[0].row()+i, 6, QTableWidgetItem(str('Centro inválido')))

        
        elif col == 2:
            if len(dados) > 0:
                for i, row in enumerate(dados):
                    if len(row[0]) == 4:    
                        self.alt_loc_tb_alt_massa.setItem(linhaselecionada[0].row()+i, col, QTableWidgetItem(str(row[0])))
                        self.alt_loc_tb_alt_massa.setItem(linhaselecionada[0].row()+i, 6, QTableWidgetItem(str('')))

                    elif row[0] != '':
                        self.alt_loc_tb_alt_massa.setItem(linhaselecionada[0].row()+i, col, QTableWidgetItem(str(row[0])))
                        self.alt_loc_tb_alt_massa.setItem(linhaselecionada[0].row()+i, 6, QTableWidgetItem(str('Depósito inválido')))


        elif col == 3:
            if len(dados) > 0:
                for i, row in enumerate(dados):
                    if len(row[0]) < 11: 
                        self.alt_loc_tb_alt_massa.setItem(linhaselecionada[0].row()+i, col, QTableWidgetItem(str(row[0])))
                        self.alt_loc_tb_alt_massa.setItem(linhaselecionada[0].row()+i, 6, QTableWidgetItem(str('')))

                    elif row[0] != '':
                        self.alt_loc_tb_alt_massa.setItem(linhaselecionada[0].row()+i, col, QTableWidgetItem(str(row[0])))
                        self.alt_loc_tb_alt_massa.setItem(linhaselecionada[0].row()+i, 6, QTableWidgetItem(str('Localização inválida')))


    else:
        MsgErro('Nenhuma Coluna selecionada!')

# Add linha a baixo
def add_Linha_tabela_low(self):
    linhaselecionada = self.alt_loc_tb_alt_massa.selectedIndexes()
    if linhaselecionada:                    
        self.alt_loc_tb_alt_massa.insertRow(self.alt_loc_tb_alt_massa.selectedIndexes()[0].row()+1)

# Add linha a cima
def add_linha_tabela_top(self):
    linhaselecionada = self.alt_loc_tb_alt_massa.selectedIndexes()
    if linhaselecionada:                    
        self.alt_loc_tb_alt_massa.insertRow(self.alt_loc_tb_alt_massa.selectedIndexes()[0].row())

# Replicar dados selecionados
def replicar_dados(self):
    linhaselecionada = self.alt_loc_tb_alt_massa.selectedIndexes()
    if linhaselecionada:
        txt = self.alt_loc_tb_alt_massa.item(linhaselecionada[0].row(), linhaselecionada[0].column()).text()

        for index in linhaselecionada[1:]:
            self.alt_loc_tb_alt_massa.setItem(index.row(),index.column(), QTableWidgetItem(str(txt)))

# Excluir linha selecionada
def excluir_linha(self):
    if int(self.alt_loc_tb_alt_massa.rowCount()) > 0:       
        linhaselecionada = self.alt_loc_tb_alt_massa.selectedIndexes()
        if linhaselecionada:
            rows = set()
            for index in self.alt_loc_tb_alt_massa.selectedIndexes():
                rows.add(index.row())

            for row in sorted(rows, reverse=True):
                self.alt_loc_tb_alt_massa.removeRow(row)
            
            if self.alt_loc_tb_alt_massa.rowCount() == 0:
                self.alt_loc_tb_alt_massa.setRowCount(1)

# Limpar lista alteração 
def limpar_tabela_alt_massiva(self):        
    msg_info = 'Deseja realmente limpar a lista de alteração?'
    resp = MsgQuestion(msg_info)
    if resp == 16384:
        self.alt_loc_tb_alt_massa.clearContents()
        self.alt_loc_tb_alt_massa.setRowCount(1)
        self.alt_loc_chcb_alt_massiva.setChecked(False)

# Gerara planilha da lista de materiais
def exportar_excel(self):
    msg_text = 'Exportar Excel!'
    msg_info = 'Deseja realmente exportar a lista de alteração para Excel?'
    resp = MsgQuestion(msg_info)
    if resp == 16384:
        if self.alt_loc_tb_alt_massa.rowCount() == 0:
            msg_info = 'A lista não possui nenhum dado preenchido.'
            MsgErro(msg_info)
        else:
            dados = []
            all_dados = []
            for row in range(self.alt_loc_tb_alt_massa.rowCount()):
                if self.alt_loc_tb_alt_massa.item(row, 0):
                    for column in range(self.alt_loc_tb_alt_massa.columnCount()):
                        if self.alt_loc_tb_alt_massa.item(row, column):
                            dados.append(self.alt_loc_tb_alt_massa.item(row, column).text())
                        else:
                            dados.append('')
                        all_dados.append(dados)
                    dados = []
            columns = ['SKU','CENTRO','DEPÓSITO','NOVA LOCALIZAÇÃO','LOCAL ANTIGO','STATUS','ERRO']
            materiais = pd.DataFrame(all_dados,columns= columns)
            arquivo = QFileDialog.getSaveFileName(self,'Salvar como','Alteração Posição Depósito','Pasta de Trabalho do Excel (*.xlsx)')[0]
            materiais.to_excel(f'{arquivo}', sheet_name='Lista Materiais', index=False)
            msg_text = 'Exportar Excel!'
            msg_info = 'Arquivo Excel exportado com sucesso!'
            MsgInformation(msg_text,  msg_info)

# Importar um arquivo excel
def importar_excel(self):
    msg_info = 'Deseja realmente importar um arquivo Excel?'
    resp = MsgQuestion(msg_info)
    if resp == 16384:
        arquivo = QFileDialog.getOpenFileName(self, 'Selecionar arquivo...', '', filter='Excel (*.xls*)')[0] 
        if arquivo:            
            self.df = pd.read_excel(arquivo) #Ler o arquivo Excel selecionado
            if len(self.df.columns) >= 4:                
                from controllers.interface import SelectColunms #Importar o formulário atribuir colunas
                self.atribuir_colunms = SelectColunms(self) #Instanciar a classe SelectColunms
                self.atribuir_colunms.show() #Exibir o formulário
                self.alt_loc_chcb_alt_massiva.setChecked(True) #Marcar opção alteração massiva
            else:
                MsgErro('Erro ao importar a planilha selecionada.') #Menssagem erro ao carregar o arquivo Excel

# Adicionar material na lista de alteração em massa
def add_item_alt_massiva(self):
    if self.alt_loc_txt_mat.text() == '' or self.alt_loc_txt_cen.text() == '' or self.alt_loc_txt_dep.text() == '' or self.alt_loc_txt_pos_local.text() == '':  

        codigo = 'SKU' if self.alt_loc_txt_mat.text() == '' else ''
        centro = 'Centro' if self.alt_loc_txt_cen.text() == '' else ''
        deposito = 'Deposito' if self.alt_loc_txt_dep.text() == '' else ''
        local = 'Local' if self.alt_loc_txt_pos_local.text() == '' else ''

        txt = f'{codigo} {centro} {deposito} {local}'
        txt = '\n'.join(txt.upper().split())
        msg_info = f'Por gentilezar preencher o(s) campo(s):\n{txt}'
        MsgErro(msg_info)
    else:     
        ultlinhatb = int(self.alt_loc_tb_alt_massa.rowCount())
        result = [self.alt_loc_txt_mat.text(),self.alt_loc_txt_cen.text(),self.alt_loc_txt_dep.text(),self.alt_loc_txt_pos_local.text()]
        self.alt_loc_tb_alt_massa.insertRow(ultlinhatb)
        self.alt_loc_tb_alt_massa.setItem(ultlinhatb - 1, 0, QTableWidgetItem(str(result[0]).strip()))
        self.alt_loc_tb_alt_massa.setItem(ultlinhatb - 1, 1, QTableWidgetItem(str(result[1]).strip()))
        self.alt_loc_tb_alt_massa.setItem(ultlinhatb - 1, 2, QTableWidgetItem(str(result[2]).strip()))
        self.alt_loc_tb_alt_massa.setItem(ultlinhatb - 1, 3, QTableWidgetItem(str(result[3]).strip()))
        self.alt_loc_chcb_alt_massiva.setChecked(True)
        
        self.alt_loc_txt_mat.setText('')
        self.alt_loc_txt_cen.setText('')
        self.alt_loc_txt_dep.setText('')
        self.alt_loc_txt_pos_local.setText('')

# Valida se a alteração no SAP será massiva ou individual
def alterar_btn(self):
    from time import sleep
    if self.alt_loc_chcb_alt_massiva.isChecked():    
        # msg_text = 'Confirmar Alteração'       
        msg_info = 'Deseja realmente realizar a alterar em massa da posição no depósito?'
        #resp YES = 16384, NO = 65536
        resp = MsgQuestion(msg_info)            
        if resp == 16384:
            status_conexao = conexao_sap_gui()
            if status_conexao["status"] == "OK":
                if self.alt_loc_tb_alt_massa.rowCount() == 1:
                    #msg erro   
                    msg_info = 'Por gentileza informar mais de um item para alteração massiva!'
                    resp = MsgErro(msg_info)                    
                else:
                    tltb = self.alt_loc_tb_alt_massa.rowCount() 
                    self.prog_bar_pos.setVisible(True)
                    self.prog_bar_pos.setMaximum(tltb)
                    self.prog_bar_pos.setValue(0)               
                    for row in range(tltb):
                        try:  
                            if self.alt_loc_tb_alt_massa.item(row, 1).text() in self.cen_user:
                                sku = self.alt_loc_tb_alt_massa.item(row, 0).text() if len(self.alt_loc_tb_alt_massa.item(row, 0).text()) == 8 else "Erro, material inválido"
                                centro = self.alt_loc_tb_alt_massa.item(row, 1).text() if len(self.alt_loc_tb_alt_massa.item(row, 1).text()) == 4 else "Erro, centro inválido"
                                deposito = self.alt_loc_tb_alt_massa.item(row, 2).text() if len(self.alt_loc_tb_alt_massa.item(row, 2).text()) == 4 else "Erro, deposito inválido"
                                local = self.alt_loc_tb_alt_massa.item(row, 3).text() if len(self.alt_loc_tb_alt_massa.item(row, 3).text()) <= 10 else "Erro, local inválido"

                                if "Erro" in sku:
                                    self.alt_loc_tb_alt_massa.setItem(row, 4, QTableWidgetItem(str("Erro")))
                                    self.alt_loc_tb_alt_massa.setItem(row, 6, QTableWidgetItem(str(sku)))
                                elif "Erro" in centro:
                                    self.alt_loc_tb_alt_massa.setItem(row, 4, QTableWidgetItem(str("Erro")))
                                    self.alt_loc_tb_alt_massa.setItem(row, 6, QTableWidgetItem(str(centro)))
                                elif "Erro" in deposito:
                                    self.alt_loc_tb_alt_massa.setItem(row, 4, QTableWidgetItem(str("Erro")))
                                    self.alt_loc_tb_alt_massa.setItem(row, 6, QTableWidgetItem(str(deposito)))
                                elif "Erro" in local:
                                    self.alt_loc_tb_alt_massa.setItem(row, 4, QTableWidgetItem(str("Erro")))
                                    self.alt_loc_tb_alt_massa.setItem(row, 6, QTableWidgetItem(str(local))) 
                                else:
                                    status_alteracao = alterar_dados_sap_gui(status_conexao["session"], sku, centro, deposito, local)
                                    if status_alteracao["status"] == "OK":
                                        self.alt_loc_tb_alt_massa.setItem(row, 4, QTableWidgetItem(str(status_alteracao["status"])))
                                        self.alt_loc_tb_alt_massa.setItem(row, 5, QTableWidgetItem(str(status_alteracao["local_antigo"])))
                                        self.alt_loc_tb_alt_massa.setItem(row, 6, QTableWidgetItem(str("")))
                                    else:
                                        self.alt_loc_tb_alt_massa.setItem(row, 4, QTableWidgetItem(str(status_alteracao["status"])))
                                        self.alt_loc_tb_alt_massa.setItem(row, 5, QTableWidgetItem(str("")))
                                        self.alt_loc_tb_alt_massa.setItem(row, 6, QTableWidgetItem(str(status_alteracao["MSG"])))

                            else:
                                self.alt_loc_tb_alt_massa.setItem(row, 4, QTableWidgetItem(str("Erro")))
                                self.alt_loc_tb_alt_massa.setItem(row, 6, QTableWidgetItem(str("Usuário sem acesso ao centro informado!")))   
                        except:
                            ...

                        self.prog_bar_pos.setValue(row+1)
                        sleep(1)

                    status_conexao["conn"].CloseSession("ses[0]")

                    MsgFinalizado('Processo finalizado!')
                    
                    self.prog_bar_pos.setVisible(False)
            
            elif status_conexao["status"] == "ERRO_OPEN":
                MsgErro(status_conexao["MSG"])

            elif status_conexao["ERRO"] == "ERRO":
                status_alteracao["conn"].CloseSession("ses[0]")
                MsgErro(status_conexao["MSG"])
                
            # Continuar o codigo
        else:
            MsgCancelado()

    else:
        # msg_text = 'Confirmar Alteração'  
        msg_info = 'Deseja realmente Alterar a posição no depósito?'
        resp = MsgQuestion(msg_info)
        if resp == 16384:
            status_conexao = conexao_sap_gui()
            if status_conexao["status"] == "OK":
                txt = ''
                codigo = 'SKU' if self.alt_loc_txt_mat.text() == '' else ''
                centro = 'Centro' if self.alt_loc_txt_cen.text() == '' else ''
                deposito = 'Deposito'if self.alt_loc_txt_dep.text() == '' else ''
                local = 'Local' if self.alt_loc_txt_pos_local.text() == '' else ''

                txt = f'{codigo} {centro} {deposito} {local}'
                txt = '\n'.join(txt.upper().split())

                if txt != '':
                    msg_info = f'Por gentilezar preencher o(s) campo(s):\n{txt}'
                    MsgErro(msg_info)
                else:
                    sku = self.alt_loc_txt_mat.text()
                    centro = self.alt_loc_txt_cen.text()
                    deposito = self.alt_loc_txt_dep.text()
                    local = self.alt_loc_txt_pos_local.text()

                    if centro in self.cen_user:
                        status_alteracao = alterar_dados_sap_gui(status_conexao["session"], sku, centro, deposito, local)
                        
                        if status_alteracao["status"] == "OK":
                            status_conexao["conn"].CloseSession("ses[0]")
                            MsgFinalizado(f"Alteração realizada com sucesso conforme abaixo:\nMaterial: {sku}\nCentro: {centro}\nDepósito: {deposito}\nLocal: {local}")

                        elif status_alteracao["status"] == "ERRO":
                            status_conexao["conn"].CloseSession("ses[0]")
                            MsgErro(status_alteracao["MSG"])
                        else:
                            MsgErro(status_alteracao["MSG"])
                    else:
                        MsgErro(f"Usuário sem acesso ao centro {centro}.\nCentros liberados: {self.cen_user}")

            elif status_conexao["status"] == "ERRO_OPEN":
                MsgErro(status_conexao["MSG"])

            elif status_conexao["ERRO"] == "ERRO":
                status_alteracao["conn"].CloseSession("ses[0]")
                MsgErro(status_conexao["MSG"])
        else:
            MsgCancelado()

# Função atualizar tabela alteração massiva Pagina Alteração Posição Depósito
def atualizar_tabela(self):
    mat = self.cmb_mat.currentText()
    cen = self.cmb_cen.currentText()
    dep = self.cmb_dep.currentText()
    local = self.cmb_loc.currentText()

    for row in self.parent.df.index: 
        ultlinhatb = int(self.parent.alt_loc_tb_alt_massa.rowCount())                   
        self.parent.alt_loc_tb_alt_massa.setItem(ultlinhatb - 1, 0, QTableWidgetItem(str(self.parent.df.loc[row, mat]).strip()))
        self.parent.alt_loc_tb_alt_massa.setItem(ultlinhatb - 1, 1, QTableWidgetItem(str(self.parent.df.loc[row, cen]).strip()))
        self.parent.alt_loc_tb_alt_massa.setItem(ultlinhatb - 1, 2, QTableWidgetItem(str(self.parent.df.loc[row, dep]).strip()))
        self.parent.alt_loc_tb_alt_massa.setItem(ultlinhatb - 1, 3, QTableWidgetItem(str(self.parent.df.loc[row, local]).strip()))
        self.parent.alt_loc_tb_alt_massa.insertRow(ultlinhatb)

    
    msg_text = 'Importar Excel'
    msg_info = 'Arquivo Excel importado com sucesso!'
    MsgInformation(msg_text,  msg_info)

    self.close()



################ Funções Controle Pagina Controle acesso ###############
# Abrir formulário alteração usuário
def abrir_form_alt_user(self, tp):
    from controllers.interface import AlterarUsuario
    cen_adm = self.consulta_db['ADM']["CENTRO"].values

    if tp == "ALT":
        if self.cont_aces_tb_usuarios.selectedIndexes():
            row = self.cont_aces_tb_usuarios.selectedIndexes()[0].row()          
            id = self.cont_aces_tb_usuarios.item(row, 0).text()
            user = self.cont_aces_tb_usuarios.item(row, 1).text()
            nome = self.cont_aces_tb_usuarios.item(row, 2).text()
            cen = self.cont_aces_tb_usuarios.item(row, 3).text() 
            acesso =  self.cont_aces_tb_usuarios.item(row, 4).text()         
            self.form_alt_user = AlterarUsuario(self, tp, id, user, nome, cen, cen_adm, acesso)
            self.form_alt_user.show()

        else:
            MsgErro('Por gentileza selecionar o usuário para alteração!')

    elif tp == "CAD":
        self.form_alt_user = AlterarUsuario(self, tp=tp, cen_adm=cen_adm)
        self.form_alt_user.show()

# Alterar usuários 
def alterar_usuario(self):
    user_novo = self.txt_user.text()
    nome_novo = self.txt_nome.text()
    cen_novo = self.cmb_cen.currentText()
    ace_novo = self.cmb_acesso.currentText()

    if self.tp == "ALT":
        id_user = self.lb_id.text()
        status = db_alterar_usuario(id_user, user_novo.upper(), nome_novo.upper(), cen_novo, ace_novo)
        if status["status"] == "OK":
            MsgFinalizado(status["MGS"])
            self.close()
            atualizar_tabela_usuarios_controle_acesso(self.parent)
            
        else:
            MsgErro(status["MGS"])

    elif self.tp == "CAD":
        status = db_incluir_usuario(user_novo.upper(), nome_novo.upper(), cen_novo, ace_novo)
        if status["status"] == "OK":
            MsgFinalizado(status["MGS"])
            self.close()
            atualizar_tabela_usuarios_controle_acesso(self.parent)
        else:
            MsgErro(status["MGS"])

# Excluir usuário 
def exluir_usuario(self):
    if self.cont_aces_tb_usuarios.selectedIndexes():
        row = self.cont_aces_tb_usuarios.selectedIndexes()[0].row()
        id = self.cont_aces_tb_usuarios.item(row, 0).text()
        user = self.cont_aces_tb_usuarios.item(row, 1).text()
        nome = self.cont_aces_tb_usuarios.item(row, 2).text()
        msg_info = f'Deseja realmente excluir o usuário conforme abaixo?\nUsuário: {user}\nNome: {nome}'
        resp = MsgQuestion(msg_info)
        if resp == 16384:
            status = db_excluir_usuario(id)

            atualizar_tabela_usuarios_controle_acesso(self)            

            MsgInformation("", status["MSG"])

    else:
        MsgErro('Por gentileza selecionar o usuário para eliminação!')

# # Exibir e ocultar senha
# def exibir_ocultar_senha(self):
#     if self.btn_visivel.isChecked():
#         # Se o botão estiver marcado, mostrar o texto
#         self.txt_senha.setEchoMode(QLineEdit.Normal)            
#     else:
#         # Se o botão não estiver marcado, ocultar o texto
#         self.txt_senha.setEchoMode(QLineEdit.Password)

# # Criar um arquivo novo
# def criar_arquivo_configuracao(self):                
#     emai_login = 'E-mail login;' if self.txt_email_login.text() == '' else ''
#     emai_envio = 'E-mail envio;' if self.txt_email_envio.text() == '' else ''
#     senha = 'Senha e-mail;' if self.txt_senha.text() == '' else ''
    
#     txt = f'{emai_login}{emai_envio}{senha}'
#     txt = '\n'.join(txt.split(';'))
#     if txt != "":
#         msg_info = f'Por gentilezar preencher o(s) campo(s):\n\n{txt}'
#         MsgErro(msg_info)

#     else:
#         # Obter o caminho para o diretório AppData\Local\Programs
#         appdata_local_programs_path = os.path.join(os.environ['LOCALAPPDATA'], 'Programs')
#         # Nome da nova pasta a ser criada
#         nova_pasta = 'Configuracoes Almox'
#         # Caminho completo para a nova pasta
#         caminho_nova_pasta = os.path.join(appdata_local_programs_path, nova_pasta)
#         if not os.path.exists(caminho_nova_pasta):
#             os.makedirs(caminho_nova_pasta)

#         # Nome do arquivo TXT para senhas e configurações
#         arquivo_config = 'configuracoes.json'

#         # Caminho completo para o arquivo
#         caminho_arquivo_config = os.path.join(caminho_nova_pasta, arquivo_config)

#         # Verificar se o arquivo já existe antes de criá-lo
#         dados = {
#             "EmailLogin": self.txt_email_login.text(), 
#             "EmailSend": self.txt_email_envio.text(), 
#             "Senha": self.txt_senha.text(),
#             "Porta": self.txt_porta.text(),
#             }
        
#         # Criar e escrever no arquivo
#         with open(caminho_arquivo_config, 'w') as arquivo:
#             json.dump(dados, arquivo, indent=2)

#         # self.parent.pgs_principal.setCurrentWidget(self.parent.pg_alt_dep)
#         self.parent.btn_home.setVisible(True)
#         validar_acesso(self.parent)

#         self.close()

# # Adicionar configuração incial do sistema
# def configuracao_inicial(self):
#     # Obter o caminho para o diretório AppData\Local\Programs
#     appdata_local_programs_path = os.path.join(os.environ['LOCALAPPDATA'], 'Programs')
#     # Nome da nova pasta a ser criada
#     novo_arquivo = 'Configuracoes Almox\configuracoes.json'
#     # Caminho completo para a nova pasta
#     caminho_arquivo_json = os.path.join(appdata_local_programs_path, novo_arquivo)
#     # Verificar se a pasta já existe antes de criá-la
#     if not os.path.exists(caminho_arquivo_json):
#         self.pgs_principal.setCurrentWidget(self.pg_notificacao)
#         self.lb_notificacao.setText(f"Realizar a cofiguração inícial!")
#         self.btn_home.setVisible(False)
#         # Abrir interface para configuração inicial
#         from controllers.interface import ConfiguracaoInical
#         self.form_config_inicial = ConfiguracaoInical(self)
#         self.form_config_inicial.show()
        
#     else:
#         validar_acesso(self)
        

# # Alterar configuração incial do sistema
# def alterar_configuracao_inicial(self):
#     self.pgs_principal.setCurrentWidget(self.pg_notificacao)
#     self.lb_notificacao.setText(f"Realizar a cofiguração inícial!")
#     self.btn_home.click()
#     # Obter o caminho para o diretório AppData\Local\Programs
#     appdata_local_programs_path = os.path.join(os.environ['LOCALAPPDATA'], 'Programs')
#     # Nome da nova pasta a ser criada
#     novo_arquivo = 'Configuracoes Almox\configuracoes.json'
#     # Caminho completo para a nova pasta
#     self.caminho_arquivo_json = os.path.join(appdata_local_programs_path, novo_arquivo)

#     from controllers.interface import ConfiguracaoInical
#     self.form_config_inicial = ConfiguracaoInical(self, "ALT")
#     self.form_config_inicial.show()

# Consultar usuário conectado
def validar_acesso(self):    
    self.cont_aces_tb_usuarios.clearContents()
    self.cont_aces_tb_usuarios.setRowCount(0)
    self.acesso = "OK"
    self.cen_user = ""
    user = os.getlogin().upper()
    self.consulta_db = db_consulta_usuarios(user)
    if self.consulta_db["status"] == "OK":
        if len(self.consulta_db['ADM']) > 0:
            self.home_btn_cont_acesso.setVisible(True)
            self.cen_user = self.consulta_db['ADM']['CENTRO'].values
            self.cont_aces_lb_user_resp.setText(f"Usuário: {self.consulta_db['ADM'].loc[0, 'NOME']}\nCentro Liberado: {', '.join(self.cen_user)}")

            self.alt_loc_lb_dados_user.setText(f"Usuário: {self.consulta_db['ADM'].loc[0, 'NOME']}\nCentro Liberado: {', '.join(self.cen_user)}")
            
            if len(self.consulta_db["USUARIOS"]) > 0:
                for row in self.consulta_db["USUARIOS"].index: 
                    ultlinhatb = int(self.cont_aces_tb_usuarios.rowCount())
                    self.cont_aces_tb_usuarios.setRowCount(ultlinhatb+1)
                    self.cont_aces_tb_usuarios.setItem(ultlinhatb, 0, QTableWidgetItem(str(self.consulta_db["USUARIOS"].loc[row, "ID"])))
                    self.cont_aces_tb_usuarios.setItem(ultlinhatb, 1, QTableWidgetItem(str(self.consulta_db["USUARIOS"].loc[row, "USER"])))
                    self.cont_aces_tb_usuarios.setItem(ultlinhatb, 2, QTableWidgetItem(str(self.consulta_db["USUARIOS"].loc[row, "NOME"])))
                    self.cont_aces_tb_usuarios.setItem(ultlinhatb, 3, QTableWidgetItem(str(self.consulta_db["USUARIOS"].loc[row, "CENTRO"])))
                    self.cont_aces_tb_usuarios.setItem(ultlinhatb, 4, QTableWidgetItem(str(self.consulta_db["USUARIOS"].loc[row, "ACESSO"])))

                valores_a_filtrar = "', '".join(self.cen_user)
                data = datetime.now()
                mes_ano = f"{calendar.month_name[data.month].upper()}/{data.year}"
                self.nao_atend_lb_dec_cen_mes.setText(f"CONTROLE DE MATERIAL NÃO ATENDIDO - CENTRO {valores_a_filtrar} - {mes_ano}")

                # Dimensionar tabela
                cont_aces_tb_usuarios = self.cont_aces_tb_usuarios.horizontalHeader()
                cont_aces_tb_usuarios.setSectionResizeMode(QHeaderView.ResizeToContents)

                if "ALMOX" in self.consulta_db['ADM']["ACESSO"].unique():
                    self.home_btn_alt_local.setVisible(True)
                    self.home_btn_nao_atendidos.setVisible(True)
                                        
                elif "GERAL" in self.consulta_db['ADM']["ACESSO"].unique():
                    self.home_btn_alt_local.setVisible(True)
                    self.home_btn_nao_atendidos.setVisible(True)

                elif "PLAN" in self.consulta_db['ADM']["ACESSO"].unique():
                    self.home_btn_nao_atendidos.setVisible(True)


        else:
            self.home_btn_cont_acesso.setVisible(False)
            if len(self.consulta_db["USUARIOS"]) == 0:
                self.acesso = ""
                self.pgs_principal.setCurrentWidget(self.pg_notificacao)
                self.lb_notificacao.setText(f"Usuário {user} sem acesso, por gentileza verificar com seu superior!")
                self.btn_home.setVisible(False)
                self.lb_titulo.setText("Gerenciador Almoxarifado")
            else:
                if self.consulta_db["USUARIOS"].loc[row, "ACESSO"] == "ALMOX":
                    self.home_btn_alt_local.setVisible(True)
                    self.home_btn_nao_atendidos.setVisible(True)
                    self.cen_user = self.consulta_db['USUARIOS']['CENTRO'].values
                    self.alt_loc_lb_dados_user.setText(f"Usuário: {self.consulta_db['USUARIOS'].loc[0, 'NOME']}\nCentro Liberado: {', '.join(self.cen_user)}")

                    valores_a_filtrar = "', '".join(self.cen_user)
                    data = datetime.now()
                    mes_ano = f"{calendar.month_name[data.month].upper()}/{data.year}"
                    self.nao_atend_lb_dec_cen_mes.setText(f"CONTROLE DE MATERIAL NÃO ATENDIDO - CENTRO {valores_a_filtrar} - {mes_ano}") 


def atualizar_tabela_usuarios_controle_acesso(self):
    self.cont_aces_tb_usuarios.clearContents()
    self.cont_aces_tb_usuarios.setRowCount(0)
    user = os.getlogin().upper()
    self.consulta_db = db_consulta_usuarios(user)
    if self.consulta_db["status"] == "OK":
        if len(self.consulta_db["USUARIOS"]) > 0:
            for row in self.consulta_db["USUARIOS"].index: 
                ultlinhatb = int(self.cont_aces_tb_usuarios.rowCount())
                self.cont_aces_tb_usuarios.setRowCount(ultlinhatb+1)
                self.cont_aces_tb_usuarios.setItem(ultlinhatb, 0, QTableWidgetItem(str(self.consulta_db["USUARIOS"].loc[row, "ID"])))
                self.cont_aces_tb_usuarios.setItem(ultlinhatb, 1, QTableWidgetItem(str(self.consulta_db["USUARIOS"].loc[row, "USER"])))
                self.cont_aces_tb_usuarios.setItem(ultlinhatb, 2, QTableWidgetItem(str(self.consulta_db["USUARIOS"].loc[row, "NOME"])))
                self.cont_aces_tb_usuarios.setItem(ultlinhatb, 3, QTableWidgetItem(str(self.consulta_db["USUARIOS"].loc[row, "CENTRO"])))
                self.cont_aces_tb_usuarios.setItem(ultlinhatb, 4, QTableWidgetItem(str(self.consulta_db["USUARIOS"].loc[row, "ACESSO"])))

            self.cont_aces_tb_usuarios.setColumnHidden(0, True)

################ Funções controle interface Não Atendidos ###############
# Abrir formulário Não Atendidos
def abrir_form_nao_atendidos(self, tp):
    from controllers.interface import NaoAtendidos
    if tp == "ALT":
        if self.nao_atend_tb_registros.selectedIndexes():
            row = self.nao_atend_tb_registros.selectedIndexes()[0].row()
            if self.nao_atend_tb_registros.item(row, 38).text() == "":                
                id_alt = self.nao_atend_tb_registros.item(row, 0).text()
                self.nao_atendidos = NaoAtendidos(self, tp=tp, id_alt=id_alt)
                self.nao_atendidos.btn_salvar_novo.setVisible(False)
                self.nao_atendidos.txt_data.setText(str(self.nao_atend_tb_registros.item(row, 1).text()))
                self.nao_atendidos.txt_hora.setText(str(self.nao_atend_tb_registros.item(row, 2).text()))
                self.nao_atendidos.txt_mat.setText(str(self.nao_atend_tb_registros.item(row, 3).text()))
                self.nao_atendidos.txt_decricao.setText(str(self.nao_atend_tb_registros.item(row, 4).text()))
                self.nao_atendidos.txt_und_med.setText(str(self.nao_atend_tb_registros.item(row, 5).text()))
                self.nao_atendidos.txt_solicitante.setText(str(self.nao_atend_tb_registros.item(row, 6).text()))
                self.nao_atendidos.txt_ramal.setText(str(self.nao_atend_tb_registros.item(row, 7).text()))
                self.nao_atendidos.cmb_setor.setCurrentText(str(self.nao_atend_tb_registros.item(row, 8).text()))

                obs_almox = self.nao_atend_tb_registros.item(row, 9).text().split(". &")
                self.nao_atendidos.txt_obs_almox.setText(str(obs_almox[0]))
                if len(obs_almox) == 2:
                    self.nao_atendidos.lb_info.setVisible(True)
                    self.nao_atendidos.lb_info.setText(str(obs_almox[1]))
                    if "Não Amp." in obs_almox[1]:
                        self.nao_atendidos.cmb_cod_sit.setDisabled(True)


                self.nao_atendidos.txt_qt_solicitada.setText(str(self.nao_atend_tb_registros.item(row, 10).text()))

                status_erp_geral = self.nao_atend_tb_registros.item(row, 11).text()
                if status_erp_geral == "VB":
                    self.nao_atendidos.txt_tp_mrp.setStyleSheet("background-color: #00c300;")
                else:
                    self.nao_atendidos.txt_tp_mrp.setStyleSheet("background-color: red;")
                self.nao_atendidos.txt_tp_mrp.setText(str(status_erp_geral))

                self.nao_atendidos.txt_minimo.setText(str(self.nao_atend_tb_registros.item(row, 12).text()))
                self.nao_atendidos.txt_maximo.setText(str(self.nao_atend_tb_registros.item(row, 13).text()))
                self.nao_atendidos.txt_grp_plan.setText(str(self.nao_atend_tb_registros.item(row, 14).text()))
                self.nao_atendidos.txt_plan.setText(str(self.nao_atend_tb_registros.item(row, 15).text()))
                self.nao_atendidos.txt_critico.setText(str(self.nao_atend_tb_registros.item(row, 16).text()))
                self.nao_atendidos.txt_cons_fint.setText(str(self.nao_atend_tb_registros.item(row, 17).text()))

                status_erp_geral = self.nao_atend_tb_registros.item(row, 18).text()
                if status_erp_geral in ["", "Z2"]:
                    self.nao_atendidos.txt_status_erp_geral.setStyleSheet("background-color: #00c300;")
                else:
                    self.nao_atendidos.txt_status_erp_geral.setStyleSheet("background-color: red;")
                self.nao_atendidos.txt_status_erp_geral.setText(str(status_erp_geral))

                status_erp_cen = self.nao_atend_tb_registros.item(row, 19).text()
                if status_erp_cen in ["", "Z2"]:
                    self.nao_atendidos.txt_status_erp_cen.setStyleSheet("background-color: #00c300;")
                else:
                    self.nao_atendidos.txt_status_erp_cen.setStyleSheet("background-color: red;")
                self.nao_atendidos.txt_status_erp_cen.setText(str(status_erp_cen))

                saldo_sistema = self.nao_atend_tb_registros.item(row, 20).text()
                if float(saldo_sistema) > 0:
                    self.nao_atendidos.txt_saldo_sistema.setStyleSheet("background-color: #00c300;")
                else:
                    self.nao_atendidos.txt_saldo_sistema.setStyleSheet("background-color: red;")
                self.nao_atendidos.txt_saldo_sistema.setText(str(saldo_sistema))

                self.nao_atendidos.txt_saldo_fisico.setText(str(self.nao_atend_tb_registros.item(row, 21).text()))
                self.nao_atendidos.txt_segunda_cont.setText(str(self.nao_atend_tb_registros.item(row, 22).text()))
                self.nao_atendidos.txt_bloqueado.setText(str(self.nao_atend_tb_registros.item(row, 23).text()))
                self.nao_atendidos.txt_req_manual.setText(str(self.nao_atend_tb_registros.item(row, 24).text()))
                self.nao_atendidos.txt_devergencia.setText(str(self.nao_atend_tb_registros.item(row, 25).text()))
                self.nao_atendidos.txt_total_proc.setText(str(self.nao_atend_tb_registros.item(row, 26).text()))
                self.nao_atendidos.txt_valor_unit.setText(str(self.nao_atend_tb_registros.item(row, 27).text()))
                self.nao_atendidos.txt_grp_comp.setText(str(self.nao_atend_tb_registros.item(row, 28).text()))
                self.nao_atendidos.txt_comprador.setText(str(self.nao_atend_tb_registros.item(row, 29).text()))
                self.nao_atendidos.cmb_cod_sit.setCurrentText(str(self.nao_atend_tb_registros.item(row, 30).text()))
                self.nao_atendidos.cmb_sit_ped.setCurrentText(str(self.nao_atend_tb_registros.item(row, 31).text()))

                self.nao_atendidos.ptxt_nota_mat.setPlainText(str(self.nao_atend_tb_registros.item(row, 32).text()))

                dados = self.nao_atend_tb_registros.item(row, 33).text().split("\n")
                if dados[0] != "":
                    for dado in dados:
                        ultlinhatb = int(self.nao_atendidos.tb_proc_comp.rowCount())
                        dd = dado.split(" - ")
                        self.nao_atendidos.tb_proc_comp.insertRow(ultlinhatb)
                        self.nao_atendidos.tb_proc_comp.setItem(ultlinhatb, 0, QTableWidgetItem(str(dd[0])))
                        self.nao_atendidos.tb_proc_comp.setItem(ultlinhatb, 1, QTableWidgetItem(str(dd[1])))
                        self.nao_atendidos.tb_proc_comp.setItem(ultlinhatb, 2, QTableWidgetItem(str(dd[2])))
                        self.nao_atendidos.tb_proc_comp.setItem(ultlinhatb, 3, QTableWidgetItem(str(dd[3])))
                    
                self.nao_atendidos.show()
            
            else:
                MsgErro("Não é possivel alterar o registro selecionado, pois já foi realizado o envio do e-mail!")
        else:
            MsgErro("Por gentileza selecionar a linha a ser alterada!")
    else:
        # consulta_db_nao_atendidos(self)
        self.nao_atendidos = NaoAtendidos(self, tp)
        self.nao_atendidos.show()

# Consultar e alimentar os campos com os dados do SAP
def consulta_dados_sap(self):
    limpar_campo(self)
    sku = self.txt_mat.text()
    cen = self.parent.consulta_db["USUARIOS"].loc[0, "CENTRO"]
    status_consulta = consultar_nao_atendidos(sku, cen)  
    self.lista_pedidos = ""  
    if status_consulta["status"] == "OK":
        self.txt_decricao.setText(str(status_consulta["descricao"]))
        self.txt_und_med.setText(str(status_consulta["und_med"]))        
        self.txt_minimo.setText(str(status_consulta["minimo"]))
        self.txt_maximo.setText(str(status_consulta["maximo"]))

        status_erp_geral = status_consulta["tp_mrp"]
        if status_erp_geral == "VB":
            self.txt_tp_mrp.setStyleSheet("background-color: #00c300;")
        else:
            self.txt_tp_mrp.setStyleSheet("background-color: red;")
        self.txt_tp_mrp.setText(str(status_erp_geral))

        self.txt_grp_plan.setText(str(status_consulta["grp_plan"]))
        self.txt_plan.setText(str(status_consulta["plan_mrp"]))
        self.txt_critico.setText(str(status_consulta["critico"]))
        self.txt_cons_fint.setText(str(status_consulta["cons_fint"]))


        status_erp_geral = status_consulta["status_erp_geral"]
        if status_erp_geral in ["", "Z2"]:
            self.txt_status_erp_geral.setStyleSheet("background-color: #00c300;")
        else:
            self.txt_status_erp_geral.setStyleSheet("background-color: red;")
        self.txt_status_erp_geral.setText(str(status_erp_geral))


        status_erp_cen = status_consulta["status_erp_cen"]
        if status_erp_cen in ["", "Z2"]:
            self.txt_status_erp_cen.setStyleSheet("background-color: #00c300;")
        else:
            self.txt_status_erp_cen.setStyleSheet("background-color: red;")
        self.txt_status_erp_cen.setText(str(status_erp_cen))


        saldo_sistema = status_consulta["saldo_sist"]
        if float(saldo_sistema) > 0:
            self.txt_saldo_sistema.setStyleSheet("background-color: #00c300;")
        else:
            self.txt_saldo_sistema.setStyleSheet("background-color: red;")
        self.txt_saldo_sistema.setText(str(saldo_sistema))

        self.txt_bloqueado.setText(str(status_consulta["bloqueado"]))

        self.txt_valor_unit.setText(str(status_consulta["valor_unit"]))
        self.txt_grp_comp.setText(str(status_consulta["grp_comp"]))
        self.txt_comprador.setText(str(status_consulta["comprador"]))
        self.ptxt_nota_mat.setPlainText(str(status_consulta["nota_material"]))
        
        if len(status_consulta["lista_pedidos"]) > 0:
            self.lista_pedidos = status_consulta["lista_pedidos"]
            df_dados_na = pd.DataFrame(status_consulta["lista_pedidos"], columns=["DATA", "STATUS", "TP_PROC", "PROC_COMP"])
            df_dados_na.sort_values(by="STATUS", ignore_index=True, inplace=True)            
            for i in df_dados_na.index:
                ultlinhatb = int(self.tb_proc_comp.rowCount())
                self.tb_proc_comp.insertRow(ultlinhatb)
                self.tb_proc_comp.setItem(ultlinhatb, 0, QTableWidgetItem(str(df_dados_na.loc[i, "DATA"]).strip()))
                self.tb_proc_comp.setItem(ultlinhatb, 1, QTableWidgetItem(str(df_dados_na.loc[i, "STATUS"]).strip()))
                self.tb_proc_comp.setItem(ultlinhatb, 2, QTableWidgetItem(str(df_dados_na.loc[i, "TP_PROC"]).strip()))
                self.tb_proc_comp.setItem(ultlinhatb, 3, QTableWidgetItem(str(df_dados_na.loc[i, "PROC_COMP"]).strip()))

        self.txt_total_proc.setText(str(self.tb_proc_comp.rowCount()))   
        self.cmb_cod_sit.setDisabled(False)
        self.lb_info.setVisible(False)
    else:
        if status_consulta["status"] == "SEM_AMP":
            self.lb_info.setVisible(True)
            self.lb_info.setText(str(status_consulta["MSG"]))
            self.txt_decricao.setText(str(status_consulta["descricao"]))
            self.txt_und_med.setText(str(status_consulta["und_med"]))
            self.cmb_cod_sit.setCurrentText("OC - Material de Outro Centro")
            self.cmb_cod_sit.setDisabled(True)

            status_erp_geral = status_consulta["status_erp_geral"]
            if status_erp_geral in ["", "Z2"]:
                self.txt_status_erp_geral.setStyleSheet("background-color: #00c300;")
            else:
                self.txt_status_erp_geral.setStyleSheet("background-color: red;")
            self.txt_status_erp_geral.setText(str(status_erp_geral)) 

            self.txt_saldo_sistema.setText(str(0))
            self.txt_saldo_fisico.setText(str(0))
            self.txt_segunda_cont.setText(str(0))
            MsgErro(status_consulta["MSG"])
        else:
            MsgErro(status_consulta["MSG"])
            
# Atualizar o campo divergencia
def campo_divergencia(self):
    saldo_sist = float(self.txt_saldo_sistema.text()) if self.txt_saldo_fisico.text() != "" else float(0)
    saldo_seg_cont = float(self.txt_segunda_cont.text().replace(".", "").replace(",", ".")) if self.txt_segunda_cont.text() != "" else float(0)
    # saldo_bloq = float(self.txt_bloqueado.text().replace(".", "").replace(",", ".")) if self.txt_bloqueado.text() != ""  else float(0)
    saldo_req_manual = float(self.txt_req_manual.text().replace(".", "").replace(",", ".")) if self.txt_req_manual.text() != ""  else float(0)        
    diverg = saldo_sist - saldo_seg_cont - saldo_req_manual
    self.txt_devergencia.setText(str(diverg))

# Adicionar registro no banco de dados
def incluir_registrar_nao_atendidos(self, btn_sinal=""):
    valid = []
    valid.append(f"Data") if self.txt_data.text() == "" else ...
    valid.append(f"Data Inválida") if len(self.txt_data.text()) != 10 else ...
    valid.append(f"Hora") if self.txt_hora.text() == "" else ...
    
    valid.append(f"Código Mat.") if self.txt_mat.text() == "" else ...
    
    valid.append(f"Solicitante") if self.txt_solicitante.text() == "" else ...
    valid.append(f"Ramal") if self.txt_ramal.text() == "" else ...
    valid.append(f"Setor") if self.cmb_setor.currentText() == "" else ...

    valid.append(f"Qt. Solic.") if self.txt_qt_solicitada.text() == "" else ...
    
    valid.append(f"Saldo Físico") if self.txt_saldo_fisico.text() == "" else ...
    valid.append(f"2ª Cont.") if self.txt_segunda_cont.text() == "" else ...
    
    valid.append(f"Req.Man.") if self.txt_req_manual.text() == "" else ...
    
    if len(valid) == 0:
        data = datetime.strptime(self.txt_data.text(), '%d.%m.%Y').strftime('%Y.%m.%d')
        hora = self.txt_hora.text()
        cod_mat = self.txt_mat.text()
        desc = self.txt_decricao.text()
        un_med = self.txt_und_med.text()
        solicitante = self.txt_solicitante.text()
        ramal = self.txt_ramal.text()
        setor = self.cmb_setor.currentText()
        obs_almox = []
        obs_almox.append(self.txt_obs_almox.text())
        obs_almox.append(self.lb_info.text())
        obs_almox = ". &".join(obs_almox)

        qt_solic = self.txt_qt_solicitada.text()
        tp_mrp = self.txt_tp_mrp.text()
        minimo = self.txt_minimo.text()
        maximo = self.txt_maximo.text()
        grp_plan = self.txt_grp_plan.text()
        nome_plan = self.txt_plan.text()
        crit = self.txt_critico.text()
        cons_fint = self.txt_cons_fint.text()
        st_erp_geral = self.txt_status_erp_geral.text()
        st_erp_cen = self.txt_status_erp_cen.text()
        saldo_sist = self.txt_saldo_sistema.text()
        saldo_fisico = self.txt_saldo_fisico.text()
        seg_cont = self.txt_segunda_cont.text()
        bloq = self.txt_bloqueado.text()
        req_man = self.txt_req_manual.text()
        diverg = self.txt_devergencia.text()
        n_proc_comp = self.txt_total_proc.text()
        valor_unit = self.txt_valor_unit.text()
        grp_comp = self.txt_grp_comp.text()
        nome_comp = self.txt_comprador.text()
        cod_sit = self.cmb_cod_sit.currentText()
        sit_ped = self.cmb_sit_ped.currentText()
        nota_mat = self.ptxt_nota_mat.toPlainText()

        str_lista_pedidos = [" - ".join(sublista) for sublista in self.lista_pedidos]
        str_result = '\n'.join(str_lista_pedidos)
        sit_proc_comp = str_result

        acao_plan = ''
        user = os.getlogin().upper()
        data_atual = datetime.now()
        data_registro = datetime.strftime(data_atual, "%d/%m/%Y")
        
        dados = [data, hora, cod_mat, desc, un_med, solicitante, ramal, setor, obs_almox, qt_solic, tp_mrp, minimo, maximo, grp_plan, nome_plan, crit, cons_fint, st_erp_geral, st_erp_cen, saldo_sist, saldo_fisico, seg_cont, bloq, req_man, diverg, n_proc_comp, valor_unit, grp_comp, nome_comp, cod_sit, sit_ped, nota_mat, sit_proc_comp, acao_plan, self.cen_user[0], user, data_registro]

        status = db_incluir_nao_atendidos(dados)
        if status["status"] == "OK":
            limpar_campo(self)
            self.txt_mat.setText("")
            consulta_db_nao_atendidos(self.parent)
            if btn_sinal == "SALVAR_SAIR":
                self.close()

        MsgFinalizado(status["MSG"])
    else:
        valid = "\n".join(valid)
        msg_info = f"Por gentileza preencher todos os campos conforme abaixo:\n{valid}"
        MsgErro(msg_info)

# Alterar o registro não atendidos
def alterar_registrar_nao_atendidos(self, btn_sinal=""):
    valid = []
    valid.append(f"Data") if self.txt_data.text() == "" else ...
    valid.append(f"Hora") if self.txt_hora.text() == "" else ...
    valid.append(f"Código Mat.") if self.txt_mat.text() == "" else ...
    
    valid.append(f"Solicitante") if self.txt_solicitante.text() == "" else ...
    valid.append(f"Ramal") if self.txt_ramal.text() == "" else ...
    valid.append(f"Setor") if self.cmb_setor.currentText() == "" else ...

    valid.append(f"Qt. Solic.") if self.txt_qt_solicitada.text() == "" else ...
    
    valid.append(f"Saldo Físico") if self.txt_saldo_fisico.text() == "" else ...
    valid.append(f"2ª Cont.") if self.txt_segunda_cont.text() == "" else ...
    
    valid.append(f"Req.Man.") if self.txt_req_manual.text() == "" else ...
    
    if len(valid) == 0:
        data = datetime.strptime(self.txt_data.text(), '%d.%m.%Y').strftime('%Y.%m.%d')
        hora = self.txt_hora.text()
        cod_mat = self.txt_mat.text()
        desc = self.txt_decricao.text()
        un_med = self.txt_und_med.text()
        solicitante = self.txt_solicitante.text()
        ramal = self.txt_ramal.text()
        setor = self.cmb_setor.currentText()
        obs_almox = []
        obs_almox.append(self.txt_obs_almox.text())
        obs_almox.append(self.lb_info.text())
        obs_almox = ". &".join(obs_almox)

        qt_solic = self.txt_qt_solicitada.text()
        tp_mrp = self.txt_tp_mrp.text()
        minimo = self.txt_minimo.text()
        maximo = self.txt_maximo.text()
        grp_plan = self.txt_grp_plan.text()
        nome_plan = self.txt_plan.text()
        crit = self.txt_critico.text()
        cons_fint = self.txt_cons_fint.text()
        st_erp_geral = self.txt_status_erp_geral.text()
        st_erp_cen = self.txt_status_erp_cen.text()
        saldo_sist = self.txt_saldo_sistema.text()
        saldo_fisico = self.txt_saldo_fisico.text()
        seg_cont = self.txt_segunda_cont.text()
        bloq = self.txt_bloqueado.text()
        req_man = self.txt_req_manual.text()
        diverg = self.txt_devergencia.text()
        n_proc_comp = self.txt_total_proc.text()
        valor_unit = self.txt_valor_unit.text()
        grp_comp = self.txt_grp_comp.text()
        nome_comp = self.txt_comprador.text()
        cod_sit = self.cmb_cod_sit.currentText()
        sit_ped = self.cmb_sit_ped.currentText()
        nota_mat = self.ptxt_nota_mat.toPlainText()

        lista_pedidos = []
        for row in range(self.tb_proc_comp.rowCount()):
            self.tb_proc_comp.item(row, 0)
            lista_pedidos.append([self.tb_proc_comp.item(row, 0).text(), self.tb_proc_comp.item(row, 1).text(), self.tb_proc_comp.item(row, 2).text(), self.tb_proc_comp.item(row, 3).text()])

        str_lista_pedidos = [" - ".join(sublista) for sublista in lista_pedidos]
        str_result = '\n'.join(str_lista_pedidos)
        sit_proc_comp = str_result

        acao_plan = ''
        user = os.getlogin().upper()
        data_atual = datetime.now()
        data_registro = datetime.strftime(data_atual, "%d/%m/%Y")
        
        dados = [data, hora, cod_mat, desc, un_med, solicitante, ramal, setor, obs_almox, qt_solic, tp_mrp, minimo, maximo, grp_plan, nome_plan, crit, cons_fint, st_erp_geral, st_erp_cen, saldo_sist, saldo_fisico, seg_cont, bloq, req_man, diverg, n_proc_comp, valor_unit, grp_comp, nome_comp, cod_sit, sit_ped, nota_mat, sit_proc_comp, acao_plan, self.cen_user[0], user, data_registro]

        status = db_alterar_nao_atendidos(self.id, dados)

        if status["status"] == "OK":
            limpar_campo(self)
            self.txt_mat.setText("")
            consulta_db_nao_atendidos(self.parent)
            if btn_sinal == "SALVAR_SAIR":
                self.close()

        MsgFinalizado(status["MSG"])
    else:
        valid = "\n".join(valid)
        msg_info = f"Por gentileza preencher todos os campos conforme abaixo:\n{valid}"
        MsgErro(msg_info)

# Excluir registro não atendidos
def excluir_registrar_nao_atendidos(self):
    if self.nao_atend_tb_registros.selectedIndexes():
        row = self.nao_atend_tb_registros.selectedIndexes()[0].row()
        if self.nao_atend_tb_registros.item(row, 38).text() == "":
            confirmar = MsgQuestion("Deseja realmente excluir a linha selecionada?")
            if confirmar == 16384:                         
                id_db = self.nao_atend_tb_registros.item(row, 0).text()
                status = db_excluir_nao_atendidos(id_db)
                if status["status"] == "OK":
                    self.nao_atend_tb_registros.removeRow(row)
                    MsgFinalizado(status["MSG"])
                else:
                    MsgErro(", ".join(status["MSG"]))
        else:
            MsgErro("Não é possivel excluir o registro selecionado, pois já foi realizado o envio do e-mail!") 

    else:
        MsgErro("Por gentileza selecionar uma linha para eliminação!")

# Configuração incial pagina não atendidos
def iniciar_pg_nao_atendidos(self):
    valores_a_filtrar = "', '".join(self.cen_user)
    consulta_sql = f"WHERE CENTRO IN ('{valores_a_filtrar}')"
    self.status_consulta = db_consultar_nao_atendidos(consulta_sql)
    if self.status_consulta["status"] == "OK":
        if len(self.status_consulta["DADOS"]) > 0:
            def mes_ano(valor):
                data = datetime.strptime(valor, "%Y.%m.%d")
                return f"{str(data.month).zfill(2)}-{data.year}"                
            self.status_consulta["DADOS"]["MES_ANO"] = self.status_consulta["DADOS"]["DATA"].apply(mes_ano)
            self.lista_mes_ano = self.status_consulta["DADOS"].sort_values(by="MES_ANO", ascending=False)["MES_ANO"].unique()
            self.nao_atend_cmb_ano_mes.addItems(self.lista_mes_ano)

# Realizar a consulta do banco não atendidos
def consulta_db_nao_atendidos(self):
    locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')
    self.nao_atend_tb_registros.clearContents()
    self.nao_atend_tb_registros.setRowCount(0)
    valores_a_filtrar = "', '".join(self.cen_user)
    data = datetime.now()
    ano = data.year
    mes = data.month

    consulta_sql = f"WHERE CENTRO IN ('{valores_a_filtrar}')"
    if self.nao_atend_txt_material.text() != "":
        consulta_sql = f"{consulta_sql} AND COD_MAT = '{self.nao_atend_txt_material.text()}'"

    if self.nao_atend_cmb_acao_plan.currentText() == "OK":
        consulta_sql = f"{consulta_sql} AND ACAO_PLAN != ''"
    elif self.nao_atend_cmb_acao_plan.currentText() == "Pendente":
        consulta_sql = f"{consulta_sql} AND ACAO_PLAN == ''"

    if self.nao_atend_cmb_email.currentText() == "Enviado":
        consulta_sql = f"{consulta_sql} AND EMAIL != ''"
    elif self.nao_atend_cmb_email.currentText() == "Pendente":
        consulta_sql = f"{consulta_sql} AND EMAIL == ''"

    if self.nao_atend_cmb_ano_mes.currentText() != "":
        ano_mes_str = self.nao_atend_cmb_ano_mes.currentText()
        mes = int(ano_mes_str.split("-")[0])
        ano = int(ano_mes_str.split("-")[1])

        primeiro_dia = datetime(ano, mes, 1).strftime('%Y.%m.%d')
        ultimo_dia = datetime(ano, mes, calendar.monthrange(ano, mes)[1]).strftime('%Y.%m.%d')
        consulta_sql = f"{consulta_sql} AND DATA >= '{primeiro_dia}' AND DATA <= '{ultimo_dia}'"

    consulta_sql = f"{consulta_sql};"
    self.status_consulta = db_consultar_nao_atendidos(consulta_sql)
    if self.status_consulta["status"] == "OK":
        if len(self.status_consulta["DADOS"]) > 0:
            dados = self.status_consulta["DADOS"]

            dados['DATA'] = pd.to_datetime(dados['DATA'], format='%Y.%m.%d')
            dados['DATA'] = dados['DATA'].dt.strftime('%d.%m.%Y')
                        
            for r, row in enumerate(dados.index):
                ultlinhatb = int(self.nao_atend_tb_registros.rowCount())
                self.nao_atend_tb_registros.insertRow(ultlinhatb)
                for c, col in enumerate(dados.loc[row]):
                    self.nao_atend_tb_registros.setItem(r, c, QTableWidgetItem(str(col).strip()))

            self.nao_atend_tb_registros.setColumnHidden(0, True)
            self.nao_atend_lb_total_ocor.setText(str(len(self.status_consulta["DADOS"])))
            self.nao_atend_lb_itens_na.setText(str(len(self.status_consulta["DADOS"]["COD_MAT"].unique())))

            primeiro_dia = datetime(ano, mes, 1) - timedelta(days=1)
            primeiro_dia = datetime(primeiro_dia.year, primeiro_dia.month, 1)

            ultimo_dia = datetime(primeiro_dia.year, primeiro_dia.month, calendar.monthrange(primeiro_dia.year, primeiro_dia.month)[1])

            total_ocorrencia = db_consultar_nao_atendidos_total(f"WHERE CENTRO IN ('{valores_a_filtrar}') AND DATA >= '{primeiro_dia.strftime('%Y.%m.%d')}' AND DATA <= '{ultimo_dia.strftime('%Y.%m.%d')}'")

            if total_ocorrencia["status"] == "OK":
                total_ocorrencia = total_ocorrencia["DADOS"][0][0] if total_ocorrencia["DADOS"][0] is not None else 0
                self.nao_atend_lb_na_mes_ant.setText(str(total_ocorrencia))

        else:
            MsgInformation("", f"Não foi encontrado nenhum registro para o filtro selecionado!")
    else:
        MsgErro(self.status_consulta["MSG"])

# Limpar campos padrões
def limpar_campo(self):    
    self.txt_decricao.setText("")
    self.txt_und_med.setText("")
    self.txt_qt_solicitada.setText("")
    self.txt_tp_mrp.setText("")
    self.txt_minimo.setText("")
    self.txt_maximo.setText("")
    self.txt_grp_plan.setText("")
    self.txt_plan.setText("")
    self.txt_critico.setText("")
    self.txt_cons_fint.setText("")
    self.txt_status_erp_geral.setText("")
    self.txt_saldo_sistema.setText("")
    self.txt_saldo_fisico.setText("")
    self.txt_segunda_cont.setText("")
    self.txt_bloqueado.setText("")
    self.txt_req_manual.setText("")
    self.txt_devergencia.setText("")
    self.txt_total_proc.setText("")
    self.txt_valor_unit.setText("")
    self.txt_grp_comp.setText("")
    self.txt_comprador.setText("")
    self.ptxt_nota_mat.setPlainText("")
    self.lb_info.setText("")
    self.tb_proc_comp.clearContents()
    self.tb_proc_comp.setRowCount(0)
    
# Enviar e-mail
def enviar_email(self):
    confirmar = MsgQuestion("Deseja realmente enviar o e-mail para o Planejamento?")
    if confirmar == 16384: 
        import win32com.client
        valores_a_filtrar = "', '".join(self.cen_user)    
        consulta_sql = f"SELECT ID, COD_MAT, DESC, UN_MED, TP_MRP, MIN, MAX, SALDO_SIST, GRP_PLAN, NOME_PLAN, GRP_COMP, NOME_COMP, SIT_PROC_COMP FROM NAO_ATENDIDOS WHERE CENTRO IN ('{valores_a_filtrar}') AND EMAIL == ''"
        self.status_consulta = db_consultar_email_nao_atendidos(consulta_sql)
        if self.status_consulta["status"] == "OK":
            if len(self.status_consulta["DADOS"]) > 0:
                try:
                    df_email = self.status_consulta["DADOS"]
                    df_email['SIT_PROC_COMP'] = df_email['SIT_PROC_COMP'].replace('\n', '<br>', regex=True)
                    outlook_app = win32com.client.Dispatch("Outlook.Application")
                    for plan in df_email["GRP_PLAN"].unique():
                        status_email_envio = db_consultar_email_usuarios(plan, self.cen_user[0])
                        if status_email_envio["status"] == "OK":
                            i = df_email[df_email["GRP_PLAN"]==plan].index
                            id_db = df_email[df_email["GRP_PLAN"]==plan]["ID"].unique()
                            plan = df_email.loc[i, "NOME_PLAN"].unique()[0]
                            table_html = df_email.loc[i, ["COD_MAT", "DESC", "UN_MED", "TP_MRP", "MIN", "MAX", "SALDO_SIST", "GRP_PLAN", "GRP_COMP", "NOME_COMP", "SIT_PROC_COMP"]].to_html(escape=False, index=False)

                            mail = outlook_app.CreateItem(0) # 0 indica um novo e-mail
                            mail.Subject = f"Controle de Materiais Não Atendidos - Centro {valores_a_filtrar}"  

                            to_email = status_email_envio["PLAN"][1]
                            cc_email = f'{"; ".join(status_email_envio["CC"])};'

                            nome_pla = f"Prezado {plan.split()[0]}" if plan != "" else "Prezado Planejadores"

                            # Corpo do e-mail em formato HTML com a tabela
                            body = f"""
                            <html>
                                <head>
                                    <style>
                                        body {{
                                            font-family: 'Cambria', sans-serif; /* Substitua 'Arial' pela fonte desejada */
                                            font-size: 10pt;
                                        }}
                                        table {{
                                            border-collapse: collapse;
                                            background-color: #f2f2f2;
                                            width: 100%;
                                        }}
                                        th  {{                                        
                                            background-color: #00006c; 
                                            border-style: groove;
                                            padding: 2px 5px 2px 0px;
                                            color: white; 
                                            text-align: center;
                                            font-size: 9pt;
                                            }}
                                                                        
                                        td {{
                                            border: 1px solid #ffffff;
                                            border-style: groove;
                                            padding: 0px 2px 0px 2px;
                                            text-align: left;
                                            font-size: 9pt;
                                            white-space: nowrap;
                                        }}
                                        .coluna1 {{ width: 50px; }}
                                        .coluna2 {{ width: 230px; }}
                                        .coluna3 {{ width: 50px; }}
                                        .coluna4 {{ width: 50px; }}
                                        .coluna5 {{ width: 50px; }}
                                        .coluna6 {{ width: 50px; }}
                                        .coluna7 {{ width: 50px; }}
                                        .coluna8 {{ width: 50px; }}
                                        .coluna9 {{ width: 50px; }}
                                        .coluna10 {{ width: 100px; }}
                                        .coluna11 {{ width: 300px; }}
                                        
                                    </style>
                                </head>
                                <body>
                                    <p>{nome_pla},</p>
                                    <p>Houve inclusão de materiais no Não Atendidos que pode requerer uma ação sua.</p>
                                    {table_html}
                                    <br>
                                    <br>
                                    <p>Att.</p>
                                </body>
                            </html>
                            """
                            
                            mail.HTMLBody = body

                            mail.To = to_email
                            mail.CC = cc_email
                            # Enviar o e-mail
                            mail.Send()   

                            db_confirmar_envio_email_nao_atendidos(id_db)

                    MsgFinalizado(f"Envio de e-mail processado!")
                    consulta_db_nao_atendidos(self)

                except Exception as e:                    
                    MsgErro(f"Erro ao enviar o e-mail!\n{e}")
            else:
                MsgInformation("", "Sem pendencias de envio!")

        else:
            MsgErro(self.status_consulta["MSG"])

# Visualisar não atendidos
def visualisar_nao_atendidos(self):
    from controllers.interface import NaoAtendidosVisualisar
    if self.nao_atend_tb_registros.selectedIndexes():
        row = self.nao_atend_tb_registros.selectedIndexes()[0].row()
        self.nao_atendidos = NaoAtendidosVisualisar(self)
        self.nao_atendidos.txt_data.setText(str(self.nao_atend_tb_registros.item(row, 1).text()))
        self.nao_atendidos.txt_hora.setText(str(self.nao_atend_tb_registros.item(row, 2).text()))
        self.nao_atendidos.txt_mat.setText(str(self.nao_atend_tb_registros.item(row, 3).text()))
        self.nao_atendidos.txt_decricao.setText(str(self.nao_atend_tb_registros.item(row, 4).text()))
        self.nao_atendidos.txt_und_med.setText(str(self.nao_atend_tb_registros.item(row, 5).text()))
        self.nao_atendidos.txt_solicitante.setText(str(self.nao_atend_tb_registros.item(row, 6).text()))
        self.nao_atendidos.txt_ramal.setText(str(self.nao_atend_tb_registros.item(row, 7).text()))
        self.nao_atendidos.txt_setor.setText(str(self.nao_atend_tb_registros.item(row, 8).text()))

        obs_almox = self.nao_atend_tb_registros.item(row, 9).text().split(". &")
        self.nao_atendidos.txt_obs_almox.setText(str(obs_almox[0]))
        if len(obs_almox) == 2:
            self.nao_atendidos.lb_info.setVisible(True)
            self.nao_atendidos.lb_info.setText(str(obs_almox[1]))

        self.nao_atendidos.txt_qt_solicitada.setText(str(self.nao_atend_tb_registros.item(row, 10).text()))
        self.nao_atendidos.txt_tp_mrp.setText(str(self.nao_atend_tb_registros.item(row, 11).text()))
        self.nao_atendidos.txt_minimo.setText(str(self.nao_atend_tb_registros.item(row, 12).text()))
        self.nao_atendidos.txt_maximo.setText(str(self.nao_atend_tb_registros.item(row, 13).text()))
        self.nao_atendidos.txt_grp_plan.setText(str(self.nao_atend_tb_registros.item(row, 14).text()))
        self.nao_atendidos.txt_plan.setText(str(self.nao_atend_tb_registros.item(row, 15).text()))
        self.nao_atendidos.txt_critico.setText(str(self.nao_atend_tb_registros.item(row, 16).text()))
        self.nao_atendidos.txt_cons_fint.setText(str(self.nao_atend_tb_registros.item(row, 17).text()))
        self.nao_atendidos.txt_status_erp_geral.setText(str(self.nao_atend_tb_registros.item(row, 18).text()))
        self.nao_atendidos.txt_status_erp_cen.setText(str(self.nao_atend_tb_registros.item(row, 19).text()))

        self.nao_atendidos.txt_saldo_sistema.setText(str(self.nao_atend_tb_registros.item(row, 20).text()))
        self.nao_atendidos.txt_saldo_fisico.setText(str(self.nao_atend_tb_registros.item(row, 21).text()))
        self.nao_atendidos.txt_segunda_cont.setText(str(self.nao_atend_tb_registros.item(row, 22).text()))
        self.nao_atendidos.txt_bloqueado.setText(str(self.nao_atend_tb_registros.item(row, 23).text()))
        self.nao_atendidos.txt_req_manual.setText(str(self.nao_atend_tb_registros.item(row, 24).text()))
        self.nao_atendidos.txt_devergencia.setText(str(self.nao_atend_tb_registros.item(row, 25).text()))
        self.nao_atendidos.txt_total_proc.setText(str(self.nao_atend_tb_registros.item(row, 26).text()))
        self.nao_atendidos.txt_valor_unit.setText(str(self.nao_atend_tb_registros.item(row, 27).text()))
        self.nao_atendidos.txt_grp_comp.setText(str(self.nao_atend_tb_registros.item(row, 28).text()))
        self.nao_atendidos.txt_comprador.setText(str(self.nao_atend_tb_registros.item(row, 29).text()))
        self.nao_atendidos.txt_cod_sit.setText(str(self.nao_atend_tb_registros.item(row, 30).text()))
        self.nao_atendidos.txt_sit_pedido.setText(str(self.nao_atend_tb_registros.item(row, 31).text()))
        self.nao_atendidos.ptxt_nota_mat.setPlainText(str(self.nao_atend_tb_registros.item(row, 32).text()))
        self.nao_atendidos.ptxt_acao_plan.setPlainText(str(self.nao_atend_tb_registros.item(row, 34).text()))

        dados = self.nao_atend_tb_registros.item(row, 33).text().split("\n")
        if dados[0] != "":
            for dado in dados:
                ultlinhatb = int(self.nao_atendidos.tb_proc_comp.rowCount())
                dd = dado.split(" - ")
                self.nao_atendidos.tb_proc_comp.insertRow(ultlinhatb)
                self.nao_atendidos.tb_proc_comp.setItem(ultlinhatb, 0, QTableWidgetItem(str(dd[0])))
                self.nao_atendidos.tb_proc_comp.setItem(ultlinhatb, 1, QTableWidgetItem(str(dd[1])))
                self.nao_atendidos.tb_proc_comp.setItem(ultlinhatb, 2, QTableWidgetItem(str(dd[2])))
                self.nao_atendidos.tb_proc_comp.setItem(ultlinhatb, 3, QTableWidgetItem(str(dd[3])))
            
        self.nao_atendidos.show()

    else:
        MsgErro("Por gentileza selecionar a linha a ser alterada!")

# Gerar graficos
# Tratar Base de dados
def tratar_base_graficos(self):          
    # Função para formatar os rótulos do eixo y
    def formatar_rótulos_y(valor):
        return locale.format_string("%.0f", valor, grouping=True)
    def mes_ano(valor):
        ano = valor.year
        mes = str(valor.month).zfill(2)
        return f'{ano}-{mes}'
    def mes_str(valor):
        ano = valor.year
        mes = calendar.month_name[valor.month].upper()[:3]
        return f'{ano}-{mes}'
    
    if len(self.figures) > 0:
        for fig in self.figures:
            plt.close(fig)

    # Limpa a lista de figuras
    self.figures.clear()

    valores_a_filtrar = "', '".join(self.cen_user)
    consulta_sql = f"WHERE CENTRO IN ('{valores_a_filtrar}')"
    if self.rb_ano.isChecked():            
        status = db_consultar_base_grafico(consulta_sql)

    elif self.rb_mes.isChecked():
        if self.cmb_mes_ano.currentText() != "":
            ano_mes_str = self.cmb_mes_ano.currentText()
            mes = int(ano_mes_str.split("-")[0])
            ano = int(ano_mes_str.split("-")[1])
            primeiro_dia = datetime(ano, mes, 1).strftime('%Y.%m.%d')
            ultimo_dia = datetime(ano, mes, calendar.monthrange(ano, mes)[1]).strftime('%Y.%m.%d')
            consulta_sql = f"{consulta_sql} AND DATA >= '{primeiro_dia}' AND DATA <= '{ultimo_dia}'"
            status = db_consultar_base_grafico(consulta_sql)

    if status["status"] == "OK":
        df_valores = status["DADOS"]
        df_valores_gr = df_valores[['DATA', 'COD_MAT', 'CENTRO', 'CRIT', 'COD_SIT', 'SIT_PED', 'SETOR']].copy()
        df_valores_gr.loc[:, "CRIT"] = df_valores_gr.loc[:, "CRIT"].replace("", "Não")
        df_valores_gr["DATA"] = pd.to_datetime(df_valores_gr["DATA"])
        df_valores_gr["mes_str"] = df_valores_gr["DATA"].apply(mes_str)
        df_valores_gr["seq_mes_ano"] = df_valores_gr["DATA"].apply(mes_ano)
        

        if self.rb_ano.isChecked():
            df_base_gr = df_valores_gr.groupby(by=["seq_mes_ano", "mes_str"], as_index=False)["COD_MAT"].count()
            df_base_gr["label"] = df_base_gr["COD_MAT"].apply(formatar_rótulos_y)
            eixox = df_base_gr["mes_str"]
            eixoY = df_base_gr["COD_MAT"]
            rotulo = df_base_gr["label"]                
            gerar_grafico_geral(self, eixox, eixoY, rotulo)

        elif self.rb_mes.isChecked():
            df_base_gr = df_valores_gr.groupby(by=["SETOR"], as_index=False)["COD_MAT"].count()
            df_base_gr["label"] = df_base_gr["COD_MAT"].apply(formatar_rótulos_y)
            eixox = df_base_gr["SETOR"]
            eixoY = df_base_gr["COD_MAT"]
            rotulo = df_base_gr["label"]
            gerar_grafico_geral(self, eixox, eixoY, rotulo)

        atualizar_tabela_top(self, df_valores)
        gerar_grafico_total_ocor_item(self, df_valores)
        gerar_grafico_cod_sit(self, df_valores)

    else:
        MsgErro(status["MSG"])  
    
# Atualizar a tabela top 15 ocorrências
def atualizar_tabela_top(self, df_valores_gr):
    self.tb_top_ocorren.clearContents()
    self.tb_top_ocorren.setRowCount(0)
    top_ocorrenc = df_valores_gr.groupby(by=["COD_MAT", "DESC"], as_index=False)["DATA"].count()
    top_ocorrenc = top_ocorrenc.sort_values(by="DATA", ascending=False, ignore_index=True).loc[:14]
    for i in top_ocorrenc.index:
        ultlinhatb = int(self.tb_top_ocorren.rowCount())
        self.tb_top_ocorren.insertRow(ultlinhatb)
        self.tb_top_ocorren.setItem(ultlinhatb, 0, QTableWidgetItem(str(top_ocorrenc.loc[i, "DATA"])))
        self.tb_top_ocorren.setItem(ultlinhatb, 1, QTableWidgetItem(str(top_ocorrenc.loc[i, "COD_MAT"])))
        self.tb_top_ocorren.setItem(ultlinhatb, 2, QTableWidgetItem(str(top_ocorrenc.loc[i, "DESC"])))
        
# Gerar os graficos gerais
def gerar_grafico_geral(self, eixox, eixoY, rotulo):
    self.lb_geral.setText("Total Ocorrências 1 Ano")
    # Crie a figura do Matplotlib
    fig, ax = plt.subplots(figsize=(1, 1), tight_layout=True)
    self.figures.append(fig)
    self.canvas = FigureCanvas(fig)

    if self.valida_gr_geral == "":
        self.valida_gr_geral = "OK"
        self.canvas_gr_geral = FigureCanvas(fig)
        self.layout_gr_geral.addWidget(self.canvas_gr_geral)            
    else:
        self.layout_gr_geral.removeWidget(self.canvas_gr_geral)
        self.canvas_gr_geral = FigureCanvas(fig)
        self.layout_gr_geral.addWidget(self.canvas_gr_geral)

    ax.bar(eixox, eixoY, align="center")

    for (i, valor) in enumerate(eixoY, start=0):
        if valor >99999:
            ax.text(x=eixox[i], y=valor*0.98, s=f'{rotulo[i]}', color='white', fontweight='bold', fontsize=10, ha="center", va='top', rotation=270,)              
        elif valor <9999:
            ax.text(x=eixox[i], y=valor, s=f'{rotulo[i]}', color='black', fontweight='bold', fontsize=10, ha="center", va='bottom', rotation=0,)
        else:
            ax.text(x=eixox[i], y=valor*0.98, s=f'{rotulo[i]}', color='white', fontweight='bold', fontsize=10, ha="center", va='top', rotation=0,)

    plt.rcParams['axes.spines.top'] = False
    plt.rcParams['axes.spines.left'] = False
    plt.rcParams['axes.spines.right'] = False
    plt.rcParams['axes.spines.bottom'] = False

    # Definir as cores de fundo do gráfico usando plt.rcParams
    plt.rcParams['figure.facecolor'] = '#ffffff'  # Cor de fundo do gráfico
    plt.rcParams['axes.facecolor'] = '#ffffff'  # Cor de fundo da área interna do gráfico

    # Configurar o título e rótulos dos eixos com fonte personalizada
    fonte = FontProperties(size=8)
    # Configurar a fonte dos rótulos do eixo x
    rotulos_x = ax.get_xticklabels()
    for rotulo_x in rotulos_x:
        rotulo_x.set_fontproperties(fonte)

    
    # Configurar propriedades de borda diretamente no objeto de eixo
    ax = plt.gca()
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)

    plt.yticks([])
    self.layout_gr_geral.setContentsMargins(2, 2, 2, 2)
    self.canvas_gr_geral.draw()
    plt.close(fig)   
    
# Gerar os graficos total ocorrência e item
def gerar_grafico_total_ocor_item(self, df_valores_gr):
    rotulo = ["Ocorrência", "Itens"]
    t_oc = len(df_valores_gr["COD_MAT"])
    t_i = len(df_valores_gr["COD_MAT"].unique())
    dados = [t_oc, t_i]

    fig, ax = plt.subplots(figsize=(3, 2), tight_layout=True)
    self.figures.append(fig)
    if self.valida_gr_ocor_iten == "":
        self.valida_gr_ocor_iten = "OK"
        self.canvas_gr_ocor_iten = FigureCanvas(fig)
        self.layout_gr_ocor_iten.addWidget(self.canvas_gr_ocor_iten)            
    else:
        self.layout_gr_ocor_iten.removeWidget(self.canvas_gr_ocor_iten)
        self.canvas_gr_ocor_iten = FigureCanvas(fig)
        self.layout_gr_ocor_iten.addWidget(self.canvas_gr_ocor_iten)

    autopct_format = lambda p: f'{int(round(p * sum(dados) / 100.))}'
    colors = ['#00b4b4', '#ffaa00']

    # Definir a fonte para o rótulo
    fonte_rotulo = FontProperties()
    fonte_rotulo.set_family('serif')
    fonte_rotulo.set_size(8)
    fonte_rotulo.set_weight('bold')

    ax.pie(dados, labels=None, autopct=autopct_format, startangle=90, colors=colors)
    legenda = ax.legend(rotulo, title="", loc="upper left", bbox_to_anchor=(0.8, 1))
    legenda.set_frame_on(False)
    for texto in legenda.get_texts():
        texto.set_fontsize(7)

    plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
    # Remover margens
    fig.subplots_adjust(left=0, right=1, top=1, bottom=0)
    
    self.layout_gr_ocor_iten.setContentsMargins(3, 3, 3, 3)
    self.canvas_gr_ocor_iten.draw()
    plt.close(fig)

# Gerar os graficos top 5 código ocorrencia
def gerar_grafico_cod_sit(self, df_valores):
    df_cod_sit = df_valores[df_valores["COD_SIT"] != ""].groupby(by="COD_SIT", as_index=False)["COD_MAT"].count()

    df_cod_sit["ABREV_COD_SIT"] = df_cod_sit["COD_SIT"].str[:2]
    df_cod_sit.sort_values(by="COD_MAT", ascending=True, ignore_index=True, inplace=True)

    eixox = df_cod_sit["ABREV_COD_SIT"][-5:]
    eixoY = df_cod_sit["COD_MAT"][-5:]
    fig, ax = plt.subplots(figsize=(2, 1.5), tight_layout=True)
    self.figures.append(fig)
    if self.valida_gr_cod_sit == "":
        self.valida_gr_cod_sit = "OK"
        self.canvas_gr_cod_sit = FigureCanvas(fig)
        self.layout_gr_cod_sit.addWidget(self.canvas_gr_cod_sit)            
    else:
        self.layout_gr_cod_sit.removeWidget(self.canvas_gr_cod_sit)
        self.canvas_gr_cod_sit = FigureCanvas(fig)
        self.layout_gr_cod_sit.addWidget(self.canvas_gr_cod_sit)


    barras = ax.barh(eixox, eixoY)

    # Adicione rótulos nas barras
    for barra, valor in zip(barras, eixoY):
        plt.text(valor, barra.get_y() + barra.get_height() / 1.8, str(valor), ha='left', va='center', fontsize=9, fontweight='bold')

    plt.xticks([])

    plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
    # Remover margens
    fig.subplots_adjust(left=0, right=1, top=1, bottom=0)

    self.layout_gr_cod_sit.setContentsMargins(3, 3, 3, 3)
    self.canvas_gr_cod_sit.draw()

    plt.close(fig)


# 80034805