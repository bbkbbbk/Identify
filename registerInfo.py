import pygame, os, pickle, registerFace
pygame.init()

# class InputBox is for receiving input form user since pygame does not have its own way to receive input
class InputBox:
    def __init__(self, x, y, w, h, text='None', n = 0):
        font = pygame.font.SysFont('Arial Hebrew', 28)
        self.rect = pygame.Rect(x, y, w, h)
        self.pos = (x, y, w, h)
        self.color = (93, 94, 96)
        self.text = text
        self.txt_surface = font.render(text, True, self.color)
        self.active = False
        self.n = n

    def handle_event(self, event, data):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
            self.color = (255, 255, 255) if self.active else (93, 94, 96)
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    data[self.n] = self.text
                    self.color = (93, 94, 96)
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                font = pygame.font.SysFont('Arial Hebrew', 28)
                self.txt_surface = font.render(self.text, True, self.color)

    def update(self):
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        pygame.draw.rect(screen, self.color, self.pos, 2)


class regInfo(InputBox):
    def __init__(self):
        global win
        base_dir = os.path.dirname(os.path.abspath(__file__))
        path = os.path.join(base_dir, 'assets')

        self.banner = pygame.image.load(path + '/' + 'banner.png')
        self.se = pygame.image.load(path + '/' + 'se.png')
        self.se_pressed = pygame.image.load(path + '/' + 'se_pressed.png')
        self.etm = pygame.image.load(path + '/' + 'etm.png')
        self.etm_pressed = pygame.image.load(path + '/' + 'etm_pressed.png')
        self.y1 = pygame.image.load(path + '/' + 'y1.png')
        self.y2 = pygame.image.load(path + '/' + 'y2.png')
        self.y3 = pygame.image.load(path + '/' + 'y3.png')
        self.y4 = pygame.image.load(path + '/' + 'y4.png')
        self.y1_pressed = pygame.image.load(path + '/' + 'y1_pressed.png')
        self.y2_pressed = pygame.image.load(path + '/' + 'y2_pressed.png')
        self.y3_pressed = pygame.image.load(path + '/' + 'y3_pressed.png')
        self.y4_pressed = pygame.image.load(path + '/' + 'y4_pressed.png')
        self.next = pygame.image.load(path + '/' + 'next.png')
        self.cancel = pygame.image.load(path + '/' + 'cancel.png')
        self.next_pressed = pygame.image.load(path + '/' + 'next_pressed.png')
        self.cancel_pressed = pygame.image.load(path + '/' + 'cancel_pressed.png')
        self.se_active = False
        self.etm_active = False
        self.y1_active = False
        self.y2_active = False
        self.y3_active = False
        self.y4_active = False
        self.showReg()

    def showReg(self):
        font = pygame.font.SysFont('Arial Hebrew', 28)
        win = pygame.display.set_mode((600, 760))
        first_box = InputBox(180, 155, 360, 30, '', 1)
        last_box = InputBox(180, 205, 360, 30, '', 2)
        birth_box = InputBox(180, 255, 200, 30, '', 3)
        id_box = InputBox(180, 305, 200, 30, '', 0)
        email_box = InputBox(180, 355, 360, 30, '', 4)
        phone_box = InputBox(180, 405, 200, 30, '', 5)
        input_boxes = [first_box, last_box, birth_box, id_box, email_box, phone_box]
        self.running = True
        dic = ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None']

        while self.running:
            win.fill((49, 49, 49))
            win.blit(self.banner, (55, 20))
            text_name = font.render('First Name : ', 1, (255, 255, 255))
            win.blit(text_name, (50, 160))
            text_last = font.render('Last Name : ', 1, (255, 255, 255))
            win.blit(text_last, (50, 210))
            text_birth = font.render('Birth Date : ', 1, (255, 255, 255))
            win.blit(text_birth, (50, 260))
            text_date = font.render('DD/MM/YYYY', 1, (255, 255, 255))
            win.blit(text_date, (400, 260))
            text_id = font.render('Student ID: ', 1, (255, 255, 255))
            win.blit(text_id, (50, 310))
            text_email = font.render('Email: ', 1, (255, 255, 255))
            win.blit(text_email, (50, 360))
            text_phone = font.render('Phone: ', 1, (255, 255, 255))
            win.blit(text_phone, (50, 410))
            text_program = font.render('Program: ', 1, (255, 255, 255))
            win.blit(text_program, (50, 460))
            if self.se_active:
                win.blit(self.se_pressed, (40, 500))
            else:
                win.blit(self.se, (40, 500))
            if self.etm_active:
                win.blit(self.etm_pressed, (40, 560))
            else:
                win.blit(self.etm, (40, 560))
            if self.y1_active:
                win.blit(self.y1_pressed, (40, 620))
            else:
                win.blit(self.y1, (40, 620))
            if self.y2_active:
                win.blit(self.y2_pressed, (180, 620))
            else:
                win.blit(self.y2, (180, 620))
            if self.y3_active:
                win.blit(self.y3_pressed, (320, 620))
            else:
                win.blit(self.y3, (320, 620))
            if self.y4_active:
                win.blit(self.y4_pressed, (460, 620))
            else:
                win.blit(self.y4, (460, 620))
            win.blit(self.next, (470, 700))
            win.blit(self.cancel, (540, 700))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                for box in input_boxes:
                    box.handle_event(event, dic)

            for box in input_boxes:
                box.update()

            for box in input_boxes:
                box.draw(win)

            # call button function
            self.se_bt(40, 500, 286, 46, self.se_pressed, win, dic)
            self.etm_bt(40, 560, 522, 46, self.etm_pressed, win, dic)
            self.y1_bt(40, 620, 105, 46, self.y1_pressed, win, dic)
            self.y2_bt(180, 620, 105, 46, self.y2_pressed, win, dic)
            self.y3_bt(320, 620, 105, 46, self.y3_pressed, win, dic)
            self.y4_bt(460, 620, 105, 46, self.y4_pressed, win, dic)
            self.next_bt(470, 700, 48, 34, self.next_pressed, win, dic)
            self.cancel_bt(540, 700, 38, 38, self.cancel_pressed, win)

            pygame.display.update()
        win = pygame.display.set_mode((600, 600))

    def se_bt(self, x_pos, y_pos, width, height, image, win, data):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x_pos + width > mouse[0] > x_pos and y_pos + height > mouse[1] > y_pos:
            win.blit(image, (x_pos, y_pos))
            if click[0] == 1:
                self.se_active = True
                self.etm_active = False
                data[6] = 'Software Engineering'
    def etm_bt(self, x_pos, y_pos, width, height, image, win, data):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x_pos + width > mouse[0] > x_pos and y_pos + height > mouse[1] > y_pos:
            win.blit(image, (x_pos, y_pos))
            if click[0] == 1:
                self.se_active = False
                self.etm_active = True
                data[6] = 'Engineering of Technology and Management'
    def y1_bt(self, x_pos, y_pos, width, height, image, win, data):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x_pos + width > mouse[0] > x_pos and y_pos + height > mouse[1] > y_pos:
            win.blit(image, (x_pos, y_pos))
            if click[0] == 1:
                data[7] = '1'
                self.y1_active = True
                self.y2_active = False
                self.y3_active = False
                self.y4_active = False

    def y2_bt(self, x_pos, y_pos, width, height, image, win, data):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x_pos + width > mouse[0] > x_pos and y_pos + height > mouse[1] > y_pos:
            win.blit(image, (x_pos, y_pos))
            if click[0] == 1:
                data[7] = '2'
                self.y1_active = False
                self.y2_active = True
                self.y3_active = False
                self.y4_active = False

    def y3_bt(self, x_pos, y_pos, width, height, image, win, data):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x_pos + width > mouse[0] > x_pos and y_pos + height > mouse[1] > y_pos:
            win.blit(image, (x_pos, y_pos))
            if click[0] == 1:
                data[7] = '3'
                self.y1_active = False
                self.y2_active = False
                self.y3_active = True
                self.y4_active = False

    def y4_bt(self, x_pos, y_pos, width, height, image, win, data):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x_pos + width > mouse[0] > x_pos and y_pos + height > mouse[1] > y_pos:
            win.blit(image, (x_pos, y_pos))
            if click[0] == 1:
                data[7] = '4'
                self.y1_active = False
                self.y2_active = False
                self.y3_active = False
                self.y4_active = True

    def next_bt(self, x_pos, y_pos, width, height, image, win, data):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x_pos + width > mouse[0] > x_pos and y_pos + height > mouse[1] > y_pos:
            win.blit(image, (x_pos, y_pos))
            if click[0] == 1:
                self.getData(data)

    def cancel_bt(self, x_pos, y_pos, width, height, image, win):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x_pos + width > mouse[0] > x_pos and y_pos + height > mouse[1] > y_pos:
            win.blit(image, (x_pos, y_pos))
            if click[0] == 1:
                self.running = False

    def getData(self, data):
        fileName = data[0]
        base_dir = os.path.dirname(os.path.abspath(__file__))
        path = os.path.join(base_dir, 'Data')
        path = os.path.join(path, fileName)
        try:
            os.makedirs(path)
        except FileExistsError:
            raise TypeError('Already registered')

        with open('/' + path + '/' + fileName + '.pickle', 'wb') as f:
            pickle.dump(data, f)
        registerFace.registerFace(fileName)
        print('completely registered')
        self.running = False


# regInfo()