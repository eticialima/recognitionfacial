# -*- coding:utf-8-*-
import cv2
import os
import numpy as np
print("")
print("")
print("Iniciando treinamento com a base de informações")
print("")
print("")
eigenFace = cv2.face.EigenFaceRecognizer_create(num_components = 50,threshold=0)
fisherFace = cv2.face.FisherFaceRecognizer_create()
lbph = cv2.face.LBPHFaceRecognizer_create()
def getImagemComId():
    caminhos = [os.path.join('./treinamento',f) for f in os.listdir('./treinamento')]
    print(caminhos)
    faces = []
    ids = []
    for caminhoImagem in caminhos:
        imagemFace = cv2.cvtColor(cv2.imread(caminhoImagem), cv2.COLOR_BGR2GRAY)
        id = int(os.path.split(caminhoImagem)[-1].split('.')[1])
        ids.append(id)
        faces.append((imagemFace))
        #print(id)
        #cv2.imshow("Face",imagemFace)
        #cv2.waitKey(10)
    return np.array(ids),faces

ids,faces = getImagemComId()
#print(ids)
print("Treinando...")
eigenFace.train(faces,ids)
eigenFace.write('./lib/classificadorEigen.yml')


print("Treinamento Realizado")