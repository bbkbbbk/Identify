import cv2, os, faceTrain

# collecting data for face training by taking picture of individuals
class registerFace():
    def __init__(self, fileName):
        face_cascade = cv2.CascadeClassifier('cascadeData/haarcascade_frontalface_default.xml')
        base_dir = os.path.dirname(os.path.abspath(__file__))
        image_dir = os.path.join(base_dir, 'Data')
        image_dir = os.path.join(image_dir, fileName)
        red = (115, 89, 231)
        green = (182, 171, 76)
        font = cv2.FONT_ITALIC

        cap = cv2.VideoCapture(0)
        num_img = 0
        time = 0
        running = True
        while(running):
            time += 1
            if time > 1000:
                time = 0
            ret, frame = cap.read()
            frame = cv2.flip(frame, 1)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(150, 150), maxSize=(400, 400))
            for (x, y, w, h) in faces:
                roi_gray = gray[y:y+h+70, x:x+w+50]
                roi_color = frame[y:y+h+70, x:x+w+50]
                profile_img = cv2.resize(roi_color, (220, 240))
                cv2.imwrite(os.path.join(image_dir, 'profile.png'), profile_img)
                if time % 2 == 0:
                    num_img += 1
                    color = (0, 255, 0)
                    img_item = str(num_img)+'.png'
                    cv2.imwrite(os.path.join(image_dir, img_item), roi_gray)
                    print(num_img)
                    if num_img == 25:
                        running = False
                        break
                else:
                    color = (255, 0, 0)
                width = x + w
                height = y + h
                cv2.rectangle(frame, (x, y), (width, height), color, 2)
            cv2.putText(frame, 'Collecting face data: ', (50, 75), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
            cv2.rectangle(frame, (400, 50), (650, 80), red, -1)
            cv2.rectangle(frame, (400, 50), ((num_img*10)+400, 80), green, -1)
            cv2.imshow('Registering...', frame)
            if cv2.waitKey(20) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()
        faceTrain.faceTrain()

# registerFace()