import pygame, os

class about:
    def __init__(self):
        pygame.init()
        base_dir = os.path.dirname(os.path.abspath(__file__))
        path = os.path.join(base_dir, 'assets')
        self.win = pygame.display.set_mode((600, 600))
        self.win.fill((49, 49, 49))
        self.about_img = pygame.image.load(path + '/' + 'about.png')
        self.showAbout()

    def showAbout(self):
        running = True
        while running:
            self.win.blit(self.about_img, (0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            pygame.display.update()

# about()