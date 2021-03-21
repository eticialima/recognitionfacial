# -*- coding:utf-8-*-
# ------------------------------------------------- #
# ---TELA DE CADASTRO
# ------------------------------------------------- #

# ----- Initial imports ----- #
# import kivy 
import cv2
from kivy import Config 

# ----- IMPORTAR MODULOS ----- #
from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
import os
import sqlite3
from database import connection, cursor  

global connection, cursor
cursor.execute("SELECT id FROM users ORDER BY id DESC LIMIT 1")
resultado = cursor.fetchall()
print(resultado)

# ----- CADASTRO ----- #
class TCadastro(Screen):
    def do_login(self, loginText, passwordText): 
 
        self.txt_login = ''
        self.txt_cpf = ''
        self.txt_cargo = ''
        self.txt_email = '' 

        self.estado_da_camera = 0

    # --- REGISTRA DADOS DE FORMULÁRIO EM VARIÁVEIS --- #
    def register_data(self):
        self.txt_login = self.ids.login.text
        self.txt_cpf = self.ids.cpf.text
        self.txt_cargo = self.ids.identificador.text
        self.txt_email = self.ids.email.text

    # --- SISTEMA DE RECONHECIMENTO --- #
    def eigen(self):
        os.system('python3 eigen.py')

    # --- SISTEMA DE DETECÇÃO --- #
    def register_foto(self):
        os.system('python3 detection.py') 

    # --- INSERIR OS VALORES NO BANCO DE DADOS --- #
    def insert_values_in_dabatase(self):
        
        self.register_data()
        # --- PRINTA NA TELAS AS INFORMAÇÕES QUANDO REGISTAR --- #
        print(self.txt_login)
        print(self.txt_cpf)
        print(self.txt_cargo)
        print(self.txt_email)

        try:
            cursor.execute("SELECT id FROM users ORDER BY id DESC LIMIT 1")
            resultado = cursor.fetchall()
            ids = []
            for x in resultado:
                ids.append(str(x).strip('()[].,'))
            ide = ids[0]
            print(resultado)
            cursor.execute(
                """
                UPDATE users
                SET nome = ?, cargo = ?, email = ?, cpf = ?
                WHERE id = ? """,(str(self.txt_login), str(self.txt_cargo), str(self.txt_email), str(self.txt_cpf),int(ide)))
        except ValueError:
            self.ids.login.text = "Os campos não podem ser vazios."
        except:
            self.ids.login.text = "Dados Repetidos."
        else:
            connection.commit()
            #connection.close() Se fechar, ele só vai aceitar 1 usuário e vai dar erro.
            self.clean_input_values()
            self.ids.login.text = str(self.txt_login) # Coloca o último valor salvo dentro do campo login
 
    def clean_input_values(self): 
        # --- FAZ A LIMPEZA DOS INPUTS --- #
        self.ids.login.text = ''
        self.ids.identificador.text = ''
        self.ids.email.text = ''
        self.ids.cpf.text = ''	

class LoginApp(App): 
    
    def build(self):
        manager = ScreenManager() 
        manager.add_widget(TCadastro(name='login')) 
        return manager

    def get_application_config(self):
        if(not self.username):
            return super(LoginApp, self).get_application_config()

        conf_directory = self.user_data_dir + '/' + self.username

        if(not os.path.exists(conf_directory)):
            os.makedirs(conf_directory)

        return super(LoginApp, self).get_application_config(
            '%s/config.cfg' % (conf_directory)
        ) 

if __name__ == '__main__':
    LoginApp().run()
