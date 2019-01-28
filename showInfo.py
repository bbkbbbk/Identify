import pygame, os, pickle
pygame.init()

#this class only show information of the desire individual
class showInfo:
    def __init__(self, fileName):
        self.fileName = fileName
        self.title = 'ID:   ' + self.fileName
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.path = os.path.join(base_dir, 'Data')
        self.path = os.path.join(self.path, fileName)

        info = []
        with open('/'+self.path+'/'+fileName+'.pickle', 'rb') as f:
            info = pickle.load(f)

        self.profile_img = pygame.image.load(self.path+'/'+'profile.png')
        self.name = 'Name:   ' + str(info[1]) + '   ' + str(info[2])
        self.birth = 'Birth Date:   ' + str(info[3])
        self.phone = 'Phone Number:   ' + str(info[5])
        self.email = 'Email:   ' + str(info[4])
        self.program = 'Program:   ' + str(info[6])
        self.year = 'Year:    ' + str(info[7])

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
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            pygame.display.update()



# showInfo('61090026')