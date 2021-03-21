# ------------------------------------------------- #
# ---Registration and Photos
# ------------------------------------------------- #
 
# ----- Imports ----- #
import cv2
from kivy.uix.screenmanager import Screen
from kivy.clock import Clock
import os
import sqlite3
from database import connection, cursor 

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

class TReconhecimento(Screen):
    def eigen(self): 
        print("oi")
        os.system('python3 eigen.py')