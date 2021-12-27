import pygame
from random import *

clock = pygame.time.Clock()
fps=60
font = "calibri.ttf"
white=(255, 255, 255)
black=(0, 0, 0)
gray=(50, 50, 50)
red=(240, 30, 30)
green=(30, 50, 200)
blue=(85, 150, 220)
yellow=(255, 225, 10)

class MyGame:
    def __init__(self):
        pygame.init()
    
        self.level=1
        self.win=0
        self.load_images(self.level)
        self.window_height = 480
        self.window_width = 640
        self.new_game()

        self.window = pygame.display.set_mode((self.window_width, self.window_height))
        
        pygame.display.set_caption("Infestation")

        self.main_menu()

    def load_images(self,level):
        self.imagesDict = {'blob_down': pygame.image.load('blob_down.png'),
                        'blob_left': pygame.image.load('blob_left.png'),
                        'blob_right': pygame.image.load('blob_right.png'),
                        'blob_up': pygame.image.load('blob_up.png'),
                        'block1': pygame.image.load('block1.png'),
                        'block2': pygame.image.load('block2.png'),
                        'block3': pygame.image.load('block3.png'),
                        'bridge_c_left': pygame.image.load('bridge_c_left.png'),
                        'bridge_c_right': pygame.image.load('bridge_c_right.png'),
                        'bridge_c_up': pygame.image.load('bridge_c_up.png'),
                        'bridge_c_down': pygame.image.load('bridge_c_down.png'),
                        'bridge_w': pygame.image.load('bridge_w.png'),
                        'bridge_w_up': pygame.image.load('bridge_w_up.png'),
                        'coast_l1': pygame.image.load('coast_l1.png'),
                        'coast_l2': pygame.image.load('coast_l2.png'),
                        'coast_l3': pygame.image.load('coast_l3.png'),
                        'coast_l4': pygame.image.load('coast_l4.png'),
                        'coast_point1': pygame.image.load('coast_point1.png'),
                        'coast_point2': pygame.image.load('coast_point2.png'),
                        'coast_point3': pygame.image.load('coast_point3.png'),
                        'coast_point4': pygame.image.load('coast_point4.png'),
                        'coast_left': pygame.image.load('coast_left.png'),
                        'coast_right': pygame.image.load('coast_right.png'),
                        'coast_up': pygame.image.load('coast_up.png'),
                        'coast_down': pygame.image.load('coast_down.png'),
                        'goal_closed': pygame.image.load('goal_closed.png'),
                        'goal_open': pygame.image.load('goal_open.png'),
                        'grave_1': pygame.image.load('grave_1.png'),
                        'grave_2': pygame.image.load('grave_2.png'),
                        'grave_3': pygame.image.load('grave_3.png'),
                        'npc1_left': pygame.image.load('npc1_left.png'),
                        'npc2_down': pygame.image.load('npc2_down.png'),
                        'npc3_right': pygame.image.load('npc3_right.png'),
                        'orb': pygame.image.load('orb.png'),
                        'pdown': pygame.image.load('pdown.png'),
                        'pleft': pygame.image.load('pleft.png'),
                        'pright': pygame.image.load('pright.png'),
                        'pup': pygame.image.load('pup.png'),
                        'skeleton_down': pygame.image.load('skeleton_down.png'),
                        'skeleton_left': pygame.image.load('skeleton_left.png'),
                        'skeleton_right': pygame.image.load('skeleton_right.png'),
                        'skeleton_up': pygame.image.load('skeleton_up.png'),
                        't1': pygame.image.load('t1.png'),
                        'tree_1': pygame.image.load('tree_1.png'),
                        'tree_2': pygame.image.load('tree_2.png'),
                        'tree_3': pygame.image.load('tree_3.png'),
                        'tree_4': pygame.image.load('tree_4.png'),
                        'tree_5': pygame.image.load('tree_5.png'),
                        'tree_6': pygame.image.load('tree_6.png'),
                        'water': pygame.image.load('water.png'),
                        'water_stone': pygame.image.load('water_stone.png'),
                        'boat': pygame.image.load('boat.png'),
                        'tu': pygame.image.load('tu.png'),
                        'block_u': pygame.image.load('block_under.png'),
                        'crystal': pygame.image.load('crystal.png'),
                        'gold': pygame.image.load('gold.png'),
                        'plaque': pygame.image.load('plaque.png'),
                        'skull_tile': pygame.image.load('skull_tile.png'),
                        'water_under': pygame.image.load('water_under.png'),
                        'grave_u': pygame.image.load('grave_u.png'),
                        'ladder': pygame.image.load('ladder.png'),
                        'diary': pygame.image.load('diary.png'),
                        'necklace': pygame.image.load('necklace.png')}

        # Different objects depending on the level
        if level==1:

            self.ground = {'f': self.imagesDict['t1'],
            'g': self.imagesDict['bridge_w'],
            'h': self.imagesDict['bridge_w_up'],
            'j': self.imagesDict['bridge_c_left'],
            'k': self.imagesDict['bridge_c_right'],
            'l': self.imagesDict['bridge_c_up'],
            'd': self.imagesDict['bridge_c_down']}

            self.block = {'w': self.imagesDict['water'],
            'Q': self.imagesDict['coast_l1'],
            'W': self.imagesDict['coast_l2'],
            'E': self.imagesDict['coast_l3'],
            'R': self.imagesDict['coast_l4'],
            'T': self.imagesDict['coast_point1'],
            'Y': self.imagesDict['coast_point2'],
            'U': self.imagesDict['coast_point3'],
            'I': self.imagesDict['coast_point4'],
            'O': self.imagesDict['coast_left'],
            'P': self.imagesDict['coast_up'],
            'A': self.imagesDict['coast_right'],
            'S': self.imagesDict['coast_down'],
            'D': self.imagesDict['block1'],
            'F': self.imagesDict['block2'],
            'G': self.imagesDict['block3'],
            'H': self.imagesDict['grave_1'],
            'J': self.imagesDict['grave_2'],
            'K': self.imagesDict['grave_3'],
            'L': self.imagesDict['tree_1'],
            'Z': self.imagesDict['tree_2'],
            'X': self.imagesDict['tree_3'],
            'C': self.imagesDict['tree_4'],
            'V': self.imagesDict['tree_5'],
            'B': self.imagesDict['tree_6'],
            'q': self.imagesDict['water_stone'],
            'N': self.imagesDict['boat']}

            self.objects = {'x': self.imagesDict['orb']}
            
            self.npc = {'7': self.imagesDict['npc1_left'],
            '8': self.imagesDict['npc2_down'],
            '9': self.imagesDict['npc3_right']}

            self.players = {'p': self.imagesDict['pdown']}

            self.enemies = {'m': self.imagesDict['blob_down'],
            's': self.imagesDict['skeleton_down']}

            self.goal = {'0': self.imagesDict['goal_closed'],
                        '1': self.imagesDict['goal_open']}

            self.impassable_enemy = {}
            self.impassable_enemy.update(**self.block,**self.objects,**self.npc,**self.enemies,**self.goal)

            self.impassable_player = {}
            self.impassable_player.update(**self.block)
            self.impassable_player = list(self.impassable_player)
            self.impassable_player.append("0")

            self.impassable_object = {}
            self.impassable_object.update(**self.block,**self.objects,**self.npc,**self.goal)

        elif level==2:
    
            self.ground = {'f': self.imagesDict['tu']}

            self.block = {'w': self.imagesDict['block_u'],
            'Q': self.imagesDict['water_under'],
            'W': self.imagesDict['crystal'],
            'E': self.imagesDict['gold'],
            'R': self.imagesDict['skull_tile'],
            'T': self.imagesDict['grave_u'],
            'I': self.imagesDict['necklace']}

            self.objects = {'x': self.imagesDict['orb']}
            
            self.npc = {'6': self.imagesDict['plaque'],
            '5': self.imagesDict['ladder'],
            '4': self.imagesDict['diary']}

            self.players = {'p': self.imagesDict['pup']}

            self.enemies = {'m': self.imagesDict['blob_down'],
            's': self.imagesDict['skeleton_down']}

            self.goal = {'0': self.imagesDict['goal_closed'],
                        '1': self.imagesDict['goal_open']}

            self.impassable_enemy = {}
            self.impassable_enemy.update(**self.block,**self.objects,**self.npc,**self.enemies,**self.goal)

            self.impassable_player = {}
            self.impassable_player.update(**self.block)
            self.impassable_player = list(self.impassable_player)
            self.impassable_player.append("0")

            self.impassable_object = {}
            self.impassable_object.update(**self.block,**self.objects,**self.npc,**self.goal)

    def new_game(self):
        self.map = []
        linemap = []
        
        with open(f"{self.level}.txt") as new_file:
            for line in new_file:
                line = line.replace("\n", "")
                linemap.append(line)

        # Find the longest row in the map.
        maxWidth = -1
        for i in range(len(linemap)):
            if len(linemap[i]) > maxWidth:
                maxWidth = len(linemap[i])
        # Add spaces to the ends of the shorter rows. This ensures the map will be rectangular.
        for i in range(len(linemap)):
            linemap[i] += 'w' * (maxWidth - len(linemap[i]))

        # Create map file
        for line in linemap:
            a = []
            for char in line:
                a.append(char)
            self.map.append(a)

        self.timePassed = 0
        self.passed = False

        self.height = len(self.map)
        self.width = len(self.map[0])
        self.scale = list(self.imagesDict.values())[0].get_width()
        self.block_width = list(self.imagesDict.values())[0].get_width()
        self.block_height = list(self.imagesDict.values())[0].get_height()
        self.camera_offsety = self.window_height/self.block_height
        self.camera_offsetx = self.window_width/self.block_width
        initp = self.find_player()
        self.initial_camera=[-self.camera_offsety/2+initp[0],-self.camera_offsetx/2+initp[1]]
        self.camera=[-self.camera_offsety/2+initp[0],-self.camera_offsetx/2+initp[1]]
        self.background_static = self.background()

    def background(self):
        self.background_static = []
        for y in range(self.height):
            a = []
            for x in range(self.width):
                square = self.map[y][x]
                if square in self.ground.keys() or square in self.block.keys() or square in self.goal.keys() or square in self.npc.keys():
                    a.append(square)
                else:
                    a.append("f")
            self.background_static.append(a)
        return self.background_static

    def draw_background(self,dy,dx):
        for y in range(self.height):
            for x in range(self.width):
                square = self.background_static[y][x]
                if square in self.ground.keys():
                    self.window.blit(self.ground[square], ((x-dx) * self.scale, (y-dy) * self.scale))
                elif square in self.block.keys():
                    self.window.blit(self.block[square], ((x-dx) * self.scale, (y-dy) * self.scale))
                elif square in self.npc.keys():
                    self.window.blit(self.npc[square], ((x-dx) * self.scale, (y-dy) * self.scale))
                else:
                    self.window.blit(self.ground["f"], ((x-dx) * self.scale, (y-dy) * self.scale))

    def draw_window(self):
        self.draw_background(self.camera[0],self.camera[1])
        dy=self.camera[0]
        dx=self.camera[1]
        for y in range(self.height):
            for x in range(self.width):
                square = self.map[y][x]
                if square in self.players.keys():
                    self.window.blit(self.players[square], ((x-dx) * self.scale, (y-dy) * self.scale))
                if square in self.objects.keys():
                    self.window.blit(self.objects[square], ((x-dx) * self.scale, (y-dy) * self.scale))
                if square in self.enemies.keys():
                    self.window.blit(self.enemies[square], ((x-dx) * self.scale, (y-dy) * self.scale))
                if square in self.goal.keys():
                    self.window.blit(self.goal[square], ((x-dx) * self.scale, (y-dy) * self.scale))
        self.draw_counter()
        pygame.display.flip()

    def text_format(self, message, textFont, textSize, textColor):
        newFont=pygame.font.Font(textFont, textSize)
        newText=newFont.render(message, 0, textColor)
        return newText

    def draw_counter(self):
        if len(self.find_enemy()) > 0:
            counter=self.text_format(f"Monsters alive: {len(self.find_enemy())}", font, 18, black)
            pygame.draw.rect(self.window, (white), (0,self.window_height-25, 140, 50))
            pygame.draw.rect(self.window, (black), (0,self.window_height-25, 140, 50), 2)
            self.window.blit(counter, (10, self.window_height-20))
        else:
            counter=self.text_format(f"Go to the exit", font, 18, black)
            pygame.draw.rect(self.window, (white), (0,self.window_height-25, 140, 50))
            pygame.draw.rect(self.window, (black), (0,self.window_height-25, 140, 50), 2)
            self.window.blit(counter, (10, self.window_height-20))

    def draw_hint(self):
        nextlevel = True

        hint=self.text_format("Try pushing the ball againt something. It bounces!", font, 20, blue)
        hint2=self.text_format("Go to the graveyard and enter the tomb", font, 20, blue)
        title_rect=hint.get_rect()
        title_rect2=hint2.get_rect()
        pygame.draw.rect(self.window, (white), (100,self.window_height/2-25, self.window_width-200, 100))
        pygame.draw.rect(self.window, (black), (100,self.window_height/2-25, self.window_width-200, 100), 2)
        if len(self.find_enemy())>0:
            self.window.blit(hint, (self.window_width/2 - (title_rect[2]/2), 255))
        else:
            self.window.blit(hint2, (self.window_width/2 - (title_rect2[2]/2), 255))
        pygame.display.update()

        while nextlevel == True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key==pygame.K_h:
                        nextlevel = False
        
        self.draw_window()

    def draw_npc_dialog(self, npc):
        dialog = True

        if npc=="4":
            pygame.draw.rect(self.window, (white), (100,50, self.window_width-200, 130))
            pygame.draw.rect(self.window, (black), (100,50, self.window_width-200, 130), 2)
            self.window.blit(self.text_format("You", font, 20, black), (120, 70))
            self.window.blit(self.text_format("Why is there a diary down here? and the ink", font, 18, gray), (120, 100))
            self.window.blit(self.text_format("is still fresh...but this language...is", font, 18, gray), (120, 120))
            self.window.blit(self.text_format("something I've never seen before...", font, 18, gray), (120, 140))
        if npc=="5":
            pygame.draw.rect(self.window, (white), (100,50, self.window_width-200, 150))
            pygame.draw.rect(self.window, (black), (100,50, self.window_width-200, 150), 2)
            self.window.blit(self.text_format("You:", font, 20, black), (120, 70))
            self.window.blit(self.text_format("Where does this ladder lead? It's soo", font, 18, gray), (120, 100))
            self.window.blit(self.text_format("dark down there, I can't see a thing.", font, 18, gray), (120, 120))
            self.window.blit(self.text_format("But...what?! what was that sound?", font, 18, gray), (120, 140))
            self.window.blit(self.text_format("Better keep going forward...", font, 18, gray), (120, 160))
        if npc=="6":
            pygame.draw.rect(self.window, (white), (100,50, self.window_width-200, 150))
            pygame.draw.rect(self.window, (black), (100,50, self.window_width-200, 150), 2)
            self.window.blit(self.text_format("Plaque:", font, 20, black), (120, 70))
            self.window.blit(self.text_format("Urlov the all mighty will come for you all!!!", font, 18, red), (120, 100))
            self.window.blit(self.text_format("But for now, I got out of time to code so", font, 18, red), (120, 120))
            self.window.blit(self.text_format("you'll have to wait to see his WRATH!!!", font, 18, red), (120, 140))
            self.window.blit(self.text_format("Thank you for playing!", font, 18, red), (120, 160))
        if npc=="7":
            pygame.draw.rect(self.window, (white), (100,50, self.window_width-200, 150))
            pygame.draw.rect(self.window, (black), (100,50, self.window_width-200, 150), 2)
            self.window.blit(self.text_format("Isabel:", font, 20, black), (120, 70))
            self.window.blit(self.text_format("They are all comming from the grave of our shaman,", font, 18, yellow), (120, 100))
            self.window.blit(self.text_format("but some ghost is blocking the path to it.", font, 18, yellow), (120, 130))
            self.window.blit(self.text_format("Maybe if you kill all the blue blobs it will", font, 18, yellow), (120, 160))
            self.window.blit(self.text_format("away!", font, 20, yellow), (120, 180))
        elif npc=="8":
            pygame.draw.rect(self.window, (white), (100,50, self.window_width-200, 200))
            pygame.draw.rect(self.window, (black), (100,50, self.window_width-200, 200), 2)
            self.window.blit(self.text_format("Pedro:", font, 20, black), (120, 70))
            self.window.blit(self.text_format("What the hell are these things? Blue blobs?!", font, 18, black), (120, 110))
            self.window.blit(self.text_format("Where are they comming from? I bet it has", font, 18, black), (120, 140))
            self.window.blit(self.text_format("something to do with the experiment Miguel", font, 18, black), (120, 160))
            self.window.blit(self.text_format("did in the shaman's grave yesterday.", font, 18, black), (120, 180))
            self.window.blit(self.text_format("Oh god, oh god, oh god. There are only 3", font, 18, black), (120, 200))
            self.window.blit(self.text_format("of us left alive. We're doomed...", font, 18, black), (120, 220))
        elif npc=="9":
            pygame.draw.rect(self.window, (white), (100,50, self.window_width-200, 200))
            pygame.draw.rect(self.window, (black), (100,50, self.window_width-200, 200), 2)
            self.window.blit(self.text_format("Miguel:", font, 20, black), (120, 70))
            self.window.blit(self.text_format("You shouldn't be here!! We don't know what", font, 18, blue), (120, 110))
            self.window.blit(self.text_format("else to do. We have a monster infestation", font, 18, blue), (120, 130))
            self.window.blit(self.text_format("that is wipping us out. Only this orb can", font, 18, blue), (120, 150))
            self.window.blit(self.text_format("kill them but no one has the strength to", font, 18, blue), (120, 170))
            self.window.blit(self.text_format("push it. Well, since you're here, please,", font, 18, blue), (120, 190))
            self.window.blit(self.text_format("just give it a try...", font, 18, blue), (120, 210))
        pygame.display.update()

        while dialog == True:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN:
                        dialog = False
        self.draw_window()

    def draw_how_to(self):
        how_to = True
        pygame.draw.rect(self.window, (white), (100,self.window_height/2-150, self.window_width-200, 230))
        pygame.draw.rect(self.window, (black), (100,self.window_height/2-150, self.window_width-200, 230), 2)
        self.window.blit(self.text_format("UP KEY: Go Up", font, 19, black), (120, 110))
        self.window.blit(self.text_format("DOWN KEY: Go Down", font, 19, black), (120, 140))
        self.window.blit(self.text_format("LEFT KEY: Go Left", font, 19, black), (120, 170))
        self.window.blit(self.text_format("RIGHT KEY: Go Right", font, 19, black), (120, 200))
        self.window.blit(self.text_format("H KEY: Show Hint", font, 19, black), (120, 230))
        self.window.blit(self.text_format("Bump into NPC: Show Dialog", font, 19, black), (120, 260))
        self.window.blit(self.text_format("Press Enter again to close the window", font, 16, black), (120, 290))
        pygame.display.update()

        while how_to == True:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN:
                        how_to = False
                    if event.key==pygame.K_ESCAPE:
                        pygame.quit()
        self.draw_window()

    def main_menu(self):
        menu = True
        selected="start"
        self.level = 1
        while menu:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_UP and selected in ["start","how to play"]:
                        selected="start"
                    elif event.key==pygame.K_UP and selected in ["quit"]:
                        selected="how to play"
                    elif event.key==pygame.K_DOWN and selected in ["how to play","quit"]:
                        selected="quit"
                    elif event.key==pygame.K_DOWN and selected in ["start"]:
                        selected="how to play"
                    if event.key==pygame.K_RETURN:
                        if selected=="start":
                            self.window.fill((0, 0, 0))
                            self.main_loop()
                        if selected=="quit":
                            pygame.quit()
                            quit()
                        if selected=="how to play":
                            self.draw_how_to()
                        
            # Main Menu UI
            self.window.fill(gray)
            title=self.text_format("Infestation", font, 100, blue)
            if selected=="start":
                text_start = self.text_format("START", font, 75, white)
                text_how = self.text_format("HOW TO PLAY", font, 75, black)
                text_quit = self.text_format("QUIT", font, 75, black)
            elif selected=="how to play":
                text_start = self.text_format("START", font, 75, black)
                text_how = self.text_format("HOW TO PLAY", font, 75, white)
                text_quit = self.text_format("QUIT", font, 75, black)
            elif selected=="quit":
                text_start = self.text_format("START", font, 75, black)
                text_how = self.text_format("HOW TO PLAY", font, 75, black)
                text_quit = self.text_format("QUIT", font, 75, white)
    
            title_rect=title.get_rect()
            start_rect=text_start.get_rect()
            how_rect=text_how.get_rect()
            quit_rect=text_quit.get_rect()
    
            # Main Menu Text
            self.window.blit(title, (self.window_width/2 - (title_rect[2]/2), 60))
            self.window.blit(text_start, (self.window_width/2 - (start_rect[2]/2), 200))
            self.window.blit(text_how, (self.window_width/2 - (how_rect[2]/2), 280))
            self.window.blit(text_quit, (self.window_width/2 - (quit_rect[2]/2), 360))
            # by Manuel Felix - first Sokoban-like game
            pygame.display.update()
            clock.tick(fps)   

    def main_loop(self):
        while True:
            self.timePassed = self.timePassed + clock.tick()
            if self.timePassed > 1500:
                self.enemy_move()
                self.timePassed = 0
            self.check_events()
            self.draw_window()
            if self.win==1:
                self.win=0
                self.win_text()
                self.window.fill((0, 0, 0))
                self.next_level()
            
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit()
                if event.key == pygame.K_LEFT:
                    self.players = {'p': self.imagesDict['pleft']}
                    self.move(0, -1)
                if event.key == pygame.K_RIGHT:
                    self.players = {'p': self.imagesDict['pright']}
                    self.move(0, 1)
                if event.key == pygame.K_UP:
                    self.players = {'p': self.imagesDict['pup']}
                    self.move(-1, 0)
                if event.key == pygame.K_DOWN:
                    self.players = {'p': self.imagesDict['pdown']}
                    self.move(1, 0)
                if event.key == pygame.K_h:
                    self.draw_hint()
            if event.type == pygame.QUIT:
                exit()

    def find_player(self):
        for y in range(self.height):
            for x in range(self.width):
                if self.map[y][x] in ["p"]:
                    return (y, x)

    def find_ball(self):
            for y in range(self.height):
                for x in range(self.width):
                    if self.map[y][x] in ["x"]:
                        return (y, x)

    def find_enemy(self):
        position=[]
        for y in range(self.height):
            for x in range(self.width):
                if self.map[y][x] in ["m","s"]:
                    position.append((y, x))
        return position

    def find_goal(self):
        for y in range(self.height):
            for x in range(self.width):
                if self.map[y][x] in ["0"]:
                    return (y, x)

    def enemy_move(self):
        listEnemies = self.find_enemy()
        if len(listEnemies) == 0:
            return
        for enemy in listEnemies:
            enemy_old_y, enemy_old_x = enemy
            move_ey = randint(-1,1)
            if move_ey == 0:
                move_ex = randrange(-1,2,2)
            else:
                move_ex = 0

            enemy_new_y = enemy_old_y + move_ey
            enemy_new_x = enemy_old_x + move_ex

            if self.map[enemy_new_y][enemy_new_x] not in self.impassable_enemy.keys():
                if self.map[enemy_new_y][enemy_new_x] in ["p"]:
                    self.death()
                    return

                if self.map[enemy_old_y][enemy_old_x] == "m":
                    self.map[enemy_old_y][enemy_old_x] = " "
                    self.map[enemy_new_y][enemy_new_x] = "m"
                elif self.map[enemy_old_y][enemy_old_x] == "s":
                    self.map[enemy_old_y][enemy_old_x] = " "
                    self.map[enemy_new_y][enemy_new_x] = "s"
        self.draw_window()

    def next_level(self):
        self.level = self.level + 1
        nextlevel = False
        while nextlevel == False:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN:
                        nextlevel = True
                if event.type == pygame.QUIT:
                    exit()
        self.load_images(self.level)
        self.new_game()
        
    def death(self):
        dead=self.text_format("Well...you're dead", font, 60, red)
        title_rect=dead.get_rect()
        pygame.draw.rect(self.window, (white), (0,self.window_height/2-25, self.window_width, 100))
        pygame.draw.rect(self.window, (black), (0,self.window_height/2-25, self.window_width, 100), 2)
        self.window.blit(dead, (self.window_width/2 - (title_rect[2]/2), 240))
        pygame.display.update()
        clock.tick(fps)
        startanew = False
        while startanew == False:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN:
                        startanew = True
                if event.type == pygame.QUIT:
                    exit()
        self.new_game()
        self.main_menu()

    def win_text(self):
        win=self.text_format("Entering the Crypt", font, 40, blue)
        title_rect=win.get_rect()
        pygame.draw.rect(self.window, (white), (0,self.window_height/2-25, self.window_width, 100))
        pygame.draw.rect(self.window, (black), (0,self.window_height/2-25, self.window_width, 100), 2)
        self.window.blit(win, (self.window_width/2 - (title_rect[2]/2), 240))
        self.window.blit(self.text_format("Press Enter to continue", font, 16, blue), (240, 280))
        pygame.display.update()
        clock.tick(fps)

    def move(self, move_y, move_x):
        player_old_y, player_old_x = self.find_player()
        player_new_y = player_old_y + move_y
        player_new_x = player_old_x + move_x
        bounce = 0

        if self.map[player_new_y][player_new_x] in self.impassable_player:
            return

        if self.map[player_new_y][player_new_x] in ["x"]:
            object_new_y = player_new_y + move_y
            object_new_x = player_new_x + move_x

            # Make the ball bounce
            if self.map[object_new_y][object_new_x] in self.impassable_object:
                self.map[player_new_y][player_new_x] = "p"
                self.map[player_old_y][player_old_x] = "x"
                bounce = 1
            else: 
                self.map[player_new_y][player_new_x] = "p"
                self.map[object_new_y][object_new_x] = "x"

        if self.map[player_new_y][player_new_x] in ["m","s"]:
            self.death()
            return

        if self.map[player_new_y][player_new_x] in ["1"]:
            self.win=1

        if self.map[player_new_y][player_new_x] in self.npc.keys():
            self.draw_npc_dialog(self.map[player_new_y][player_new_x])
            if self.map[player_new_y][player_new_x] in ["6"]:
                pygame.quit()
            return

        # Open the goal tile
        if len(self.find_enemy()) == 0 and self.passed == False:
            goal_y, goal_x = self.find_goal()
            if self.map[goal_y][goal_x] == "0":
                self.map[goal_y][goal_x] = "1"
            self.passed = True

        # Bounce
        if bounce == 0:
            self.map[player_old_y][player_old_x] = " "
        elif bounce == 1:
            bounce = 0
        self.map[player_new_y][player_new_x] = "p"
        movement = [move_y,move_x]
        self.camera = [a+b for a,b in zip(self.camera,movement)]

if __name__ == "__main__":
    MyGame()