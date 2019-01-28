import pygame, os
import showFindInfo
pygame.init()

class InputBox:
    def __init__(self, x, y, w, h, text=''):
        font = pygame.font.SysFont('Arial Hebrew', 28)
        self.rect = pygame.Rect(x, y, w, h)
        self.pos = (x, y, w, h)
        self.color = (93, 94, 96)
        self.text = text
        self.txt_surface = font.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
            self.color = (255, 255, 255) if self.active else (93, 94, 96)
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    print('Searching...', self.text)
                    self.color = (93, 94, 96)
                    # check whether the searched name exists or not
                    base_dir = os.path.dirname(os.path.abspath(__file__))
                    path = os.path.join(base_dir, 'Data')
                    path = os.path.join(path, self.text)
                    try:
                        os.path.isfile(path)
                        showFindInfo.showFindInfo(self.text)
                    except IOError:
                        print('Error: Not found try again')

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


class findInfo(InputBox):
    def __init__(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        path = os.path.join(base_dir, 'assets')
        self.banner = pygame.image.load(path + '/' + 'banner.png')
        search_box = InputBox(180, 195, 340, 30)
        self.input_boxes = [search_box]

        self.showFind()

    def showFind(self):
        font = pygame.font.SysFont('Arial Hebrew', 28)
        win = pygame.display.set_mode((600, 300))
        pygame.display.set_caption('Find Information')

        running = True
        while running:
            win.fill((49, 49, 49))
            win.blit(self.banner, (55, 30))
            text_name = font.render('Search: ', 1, (255, 255, 255))
            win.blit(text_name, (80, 200))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                for box in self.input_boxes:
                    box.handle_event(event)
            for box in self.input_boxes:
                box.update()
            for box in self.input_boxes:
                box.draw(win)
            pygame.display.update()
        win = pygame.display.set_mode((600, 600))



# findInfo()


