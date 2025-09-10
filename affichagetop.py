import pygame
import time
import numpy as np

#code  de chatgpt afin d'afficher des images contenues dans une liste grace a pygame avec un delai de 0.5 par defaut
def afficher_images_fullscreen(l1, delay=0.5):
 #   pygame.init()
    # Récupérer la résolution de l'écran
    info = pygame.display.Info()
    screen_width, screen_height = info.current_w, info.current_h
    # Passer en plein écran
    screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
    pygame.display.set_caption("Jeu de la vie")
    for img in l1:
        # Redimensionner l'image à la taille de l'écran
        img_surface = pygame.surfarray.make_surface(np.transpose(img, (1, 0, 2)))
        img_surface = pygame.transform.scale(img_surface, (screen_width, screen_height))
        screen.blit(img_surface, (0, 0))
        pygame.display.flip()
        # Pause et gestion des événements
        start_time = time.time()
        while time.time() - start_time < delay:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    pygame.quit()
                    return
    time.sleep(1)
 #   pygame.quit()

#code pour changer l'etat de la case i j du tableau t afin qu'elle represente l'etat de cette meme case apres
#avoir appliquer une etape au tableau l
def etape(l,i,j):
    acc=-l[i][j]
    for x in range(i-1,i+2):
        for y in range(j-1,j+2):
            acc=acc+l[x][y]
    if l[i][j]==1 and (acc==2 or acc==3):
        return 1
    if l[i][j]==0 and acc==3:
        return 1
    return 0

def tousacote(l1):
    l=[(a[0],a[1]) for a in l1]
    for a in l1:
        i,j=a
        for x in range(i-1,i+2):
            for y in range(j-1,j+2):
                if (x,y) not in l:
                    l.append((x,y))
    return l


def etat_suivant(l,l1=[[]],ind=False):
    n,m=len(l),len(l[0])
    if l1==[[]]:
        l1=[(i,j) for i in range(n) for j in range(m)]
    t=[l[i[0]][i[1]] for i in l1 ]
    l2=[]
    for i in range(len(l1)) :
        t[i]=etape(l,l1[i][0],l1[i][1])
        if t[i]!=l[l1[i][0]][l1[i][1]]:
            l2.append((l1[i][0],l1[i][1]))
    for i in range(len(l1)):
        l[l1[i][0]][l1[i][1]] =t[i]
    if ind:
        return (l,l2)
    else:
        return l

"""code principal qui renvoie le tableau encodant l'etape suivante du jeu de la vie.ici j'ai choisi une implementation
particuliere ou je garde constament en memoire ou commence et ou finit la figure que represente la liste,
avec l[0]la premiere ligne non nulle,l[1] la derniere (si t=0,l[0]>l[1]), et l[2] et l[3] la premiere et derniere
colonne non nulle """

#prend en entree la representation "simple" d'une figure dans le jeu de la vie, et renvoie son implementation
#en rajoutant n 0 dans tout les sens
def initialisation(l,n):
    t=[[0 for j in range(2*n+len(l[0]))] for i in range(2*n+len(l))]
    for i in range(n,n+len(l)):
        for j in range(n,n+len(l[0])):
            t[i][j]=l[i-n][j-n]
    return t


def min(a,b):
    if a>b:
        return b
    return a
def max(a,b):
    if a>b:
        return a
    return b

#afficher les n etapes succesives dans le jeu de la vie en partant de 'l'etape 0 encodee par la figure l
def show(input,n,laps,taille=-1,option_d_affichage=False):
    if taille==-1:
        taille=n
    l=initialisation(input,taille +2)
    nbr1=len(l)
    nbr2=len(l[0])
    l1=[[[(250*l[i][j],250*l[i][j],250*l[i][j]) for j in range(nbr2)] for i in range(nbr1)]]
    bouge=[(i,j) for i in range(taille-1,taille-1+len(input)) for j in range(taille-1,taille-1+len(input[0])) ]
    for k in range(n):
        l,bouge=etat_suivant(l,bouge,True)
        bouge=tousacote(bouge)
        l1.append([[(250*l[i][j],250*l[i][j],250*l[i][j]) for j in range(nbr2)] for i in range(nbr1)])
    print("l realises avec succes")
    afficher_images_fullscreen(l1,laps)
    if option_d_affichage==True:
        return l1

figures={'glider': [[0, 1, 0], [0, 0, 1], [1, 1, 1]], 'blinker': [[1, 1, 1]], 'toad': [[
0, 1, 1, 1], [1, 1, 1, 0]], 'beacon': [[1, 1, 0, 0], [1, 0, 0, 0], [0, 0, 0, 1],
 [0, 0, 1, 1]], 'pulsar': [[0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0,
 0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1], [1, 0, 0,
0, 0, 1, 0, 1, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1], [0, 0, 1
, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0]], 'pentadecathlon': [[0, 1, 0], [1, 1, 1], [0, 1
, 0], [0, 1, 0], [0, 1, 0], [0, 1, 0], [1, 1, 1], [0, 1, 0]], 'lwss': [[0, 1, 1,
 1, 1], [1, 0, 0, 0, 1], [0, 0, 0, 0, 1], [1, 0, 0, 1, 0]], 'mwss': [[0, 1, 1, 1
, 1, 1], [1, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 1, 0]], 'hwss': [[
0, 1, 1, 1, 1, 1, 1], [1, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 1], [1, 0, 0, 0,
 0, 1, 0]], 'diehard': [[0, 0, 0, 0, 0, 0, 1], [1, 1, 0, 0, 0, 0, 0], [0, 1, 0,
0, 0, 1, 1]], 'acorn': [[0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0], [1, 1, 0,
0, 1, 1, 1]], 'r-pentomino': [[0, 1, 1], [1, 1, 0], [0, 1, 0]], 'block': [[1, 1]
, [1, 1]], 'boat': [[1, 1, 0], [1, 0, 1], [0, 1, 0]], 'loaf': [[0, 1, 1, 0], [1,
 0, 0, 1], [0, 1, 0, 1], [0, 0, 1, 0]], 'tub': [[0, 1, 0], [1, 0, 1], [0, 1, 0]]
, 'snake': [[1, 1, 0], [0, 1, 1], [0, 0, 1]]}

gosper_glider_gun = [
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
[1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

