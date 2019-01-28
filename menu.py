import pygame, os
pygame.init()

class menu:
    def __init__(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        path = os.path.join(base_dir, 'assets')
        self.icon = pygame.image.load(path + '/' + 'icon.png')
        self.banner = pygame.image.load(path + '/' + 'banner.png')
        self.regis_img = pygame.image.load(path + '/' + 'reg.png')
        self.face_img = pygame.image.load(path + '/' + 'face.png')
        self.find_img = pygame.image.load(path + '/' + 'find info.png')
        self.question_img = pygame.image.load(path + '/' + 'q.png')
        self.reg_pressed = pygame.image.load(path + '/' + 'reg_pressed.png')
        self.face_pressed = pygame.image.load(path + '/' + 'face_pressed.png')
        self.find_pressed = pygame.image.load(path + '/' + 'find_pressed.png')
        self.q_pressed = pygame.image.load(path + '/' + 'q_pressed.png')
        self.showMenu()

    def showMenu(self):
        win = pygame.display.set_mode((600, 600))
        running = True
        while running:
            pygame.display.set_caption('Identify')
            pygame.display.set_icon(self.icon)
            win.fill((49, 49, 49))
            win.blit(self.banner, (55, 30))
            win.blit(self.regis_img, (50, 140))
            win.blit(self.face_img, (270, 130))
            win.blit(self.find_img, (90, 310))
            win.blit(self.question_img, (510, 510))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.reg_bt(50, 140, 177, 192, self.reg_pressed, win)
            self.face_bt(270, 130, 296, 321, self.face_pressed, win)
            self.find_bt(90, 310, 234, 252, self.find_pressed, win)
            self.q_bt(510, 510, 60, 60, self.q_pressed, win)
            # button(510, 510, 70, 70, q_pressed, test)
            pygame.display.update()
        pygame.quit()

    def face_bt(self, x_pos, y_pos, width, height, image, win):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x_pos + width > mouse[0] > x_pos and y_pos + height > mouse[1] > y_pos:
            win.blit(image, (x_pos, y_pos))
            if click[0] == 1:
                import faceDection
                faceDection.faceDetect()
    def reg_bt(self, x_pos, y_pos, width, height, image, win):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x_pos + width > mouse[0] > x_pos and y_pos + height > mouse[1] > y_pos:
            win.blit(image, (x_pos, y_pos))
            if click[0] == 1:
                import registerInfo
                registerInfo.regInfo()
    def find_bt(self, x_pos, y_pos, width, height, image, win):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x_pos + width > mouse[0] > x_pos and y_pos + height > mouse[1] > y_pos:
            win.blit(image, (x_pos, y_pos))
            if click[0] == 1:
                import findInfo
                findInfo.findInfo()
    def q_bt(self, x_pos, y_pos, width, height, image, win):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x_pos + width > mouse[0] > x_pos and y_pos + height > mouse[1] > y_pos:
            win.blit(image, (x_pos, y_pos))
            if click[0] == 1:
                import  about
                about.about()

menu()
