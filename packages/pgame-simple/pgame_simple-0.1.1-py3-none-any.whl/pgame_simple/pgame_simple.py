import pygame


class screen:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption('pgsimple project')
        self.running = False
        self._running = False 
        self._update_func = None  

    def start(self, update_func):
        self._update_func = update_func
        self._running = True
        self.running = True
        while self._running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self._running = False
            self._update_func()
            
            pygame.display.flip()
            self.clock.tick(60)
        pygame.quit()

    def bg(self, color):
        self.screen.fill(color)

    def image(self, path):
        return pygame.image.load(path)

    def draw(self, sprite, x, y):
        self.screen.blit(sprite, (x, y))
        
    def get_key(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            return "up"
        if keys[pygame.K_DOWN]:
            return "down"
        if keys[pygame.K_LEFT]:
            return "left"
        if keys[pygame.K_RIGHT]:
            return "right"
        if keys[pygame.K_w]:
            return "w"
        if keys[pygame.K_x]:
            return "x"
        if keys[pygame.K_z]:
            return "z"
        return None
    def movex(self, sprite_x, speed):
        keys = pygame.key.get_pressed() 
        if keys[pygame.K_LEFT]:
            sprite_x -= speed  
        if keys[pygame.K_RIGHT]:
            sprite_x += speed
        return  sprite_x
    def movey(self, sprite_y, speed):
        keys = pygame.key.get_pressed() 
        if keys[pygame.K_UP]:
            sprite_y -= speed  
        if keys[pygame.K_DOWN]:
            sprite_y += speed
        return  sprite_y
    def collisionx(self, sprite1_x, sprite2_x, img):
        if abs(sprite1_x - sprite2_x) < (img.get_width() / 2):
            return True
        return False
    def collisiony(self, sprite1_y, sprite2_y, img):
        if abs(sprite1_y - sprite2_y) < (img.get_height() / 2):
            return True
        return False
    def text(self,text,size):
        font =  pygame.font.Font(None, size)
        return font.render(text, True, (0, 0, 0))
    def title(self,text):
        pygame.display.set_caption(text)
    def icon(self,img):
        icon_img = pygame.image.load(img)
        pygame.display.set_icon(icon_img)
