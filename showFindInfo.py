import pygame, os, pickle, editInfo

#this class only show information of the desire individual
class showFindInfo:
    def __init__(self, fileName):
        self.fileName = fileName
        self.title = 'ID:   ' + self.fileName
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.path = os.path.join(base_dir, 'Data')
        self.path = os.path.join(self.path, fileName)
        self.asset_path = os.path.join(base_dir, 'assets')

        info = []
        with open('/'+self.path+'/'+fileName+'.pickle', 'rb') as f:
            info = pickle.load(f)

        self.profile_img = pygame.image.load(self.path+'/'+'profile.png')
        self.edit_img = pygame.image.load(self.asset_path+'/'+'edit.png')
        self.edit_pressed = pygame.image.load(self.asset_path+'/'+'edit_pressed.png')
        self.name = 'Name:   ' + info[1] + '   ' + info[2]
        self.birth = 'Birth Date:   ' + info[3]
        self.phone = 'Phone Number:   ' + info[5]
        self.email = 'Email:   ' + info[4]
        self.program = 'Program:   ' + info[6]
        self.year = 'Year:    ' + info[7]
        self.guiInfo()

    def guiInfo(self):
        pygame.init()
        font = pygame.font.SysFont('Andale Mono', 28)
        win = pygame.display.set_mode((850, 310))
        pygame.display.set_caption(self.title)
        win.fill((255, 255, 255))
        win.blit(self.profile_img, (35, 35))

        text_name = font.render(self.name, 1, (0, 0, 0))
        win.blit(text_name, (290, 45))
        text_birth = font.render(self.birth, 1, (0, 0, 0))
        win.blit(text_birth, (290, 85))
        text_phone = font.render(self.phone, 1, (0, 0, 0))
        win.blit(text_phone, (290, 125))
        text_email = font.render(self.email, 1, (0, 0, 0))
        win.blit(text_email, (290, 165))
        text_program = font.render(self.program, 1, (0, 0, 0))
        win.blit(text_program, (290, 205))
        text_year = font.render(self.year, 1, (0, 0, 0))
        win.blit(text_year, (290, 245))

        running = True
        while running:
            # self.redrawWindow()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            win.blit(self.edit_img, (800, 15))
            self.edit_bt(800, 15, 33, 33, self.edit_pressed, win)
            pygame.display.update()
        pygame.display.set_caption('Find Information')
        win = pygame.display.set_mode((600, 300))

    def edit_bt(self, x_pos, y_pos, width, height, image, win):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x_pos + width > mouse[0] > x_pos and y_pos + height > mouse[1] > y_pos:
            win.blit(image, (x_pos, y_pos))
            if click[0] == 1:
                editInfo.editInfo(self.fileName)


# showFindInfo('61090026')