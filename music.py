
import pygame
from keyboard import on_press,wait,unhook_all
import os

corrent_red = '\033[31m {} \033[m'.format('='*20)

def music_tocar(list,n):

    pygame.init()

    print(f"{corrent_red}\n\033[32m---TOCANDO MUSICA:\033[m \033[33m{list[n]}.\033[m\n{corrent_red}\n")
    pygame.mixer.music.load(f'musicas/{list[n]}')
    pygame.mixer.music.set_volume(1.0)
    pygame.mixer.music.play() 
    on_press(press_space)

    while pygame.mixer.music.get_busy():
        pass

t = 0

def press_space(event):
    global t

    if event.name == "space":
        t += 1
        print(t)
        if t % 2 == 1:
            print("\033[31mPAUSADO!!!\033[m")
            pygame.mixer.music.pause()
        else: 
            print("\033[32mPLAY!!!\033[m")
            pygame.mixer.music.unpause()
        
    if event.name == "left":
        print("AVANÇAR")
        pygame.mixer.music.set_pos(30)
    
    if event.name == "right":
        print("RETROCEDER")
        pygame.mixer.music.set_pos(-30)
    

past = 'musicas'
musica_list = []

arquive_music = os.listdir(past)

for m in arquive_music:
    
    caminho_musica = os.path.join(past, m)
    musica_list.append(m)

i = 0

for m in arquive_music:

    print(f"{i}- {m}")
    i += 1

def input_esc():
    escolha = int(input(f"\n Digite um número de 0 a {len(musica_list) - 1}: "))
    return escolha

inp = input_esc()


def escolha_validacao(escolha):
   while True:
        if escolha < 0 or escolha >= len(musica_list):
            print("digite novamente, número invalido!")
            escolha = input_esc()
        else:
           return escolha

music_selector = escolha_validacao(inp)

if musica_list:
    music_tocar(musica_list,music_selector)
else:
    print("Nenhuma música encontrada no diretório.")

wait("esc")  
unhook_all()