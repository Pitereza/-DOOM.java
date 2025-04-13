#Создай собственный Шутер!


from pygame import*
import random
win = display.set_mode((700,500))
display.set_caption("DOOM.java")
pole = transform.scale(image.load("1.png"), (700,500))
mixer.init()
clock = time.Clock()
FPS = 120
font.init()
# font = font.Font(None,40)
font = font.SysFont("Arial", 40)
# font1 = font.Font(None, 36)
width = 70
height = 70
lost = 100
schot = 0
# wine = font.render("YOU WIN", True, (255, 0, 0))
# lost = font.render("YOU LOSE", True, (255, 255, 255))
mixer.music.load("2.ogg")
num = 0
bullets = sprite.Group()
f = mixer.Sound("6.ogg")

w = font.render("YOU WIN", True, (255,0,0))
go = font.render("GAME OVER", True, (255,0,0))
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, ww=60, hh=80):
        super().__init__()
        self.ww = ww
        self.hh = hh
        self.image = transform.scale(image.load(player_image),(self.ww, self.hh))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        win.blit(self.image,(self.rect.x, self.rect.y))


class player(GameSprite):
    def __init__(self, player_image, x1, y1, player_speed,wall_width, wall_height):
        super().__init__(player_image, x1, y1, player_speed,wall_width, wall_height)
        self.width = wall_width
        self.height = wall_height
    def update(self):
        keys_pressed = key.get_pressed()
        clock.tick(FPS)
        if keys_pressed[K_a] and self.rect.x > 5:
            self.rect.x -= 15
        if keys_pressed[K_d] and self.rect.x < 595:
            self.rect.x += 15
        if keys_pressed[K_p]:
            fin = False        
        
    def fire(self):
        global bullets
        bu = Bullet("7.png",self.rect.x, self.rect.y, 10, 100, 100)
        bullets.add(bu)
        # if self.rect.y > 0: 
        #     bullet.kill()
        if self.rect.y < 200:
            
            bu.kill()
            
            
            self.ww = 100
            self.hh = 100    
        

class enemi(GameSprite):
    def __init__(self, player_image, x1, y1, player_speed,wall_w, wall_h):
        super().__init__(player_image, x1, y1, player_speed,wall_w, wall_h)
    def update(self,player_image):
        self.speed = 3
        self.rect.y += self.speed
        global lost
        self.image = transform.scale(image.load(player_image),(self.ww, self.hh))
        clock.tick(FPS)
        self.ww += 2
        self.hh += 2
        # if self.ww <= 120 and self.hh <= 120:
        #     self.ww == 70
        #     self.hh == 70
        # wall_w = width + 10
        # wall_h = height + 10
        if self.rect.y > 360:
            self.rect.x = random.randint(5,595)
            self.rect.y = 200
            self.wall_w = 70
            self.wall_h = 70 
            lost = lost - 20
            self.ww = 70
            self.hh = 70
        # while self.rect.y > 360:
        #     self.wall_w = 70 + 5
        #     self.wall_h = 70 + 5
        
           
        # if self.rect.y <= 360:
        #     self.direction = "down"
        #     self.wall_width = width
        #     self.wall_height = height 
        # if self.rect.y >= 360:
        #     self.direction = "kon"

        # if self.direction == "down":
        #     self.rect.y += self.speed
        # else:
        #     my = 250
        #     mx = random.randint(5,595)
class Bullet(GameSprite):
     
    def __init__(self, player_image, x1, y1, player_speed,wall_w, wall_h):
        super().__init__(player_image, x1, y1, player_speed,wall_w, wall_h)
    def update(self,player_image):
        self.speed = 4
        self.rect.y -= self.speed
        global lost
        self.image = transform.scale(image.load(player_image),(self.ww, self.hh))
        self.ww -= 2
        self.hh -= 2
        global num
        if self.rect.y < 250:
            
            self.kill()
            
            
            self.ww = 100
            self.hh = 100  
        # if self.wall_w and self.wall_h < 1:
        
            
        #     self.wall_w = 100
        #     self.wall_h = 100
        #     self.rect.y = 330
        
        
        #     keys_pressed = key.get_pressed()
        #     self.rect.x = random.randint(5,595)
        #     self.rect.y = 200
        #     self.wall_w = 70
        #     self.wall_h = 70 
        #     lost = lost - 5
        #     self.ww = 70
        #     self.hh = 70
    # 
        
# def yvel(self):
my = 200
mx = random.randint(5,595)
# sp = random.randint(1,15)                  
mixer.music.play()
her = player("9.png", 200, 330, 5, 150,100)
t = GameSprite("11.png", 0, 430, 0,700, 70)
w = GameSprite("13.PNG", 0, 0, 0, 700, 500)
lo = GameSprite("14.png", -10, -10, 0, 800, 600)
Sprite_x = her.rect.x
Sprite_y = her.rect.y
Sprite_center_x = her.rect.centerx
Sprite_top = her.rect.top
# bu = Bullet("7.png",200, 330, 10, 100, 100)
g = True
fin = False
monsters = sprite.Group()
bullets = sprite.Group()

for i in range(1,6):
    r = enemi("5.png", random.randint(5,595), my, 2, width, height )
    monsters.add(r)

keys_pressed = key.get_pressed()




while g:
    for e in event.get():
        if e.type == QUIT:
            g = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                f.play()
                her.fire()

    if fin != True:
        
        win.blit(pole,(0,0))
        text_lose = font.render("Здоровье: " + str(lost), 1, (255, 0, 0))
        kils = font.render("Счётчик: " + str(num), 1, (255, 0, 0))
        win.blit(text_lose,(5,10))
        win.blit(kils,(5,50))
        monsters.draw(win)
        monsters.update("5.png")
        # r.yvel()
        collides = sprite.groupcollide(monsters, bullets, True, True)
        for c in collides:
            # этот цикл повторится столько раз, сколько монстров подбито
            num = num + 1
            r = enemi("5.png", random.randint(5,595), my, 2, width, height )
            monsters.add(r)

        her.update()
        her.reset()
        t.update()
        t.reset()
        bullets.draw(win)
        # bu.update("7.png")
        # bu.reset()
        bullets.update("7.png")
        
    #if sprite.collide_circle(bullets, monsters):
        #self.kill()
        #num + 1            
    if num >= 101:
        w.reset()
        fin = True    
    if lost <= 0 :
        lo.reset()
        fin = True 
    # if schot >= 24:
    #     w.reset()
    #     fin = True 
    


    # r.reset()
    # r.update()
        
    #clock.tick(60)
    # dt = clock.tick(60)
    # her.x1 += her.player_speed * dt
    # her.y1 += her.player_speed * dt
    display.update()
    
    # цикл срабатывает каждую 0.05 секунд
    time.delay(50)

