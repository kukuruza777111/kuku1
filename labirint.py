from pygame import*
class GameSprite(sprite.Sprite):
        def _init_(self, picture, w, h, x,y):
            super()._init_()
            self.image = transform.scale(image.load(picture), (w,h))
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
        def reset(self):
            window.blit(self.image,(self.rect.x,self.rect.y))
class GameSprite(sprite.Sprite):
    def _init_(self,player_image, player_x, player_y, size_x, size_y):
        sprite.Sprite._init_(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def _init_(self, player_image, player_x, player_y,size_x,size_y, player_x_speed, player_y_speed):
        GameSprite._init_(self, player_image, player_x, player_y,size_x,size_y)
        self.x_speed = player_x_speed
        self.y_speed = player_y_speed


def update(self):
    if packman.rect.x <= win_width-80 and packman.x.speed > 0 or packman.rect.x >= 0 and packman.x_speed <= 0:
        self.rect.x += self.x_speed
        platforms_touched = sprite.spritecollide(self, barriers, False)
        if self.x_speed >0:
            for p in platforms_touched:
                self.rect.right = min(self.rect.right, p.rect.left)
        elif self.x_speed < 0:
            for p in platforms_touched:
                self.rect.left = max(self.rect.left, p.rect.right)
    if packman.rect.y <= win.height+80 and packman.y.speed < 0 or packman.rect.y <= 0 and packman.y_speed >= 0:
        self.rect.y += self.y_speed
        platforms_touched = sprite.spritecollide(self, barriers, False)
        if self.y_speed >0:
            for p in platforms_touched:
                self.rect.bottom = min(self.rect.right, p.rect.left)
        elif self.y_speed < 0:
            for p in platforms_touched:
                self.rect.top = max(self.rect.left, p.rect.right)

    def fire(self):
        bullet = Bullet('bullet.png', self.rect.right, self.rect.centery, 15, 20,15)
class Enemy(GameSprite):
    side = 'left'
    def _init_(self,player_image, player_x, player_y, size_x,size_y, player_speed):
        self.speed = player_speed

    def update(self):
        if self.rect.x <= 420: 
            self.side = 'right'
        if self.rect.x >=win_width-85:
            self.side = 'left'
        if self.side == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed






class Bullet(GameSprite):
    def _init_(self,player_image, player_x, player_y, size_x,size_y, player_speed):
        GameSprite._init_(self,player_image, player_x, player_y, size_x,size_y,)
        self.speed = player.speed
    
    
    def update(self):
        self.rect.x += self.speed
        if self.rect.x>win_width+10:
            self.kill()



win_width=700
win_height=500
window = display.set_mode((win_width, win_height))
display.set_caption("lab - not labarotory, it is labirint")
back = (134,138,204)
w1 = GameSprite('zxc.jpg', win_width / 2 - win_width /3, win_height /2, 300, 500)
w2 = GameSprite('zxc.jpg', 370,100,50,400)
hero = Player('qwe.png', 5, win_height - 80,80,80,0,0)
enemy = Enemy('asd.jpg',5, win_height - 80,80,80,0)

barriers = sprite.Group()

bullets = sprite.Group()

monsters = sprite.Group()
run = True
while run:
    time.delay(50)
    for i in event.get():
        if i.type == QUIT:
            run = False
    wall_12 = GameSprite('zxc.jpg', 80,180,200,250)
    
    display.update()