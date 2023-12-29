import pandas as pd
import sqlite3

#### FUNÇÕES PARA REGISTRO E CONSULTA CONTROLE ACESSO E E-MAIL
# Consultar Usuários Tabela Usuário - Controle acesso
def db_consulta_usuarios(user):
    adm = ""
    usuarios = ""
    try:
        conn = sqlite3.connect(r"\\berneckadm\auc_almox\Arquivos\ALMOXARIFADO - DOCUMENTOS COMPARTILHADOS\GerenciadorAlmox\db_acesso_almox.db")
        consulta_adm = pd.read_sql(f'SELECT * FROM ADM WHERE USER == "{user}"', conn)

        if len(consulta_adm) > 0:
            adm = consulta_adm.astype(str)
            centros = '", "'.join(consulta_adm["CENTRO"].values)
            consulta_usuarios = pd.read_sql(f'SELECT * FROM USUARIOS WHERE CENTRO IN ("{centros}")', conn)
            usuarios = consulta_usuarios.astype(str) if len(consulta_usuarios) > 0 else ''
        else:
            consulta_usuarios = pd.read_sql(f'SELECT * FROM USUARIOS WHERE USER = "{user}"', conn)
            usuarios = consulta_usuarios.astype(str) if len(consulta_usuarios) > 0 else ''

        return {"status": "OK", "ADM": adm, "USUARIOS": usuarios}
    
    except sqlite3.Error as e:
        return {"status": "ERRO", "MSG": [e]}
    
    finally:
        conn.close()

# Alterar acesso usuário Tabela Usuário - Controle acesso
def db_alterar_usuario(id_user, user_novo, nome_novo, cen_novo, ace_novo):
    try:
        conn = sqlite3.connect(r"\\berneckadm\auc_almox\Arquivos\ALMOXARIFADO - DOCUMENTOS COMPARTILHADOS\GerenciadorAlmox\db_acesso_almox.db")        
        cursor = conn.cursor()        
        cursor.execute(f'UPDATE USUARIOS SET USER = ?, NOME = ?, CENTRO = ?, ACESSO = ? WHERE ID = {id_user}', (user_novo, nome_novo, cen_novo, ace_novo))
        conn.commit()
        return {"status": "OK", "MGS": f"Acesso usuário alterado!\nID: {id_user}\nUSUÁRIO: {user_novo}\nNOME: {nome_novo}\nCENTRO: {cen_novo}\nACESSO: {ace_novo}"}
    
    except sqlite3.Error as e:
        return {"status": "ERRO", "MSG": [e]}
    
    finally:
        conn.close()

# Incluir Novo Usuário Tabela Usuário - Controle acesso
def db_incluir_usuario(user_novo, nome_novo, cen_novo, ace_novo):
    try:
        conn = sqlite3.connect(r"\\berneckadm\auc_almox\Arquivos\ALMOXARIFADO - DOCUMENTOS COMPARTILHADOS\GerenciadorAlmox\db_acesso_almox.db")        
        cursor = conn.cursor()        
        cursor.execute(f'INSERT INTO USUARIOS (USER, NOME, CENTRO, ACESSO) VALUES (?, ?, ?, ?)', (user_novo, nome_novo, cen_novo, ace_novo))
        conn.commit()
        return {"status": "OK", "MGS": f"Usuários cadastrados!\nUSUÁRIO: {user_novo}\nNOME: {nome_novo}\nCENTRO: {cen_novo}\nACESSO: {ace_novo}"}
    
    except sqlite3.Error as e:
        return {"status": "ERRO", "MSG": [e]}
    
    finally:
        conn.close()

# Excluir usuário
def db_excluir_usuario(id_na):
    try:
        conn = sqlite3.connect(r"\\berneckadm\auc_almox\Arquivos\ALMOXARIFADO - DOCUMENTOS COMPARTILHADOS\GerenciadorAlmox\db_acesso_almox.db")
        cursor = conn.cursor()
        cursor.execute(f"DELETE FROM USUARIOS WHERE ID = {id_na}")
        conn.commit()
        return {"status": "OK", "MSG": "Usuário excluido com sucesso!"}
    
    except sqlite3.Error as e:
        return {"status": "ERRO", "MSG": [e]}
    
    finally:
        conn.close()

# Carregar os e-mail
def db_consultar_email_usuarios(plan, cen):
    try:
        conn = sqlite3.connect(r"\\berneckadm\auc_almox\Arquivos\ALMOXARIFADO - DOCUMENTOS COMPARTILHADOS\GerenciadorAlmox\db_acesso_almox.db")
        cursor = conn.cursor()
        cursor.execute(f"SELECT NOME, EMAIL FROM EMAIL WHERE FILTRO = '{plan}'")
        e_to = cursor.fetchall()
        cursor.execute(f"SELECT EMAIL FROM EMAIL WHERE FILTRO = 'CC' AND LOCAL IN ('GERAL' , '{cen}')")
        l_e_cc = cursor.fetchall()
        conn.close()
        e_cc = []
        for i in l_e_cc:
            e_cc.append(i[0])

        return {"status": "OK", "PLAN": [e_to[0][0], e_to[0][1]], "CC": e_cc}

    except sqlite3.Error as e:
        return {"status": "ERRO", "MSG": [e]}    

    finally:
        conn.close()


#### FUNÇÕES PARA REGISTRO E CONSULTA NÃO ATENDIDOS
# Incluir regitro tabela Não Atendidos
def db_incluir_nao_atendidos(dados):
    try:
        conn = sqlite3.connect(r"\\berneckadm\auc_almox\Arquivos\ALMOXARIFADO - DOCUMENTOS COMPARTILHADOS\GerenciadorAlmox\db_dados_almox.db")        
        cursor = conn.cursor()        
        cursor.execute(f'INSERT INTO NAO_ATENDIDOS (DATA, HORA, COD_MAT, DESC, UN_MED, SOLICITANTE, RAMAL, SETOR, OBS_ALMOX, QT_SOLIC, TP_MRP, MIN, MAX, GRP_PLAN, NOME_PLAN, CRIT, CONS_FINT, ST_ERP_GERAL, ST_ERP_CEN, SALDO_SIST, SALDO_FISICO, SEG_CONT, BLOQ, REQ_MAN, DIVERG, N_PROC_COMP, VALOR_UNIT, GRP_COMP, NOME_COMP, COD_SIT, SIT_PED, NOTA_MAT, SIT_PROC_COMP, ACAO_PLAN, CENTRO, USER, DATA_REGISTRO) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', dados)
        conn.commit()
        return {"status": "OK", "MSG": f"Registro realizado com sucesso!"}
    
    except sqlite3.Error as e:
        return {"status": "ERRO", "MSG": [e]}
    
    finally:
        conn.close()

# Alterar regitro tabela Não Atendidos
def db_alterar_nao_atendidos(id_na, dados):
    try:
        conn = sqlite3.connect(r"\\berneckadm\auc_almox\Arquivos\ALMOXARIFADO - DOCUMENTOS COMPARTILHADOS\GerenciadorAlmox\db_dados_almox.db")        
        cursor = conn.cursor() 
        sql_update = f"""
        UPDATE NAO_ATENDIDOS
        SET DATA = ?,
        HORA = ?,
        COD_MAT = ?,
        DESC = ?,
        UN_MED = ?,
        SOLICITANTE = ?,
        RAMAL = ?,
        SETOR = ?,
        OBS_ALMOX = ?,
        QT_SOLIC = ?,
        TP_MRP = ?,
        MIN = ?,
        MAX = ?,
        GRP_PLAN = ?,
        NOME_PLAN = ?,
        CRIT = ?,
        CONS_FINT = ?,
        ST_ERP_GERAL = ?,
        ST_ERP_CEN = ?,
        SALDO_SIST = ?,
        SALDO_FISICO = ?,
        SEG_CONT = ?,
        BLOQ = ?,
        REQ_MAN = ?,
        DIVERG = ?,
        N_PROC_COMP = ?,
        VALOR_UNIT = ?,
        GRP_COMP = ?,
        NOME_COMP = ?,
        COD_SIT = ?,
        SIT_PED = ?,
        NOTA_MAT = ?,
        SIT_PROC_COMP = ?,
        ACAO_PLAN = ?,
        CENTRO = ?,
        USER = ?,
        DATA_REGISTRO = ?
        WHERE ID = {id_na}
        """       
        cursor.execute(sql_update, dados)

        conn.commit()
        return {"status": "OK", "MSG": f"Registro alterado com sucesso!"}
    
    except sqlite3.Error as e:
        return {"status": "ERRO", "MSG": [e]}
    
    finally:
        conn.close()

# Consultar regitro tabela Não Atendidos
def db_consultar_nao_atendidos(filtro=""):
    try:
        conn = sqlite3.connect(r"\\berneckadm\auc_almox\Arquivos\ALMOXARIFADO - DOCUMENTOS COMPARTILHADOS\GerenciadorAlmox\db_dados_almox.db")
        consulta_na = pd.read_sql(f'SELECT * FROM NAO_ATENDIDOS {filtro}', conn)
        
        return {"status": "OK", "DADOS": consulta_na}
    
    except sqlite3.Error as e:
        return {"status": "ERRO", "MSG": [e]}
    
    finally:
        conn.close()

# Consultar e-mail tabela Não Atendidos
def db_consultar_email_nao_atendidos(filtro=""):
    try:
        conn = sqlite3.connect(r"\\berneckadm\auc_almox\Arquivos\ALMOXARIFADO - DOCUMENTOS COMPARTILHADOS\GerenciadorAlmox\db_dados_almox.db")
        consulta_na = pd.read_sql(filtro, conn)
        
        return {"status": "OK", "DADOS": consulta_na}
    
    except sqlite3.Error as e:
        return {"status": "ERRO", "MSG": [e]}
    
    finally:
        conn.close()

# Alterar o e-mail para enviado
def db_confirmar_envio_email_nao_atendidos(id_na):
    id_na_alt = tuple(id_na)
    try:
        conn = sqlite3.connect(r"\\berneckadm\auc_almox\Arquivos\ALMOXARIFADO - DOCUMENTOS COMPARTILHADOS\GerenciadorAlmox\db_dados_almox.db")        
        cursor = conn.cursor()
        if len(id_na_alt) > 1:
            sql_update = f'UPDATE NAO_ATENDIDOS SET EMAIL = ? WHERE ID IN {id_na_alt}'
        else:
            sql_update = f'UPDATE NAO_ATENDIDOS SET EMAIL = ? WHERE ID = {id_na_alt[0]}'

        cursor.execute(sql_update, ["ENVIADO"])
        conn.commit()
        return {"status": "OK", "MSG": f"Registro alterado com sucesso!"}

    except sqlite3.Error as e:
        return {"status": "ERRO", "MSG": [e]}    

    finally:
        conn.close()

# Excluir regitro tabela Não Atendidos
def db_excluir_nao_atendidos(id_na):
    try:
        conn = sqlite3.connect(r"\\berneckadm\auc_almox\Arquivos\ALMOXARIFADO - DOCUMENTOS COMPARTILHADOS\GerenciadorAlmox\db_dados_almox.db")
        cursor = conn.cursor()
        cursor.execute(f"DELETE FROM NAO_ATENDIDOS WHERE ID = {id_na}")
        conn.commit()
        return {"status": "OK", "MSG": "Registro excluido com sucesso!"}
    
    except sqlite3.Error as e:
        return {"status": "ERRO", "MSG": [e]}
    
    finally:
        conn.close()

# Consultar total Não Atendidos mês anterior
def db_consultar_nao_atendidos_total(filtro=""):
    try:
        conn = sqlite3.connect(r"\\berneckadm\auc_almox\Arquivos\ALMOXARIFADO - DOCUMENTOS COMPARTILHADOS\GerenciadorAlmox\db_dados_almox.db")
        cursor = conn.cursor()
        cursor.execute(f'SELECT COUNT(*) FROM NAO_ATENDIDOS {filtro}')
        total_ocorrencia = cursor.fetchall()

        return {"status": "OK", "DADOS": total_ocorrencia}
    
    except sqlite3.Error as e:
        return {"status": "ERRO", "MSG": [e]}
    
    finally:
        conn.close()

# Consultar histórico Não Atendidos
def db_consultar_base_grafico(filtro=""):
    try:
        conn = sqlite3.connect(r"\\berneckadm\auc_almox\Arquivos\ALMOXARIFADO - DOCUMENTOS COMPARTILHADOS\GerenciadorAlmox\db_dados_almox.db")
        df_valores = pd.read_sql(f'SELECT * FROM NAO_ATENDIDOS {filtro}', conn)        
        return {"status": "OK", "DADOS": df_valores}
    
    except sqlite3.Error as e:
        return {"status": "ERRO", "MSG": [e]}
    
    finally:
        conn.close()