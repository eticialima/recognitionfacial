
from database import *
from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.properties import StringProperty 
import os
import cv2

camera = cv2.VideoCapture(0)
detectorFace = cv2.CascadeClassifier("lib/haarcascade_frontalface_default.xml")
reconhecedor = cv2.face.EigenFaceRecognizer_create()
reconhecedor.read("lib/classificadorEigen.yml")
largura,altura = 220,220
font = cv2.FONT_HERSHEY_COMPLEX_SMALL
id_t = ''

while (True):
    conectado, imagem = camera.read()
    imagem = cv2.resize(imagem, (480, 360))
    imagemCinza = cv2.cvtColor(imagem,cv2.COLOR_BGR2GRAY)
    facesDetectadas = detectorFace.detectMultiScale(imagemCinza, minNeighbors=20, minSize=(30, 30), maxSize=(400, 400))
    for (x,y,l,a) in facesDetectadas:
        imagemFace = cv2.resize(imagemCinza[y:y+a,x:x+l],(largura,altura))
        cv2.rectangle(imagem,(x,y),(x+l,y+a),(0,0,255),2)
        id,confianca = reconhecedor.predict(imagemFace)
        print(id)
        id_t = id
        cursor.execute("SELECT nome FROM users WHERE id = ?",(int(id),))
        resultado = cursor.fetchall()
        print(resultado)
        if not resultado:
            cv2.putText(imagem, "Nenhum user encontrado".strip("(),'"), (x, y + (a + 30)), font, 2, (0, 0, 255))
        else:
            cv2.putText(imagem, str(resultado[0]).strip("(),'"), (x, y + (a + 30)), font, 2, (0, 0, 255))
                    
    cv2.imshow("Face",imagem)

    if cv2.waitKey(1) == ord('q'):
        Builder.load_file('showresults.kv') # Carrega o arquivo login.kv
        class AnswerInput(Screen):
            pass
        class MainApp(App):

            global result

            cursor.execute("SELECT id, nome, cargo, email, cpf FROM users WHERE id = ?",(str(id_t)))
            result = cursor.fetchone()
            print(result)
            nome = "Nome: " + result[1]
            cargo = "Cargo: " + result[2]
            email = "Email: " + result[3]
            cpf = "CPF: " + result[4]
            source_ = 'pessoas/pessoa.'+str(result[0])+'.1.jpg'

            def build(self):
                return AnswerInput()
        if __name__ == '__main__':
            MainApp().run()
        break
    if cv2.getWindowProperty("Face", cv2.WND_PROP_VISIBLE) <1:
        break

camera.release()
cv2.destroyAllWindows()
