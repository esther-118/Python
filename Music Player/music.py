import pygame
from playsound import playsound
from pygame import mixer
import os

#colours
white = (255, 255, 255)
black = (0, 0, 0)
color = black
song_input_color = (122, 11, 34)

#pygame window stuff
pygame.init()
pygame.font.init()
screen_height = 500
screen_width = 500
screen = pygame.display.set_mode((screen_height, screen_width))
screen.fill(white)
my_font = pygame.font.SysFont('Arial MT', 30)

#global variables
playlist = [] # global playlist
text = "" # text to display
clicked = False # if a button was pressed

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
            color = (144, 144, 144)
        elif hover:
            color = (100, 100, 100)
        pygame.draw.rect(screen, color, button_rect)
        text_surface = my_font.render(self.text, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=(self.w/2 + self.x, self.h/2 + self.y))
        screen.blit(text_surface, text_rect)
        #screen.blit(text_surface, (self.x + self.w/3,self.y + self.h/3))

    def call_back (self, *args):
        if self.func:
            return self.func(*args)

def func1():
    print("1")

def func2():
    print("2")

def add_delete_song (song_name, action):
    global text
    print("\n\nList of songs: ")
    directory = os.getcwd() + '/'
    for file in os.listdir(directory): # print list of songs
        if (file.endswith(".wav")):
            print("- " + file.split(".")[0])
    
    song = song_name + ".wav"
    if (os.path.exists(directory + song)):
        if action == 0:
            playlist.append(song)
            print("\nCurrent playlist: ")
            print(playlist)
            text = "Added song " + song_name + " to the playlist."
        else:
            playlist.remove(song)
            print("\nCurrent playlist: ")
            print(playlist)
            text = "Removed song" + song_name + " from the playlist"         
    else:
        print("Song does not exist!")
        text = "Song does not exist!"

if __name__ == '__main__':
    
    width = screen.get_width()
    height = screen.get_height()

    by = 50
    bx = 100
    
    #buttons https://stackoverflow.com/questions/63435298/how-to-create-a-button-class-in-pygame
    #add_song_active = False
    type_active = False # used for active user input
    song = ''
    
    song_input = pygame.Rect(200, 100, bx, by)
    #add_song_box = pygame.Rect(100, 100, bx, by)

    add_button = button(black, 100, 100, 100, 50, "Add", func1)
    delete_song = button(black, 100, 160, 100, 50, "Delete", func2)
    play_song = button(black, 100, 220, 100, 50, "Play", func2)
    pause_song = button(black, 100, 280, 100, 50, "Pause", func2)
    unpause_song = button(black, 100, 340, 100, 50, "Unpause", func2)
    
    running = True
    pause = 1
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                    if (add_button.rect.collidepoint(event.pos)): # add song
                        clicked = True
                        add_delete_song(song, 0)
                        song = ''
                        color = black
                        add_button.color = (12, 12, 14)
                    else:
                        clicked = False
                    
                    if (delete_song.rect.collidepoint(event.pos)): # delete song
                        clicked = True
                        add_delete_song(song, 1)
                        song = ''
                        color = black
                    else:
                        clicked = False

                    if (song_input.collidepoint(event.pos)): # input box
                        type_active = True
                    else:
                        type_active = False
                    
                    if (play_song.rect.collidepoint(event.pos)):
                        if len(playlist) > 0:
                            pygame.mixer.music.load(playlist[0])
                            playlist.pop(0)
                            pygame.mixer.music.play()

                    if (pause_song.rect.collidepoint(event.pos)):
                        pygame.mixer.pause()
                        pause = 0
                    
                    if (unpause_song.rect.collidepoint(event.pos)):
                        pygame.mixer.unpause()
                        pause = 1
            
            if event.type == pygame.KEYDOWN:
                if type_active: #song input
                    if event.key == pygame.K_RETURN: 
                        #print(song)
                        add_delete_song(song, 0)
                        song = ''
                        color = black
                    elif event.key == pygame.K_BACKSPACE:
                        song = song[:-1]
                    else:
                        song += event.unicode
        
        screen.fill(white)
        color = (144, 144, 144) if type_active else black
        #song_input_color = (144, 144, 144) if add_song_active else song_input_color
        pygame.draw.rect(screen, color, song_input, 2)
        
        add_button.draw_button()
        delete_song.draw_button()
        play_song.draw_button()
        pause_song.draw_button()
        unpause_song.draw_button()
        my_font = pygame.font.SysFont('Comic Sans MS', 30)
        text_surface = my_font.render(text, False, (0, 0, 0))
        #print(text)
        screen.blit(text_surface, (0,0))
        
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
