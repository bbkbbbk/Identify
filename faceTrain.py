import cv2, os, pickle, numpy
from PIL import Image

# face train run through every folder in the Data
class faceTrain:
    def __init__(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.image_dir = os.path.join(base_dir, 'Data')
        self.current_id = 0
        self.label_ids = {}
        self.y_labels = []
        self.x_train = []

        self.training()

    def training(self):
        print('Training...')
        face_cascade = cv2.CascadeClassifier('cascadeData/haarcascade_frontalface_default.xml')
        recognizer = cv2.face.LBPHFaceRecognizer_create()

        for root, dirs, files in os.walk(self.image_dir):
            for file in files:
                if file.endswith('jpg') or file.endswith('png'):
                    path = os.path.join(root, file)
                    label = os.path.basename(root).replace(' ', '-').upper()
                    if not label in self.label_ids:
                        self.label_ids[label] = self.current_id
                        self.current_id += 1
                    id_ = self.label_ids[label]

                    pil_image = Image.open(path).convert('L')
                    image_array = numpy.array(pil_image, 'uint8')
                    faces = face_cascade.detectMultiScale(image_array, scaleFactor=1.1, minNeighbors=5, minSize=(100, 100), maxSize=(400, 400))

                    for (x, y, w, h) in faces:
                        roi = image_array[y:y+h, x:x+w]
                        self.x_train.append(roi)
                        self.y_labels.append(id_)

        with open('Data.pickle', 'wb') as f:
            pickle.dump(self.label_ids, f)

        recognizer.train(self.x_train, numpy.array(self.y_labels))
        recognizer.save('Data.yml')

        print('Training successful')

# faceTrain()