# ----- Initial imports ----- #
import kivy 
import cv2
from kivy import Config
 
# ----- Window configuration ----- # 
from kivy.clock import Clock
from kivy.graphics.texture import Texture
from kivy.uix.image import Image 
from threading import Thread

Config.set('graphics', 'resizable', True)
Config.set('kivy', 'exit_on_escape', '0')
#Config.set('graphics', 'window_state', 'maximized')
Config.set('graphics', 'width', 1000)
Config.set('graphics', 'height', 600)

# ----- Imports ----- #
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.floatlayout import FloatLayout
 
# ----- Importing Modules ----- # 
from py_cadastro import TCadastro 
from py_principal import TPrincipal
from py_reconhecimento import TReconhecimento 

# ----- Window management class ----- #
class GerenciadorTelas(ScreenManager):
	def __init__(self):
		super().__init__()

		# --- Instantiate classes --- #
		self.tprincipal = TPrincipal()
		self.tcadastro = TCadastro()
		self.treconhecimento = TReconhecimento()
		 
		# --- Place the window classes in the ScreenManager --- #
		self.add_widget(self.tprincipal)
		self.add_widget(self.tcadastro)
		self.add_widget(self.treconhecimento)
 
# --- Classe App --- #
class Kv_Main(App):

	title = 'Sistema de controle de acesso por Reconheicmento Facial'
	icon = 'ImagesApp/logo.png'

	def build(self):
		return GerenciadorTelas() 

if __name__ == '__main__':
	Kv_Main().run()

