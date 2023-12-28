import pygame
from playsound import playsound
from pygame import mixer
import os

#colours
white = (255, 255, 255)
black = (0, 0, 0)

#pygame window stuff
screen_height = 500
screen_width = 500
screen = pygame.display.set_mode((screen_height, screen_width))
screen.fill(white)
pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans MS', 30)

clicked = False

class button():
    def __init__(self, color, x, y, w, h, text, func = None):
        self.color = color
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.text = text
        self.func = func
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
    
    def draw_button (self): 
        global clicked
        pos = pygame.mouse.get_pos()
        button_rect = self.rect
        hover = button_rect.collidepoint(pos)
        if hover and pygame.mouse.get_pressed()[0] == 1:
            clicked = not clicked
        color = (144, 144, 144)
        if clicked:
            color = (144, 20, 55)
        elif hover:
            color = (100, 100, 100)
        pygame.draw.rect(screen, color, button_rect)
        text_surface = my_font.render(self.text, False, (0, 0, 0))
        screen.blit(text_surface, (self.x + self.w/3,self.y + self.h/3))

    def call_back (self, *args):
        if self.func:
            return self.func(*args)

def func1():
    print("1")

def func2():
    print("2")

playlist = []

def addSong ():
    print("\n\nList of songs: ")
    directory = os.getcwd() + '/Music Player/'
    for file in os.listdir(directory):
        if (file.endswith(".wav")):
            print("- " + file.split(".")[0])

    song = input("\nEnter the song name you would like to add to the playlist: ")
    song = song + ".wav"
    
    if (os.path.exists(directory + song)):
        playlist.append(song)
        print("\nCurrent playlist: ")
        print(playlist)
    else:
        print("Song does not exist!")

#colours
color = black
song_input_color = (122, 11, 34)

if __name__ == '__main__':
    
    width = screen.get_width()
    height = screen.get_height()

    by = 50
    bx = 100
    
    #buttons https://stackoverflow.com/questions/63435298/how-to-create-a-button-class-in-pygame
    add_song_active = False
    type_active = False
    song = ''
    
    song_input = pygame.Rect(200, 100, bx, by)
    add_song_box = pygame.Rect(100, 100, bx, by)

    button1 = button(black, 300, 300, 100, 50, "add", func1)
    button2 = button(black, 400, 300, 100, 50, "delete", func2)
    button_list = [button1, button2]
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                    clicked = True
                    if (button1.rect.collidepoint(event.pos)): 
                        type_active = True
                    else:
                        type_active = False
            if event.type == pygame.KEYDOWN:
                if type_active:
                    if event.key == pygame.K_RETURN:
                        print(song)
                        song = ''
                        color = black
                    elif event.key == pygame.K_BACKSPACE:
                        song = song[:-1]
                    else:
                        song += event.unicode

            if event.type == pygame.MOUSEBUTTONUP:
                clicked = False
                if song_input.collidepoint(event.pos):
                    add_song_active = False
        screen.fill(white)
        color = (144, 144, 144) if type_active else black
        song_input_color = (144, 144, 144) if add_song_active else song_input_color
        pygame.draw.rect(screen, color, song_input, 2)
        button1.draw_button()
        pygame.display.update()

'''
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                    clicked = True
                    if (song_input.collidepoint(event.pos)): 
                        type_active = True
                    else:
                        type_active = False
                    
                    if (add_song_box.collidepoint(event.pos)):
                        add_song_active = True
                    else:
                        add_song_active = False
            if event.type == pygame.KEYDOWN:
                if type_active:
                    if event.key == pygame.K_RETURN:
                        print(song)
                        song = ''
                        color = black
                    elif event.key == pygame.K_BACKSPACE:
                        song = song[:-1]
                    else:
                        song += event.unicode

            if event.type == pygame.MOUSEBUTTONUP:
                if song_input.collidepoint(event.pos):
                    add_song_active = False
        screen.fill(white)
        color = (144, 144, 144) if type_active else black
        song_input_color = (144, 144, 144) if add_song_active else song_input_color
        pygame.draw.rect(screen, song_input_color, add_song_box)
        pygame.draw.rect(screen, color, song_input, 2)
'''
