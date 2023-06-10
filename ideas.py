import time
import threading
import cv2
import pyqrcode
from pyqrcode import QRCode
from pyzbar.pyzbar import decode
import numpy as np

with open(file="kilate.csv", mode='a') as file:
    file.write(f"Hora de creacion: {time.strftime('%M:%H | %d/%m/%Y')}\n\n")
    file.close()

cap = cv2.VideoCapture(0)
detector = cv2.QRCodeDetector()
estado = str()
texto = ""
ultimo = ""
num = 0

while (1):
    print("escriba los objetos solicitado:")
    objeto = input()
    print("estas seguro ?")
    seguridad = input()
    if seguridad == "no":
        print("escriba los objetos solicitado:")
        objeto = input()
        print("estas seguro ?")
        seguridad = input()

    print("coloque su credencial frente a la camara de forma que se vea el codigoQR y su rostro ")
    break
while True:

    _, img = cap.read()


    for codes in decode(img):

            data, vertices_array, _ = detector.detectAndDecode(img)
            pts = np.array([codes.polygon], np.int32)
            xi, yi = codes.rect.left, codes.rect.top


            pts = pts.reshape((-1, 1, 2))

            if vertices_array is not None:
                time.sleep(1)
                if data and ultimo != data:
                    cv2.polylines(img, [pts], True, (255, 255, 0), 5)
                    ultimo = data
                    print(ultimo)
                    with open(file="kilate.csv", mode='a') as file:
                        file.write(f"{data},{objeto},Hora de {estado}:,{time.strftime('%H:%M:%S')}\n")
                        cv2.imwrite("C:/Users/espar/OneDrive/Escritorio/python/mocallo/odio-esto" + str(num) + '.png',img)
                        num += 1
                        file.close()


cv2.imshow("img", img)


cap.release()
cv2.destroyAllWindows()
