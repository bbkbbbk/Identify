# Identify
Identify is a face detection and recognition program written in python. Identify was designed to use in a college to help identifies student and provides student's basic information.

## Requirement
- openCV
- os
- pickle
- numpy

## Program Run Example
<p align="center">
  <img width="350" alt="menu_screen" src="https://user-images.githubusercontent.com/47117776/51985576-c5b0b300-24d0-11e9-8af2-afc5f42e7830.png">
 </p>
<p align="center">Identify has 3 main parts, registeration, face detection and recognition and searching.</p>

<p align="center">
  <img width="350" alt="reg_screen" src="https://user-images.githubusercontent.com/47117776/51986242-6489df00-24d2-11e9-8ea3-2ae7c37b578a.png">
 </p>
<p align="center">In the registeration part, the program will asks user for a basic information.</p>

<p align="center">
  <img width="500" alt="facereg_screen" src="https://user-images.githubusercontent.com/47117776/51986512-f85bab00-24d2-11e9-975f-b658bac01be0.png">
 </p>
<p align="center">After user has filled in their information, the program will open a camera and detect face usong haar cascade in opencv and cellect data of user's face and saves images in Data folder. During this process, the program will captures 25 images of user's face and the last taken image will be user's profile picture that will displays along with user's information. When finished the program will automatically closes and train itself and saves data in xml file.</p>

<p align="center">
  <img width="500" alt="detect_scrn" src="https://user-images.githubusercontent.com/47117776/51987058-31e0e600-24d4-11e9-9393-c9cacfaf234f.png">
 </p>
<p align="center">If user has registerd, Identify will be able to recognized and displays the name that has given in student id in the registeration process. Otherwise, if user hasn't registered the program would not be able to recognize and will display 'unknow' instead.</p>

<p align="center">
  <img width="400" alt="id_scrn" src="https://user-images.githubusercontent.com/47117776/51987421-0ca0a780-24d5-11e9-9cf7-d374f3fc1373.png">
 </p>
<p align="center">When Identify recognized user, it will pop a windiw that contain user's information and an image of user that has taken in the registeration process.</p>

<p align="center">
  <img width="350" alt="search_scrn" src="https://user-images.githubusercontent.com/47117776/51987986-30b0b880-24d6-11e9-9194-09794bec8480.png">
 </p>
<p align="center">To search for information, user need to give the exact name that has registered to Identify. If user is exists in the program data, the program will display a window that contain user information. They also be able to edit their information after the regiseration but can not change their profile picture.</p>

## Problems
When many users have registered to the program, the program still makes a misrecognize due to inadequate data of user's face bacause the program has given only 25 images from each user. The number of image could be increase but when there are a lot of users registered it will takes more time during the training process so I limited the number to 25 to minimized the timing in traing process. Also in the registeration window, I used pygame to receive input from user because I found that pygame can works with opencv without program crashing. I have tried other python GUI i.e. pyqt5, Kivy, Tkinter but none of these can work with opencv. This problem could be fixed with Threading which I am studying about it and will come and fix this in the future.

## Conclusion
Identify is a face detection and recognition program which is a first year university project. Identify is my first project after a few months experience of coding. So, even it is not a perfect and most efficient face detection and recognition program but I have learned a lot of thing while working on this project.
