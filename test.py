from kivy.app import App
from kivy.uix.camera import Camera
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
import cv2
from kivy.app import App
# DIRETORIO DO HAAR
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#INICIA A CLASS DO PROGRAMA
class cadastro(App):
    def build(self):
        #LAYOUT FLOAT
        layout= FloatLayout()

        #CONFIGURAÇÕES DA CAMERA
        self.cameraObject = Camera(play=False)
        self.cameraObject.play = True
        self.cameraObject.resolution = (480, 350)
        self.cameraObject.size_hint = (.4, 1)
        self.cameraObject.pos_hint = {'x': .55, 'y': .10}

        #CONFIGURAÇÕES DO BOTÃO 1
        self.botaoClick1 = Button(text="BOTÃO 1 ")
        self.botaoClick1.size_hint = (.2, .1)
        self.botaoClick1.pos_hint = {'x': .55, 'y': .20}

        #CONFIGURAÇÕES DO BOTÃO 2
        self.botaoClick2 = Button(text="BOTÃO 2 ")
        self.botaoClick2.size_hint = (.2, .1)
        self.botaoClick2.pos_hint = {'x': .75, 'y': .20}

        #FUNÇÃO DE CLICK DOS BOTÕES
        self.botaoClick1.bind(on_press=self.botaoclickone)
        self.botaoClick2.bind(on_press=self.botaoclicktwo)

        #CAMPOS DE CADASTRO

        #LAYOUT PARA MOSTRAR OS WIDGET NA TELA
        layout.add_widget(self.cameraObject)
        layout.add_widget(self.botaoClick1)
        layout.add_widget(self.botaoClick2)


        #RETORNA PARA O WIDGET
        return layout

    #FUNÇÃO DO CLIQUE
    def botaoclickone(self, *args):
        print("VOCE CLICOU NO BOTÃO 1")

    def botaoclicktwo(self, *args):
        print("VOCE CLICOU NO BOTÃO 2")



#INICIA O APP
if __name__ == '__main__':
    cadastro().run()