import time
import threading
import cv2
from pyzbar.pyzbar import decode
import numpy as np
import os

with open(file="kilate.csv", mode='a') as file:
    file.write(f"Hora de creacion: {time.strftime('%M:%H | %d/%m/%Y')}\n\n")
    file.close()

cap = cv2.VideoCapture(0)
detector = cv2.QRCodeDetector()
estado = str()
texto = ""
ultimo = ""
num = 0
seguro = 0
os.mkdir('imagenes') if not os.path.exists('imagenes') else None


def preguntas():
    print("escriba los objetos solicitado:")
    objeto = input()
    return objeto


t1 = threading.Thread(name="hilo1", target=preguntas)

pata = 0
while True:
    if pata == 0:
        t1.start()
        t1.join()
        print("2")
    pata = pata +1
    _, img = cap.read()

    for codes in decode(img):
        data, vertices_array, _ = detector.detectAndDecode(img)
        pts = np.array([codes.polygon], np.int32)
        xi, yi = codes.rect.left, codes.rect.top

        pts = pts.reshape((-1, 1, 2))

        if vertices_array is not None:
            if data and ultimo != data:
                time.sleep(1)
                cv2.polylines(img, [pts], True, (255, 255, 0), 5)
                ultimo = data
                print(ultimo)
                with open(file="kilate.csv", mode='a') as file:
                    file.write(f"{data},Hora de {estado}:,{time.strftime('%H:%M:%S')}\n")
                    cv2.imwrite(
                        "imagenes/foto" + str(num) + '.png', img)
                    num += 1
                    seguro = seguro+1
                    file.close()
                cv2.destroyAllWindows()
                break
            preguntas()
    cv2.imshow("img", img)
    if cv2.waitKey(1) == ord("q"):
        break




cap.release()
cv2.destroyAllWindows()
