import cv2, os, pickle, pygame
pygame.init()

#this class will detect and recognize face and show information of the recognized face
class faceDetect:
    def __init__(self):
        self.videoDetect()

    def videoDetect(self):
        win = pygame.display.set_mode((900, 310))
        img_dir = os.path.dirname(os.path.abspath(__file__))
        path = os.path.join(img_dir, 'assets')
        bg = pygame.image.load(path + '/' + 'Background.png')
        icon = pygame.image.load(path + '/' + 'icon.png')
        pygame.display.set_caption('Processing Face Detection...')
        pygame.display.set_icon(icon)
        win.blit(bg, (0, 0))

        face_cascade = cv2.CascadeClassifier('cascadeData/haarcascade_frontalface_default.xml')
        recognizer = cv2.face.LBPHFaceRecognizer_create()
        recognizer.read('Data.yml')

        labels = {}
        with open('Data.pickle', 'rb') as f:
            og_labels = pickle.load(f)
            labels = {v:k for k, v in og_labels.items()}

        cap = cv2.VideoCapture(0)
        name = 'Identify'
        currentID = 'Waiting'
        font = cv2.FONT_ITALIC

        running = True
        while(running):
            pygame.display.update()
            ret, frame = cap.read()
            frame = cv2.flip(frame, 1)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(100, 100), maxSize=(400, 400))
            for (x, y, w, h) in faces:
                roi_gray = gray[y:y+h, x:x+w]
                id_, conf = recognizer.predict(roi_gray)
                if conf >= 15 and conf <= 45:
                    name = labels[id_]
                    if currentID != name:
                        print('Identified:', name)
                        currentID = name
                        self.redrawWindow(name, win)
                if conf > 55:
                    name = 'Identifying...'

                color = (0, 255, 0)
                cv2.rectangle(frame, (x, y), (x+w, y+h), color, 2)
                cv2.putText(frame, name, (x, y - 20), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
            cv2.imshow('Detecting...', frame)

            if cv2.waitKey(20) & 0xFF == ord('q'):
                running = False
                break

        cap.release()
        cv2.destroyAllWindows()
        win = pygame.display.set_mode((600, 600))

    # call this fucntion when face is recognized then show the information of the one program recognized
    def redrawWindow(self, fileName, win):
        title = 'ID:   ' + fileName
        base_dir = os.path.dirname(os.path.abspath(__file__))
        path = os.path.join(base_dir, 'Data')
        path = os.path.join(path, fileName)
        info = []

        with open('/' + path + '/' + fileName + '.pickle', 'rb') as f:
            info = pickle.load(f)

        profile_img = pygame.image.load(path + '/' + 'profile.png')
        name = 'Name:   ' + str(info[1]) + '   ' + str(info[2])
        birth = 'Birth Date:   ' + str(info[3])
        phone = 'Phone Number:   ' + str(info[5])
        email = 'Email:   ' + str(info[4])
        program = 'Program:   ' + str(info[6])
        year = 'Year:    ' + str(info[7])

        font = pygame.font.SysFont('Andale Mono', 28)
        win = pygame.display.set_mode((850, 310))
        pygame.display.set_caption(title)
        win.fill((255, 255, 255))
        win.blit(profile_img, (35, 35))

        text_name = font.render(name, 1, (0, 0, 0))
        win.blit(text_name, (290, 45))
        text_birth = font.render(birth, 1, (0, 0, 0))
        win.blit(text_birth, (290, 85))
        text_phone = font.render(phone, 1, (0, 0, 0))
        win.blit(text_phone, (290, 125))
        text_email = font.render(email, 1, (0, 0, 0))
        win.blit(text_email, (290, 165))
        text_program = font.render(program, 1, (0, 0, 0))
        win.blit(text_program, (290, 205))
        text_year = font.render(year, 1, (0, 0, 0))
        win.blit(text_year, (290, 245))

        pygame.display.update()

# faceDetect()