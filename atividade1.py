# Desenvolvimento Avancado de Software
# Autores: Ebenezer Andrade e Omar Junior
# Atividade 2 - Pair Programming
# Algoritmo solucionando apenas a deteccao das faces

import urllib
import cv2
import numpy as np


def menu():
    select = int(raw_input('''
        Menu
        1: Carregar imagem local
        2: Carregar imagem a partir de uma URL
        3: Capturar imagem da webcam
        4: sair

        Selecione uma das opcoes:'''))
    return select


def main():

    while True:
        select = menu()
        if select == 1:
            print('Opcao 1 escolhida')
            local_image = raw_input('Entre com o caminho da imagem:')
            processFaces(local_image)
        elif select == 2:
            # Request URL to user
            url = raw_input('Insere a URL:')

            # Get content of URL
            url_response = urllib.urlopen(url)

            # Convert into a numpy array
            image_array = np.array(bytearray(url_response.read()), dtype=np.uint8)
            imageCode = cv2.imdecode(image_array, -1)

            file = "/home/ebenezer/DAS/test_image_URL.png"
            cv2.imwrite(file, imageCode)

            imageCode = file

            processFaces(imageCode)
        elif select == 3:

            camera_port = 0
            # Initialize the camera on port 0 using Video Capture
            camera = cv2.VideoCapture(camera_port)

            # Capture a single image
            def get_image():
                retval, im = camera.read()
                return im

            print("Tirando a foto")
            # Stores obtained image
            camera_capture = get_image()
            file = "/home/ebenezer/DAS/test_image.png"

            cv2.imwrite(file, camera_capture)

            fileFinal = file
            processFaces(fileFinal)
        elif select == 4:
            exit()
        else:
            print('Opcao invalida tente novamente')


def processFaces(object):
    # Directory with the classifier for the facesFrontais
    faceCascade = cv2.CascadeClassifier('/home/ebenezer/DAS/opencv/data/haarcascades/haarcascade_frontalface_default.xml')
    image = cv2.imread(object)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect objects in the picture
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(20, 20),
        flags = cv2.CASCADE_SCALE_IMAGE
    )

    # Print amount faces found
    print "Encontradas {0} faces!".format(len(faces))

    # Draw retangle in around faces
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow('Imagem da Webcam', image)

    return cv2.waitKey()

main()
