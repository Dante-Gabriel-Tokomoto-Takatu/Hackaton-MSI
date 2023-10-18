import cv2

# Carregar o classificador de rosto pré-treinado do OpenCV
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Iniciar a webcam
cap = cv2.VideoCapture(0)

while True:
    # Ler o frame atual
    ret, frame = cap.read()

    # Converter a imagem para escala de cinza
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detectar rostos na imagem
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Para cada rosto detectado
    for (x, y, w, h) in faces:
        # Desenhar um retângulo ao redor do rosto
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        # Exibir a mensagem "Dante" abaixo do retângulo
        cv2.putText(frame, "Dante", (x, y+h+20), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
        # Exibir a mensagem "Dante Presente" quando um rosto é detectado
        print("Dante Presente")

    # Mostrar o frame atual
    cv2.imshow('Video', frame)

    # Se a tecla 'q' for pressionada, sair do loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Quando tudo estiver pronto, liberar a captura de vídeo
cap.release()
cv2.destroyAllWindows()
