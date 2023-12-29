from PySide6.QtWidgets import QMessageBox
# from PySide6.QtCore import Qt

def MsgQuestion(msg_info, backgroundcolor="rgb(0, 98, 98)"): 
    # Retorno confirmar 16384
    # Retorno não confirmar 65536
    msg = QMessageBox()
    msg.setWindowTitle('Confirmar')        
    msg.setText(msg_info)
    msg.setIcon(msg.Question)    
    msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
    msg.setButtonText(QMessageBox.Yes, 'Sim')
    msg.setButtonText(QMessageBox.No, 'Não')
    
    msg.setStyleSheet('''
                      QMessageBox{min-width:900 px; border-style: solid; border-width: 2px; border-color: rgb(234, 234, 234)} 
                      QWidget{color: rgb(255, 255, 255); font: 11pt \"Calibri\"; background-color: '''+backgroundcolor+''';}
                      QPushButton{background-color: rgb(225, 225, 225); border-style: outset; border-width: 2px; border-color: rgb(234, 234, 234); border-radius: 10px; color: rgb(0, 0, 0); font: bold 12pt; padding: 1 15 2 15; text-align: left;} 
                      QPushButton::hover {background-color: rgb(150, 150, 150); border-style: inset;}
                      ''')
    
    #Comando para alinhar os botões da MSG --> QDialogButtonBox { qproperty-centerButtons: true; }
   
    resp = msg.exec() 

    return resp
    

def MsgErro(msg_info, backgroundcolor="rgb(0, 98, 98)"):
    msg = QMessageBox()
    msg.setWindowTitle('Erro')        
    msg.setText(msg_info)    
    msg.setStandardButtons(msg.Ok)
    msg.setIcon(msg.Warning)
    msg.setStyleSheet('''
                      QMessageBox{ border-style: solid; border-width: 2px; border-color: rgb(234, 234, 234);}
                      QWidget{color: rgb(255, 255, 255); font: 11pt \"Calibri\";  background-color: '''+backgroundcolor+''';} 
                      QPushButton{ background-color: rgb(225, 225, 225); border-style: outset; border-width: 2px; border-color: rgb(234, 234, 234); border-radius: 10px; color: rgb(0, 0, 0); font: bold 12pt; padding: 1 15 2 15; text-align: left;} 
                      QPushButton::hover { background-color: rgb(150, 150, 150); border-style: inset;}''')
    
    msg.exec()

def MsgCancelado(backgroundcolor="rgb(0, 98, 98)"):
    msg = QMessageBox()
    msg.setWindowTitle('Cancelado')        
    msg.setText("Processo cancelado pelo usuário!")
    msg.setStyleSheet('''
                      QMessageBox{ border-style: solid; border-width: 2px; border-color: rgb(234, 234, 234);} 
                      QWidget{color: rgb(255, 255, 255); font: 11pt \"Calibri\";  background-color: '''+backgroundcolor+''';}
                      QPushButton{ background-color: rgb(225, 225, 225); border-style: outset; border-width: 2px; border-color: rgb(234, 234, 234); border-radius: 10px; color: rgb(0, 0, 0); font: bold 12pt; padding: 1 15 2 15; text-align: left;} 
                      QPushButton::hover { background-color: rgb(150, 150, 150); border-style: inset;}
                      ''')
    
    msg.setIcon(msg.Warning)
    msg.exec()

def MsgFinalizado(msg_info, backgroundcolor="rgb(0, 98, 98)"):
    msg = QMessageBox()
    msg.setWindowTitle('Processo finalizado!')
    msg.setText(msg_info)
    msg.setStyleSheet('''
                      QMessageBox{ border-style: solid; border-width: 2px; border-color: rgb(234, 234, 234);}
                      QWidget{color: rgb(255, 255, 255); font: 11pt \"Calibri\";  background-color: '''+backgroundcolor+''';} 
                      QPushButton{ background-color: rgb(225, 225, 225); border-style: outset; border-width: 2px; border-color: rgb(234, 234, 234); border-radius: 10px; color: rgb(0, 0, 0); font: bold 12pt; padding: 1 15 2 15; text-align: left;} 
                      QPushButton::hover { background-color: rgb(150, 150, 150); border-style: inset;}
                      ''')
    
    msg.setIcon(msg.Information)
    msg.setStandardButtons(msg.Ok)
    msg.exec()

def MsgAlteracao(msg_text, msg_info, msg_icon, backgroundcolor="rgb(0, 98, 98)"):
    msg = QMessageBox()
    if msg_icon == 'Information':
        msg.setIcon(msg.Information)
    else:
        msg.setIcon(msg.Critical)

    msg.setWindowTitle(msg_text)  
    msg.setText(msg_info)
    msg.setStyleSheet('''
                      QMessageBox{ border-style: solid; border-width: 2px; border-color: rgb(234, 234, 234);}
                      QWidget{color: rgb(255, 255, 255); font: 11pt \"Calibri\";  background-color: '''+backgroundcolor+''';} 
                      QPushButton{ background-color: rgb(225, 225, 225); border-style: outset; border-width: 2px; border-color: rgb(234, 234, 234); border-radius: 10px; color: rgb(0, 0, 0); font: bold 12pt; padding: 1 15 2 15; text-align: left;} 
                      QPushButton::hover { background-color: rgb(150, 150, 150); border-style: inset;}
                      ''')

    msg.StandardButton(msg.Ok)
    msg.exec()

def MsgInformation(msg_text,  msg_info, backgroundcolor="rgb(0, 98, 98)"):
    msg = QMessageBox()
    msg.setWindowTitle(msg_text)        
    msg.setText(msg_info)
    msg.setStandardButtons(msg.Ok)
    msg.setIcon(msg.Information)

    msg.setStyleSheet('''
                      QMessageBox{ border-style: solid; border-width: 2px; border-color: rgb(234, 234, 234);} 
                      QWidget{color: rgb(255, 255, 255); font: 11pt \"Calibri\";  background-color: '''+backgroundcolor+''';}
                      QPushButton{ background-color: rgb(225, 225, 225); border-style: outset; border-width: 2px; border-color: rgb(234, 234, 234); border-radius: 10px; color: rgb(0, 0, 0); font: bold 12pt; padding: 1 15 2 15; text-align: left;} 
                      QPushButton::hover { background-color: rgb(150, 150, 150); border-style: inset;}
                      ''')           
    
    msg.exec()

def MsgInfoCodAlter(backgroundcolor="rgb(0, 98, 98)"):
    msg = QMessageBox()
    msg.setWindowTitle("Código Exceção") 
    msg.setText("Informar o Código Exceção:") 
    msg.setStandardButtons(msg.Ok)
    msg.setIcon(msg.Information)
    msg.setStyleSheet('''
                      QMessageBox{ border-style: solid; border-width: 2px; border-color: rgb(234, 234, 234);} 
                      QWidget{color: rgb(255, 255, 255); font: 11pt \"Calibri\"; background-color: '''+backgroundcolor+''';}
                      QPushButton{ background-color: rgb(225, 225, 225); border-style: outset; border-width: 2px; border-color: rgb(234, 234, 234); border-radius: 10px; color: rgb(0, 0, 0); font: bold 12pt; padding: 1 15 2 15; text-align: left;} 
                      QPushButton::hover { background-color: rgb(150, 150, 150); border-style: inset;}
                      ''')    
    msg.exec()