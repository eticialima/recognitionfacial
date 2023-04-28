from kivy.uix.screenmanager import Screen
import os

class TReconhecimento(Screen):
    def eigen(self):
        os.system('python project/script/eigen.py')
