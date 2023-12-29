import os
import win32com.client
import subprocess
from datetime import datetime, timedelta
from time import sleep

# Validar se o SAP Gui está aberto
def validar_sap():    
    try:
        SapGuiAuto = win32com.client.GetObject("SAPGUI")
        application = SapGuiAuto.GetScriptingEngine
        try:
            connection = application.Children(0)
            try:
                session = connection.Children(0)
                try:
                    if session.findById("wnd[0]/usr/lblRSYST-BNAME").Text == "Usuário":
                        return "Erro", "Por gentileza realizar o login no SAP."   
                                
                except:
                    return "OK", ""
                
            except:
                return "Erro", "Por gentileza verificar se a opção do Script está habilitado."
            
        except:
            connection = application.OpenConnection("4. S4HANA Produção", True)
            return "Erro", "Por gentileza realizar o login no SAP."

    except:
        subprocess.Popen(r"C:\Program Files (x86)\SAP\FrontEnd\SAPgui\saplogon.exe")
        sleep(5)        
        SapGuiAuto = win32com.client.GetObject("SAPGUI")
        application = SapGuiAuto.GetScriptingEngine
        connection = application.OpenConnection("4. S4HANA Produção", True)
        return "Erro", "Por gentileza realizar o login no SAP"

# Abrir e conectar no SAP Gui
def conexao_sap_gui():
    try:
        subprocess.Popen(r"C:\Program Files (x86)\SAP\FrontEnd\SAPgui\saplogon.exe")
        SapGuiAuto = ""
        while SapGuiAuto == "":
            try:
                SapGuiAuto = win32com.client.GetObject("SAPGUI")
            except:
                pass
        application = SapGuiAuto.GetScriptingEngine
        connection = application.OpenConnection("4. S4HANA Produção", True)
        session = connection.Children(0)
        try:
            session.findById("wnd[0]/usr/txtRSYST-MANDT").Text = "100"
            session.findById("wnd[0]/usr/txtRSYST-BNAME").Text = "ALT_POSICAO"
            session.findById("wnd[0]/usr/pwdRSYST-BCODE").Text = "gestaocad@2021"
            session.findById("wnd[0]").sendVKey(0)
            try:
                erro = session.findById("wnd[1]/usr/txtMULTI_LOGON_TEXT").text
                session.findById("wnd[0]").sendVKey(0)                
                return {"status": "ERRO_OPEN", "MSG": f"{erro}\nPor gentileza verificar se o aplicativo não esta sendo utilizado por outro usuário ou centro!"}
            
            except:
                return {"status": "OK", "session": session, "conn": connection}
            
        except:            
                return {"status": "ERRO", "MSG": "Erro ao realizar o login no SAP!", "conn": connection}
            
    except:
        return {"status": "ERRO_OPEN", "MSG": "Erro ao abrir o SAP Longo!"}            

# Realiza a alteração dos daso no SAP
def alterar_dados_sap_gui(session, sku, centro, deposito, local):
    try:
        #Abri tela MM02 (Alteração material)
        session.findById("wnd[0]/tbar[0]/okcd").text = "/NMM02"
        session.findById("wnd[0]").sendVKey(0)
        
        #Preencher Número Material
        session.findById("wnd[0]/usr/ctxtRMMG1-MATNR").text = sku
        session.findById("wnd[0]/tbar[1]/btn[5]").press()
        erro = session.findById("wnd[0]/sbar").text

        user = os.getlogin().upper()
        errouser = f"Dados de grupo de empresas do material {sku} bloqueados pelo usuário {user}"
        sbar = session.findById("wnd[0]/sbar").text        
        while sbar == errouser: 
            #Abri tela MM02 (Alteração material)
            session.findById("wnd[0]/tbar[0]/okcd").text = "/NMM02"
            session.findById("wnd[0]").sendVKey(0)
            #Preencher Número Material
            session.findById("wnd[0]/usr/ctxtRMMG1-MATNR").text = sku
            session.findById("wnd[0]/tbar[1]/btn[5]").press()
            sbar = str(session.findById("wnd[0]/sbar").text)

        #Selecionar a visão Dds.gerais centro/armazen.1
        session.findById("wnd[1]/tbar[0]/btn[19]").press()

        session.findById("wnd[1]/usr/tblSAPLMGMMTC_VIEW").verticalScrollbar.Position = 12
        lvis = 0
        visao = session.findById(f"wnd[1]/usr/tblSAPLMGMMTC_VIEW/txtMSICHTAUSW-DYTXT[0,{lvis}]").text
        while visao != "Dds.gerais centro/armazen.1":
            lvis += 1
            visao = session.findById(f"wnd[1]/usr/tblSAPLMGMMTC_VIEW/txtMSICHTAUSW-DYTXT[0,{lvis}]").text

        session.findById("wnd[1]/usr/tblSAPLMGMMTC_VIEW").getAbsoluteRow(lvis + 12).selected = True
        session.findById("wnd[1]/tbar[0]/btn[6]").press()

        #Preencher o Centro e o Depósito
        session.findById("wnd[1]/usr/ctxtRMMG1-WERKS").text = centro
        session.findById("wnd[1]/usr/ctxtRMMG1-LGORT").text = deposito
        session.findById("wnd[1]/tbar[0]/btn[0]").press()

        local_antigo = session.findById("wnd[0]/usr/tabsTABSPR1/tabpSP19/ssubTABFRA1:SAPLMGMM:2000/subSUB2:SAPLMGD1:2701/txtMARD-LGPBE").text
        session.findById("wnd[0]/usr/tabsTABSPR1/tabpSP19/ssubTABFRA1:SAPLMGMM:2000/subSUB2:SAPLMGD1:2701/txtMARD-LGPBE").text = local
        status = "OK"
        session.findById("wnd[0]/tbar[0]/btn[11]").press()

        return {"status": status, "local_antigo": local_antigo}
    
    except:
        try:
            if erro == f'O material {sku} não existe ou não foi ativado':
                status = "ERRO"
                msg = f"ERRO: {erro}"
                local_antigo = ''
                session.findById("wnd[0]/tbar[0]/okcd").text = "/NMM02"
                session.findById("wnd[0]").sendVKey(0)
            else:
                msgerro = session.findById("wnd[2]/usr/txtMESSTXT1").text
                status = f"ERRO: {msgerro} centro {centro}"
                local_antigo = ''
                session.findById("wnd[0]/tbar[0]/okcd").text = "/NMM02"
                session.findById("wnd[0]").sendVKey(0)
        except:

            status = "ERRO"
            msg = "Analizar erro"
            local_antigo = '' 
            session.findById("wnd[0]/tbar[0]/okcd").text = "/NMM02"
            session.findById("wnd[0]").sendVKey(0)
        
        return  {"status": "ERRO", "MSG": msg}

# Carregar os dados MD04 e ZMM073
def consultar_nao_atendidos(material, centro):
    try:
        SapGuiAuto  = win32com.client.GetObject("SAPGUI")
        application = SapGuiAuto.GetScriptingEngine
        connection = application.Children(0)
        session  = connection.Children(0)
        try:
            session.findById("wnd[0]/tbar[0]/okcd").text = "/NZMM073"
            session.findById("wnd[0]").sendVKey(0)

            session.findById("wnd[0]/usr/ctxtS_MATNR-LOW").text = material
            session.findById("wnd[0]/usr/ctxtS_MATNR-HIGH").text = ""

            session.findById("wnd[0]/usr/ctxtS_MTART-LOW").text = ""
            session.findById("wnd[0]/usr/ctxtS_MTART-HIGH").text = ""

            session.findById("wnd[0]/usr/ctxtS_WERKS-LOW").text = centro
            session.findById("wnd[0]/usr/ctxtS_WERKS-HIGH").text = ""

            session.findById("wnd[0]/usr/ctxtS_LGORT-LOW").text = ""
            session.findById("wnd[0]/usr/ctxtS_LGORT-HIGH").text = ""

            session.findById("wnd[0]/usr/ctxtS_DISPO-LOW").text = ""
            session.findById("wnd[0]/usr/ctxtS_DISPO-HIGH").text = ""

            session.findById("wnd[0]/usr/ctxtS_DISMM-LOW").text = ""
            session.findById("wnd[0]/usr/ctxtS_DISMM-HIGH").text = ""

            session.findById("wnd[0]/usr/ctxtS_MSTAE-LOW").text = ""
            session.findById("wnd[0]/usr/ctxtS_MSTAE-HIGH").text = ""

            session.findById("wnd[0]/usr/ctxtS_EKGRP-LOW").text = ""
            session.findById("wnd[0]/usr/ctxtS_EKGRP-HIGH").text = ""

            session.findById("wnd[0]/usr/ctxtS_MATKL-LOW").text = ""
            session.findById("wnd[0]/usr/ctxtS_MATKL-HIGH").text = ""

            session.findById("wnd[0]/usr/ctxtS_PDATE-LOW").text = ""
            session.findById("wnd[0]/usr/ctxtS_PDATE-HIGH").text = ""

            session.findById("wnd[0]/usr/ctxtS_DTMOV-LOW").text = ""
            session.findById("wnd[0]/usr/ctxtS_DTMOV-HIGH").text = ""

            session.findById("wnd[0]/usr/txtP_LAY06").text = "/NAATENDIDO"

            session.findById("wnd[0]/tbar[1]/btn[8]").press()

            # Ajuste o caminho do controle de grade conforme necessário
            grid_path = "wnd[0]/usr/cntlGRID1/shellcont/shell"
            # Obtém o objeto de controle de grade
            grid = session.FindById(grid_path)
            # Pegar o total de linhas
            row_total = grid.RowCount
            if row_total > 0:
                minimo = float(grid.GetCellValue(0, "MINBE").replace(".", "").replace(",", "."))

                if grid.GetCellValue(0, "DISLS") == "FX":
                    maximo = float(grid.GetCellValue(0, "BSTFE").replace(".", "").replace(",", ".")) + minimo - 1
                elif grid.GetCellValue(0, "DISLS") == "HB":
                    maximo = float(grid.GetCellValue(0, "MABST").replace(".", "").replace(",", "."))
                else:
                    maximo = float(0)

                critico = grid.GetCellValue(0, "EST")

                if grid.GetCellValue(0, "CONS") == "Sim" or grid.GetCellValue(0, "FINT") == "Sim":
                    cons_fint = "Sim"
                else:
                    cons_fint = "Não"

                tmp_proc_em = int(grid.GetCellValue(0, "WEBAZ"))

                status_erp_geral = grid.GetCellValue(0, "MSTAE")
                status_erp_cen = grid.GetCellValue(0, "MMSTA")
                
                tp = []
                bloqueado = 0
                for row in range(row_total):
                    if grid.GetCellValue(row, "BWTAR") not in tp and grid.GetCellValue(row, "BWTAR") != "DANIFICADO":
                        tp.append(grid.GetCellValue(row, "BWTAR"))
                        bloqueado += float(grid.GetCellValue(row, "ESTOQUE_BLOQ_DEP").replace(".", "").replace(",", "."))

                saldo_sist = float(grid.GetCellValue(0, "LBKUM").replace(".", "").replace(",", "."))
                valor_unit = float(grid.GetCellValue(0, "PRECO_UNIT_CENTRO").replace(".", "").replace(",", "."))
                try:
                    session.findById("wnd[0]/tbar[0]/okcd").text = "/NMD04"
                    session.findById("wnd[0]").sendVKey(0)

                    session.findById("wnd[0]/usr/tabsTAB300/tabpF01/ssubINCLUDE300:SAPMM61R:0301/ctxtRM61R-MATNR").text = material
                    session.findById("wnd[0]/usr/tabsTAB300/tabpF01/ssubINCLUDE300:SAPMM61R:0301/ctxtRM61R-BERID").text = centro
                    session.findById("wnd[0]").sendVKey(0)
                    try:
                        if session.findById("wnd[0]/usr/btnBUTTON_MTREE"): ...
                    except:
                        session.findById("wnd[0]/usr/btnBUTTON_GROKO").press()

                    descricao = session.findById("wnd[0]/usr/subINCLUDE8XX:SAPMM61R:0800/txtMT61D-MAKTX").text
                    und_med = session.findById("wnd[0]/usr/subINCLUDE8XX:SAPMM61R:0800/ctxtRM61R-MEINH").text
                    tp_mrp = session.findById("wnd[0]/usr/subINCLUDE8XX:SAPMM61R:0800/ctxtMDKP-DISMM").text

                    while True:
                        try:
                            if session.findById("wnd[0]/usr/tabsTABTC/tabpTB01/ssubINCLUDE7XX:SAPLM61K:0120/ctxtMDKP-DISPO").text:
                                break
                        except: ...

                    grp_plan = session.findById("wnd[0]/usr/tabsTABTC/tabpTB01/ssubINCLUDE7XX:SAPLM61K:0120/ctxtMDKP-DISPO").text
                    plan_mrp = session.findById("wnd[0]/usr/tabsTABTC/tabpTB01/ssubINCLUDE7XX:SAPLM61K:0120/txtT024D-DSNAM").text
                    grp_comp = session.findById("wnd[0]/usr/tabsTABTC/tabpTB01/ssubINCLUDE7XX:SAPLM61K:0120/ctxtMDKP-EKGRP").text
                    comprador = session.findById("wnd[0]/usr/tabsTABTC/tabpTB01/ssubINCLUDE7XX:SAPLM61K:0120/txtT024-EKNAM").text

                    nota_material = ""
                    if session.FindById(f"wnd[0]/usr/subINCLUDE8XX:SAPMM61R:0800/btnRM61R-MNTXT").text != "":
                        session.FindById(f"wnd[0]/usr/subINCLUDE8XX:SAPMM61R:0800/btnRM61R-MNTXT").press()
                        total_linha = session.FindById("wnd[0]/usr/tblSAPLSTXXEDITAREA").rowCount-43
                        nota_material = ""
                        for row in range(1, total_linha):
                            texto = session.FindById(f"wnd[0]/usr/tblSAPLSTXXEDITAREA/txtRSTXT-TXLINE[2,{row}]").text
                            if texto != "":
                                nota_material = f'{nota_material}{session.FindById(f"wnd[0]/usr/tblSAPLSTXXEDITAREA/txtRSTXT-TXLINE[2,{row}]").text}\n'

                        session.FindById(f"wnd[0]/tbar[0]/btn[3]").press()

                    row_total = session.FindById("wnd[0]/usr/subINCLUDE1XX:SAPMM61R:0780/tabsGL_TAB/tabpGL_1/ssubGL_SUBSCR:SAPMM61R:0750/tblSAPMM61RTC_EZ").RowCount

                    colunas = session.FindById("wnd[0]/usr/subINCLUDE1XX:SAPMM61R:0780/tabsGL_TAB/tabpGL_1/ssubGL_SUBSCR:SAPMM61R:0750/tblSAPMM61RTC_EZ").Columns
                    nomes_colunas = [coluna.Name for coluna in colunas]
                    
                    # Obtém a data e hora atuais
                    data_atual = datetime.now()
                    # Obtém apenas a parte da data com hora zero (00:00:00)
                    data_apenas = datetime(data_atual.year, data_atual.month, data_atual.day, 0, 0, 0)
                    lista_pedidos_txt = ""
                    proc_compra = ""
                    lista_pedidos = []
                    lista_pedidos_valida = []
                    for i in range(row_total):
                        session.findById("wnd[0]/usr/subINCLUDE1XX:SAPMM61R:0780/tabsGL_TAB/tabpGL_1/ssubGL_SUBSCR:SAPMM61R:0750/tblSAPMM61RTC_EZ").verticalScrollbar.position = i
                        elemento_mrp = session.FindById(f"wnd[0]/usr/subINCLUDE1XX:SAPMM61R:0780/tabsGL_TAB/tabpGL_1/ssubGL_SUBSCR:SAPMM61R:0750/tblSAPMM61RTC_EZ/txtMDEZ-DELB0[2,1]").text
                        if elemento_mrp == "______":     
                            break
                        elif elemento_mrp == "----->":
                            break
                        elif elemento_mrp not in ["DivEst", "AviPed", "ReqCmp"]:
                            ...
                        else:   
                            qtd_soma = float(session.FindById(f"wnd[0]/usr/subINCLUDE1XX:SAPMM61R:0780/tabsGL_TAB/tabpGL_1/ssubGL_SUBSCR:SAPMM61R:0750/tblSAPMM61RTC_EZ/txtMDEZ-MNG02[9,1]").text)

                            if "MDEZ-WRK02" in nomes_colunas:
                                transf = session.FindById("wnd[0]/usr/subINCLUDE1XX:SAPMM61R:0780/tabsGL_TAB/tabpGL_1/ssubGL_SUBSCR:SAPMM61R:0750/tblSAPMM61RTC_EZ/txtMDEZ-WRK02[10,1]").text
                            else:
                                transf = ""

                            if elemento_mrp in ["DivEst", "AviPed", "ReqCmp"] and qtd_soma > 0 and transf == "":
                                proc_compra = session.FindById(f"wnd[0]/usr/subINCLUDE1XX:SAPMM61R:0780/tabsGL_TAB/tabpGL_1/ssubGL_SUBSCR:SAPMM61R:0750/tblSAPMM61RTC_EZ/txtMDEZ-EXTRA[5,1]").text
                                if proc_compra not in lista_pedidos_valida:
                                    dt = session.FindById(f"wnd[0]/usr/subINCLUDE1XX:SAPMM61R:0780/tabsGL_TAB/tabpGL_1/ssubGL_SUBSCR:SAPMM61R:0750/tblSAPMM61RTC_EZ/ctxtMDEZ-DAT00[1,1]").text
                                    data_remessa = datetime.strptime(dt, "%d.%m.%Y")
                                    data_remessa = data_remessa - timedelta(days=tmp_proc_em)
                                    if data_remessa >= data_apenas:
                                        situacao = "Em dia"
                                    else:
                                        situacao = "Em atraso"
                                    lista_pedidos.append([datetime.strftime(data_remessa, '%d.%m.%Y'), situacao, elemento_mrp, proc_compra])
                                    lista_pedidos_valida.append(proc_compra)

                    lista_pedidos.sort()

                    return {"status": "OK", "descricao": descricao, "und_med": und_med, "tp_mrp": tp_mrp, "grp_plan": grp_plan, "plan_mrp": plan_mrp, "grp_comp": grp_comp, "comprador": comprador, "nota_material": nota_material, "lista_pedidos": lista_pedidos, "minimo": minimo, "maximo": maximo, "critico": critico, "cons_fint": cons_fint, "status_erp_geral": status_erp_geral, "status_erp_cen": status_erp_cen, "bloqueado": bloqueado, "saldo_sist": saldo_sist, "valor_unit": valor_unit}
            
                except:
                    return {"status": "ERRO", "MSG": "Erro ao consultar no MD04"}
                
            else:
                session.findById("wnd[0]/tbar[0]/okcd").text = "/NMM03"
                session.findById("wnd[0]").sendVKey(0)
                session.findById("wnd[0]/usr/ctxtRMMG1-MATNR").text = material
                session.FindById("wnd[0]/tbar[1]/btn[5]").press()
                session.FindById("wnd[1]/tbar[0]/btn[19]").press()
                session.FindById("wnd[1]/usr/tblSAPLMGMMTC_VIEW").getAbsoluteRow(0).selected = True
                session.FindById("wnd[1]/tbar[0]/btn[0]").press()
                descricao = session.FindById("wnd[0]/usr/tabsTABSPR1/tabpSP01/ssubTABFRA1:SAPLMGMM:2004/subSUB1:SAPLMGD1:1002/txtMAKT-MAKTX").text
                und_med = session.FindById("wnd[0]/usr/tabsTABSPR1/tabpSP01/ssubTABFRA1:SAPLMGMM:2004/subSUB2:SAPLMGD1:2001/ctxtMARA-MEINS").text
                status_erp_geral = session.FindById("wnd[0]/usr/tabsTABSPR1/tabpSP01/ssubTABFRA1:SAPLMGMM:2004/subSUB2:SAPLMGD1:2001/ctxtMARA-MSTAE").text
                session.FindById("wnd[0]/tbar[0]/btn[15]").press()


                return {"status": "SEM_AMP", "MSG": f"Material {material} Não Amp. no Cen. {centro}.", "descricao": descricao, "und_med": und_med, "status_erp_geral": status_erp_geral}
            
        except:
                return {"status": "ERRO", "MSG": "Erro ao consultar na ZMM073"}
        

    except:
        return {"status": "ERRO", "MSG": "Erro ao conectar no SAP"}


