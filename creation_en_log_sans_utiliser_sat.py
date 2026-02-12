"""On accéde aux listes encodant les figures que je souhaite traiter, c'est a dire
un Herschel et les conduits utilisés. Ces derniers sont des conduits de Herschel, representés par une lettre indiquant la rotation qu'ils effectuent, R pour Right, L pour Left et F pour Forward, et le temps qu'ils prennent a modifier le Herschel.
On utilise egalement Snark et Semi-Snark, qui sont des reflécteurs de planeurs, Snark etant un reflecteur typique et Semi-Snark un multiplicateur de période, c'est à dire qu'il agit comme un Snark à ceci prés qu'il consomeun planeur sur 2.
On a enfin le eater, une figure qui absorbe et détruit un planeur incident, sans se modifier"""

herschel=[
[1, 0, 0],
[1, 0, 1],
[1, 1, 1],
[0, 0, 1]]

glider=[
[0,1,0],
[0,0,1],
[1,1,1]]

import repertoire

R64=repertoire.R64
R190=repertoire.R190
Fx77double=repertoire.Fx77double
Fx77double_de_gun=repertoire.Fx77double_de_gun
F116=repertoire.F116
F117=repertoire.F117
L112=repertoire.L112
F282=repertoire.F282

semisnarkactif=repertoire.semisnarkactif
semisnark=repertoire.semisnark
semisnarkrenverseactif=repertoire.semisnarkrenverseactif
semisnarkrenverse=repertoire.semisnarkrenverse

eater=repertoire.eater
snark=repertoire.snark
snarkrenverse=repertoire.snarkrenverse

scorbie_splitter_off=repertoire.scorbieoff
scorbie_splitter_on=repertoire.scorbieon
scorbie_splitter_renverse_off=repertoire.scorbierenverseoff
scorbie_splitter_renverse_on=repertoire.scorbierenverseon

h_to_g=repertoire.h_to_g
syringe=repertoire.syringe

mega_bistable=repertoire.mega_bistable
mega_bistabledecale=repertoire.mega_bistable_decale
mega_bistable_sans_sortie=repertoire.mega_bistable_sans_sortie
mega_bistable_decale_sans_sortie=repertoire.mega_bistable_decale_sans_sortie

"""On utilise des dictionaires pour representer des conduits :
-La clé "droit" correspond au conduit en lui même
-La clé "dx,dy" correspond au déplacement dans la grille du haut gauche du herschel en entrée. x est l'axe vertical, y l'axe horizontal de sorte que l'on connait l'etat de l en (x,y) en appelant l[x][y]
-La clé "rotation" correspond a la rotation
-La clé "positionne" correspond a la position relative du haut gauche du conduit par rapport au haut gauche du Herschel
-La clé "dimension_de_l'entrée" donne la dimension de la figure en entrée du conduit. Elle correspond a (4,3) pour Herschel mais cette representation se veut generale, par exeple en incluant Snark. SemiSnark est naivement considére comme un conduit tout comme le eater
-La clé "emission", toujours pour être general, précise si ce conduit libére un element en meme temps qu'il modifie quelqu'un. C'est une liste qui n'est pas vide uniquement pour conduit154degun qui est utilisé pour creer des guns, et qui differe de conduit154 car on en retire un eater
-La clé "ticks" qui précise en combien de temps le conduit évolue avant de recreer la figure en entrée a la position précisée par "dx,dy" """

conduitsnark={"droit":snark,"dx,dy":(-8,20),"rotation":"gauche","positionne":(-3,-6),"dimension_de_l'entree":(3,3),"emission":[],"ticks":86}
conduitsnarkrenverse={"droit":snarkrenverse,"dx,dy":(21,-3),"rotation":"droite","positionne":(-3,-1),"dimension_de_l'entree":(3,3),"emission":[],"ticks":86}

conduitsemisnarkactif={"droit":semisnarkactif,"dx,dy":(-2,17),"rotation":"gauche","positionne":(7,1),"dimension_de_l'entree":(3,3),"emission":[],"ticks":96}
conduitsemisnarkrenverseactif={"droit":semisnarkrenverseactif,"dx,dy":(17,-2),"rotation":"droite","positionne":(1,6),"dimension_de_l'entree":(3,3),"emission":[],"ticks":96}

conduitsemisnark={"droit":semisnark,"dx,dy":(-2,17),"rotation":"gauche","positionne":(7,1),"dimension_de_l'entree":(3,3),"emission":[],"ticks":96}
conduitsemisnarkrenverse={"droit":semisnarkrenverse,"dx,dy":(17,-2),"rotation":"droite","positionne":(1,6),"dimension_de_l'entree":(3,3),"emission":[],"ticks":96}

conduitscorbie_splitter_off={"droit":scorbie_splitter_off,"dx,dy":(59,0),"rotation":"droit","positionne":(18,-12),"dimension_de_l'entree":(3,3),"emission":[],"ticks":378}
conduitscorbie_splitter_renverse_off={"droit":scorbie_splitter_renverse_off,"dx,dy":(0,59),"rotation":"droit","positionne":(-11,18),"dimension_de_l'entree":(3,3),"emission":[],"ticks":378}

conduitscorbie_splitter_on={"droit":scorbie_splitter_on,"dx,dy":(59,0),"rotation":"droit","positionne":(18,-22),"dimension_de_l'entree":(3,3),"emission":[("glider","gauche",395,(39,-14))],"ticks":378}
conduitscorbie_splitter_renverse_on={"droit":scorbie_splitter_renverse_on,"dx,dy":(0,59),"rotation":"droit","positionne":(-21,18),"dimension_de_l'entree":(3,3),"emission":[("glider","gauche",395,(39,-14))],"ticks":350}


conduith_to_g={"droit":h_to_g,"dx,dy":(12,18),"rotation":"droit","positionne":(-28,-2),"dimension_de_l'entree":(4,3),"dimension_de_la_sortie":(3,3),"emission":[],"ticks":86}

conduitsyringe={"droit":syringe,"dx,dy":(10,26),"rotation":"droit","positionne":(3,-3),"dimension_de_l'entree":(3,3),"dimension_de_la_sortie":(4,3),"emission":[],"ticks":127}

conduitmega_bistable={"droit":mega_bistable,"dx,dy":(140,140),"rotation":"droit","positionne":(13,-4),"dimension_de_l'entree":(3,3),"emission":[],"ticks":560,"repeat time":(76,104),"ajout":1042}

conduitmega_bistabledecale={"droit":mega_bistabledecale,"dx,dy":(140,140),"rotation":"droit","positionne":(13,-4),"dimension_de_l'entree":(3,3),"emission":[],"ticks":560,"repeat time":(76,104),"ajout":1042}

conduitmega_bistable_sans_sortie={"droit":mega_bistable_sans_sortie,"dx,dy":(140,140),"rotation":"droit","positionne":(13,-4),"dimension_de_l'entree":(3,3),"emission":[],"ticks":560,"repeat time":(76,104),"ajout":1042}

conduitmega_bistabledecale_sans_sortie={"droit":mega_bistable_decale_sans_sortie,"dx,dy":(140,140),"rotation":"droit","positionne":(13,-4),"dimension_de_l'entree":(3,3),"emission":[],"ticks":560,"repeat time":(76,104),"ajout":1042}

conduiteater={"droit":eater,"dx,dy":(0,0),"rotation":"droit","positionne":(8,6),"dimension_de_l'entree":(4,3),"emission":[]}

conduit64={"droit":R64,"dx,dy":(10,11),"rotation":"droite","positionne":(-12,-1),"dimension_de_l'entree":(4,3),"emission":[],"ticks":64}

conduit154={"droit":Fx77double,"dx,dy":(0,50),"rotation":"droit","positionne":(-18,-1),"dimension_de_l'entree":(4,3),"emission":[],"ticks":154}

conduit154degun={"droit":Fx77double_de_gun,"dx,dy":(0,50),"rotation":"droit","positionne":(-18,-1),"dimension_de_l'entree":(4,3),"emission":[("glider","a l'envers",154,(-25,5))],"ticks":154}

conduit116={"droit":F116,"dx,dy":(1,32),"rotation":"droit","positionne":(-14,8),"dimension_de_l'entree":(4,3),"emission":[],"ticks":116}

conduit282={"droit":F282,"dx,dy":(53,53),"rotation":"droit","positionne":(-12,-1),"dimension_de_l'entree":(4,3),"emission":[],"ticks":282}

conduit117={"droit":F117,"dx,dy":(-6,40),"rotation":"droit","positionne":(-15,-2),"dimension_de_l'entree":(4,3),"emission":[],"ticks":117}

conduit112={"droit":L112,"dx,dy":(-32,11),"rotation":"gauche","positionne":(-24,-2),"dimension_de_l'entree":(4,3),"emission":[],"ticks":112}

conduit190={"droit":R190,"dx,dy":(17,24),"rotation":"droite","positionne":(-18,1),"dimension_de_l'entree":(4,3),"emission":[],"ticks":190}


"""liste_de_conduit a pour seul but de rassembler tout ces conduit, pour des raisons de lisibilité"""

liste_de_conduit={64:conduit64,112:conduit112,116:conduit116,117:conduit117,154:conduit154,282:conduit282,155:conduit154degun,190:conduit190,"semisnark":conduitsemisnark,"semisnarkrenverse":conduitsemisnarkrenverse,"snark":conduitsnark,"snarkrenverse":conduitsnarkrenverse,"semisnarkactif":conduitsemisnarkactif,"semisnarkrenverseactif":conduitsemisnarkrenverseactif,"scorbieon":conduitscorbie_splitter_on,"scorbieoff":conduitscorbie_splitter_off,"scorbierenverseon":conduitscorbie_splitter_renverse_on,"scorbierenverseoff":conduitscorbie_splitter_renverse_off,"syringe":conduitsyringe,"h_to_g":conduith_to_g,"mega_bistable":conduitmega_bistable}

"""positionner prend en entrée une grille l, la position du haut gauche d'une figure ainsi que son orientation representée par un string"""


def creer_liste_pour_oscillateur(k1,k2,k3,A,B):
    liste=[154]
    k1-=1
    def f(l,k1,k2,k3):
        if k3>0:
            l+=[117]
            return k1,k2,k3-1
        elif k1>0:
            l+=[154]
            return k1-1,k2,k3
        else:
            l+=[116]
            return k1,k2-1,k3
    if A==0:
        forget=190
        B-=2
        remember=190
    elif A==1:
        forget=64
        A,B=0,B-1
        remember=190
    else:
        A-=2
        forget=64
        remember=64
    for k in range(A):
        liste+=[64]
        k1,k2,k3=f(liste,k1,k2,k3)
        liste+=[112]
        k1,k2,k3=f(liste,k1,k2,k3)
    for k in range(B):
        liste+=[190]
        k1,k2,k3=f(liste,k1,k2,k3)
        liste+=[112]
        k1,k2,k3=f(liste,k1,k2,k3)
    liste+=[forget]
    liste+=[117 for i in range(k3)]+[154 for i in range(k1)]+[116 for i in  range(k2)]
    liste+=[remember]
    return liste+liste


def place(l,fig,haut_gauche,r):
    if r=="droit":
        l1=[[fig[i][j] for j in range(len(fig[0]))] for i in range(len(fig))]
    if r=="droite":
        l1=tourner_droite(fig)
    if r=="gauche":
        l1=tourner_gauche(fig)
    if r=="a l'envers":
        l1=tourner_gauche(tourner_gauche(fig))
    a,b=haut_gauche
    for i in range(len(l1)):
        for j in range(len(l1[0])):
            l[i+a][j+b]=l1[i][j]

def positionner(l,haut_gauche,r,conduit):
    a,b=conduit["dimension_de_l'entree"]
    x,y=conduit["positionne"]
    l1=conduit["droit"]
    n,m=len(l1),len(l1[0])
    if r=="droit":
        x,y=haut_gauche[0]+x,haut_gauche[1]+y
        for i in range(n):
            for j in range(m):
                l[x+i][y+j]=l1[i][j]+l[x+i][y+j]*(1-l[i][j])
    elif r=="droite":
        x,y=y,a-x-n
        x,y=haut_gauche[0]+x,haut_gauche[1]+y
        for i in range(m):
            for j in range(n):
                l[x+i][y+j]=l1[n-1-j][i]+l[x+i][y+j]*(1-l[n-1-j][i])
    elif r=="gauche":
        x,y=b-y-m,x
        x,y=haut_gauche[0]+x,haut_gauche[1]+y
        for i in range(m):
            for j in range(n):
                l[x+i][y+j]=l1[j][m-1-i]+l[x+i][y+j]*(1-l[j][m-1-i])
    elif r=="a l'envers":
        x,y=a-x-n,b-y-m
        x,y=haut_gauche[0]+x,haut_gauche[1]+y
        for i in range(n):
            for j in range(m):
                l[x+i][y+j]=l1[n-1-i][m-1-j]+l[x+i][y+j]*(1-l[n-1-i][m-1-j])
    else:
        pass

def avancer(l,haut_gauche,r,conduit):
    positionner(l,haut_gauche,r,conduit)
    a,b=conduit["dimension_de_l'entree"]
    c,d=a,b
    if "dimension_de_la_sortie" in conduit:
        c,d=conduit["dimension_de_la_sortie"]
    dx,dy=conduit["dx,dy"]
    x,y=haut_gauche
    c,d=a-c,b-d
    if conduit["rotation"]=="droit":
        if r=="droite":
            dx,dy=dy,-dx+c
        elif r=="gauche":
            dx,dy=-dy+d,dx
        elif r=="a l'envers":
            dx,dy=-dx+c,-dy+d
        return (x+dx,y+dy),r
    elif conduit["rotation"]=="droite":
        if r=="droite":
            dx,dy=dy,a-b-dx
            return (x+dx,y+dy),"a l'envers"
        if r=="gauche":
            dx,dy=b-a-dy,dx
            return (x+dx,y+dy),"droit"
        if r=="a l'envers":
            dx,dy=a-b-dx,b-a-dy
            return (x+dx,y+dy),"gauche"
        return (x+dx,y+dy),"droite"
    elif conduit["rotation"]=="gauche":
        if r=="droite":
            dx,dy=dy,a-b-dx
            return (x+dx,y+dy),"droit"
        if r=="gauche":
            dx,dy=b-a-dy,dx
            return (x+dx,y+dy),"a l'envers"
        if r=="a l'envers":
            dx,dy=a-b-dx,b-a-dy
            return (x+dx,y+dy),"droite"
        return (x+dx,y+dy),"gauche"
    elif conduit["rotation"]=="a l'envers":
        pass


def deplace(haut_gauche,r,d):
    if r=="droit":
        return (haut_gauche[0]+d, haut_gauche[1]+d)
    elif r=="gauche":
        return (haut_gauche[0]-d, haut_gauche[1]+d)
    elif r=="droite":
        return (haut_gauche[0]+d, haut_gauche[1]-d)
    elif r=="a l'envers":
        return (haut_gauche[0]-d, haut_gauche[1]-d)



"""tourner_droite et tourner_gauche qui renvoient la rotation d'une grille en entrée sans la modifier
"""


def tourner_droite(l:list[list[int]])->list[list[int]]:
    n, m = len(l), len(l[0])
    t = [[0 for j in range(n)] for i in range(m)]
    for i in range(m):
        for j in range(n):
            t[i][j] = l[n-1-j][i]
    return t

def tourner_gauche(l:list[list[int]])->list[list[int]]:
    n, m = len(l), len(l[0])
    t = [[0 for j in range(n)] for i in range(m)]
    for i in range(n):
        for j in range(m):
            t[m-1-j][i] = l[i][j]
    return t

""" Les avancer qui prennent en entrée une grille, une orientation et un haut gauche,
qui modifient la grille en y ajoutant le circuit correspondant grace aux positionner
correspondant, et renvoient l'orientation r' et les coordonnées du haut gauche du herschel
après déplacement par le conduit correspondant d'un Herschel placé en hautgauche"""



"""Quelques fonctions auxilliaires un peu plus complexes.
limit_de_oscillateur_primaire va virtuellement faire parcourir un herschel a travers
le circuit que je souhaite créer comme oscillateur, afin d'évaluer jusqu'où va le Herschel
lorsqu'il est le plus bas et le plus a droite, afin de déduire la taille de la grille
que je dois créer pour contenir l'oscillateur Herschel de constantes (k1,k2,k3,A,B)"""

"""Une version simplifiée qui n'est pas en complexité linéaire selon k1+k2+k3+A+B"""


def limit_de_oscillateur(k1:int,k2:int,k3:int,A:int,B:int)->(int,int):
    b64,b190=(0,2) if A==0 else (1,1) if A==1 else (2,0)
    a64_rem,max_a64= max(0,A-b64),0
    a190_rem,max_a190= max(0,B-b190),0
    T=1+2*(a64_rem+a190_rem)
    K=k1+k2+k3
    C=min(T,K)
    consumed117=min(k3,C)
    consumed154=min(k1,max(0,C-consumed117))
    consumed116=min(k2,max(0,C-consumed117-consumed117))
    def f(s,e):
        return ((e+1)//2)-((s+1)//2)
    droit_117=f(0,consumed117)
    droit_154=f(consumed117,consumed154+consumed117)
    droit_116=f(consumed154+consumed117,C)
    droit_64,droit_190,droite_64,droite_190=(A-1,B,1,0) if b64==2 else (A,B-1,0,1)
    droite_154=k1-droit_154
    droite_116=k2-droit_116
    droite_117=k3-droit_117
    droite_112=A+B-2
    h0=120+droite_112*11+droite_190*24+droit_190*17+droit_64*10+droite_64*11+droit_117*-6+droite_117*40+droit_116*1+droite_116*32+droite_154*50
    h1=120+droite_112*33+droit_190*24+droit_64*11+droit_117*40+droite_117*6+droit_116*32+droite_116*-1+droit_154*50
    return h0,h1

"""etape simule une étape elementaire dans le jeu de la vie, en renvoyant l'état de la cellule
d'emplacement i,j dans la grille l aprés un tick"""


def oscillateur_de_constante(p,a,k1,k2,k3,A,B):
    if p>=61:
        taillemax=limit_de_oscillateur(k1,k2,k3,A,B)
        l=[]
        for i in range(taillemax[0]):
            l.append([0 for j in range(taillemax[1])])
        haut_gauche=(50,50)
        r = "droit"
        for x in range(2):
            if x==0 and a<=2 :
                for i in range(len(herschel)):
                    for j in range(len(herschel[0])):
                        l[haut_gauche[0]+i][haut_gauche[1]+j]=herschel[i][j]
            if x==1 and a==2 :
                h=tourner_droite(tourner_droite(herschel))
                for i in range(len(h)):
                    for j in range(len(h[0])):
                        l[haut_gauche[0]+i][haut_gauche[1]+j]=h[i][j]
            a154,a116,a117,a64,a190=k1,k2,k3,A,B
            haut_gauche,r=avancer(l,haut_gauche,r,conduit154)
            a154-=1
            if a64==0:
                b64=0
                b190=2
            if a64==1:
                b64=1
                b190=1
            if a64>1:
                b64=2
                b190=0
            a64-=b64
            a190-=b190
            for k in range(a64):
                haut_gauche,r=avancer(l,haut_gauche,r,conduit64)
                haut_gauche,a154,a116,a117=un_des_F(l,haut_gauche,r,a154,a116,a117)
                haut_gauche,r=avancer(l,haut_gauche,r,conduit112)
                haut_gauche,a154,a116,a117=un_des_F(l,haut_gauche,r,a154,a116,a117)
            for k in range(a190):
                haut_gauche,r=avancer(l,haut_gauche,r,conduit190)
                haut_gauche,a154,a116,a117=un_des_F(l,haut_gauche,r,a154,a116,a117)
                haut_gauche,r=avancer(l,haut_gauche,r,conduit112)
                haut_gauche,a154,a116,a117=un_des_F(l,haut_gauche,r,a154,a116,a117)
            if b64>=1:
                haut_gauche,r=avancer(l,haut_gauche,r,conduit64)
            else:
                haut_gauche,r=avancer(l,haut_gauche,r,conduit190)
            while a154+a116+a117>=1:
                haut_gauche,a154,a116,a117=un_des_F(l,haut_gauche,r,a154,a116,a117)
            if b64==2:
                haut_gauche,r=avancer(l,haut_gauche,r,conduit64)
            else:
                haut_gauche,r=avancer(l,haut_gauche,r,conduit190)
        if a>2:
            remplir_le_chemin(l,p,a,(50,50))
        return l
    else:
        pass

def oscillateur(p):
    a,k1,k2,k3,A,B=plus_petits(p)
    return oscillateur_de_constante(p,a,k1,k2,k3,A,B)

def canon_naif(p):
    if p>=69:
        l=oscillateur(p)
        for i in range(32,40):
            for j in range(63,71):
                l[i][j]=0
        return l

def canon_booste(p,ind=False):
    m=0
    while p%(2**(m+2))==0 and p//(2**(m+1))>1395:
        m+=1
    l=canon_naif(p//2**m)
    l=[[0 for i in range(len(l[0]))] for j in range(17*m+50)]+l
    haut_gauche,r=(75+17*m,55),"a l'envers"
    for i in range(m):
        if r=="a l'envers":
            haut_gauche,r=avancer(l,haut_gauche,r,conduitsemisnarkrenverse)
        elif r=="gauche":
            haut_gauche,r=avancer(l,haut_gauche,r,conduitsemisnark)
    if ind:
        return l,haut_gauche,r
    return l

import math

def oscillateur_booste_2_0(p):
    l,haut_gauche,r=canon_booste_2_0(p,True)
    positionner(l,haut_gauche,r,conduiteater)
    return l



def ecriture_binaire(x,a=-1):
    if a==-1:
        a=math.log2(x)
    n=int(a)
    l=[0 for i in range(n+1)]
    for i in range(n+1):
        j=n-i
        if x>=(2**j):
            l[i]=1
            x=x-2**j
    return l

def place_etape_de_bit(l,haut_gauche,r,x,d=0):
    haut_gauche=deplace(haut_gauche,r,17)
    haut_gauche,r=avancer(l,haut_gauche,r,conduitsnarkrenverse)
    haut_gauche=deplace(haut_gauche,r,d+10)
    if x==0:
        haut_gauche,r=avancer(l,haut_gauche,r,conduitsemisnark)
    if x==1:
        haut_gauche,r=avancer(l,haut_gauche,r,conduitsemisnarkactif)
    haut_gauche=deplace(haut_gauche,r,-6)
    return haut_gauche,r

def fin_de_bit(l,haut_gauche,r,liste,d=0):
    haut_gauche=deplace(haut_gauche,r,8)
    haut_gauche,r=avancer(l,haut_gauche,r,conduitsnark)
    haut_gauche=deplace(haut_gauche,r,2+d)
    for i in liste:
        if i==0:
            haut_gauche,r=avancer(l,haut_gauche,r,conduitscorbie_splitter_renverse_off)
        if i==1:
            haut_gauche,r=avancer(l,haut_gauche,r,conduitscorbie_splitter_renverse_on)
    return haut_gauche,r

def period_multiplier(l,haut_gauche,r,n,d=0,Ticks=False):
    haut_gauche=deplace(haut_gauche,r,15)
    a=math.log2(n)
    ticks=60
    if n==1:
        liste=[1]
    elif a%1==0:
        liste=[0 for i in range(int(a))]
    else:
        a=int(a)-1
        b=int(2**(a+2)-n)
        liste=[0]+ecriture_binaire(b,a)
    for i in range(len(liste)-1):
        i=len(liste)-i-1
        haut_gauche,r=place_etape_de_bit(l,haut_gauche,r,liste[i])
        ticks+=266+350
    haut_gauche,r=place_etape_de_bit(l,haut_gauche,r,liste[0],d)
    ticks+=266+350+4*d
    haut_gauche=deplace(haut_gauche,r,1)
    ticks+=4
    haut_gauche,r=fin_de_bit(l,haut_gauche,r,liste,d)
    ticks+=8*4+86+4*(d+2)
    if Ticks:
        return haut_gauche,r,ticks
    else:
        return haut_gauche,r

def period_multiplier_bis(l,haut_gauche,r,n,d=0,Ticks=False):
    haut_gauche=deplace(haut_gauche,r,15)
    a=math.log2(n)
    ticks=60
    if n==1:
        liste=[1]
    elif a%1==0:
        liste=[0 for i in range(int(a))]
    else:
        a=int(a)-1
        b=int(2**(a+2)-n)
        liste=[0]+ecriture_binaire(b,a)
    for i in range(len(liste)-1):
        i=len(liste)-i-1
        haut_gauche,r=place_etape_de_bit(l,haut_gauche,r,1)
        ticks+=266+350
    haut_gauche,r=place_etape_de_bit(l,haut_gauche,r,1,d)
    ticks+=266+350+4*d
    haut_gauche=deplace(haut_gauche,r,1)
    ticks+=4
    haut_gauche,r=fin_de_bit(l,haut_gauche,r,liste,d)
    ticks+=8*4+86+4*(d+2)
    if Ticks:
        return haut_gauche,r,ticks
    else:
        return haut_gauche,r

def check_si_z_existe(p,d,liste):
    x=len(liste)
    for i in range(x):
        if liste[i]==0:
            y=616*(x-i)+8*d+72
        if liste[i]==1:
            y=644*(x-i)+8*d+72
        if 2**i==1:
            a=2**i
        else:
            a=2**i-1
        z=y%(p*a)
        if z<=20 or z>=p*a-100:
            return True
        if z==y:
            return False
    return False


def cherche_binaire(p,liste,lag=300):
    for d in range(lag):
        if not check_si_z_existe(p,d,liste):
            return d
    return -20

def cherche(p,a):
    x=math.log2(a)
    if x%1==0:
        liste=[0 for i in range(int(x))]
    else:
        liste=[0]+ecriture_binaire(2**(int(x)+1)-a)
    return cherche_binaire(p,liste,1000)

def canon_booste_max(p,d=-1):
    if p<69:
        print("oops, la periode doit etre supperieure a 69!")
        return glider
    if p<245:
        return canon_naif(p)
    a=divise(p)
    if a==1:
        return canon_naif(p)
    x=math.log2(a)
    if x%1==0:
        return canon_booste_2_0(p)
    if d==-1:
        d=cherche((p//a),a)
    l=canon_naif(p//a)
    l=[[0 for i in range(len(l[0]))] for j in range(50+d+59*(int(math.log2(a))+1))]+l
    n=d+100-len(l[0])
    haut_gauche,r=(25+50+d+59*(int(math.log2(a))+1),55+75),"a l'envers"
    if n<0:
        n=0
    l=[[0 for i in range(75)]+l1+[0 for i in range(n)] for l1 in l]
    haut_gauche,r=period_multiplier(l,haut_gauche,r,a,d)
    return l

def oscillateur_booste_max(p,d=-1):
    if p<61:
        print("oops, la periode doit etre superieure a 61")
        return glider
    if p>=61 and p<69:
        return oscillateur(p)
    if p<245:
        return oscillateur(p)
    a=divise(p)
    if a==1:
        return oscillateur(p)
    x=math.log2(a)
    if x%1==0:
        return oscillateur_booste_2_0(p)
    if d==-1:
        d=cherche((p//a),a)
    l=canon_naif(p//a)
    l=[[0 for i in range(len(l[0]))] for j in range(50+d+59*(int(math.log2(a))+1))]+l
    n=d+100-len(l[0])
    haut_gauche,r=(25+50+d+59*(int(math.log2(a))+1),55+75),"a l'envers"
    if n<0:
        n=0
    l=[[0 for i in range(75)]+l1+[0 for i in range(n)] for l1 in l]
    haut_gauche,r=period_multiplier(l,haut_gauche,r,a,d)
    haut_gauche=deplace(haut_gauche,r,15)
    positionner(l,haut_gauche,r,conduiteater)
    return l

def ligne_to_rle(l):
    t=""
    c=l[0]
    n=1
    for i in range(1,len(l)):
        if l[i]==c:
            n+=1
        if l[i]!=c :
            if c>0.5:
                if n>1:
                    t=t+str(n)+"o"
                else:
                    t=t+"o"
            if c<0.5:
                if n>1:
                    t=t+str(n)+"b"
                else:
                    t=t+"b"
            n=1
            c=l[i]
    if l[len(l)-1]==1:
        t=t+str(n)+"o"
    else:
        t=t+str(n)+"b"
    return t

def matrix_to_rle(l):
    t=""
    n,m=len(l), len(l[0])
    t="x="+str(m)+", y="+str(n)+ ", rule=B3/S23 "+"\n"
    for i in range(n-1):
        l1=l[i]
        t1=ligne_to_rle(l1)
        t=t+t1+"$"
    l1=l[n-1]
    t1=ligne_to_rle(l1)
    t=t+t1+"!"
    return t

def area_naif(p):
    a,k1,k2,k3,A,B=plus_petits(p)
    x,y=limit_de_oscillateur(k1,k2,k3,A,B)
    return x,y

def area_max(p,a=-1,Id=False,k1=-1,k2=-1,k3=-1,A=-1,B=-1):
    if p<69:
        print("oops, la periode doit etre supperieure a 69!")
        return 0
    if p<245:
        return area_naif(p)
    if a==-1:
        a=divise(p)
        i=p//a
    else:
        i=p
    d=cherche(i,a)
    if k1==-1:
        nimporte,k1,k2,k3,A,B=plus_petits(i)
    x,y=limit_de_oscillateur(k1,k2,k3,A,B)
    x=50+d+59*(int(math.log2(a))+1)+x
    n=d+100-y
    if n<0:
        n=0
    y=75+y+n
    if Id:
        return x,y,d
    return x,y

dico={}
for sum in range(0,96):
    for k2 in range(0,min(sum+1,11)):
        for k1 in range(0,min(sum-k2+1,36)):
            k3=sum-k1-k2
            for A in range(3):
                for B in range(3):
                    if A+B>=2 and k1+k2+k3>=2*(A+B+2):
                        p_apparent=2*(973+k1*154 + k2*116 + k3*117 + A*64 + B*190 + (A+B-2)*112)
                        if p_apparent not in dico:
                            dico[p_apparent]=(k1,k2,k3,A,B)
les_cles=list(dico.keys())

for i in range(len(les_cles)):
    i=len(les_cles)-i-1
    p_app=les_cles[i]
    x=0
    while x<i:
        if p_app%les_cles[x]==0:
            del dico[p_app]
            x=i+1
        x+=1
les_cles=list(dico.keys())
les_cles.sort()
def trouver_sans_sat(p):
    for ajout in range(51):
        if p%2==0:
            acc=p-1042-8*ajout
        else:
            acc=p-1367-8*ajout
        if acc>0:
            for p_app in les_cles:
                if acc%p_app==0:
                    k1,k2,k3,A,B=dico[p_app]
                    print(p_app)
                    return k1,k2,k3,A,B,acc//p_app,ajout
    return False

def canon_final(p):
    if p>=2000:
        x=trouver_sans_sat(p)
        if x==False:
            if p>=10**5:
                print("desole, la periode est trop grande pour etre manipulée par ortools, un module utilisé pour trouver des solutions aux equations a plusieurs variables")
            else:
                return canon_booste_max(p)
        a=1
        k1,k2,k3,A,B,multiplier,ajout=x
        if p%2==0:
            periode_apparente=(p-1042-8*ajout)//multiplier
        else:
            periode_apparente=(p-1367-8*ajout)//multiplier
        x,y,d=area_max(periode_apparente,multiplier,True,k1,k2,k3,A,B)
        x,y=x+200,y+150
        l=[[0 for i in range(y)] for j in range(x)]
        haut_gauche=(210+d+59*(int(math.log2(multiplier))+1),60+max(0,d-50))
        x2,y2=haut_gauche
        haut_gauche_ressortissant=(x2+29,y2+66)
        haut_gauche_apparent=(422+d+59*(int(math.log2(multiplier))+1),294+max(0,d-50))
        r = "droit"
        liste=creer_liste_pour_oscillateur(k1,k2,k3,A,B)
        n=len(liste)
        for x in range(2):
            if x==0 and a<=2 :
                for i in range(len(herschel)):
                    for j in range(len(herschel[0])):
                        l[haut_gauche[0]+i][haut_gauche[1]+j]=herschel[i][j]
            if x==1 and a==2 :
                h=tourner_droite(tourner_droite(herschel))
                for i in range(len(h)):
                    for j in range(len(h[0])):
                        l[haut_gauche[0]+i][haut_gauche[1]+j]=h[i][j]
            haut_gauche,r=avancer(l,haut_gauche,r,conduith_to_g)
            if p%2==0:
                haut_gauche,r=avancer(l,haut_gauche,r,conduitmega_bistable)
            else:
                haut_gauche,r=avancer(l,haut_gauche,r,conduitmega_bistabledecale)
            haut_gauche=deplace(haut_gauche,r,50)
            haut_gauche,r=avancer(l,haut_gauche,r,conduitsyringe)
            for i in range(n//2):
                j=liste[x*n//2+i]
                haut_gauche,r=avancer(l,haut_gauche,r,liste_de_conduit[j])
        for i in range(404+d+59*(int(math.log2(multiplier))+1),412+d+59*(int(math.log2(multiplier))+1)):
            for j in range(307+max(0,d-50),315+max(0,d-50)):
                l[i][j]=0
        x1,y1=haut_gauche_apparent
        haut_gauche_glider,r=(x1-25,y1+5),"a l'envers"
        haut_gauche_glider=deplace(haut_gauche_glider,r,10)
        haut_gauche_glider,r=avancer(l,haut_gauche_glider,r,conduitsnarkrenverse)
        haut_gauche_glider=deplace(haut_gauche_glider,r,78)
        haut_gauche_glider,r=avancer(l,haut_gauche_glider,r,conduitsnark)
        haut_gauche_glider=deplace(haut_gauche_glider,r,119)
        ticks=1180+127+560+4*50
        haut_gauche_glider,r,ticks_en_plus=period_multiplier(l,haut_gauche_glider,r,multiplier,d,True)
        print(ticks,ticks_en_plus,periode_apparente,d)
        ticks+=ticks_en_plus
        ticks+=400
        le_suivant=ticks%periode_apparente
        print(le_suivant)
        if le_suivant<200 or le_suivant>periode_apparente-80 :
            if ajout<30:
                haut_gauche_glider=deplace(haut_gauche_glider,r,25)
            else:
                haut_gauche_glider=deplace(haut_gauche_glider,r,45)
            haut_gauche_glider,r=avancer(l,haut_gauche_glider,r,conduitsnarkrenverse)
            haut_gauche_glider=deplace(haut_gauche_glider,r,5)
            haut_gauche_glider,r=avancer(l,haut_gauche_glider,r,conduitsnark)
            haut_gauche_glider,r=avancer(l,haut_gauche_glider,r,conduitsnark)
            haut_gauche_glider,r=avancer(l,haut_gauche_glider,r,conduitsnarkrenverse)
        haut_gauche,r=haut_gauche_ressortissant,"gauche"
        haut_gauche=deplace(haut_gauche,r,ajout)
        if p%2==1:
            haut_gauche,r=avancer(l,haut_gauche,r,conduitsnarkrenverse)
            haut_gauche=deplace(haut_gauche,r,29)
            haut_gauche,r=avancer(l,haut_gauche,r,conduitsyringe)
            haut_gauche,r=avancer(l,haut_gauche,r,conduith_to_g)
            haut_gauche,r=avancer(l,haut_gauche,r,conduitsnark)
            haut_gauche,r=avancer(l,haut_gauche,r,conduitsnarkrenverse)
            haut_gauche,r=avancer(l,haut_gauche,r,conduitsnarkrenverse)
            haut_gauche=deplace(haut_gauche,r,16)
            haut_gauche,r=avancer(l,haut_gauche,r,conduitsnark)
            haut_gauche=deplace(haut_gauche,r,-5)
            haut_gauche,r=avancer(l,haut_gauche,r,conduitsnarkrenverse)
        if p%2==0:
            haut_gauche,r=avancer(l,haut_gauche,r,conduitsnarkrenverse)
            haut_gauche=deplace(haut_gauche,r,63)
            haut_gauche,r=avancer(l,haut_gauche,r,conduitsnarkrenverse)
        return l
    else:
        return canon_booste_max(p)

def oscillateur_final(p):
    if p>=2000:
        x=trouver_sans_sat(p)
        if x==False:
            if p>=10**5:
                print("desole, la periode est trop grande pour etre manipulée par ortools, un module utilisé pour trouver des solutions aux equations a plusieurs variables")
                return []
            else:
                return oscillateur(p)
        a=1
        k1,k2,k3,A,B,multiplier,ajout=x
        if p%2==0:
            periode_apparente=(p-1042-8*ajout)//multiplier
        else:
            periode_apparente=(p-1367-8*ajout)//multiplier
        x,y,d=area_max(periode_apparente,multiplier,True,k1,k2,k3,A,B)
        x,y=x+400,y+300
        l=[[0 for i in range(y)] for j in range(x)]
        haut_gauche=(210+d+59*(int(math.log2(multiplier))+1),60+max(0,d-50))
        x2,y2=haut_gauche
        haut_gauche_ressortissant=(x2+29,y2+66)
        haut_gauche_apparent=(422+d+59*(int(math.log2(multiplier))+1),294+max(0,d-50))
        r = "droit"
        liste=creer_liste_pour_oscillateur(k1,k2,k3,A,B)
        n=len(liste)
        for x in range(2):
            if x==0 and a<=2 :
                for i in range(len(herschel)):
                    for j in range(len(herschel[0])):
                        l[haut_gauche[0]+i][haut_gauche[1]+j]=herschel[i][j]
            if x==1 and a==2 :
                h=tourner_droite(tourner_droite(herschel))
                for i in range(len(h)):
                    for j in range(len(h[0])):
                        l[haut_gauche[0]+i][haut_gauche[1]+j]=h[i][j]
            haut_gauche,r=avancer(l,haut_gauche,r,conduith_to_g)
            if p%2==0:
                haut_gauche,r=avancer(l,haut_gauche,r,conduitmega_bistable_sans_sortie)
            else:
                haut_gauche,r=avancer(l,haut_gauche,r,conduitmega_bistabledecale_sans_sortie)
            haut_gauche=deplace(haut_gauche,r,50)
            haut_gauche,r=avancer(l,haut_gauche,r,conduitsyringe)
            for i in range(n//2):
                j=liste[x*n//2+i]
                haut_gauche,r=avancer(l,haut_gauche,r,liste_de_conduit[j])
        for i in range(404+d+59*(int(math.log2(multiplier))+1),412+d+59*(int(math.log2(multiplier))+1)):
            for j in range(307+max(0,d-50),315+max(0,d-50)):
                l[i][j]=0
        x1,y1=haut_gauche_apparent
        haut_gauche_glider,r=(x1-25,y1+5),"a l'envers"
        haut_gauche_glider=deplace(haut_gauche_glider,r,10)
        haut_gauche_glider,r=avancer(l,haut_gauche_glider,r,conduitsnarkrenverse)
        haut_gauche_glider=deplace(haut_gauche_glider,r,78)
        haut_gauche_glider,r=avancer(l,haut_gauche_glider,r,conduitsnark)
        haut_gauche_glider=deplace(haut_gauche_glider,r,119)
        ticks=1180+127+560+4*50
        haut_gauche_glider,r,ticks_en_plus=period_multiplier(l,haut_gauche_glider,r,multiplier,d,True)
        ticks+=ticks_en_plus
        ticks+=400
        le_suivant=ticks%periode_apparente
        if le_suivant<200 or le_suivant>periode_apparente-80 :
            if ajout<30:
                haut_gauche_glider=deplace(haut_gauche_glider,r,25)
            else:
                haut_gauche_glider=deplace(haut_gauche_glider,r,45)
            haut_gauche_glider,r=avancer(l,haut_gauche_glider,r,conduitsnarkrenverse)
            haut_gauche_glider=deplace(haut_gauche_glider,r,5)
            haut_gauche_glider,r=avancer(l,haut_gauche_glider,r,conduitsnark)
            haut_gauche_glider,r=avancer(l,haut_gauche_glider,r,conduitsnark)
            haut_gauche_glider,r=avancer(l,haut_gauche_glider,r,conduitsnarkrenverse)
        haut_gauche,r=haut_gauche_ressortissant,"gauche"
        haut_gauche=deplace(haut_gauche,r,ajout)
        if p%2==1:
            haut_gauche,r=avancer(l,haut_gauche,r,conduitsnarkrenverse)
            haut_gauche=deplace(haut_gauche,r,29)
            haut_gauche,r=avancer(l,haut_gauche,r,conduitsyringe)
            haut_gauche,r=avancer(l,haut_gauche,r,conduith_to_g)
            haut_gauche,r=avancer(l,haut_gauche,r,conduitsnark)
            haut_gauche,r=avancer(l,haut_gauche,r,conduitsnarkrenverse)
            haut_gauche,r=avancer(l,haut_gauche,r,conduitsnarkrenverse)
            haut_gauche=deplace(haut_gauche,r,16)
            haut_gauche,r=avancer(l,haut_gauche,r,conduitsnark)
            haut_gauche=deplace(haut_gauche,r,-5)
            haut_gauche,r=avancer(l,haut_gauche,r,conduitsnarkrenverse)
        if p%2==0:
            haut_gauche,r=avancer(l,haut_gauche,r,conduitsnarkrenverse)
            haut_gauche=deplace(haut_gauche,r,63)
            haut_gauche,r=avancer(l,haut_gauche,r,conduitsnarkrenverse)
        return l
    else:
        return oscillateur(p)

def oscillateur_final_bis(p):
    if p>=2000:
        x=trouver_sans_sat(p)
        if x==False:
            if p>=10**5:
                print("desole, la periode est trop grande pour etre manipulée par ortools, un module utilisé pour trouver des solutions aux equations a plusieurs variables")
                return []
            else:
                return oscillateur(p)
        a=1
        k1,k2,k3,A,B,multiplier,ajout=x
        if p%2==0:
            periode_apparente=(p-1042-8*ajout)//multiplier
        else:
            periode_apparente=(p-1367-8*ajout)//multiplier
        x,y,d=area_max(periode_apparente,multiplier,True,k1,k2,k3,A,B)
        x,y=x+400,y+300
        l=[[0 for i in range(y)] for j in range(x)]
        haut_gauche=(210+d+59*(int(math.log2(multiplier))+1),60+max(0,d-50))
        x2,y2=haut_gauche
        haut_gauche_ressortissant=(x2+29,y2+66)
        haut_gauche_apparent=(422+d+59*(int(math.log2(multiplier))+1),294+max(0,d-50))
        r = "droit"
        liste=creer_liste_pour_oscillateur(k1,k2,k3,A,B)
        n=len(liste)
        for x in range(2):
            if x==0 and a<=2 :
                for i in range(len(herschel)):
                    for j in range(len(herschel[0])):
                        l[haut_gauche[0]+i][haut_gauche[1]+j]=herschel[i][j]
            if x==1 and a==2 :
                h=tourner_droite(tourner_droite(herschel))
                for i in range(len(h)):
                    for j in range(len(h[0])):
                        l[haut_gauche[0]+i][haut_gauche[1]+j]=h[i][j]
            haut_gauche,r=avancer(l,haut_gauche,r,conduith_to_g)
            if p%2==0:
                haut_gauche,r=avancer(l,haut_gauche,r,conduitmega_bistable_sans_sortie)
            else:
                haut_gauche,r=avancer(l,haut_gauche,r,conduitmega_bistabledecale_sans_sortie)
            haut_gauche=deplace(haut_gauche,r,50)
            haut_gauche,r=avancer(l,haut_gauche,r,conduitsyringe)
            for i in range(n//2):
                j=liste[x*n//2+i]
                haut_gauche,r=avancer(l,haut_gauche,r,liste_de_conduit[j])
        for i in range(404+d+59*(int(math.log2(multiplier))+1),412+d+59*(int(math.log2(multiplier))+1)):
            for j in range(307+max(0,d-50),315+max(0,d-50)):
                l[i][j]=0
        x1,y1=haut_gauche_apparent
        haut_gauche_glider,r=(x1-25,y1+5),"a l'envers"
        haut_gauche_glider=deplace(haut_gauche_glider,r,10)
        haut_gauche_glider,r=avancer(l,haut_gauche_glider,r,conduitsnarkrenverse)
        haut_gauche_glider=deplace(haut_gauche_glider,r,78)
        haut_gauche_glider,r=avancer(l,haut_gauche_glider,r,conduitsnark)
        haut_gauche_glider=deplace(haut_gauche_glider,r,119)
        ticks=1180+127+560+4*50
        haut_gauche_glider,r,ticks_en_plus=period_multiplier_bis(l,haut_gauche_glider,r,multiplier,d,True)
        ticks+=ticks_en_plus
        ticks+=400
        le_suivant=ticks%periode_apparente
        if le_suivant<200 or le_suivant>periode_apparente-80 :
            if ajout<30:
                haut_gauche_glider=deplace(haut_gauche_glider,r,25)
            else:
                haut_gauche_glider=deplace(haut_gauche_glider,r,45)
            haut_gauche_glider,r=avancer(l,haut_gauche_glider,r,conduitsnarkrenverse)
            haut_gauche_glider=deplace(haut_gauche_glider,r,5)
            haut_gauche_glider,r=avancer(l,haut_gauche_glider,r,conduitsnark)
            haut_gauche_glider,r=avancer(l,haut_gauche_glider,r,conduitsnark)
            haut_gauche_glider,r=avancer(l,haut_gauche_glider,r,conduitsnarkrenverse)
        haut_gauche,r=haut_gauche_ressortissant,"gauche"
        haut_gauche=deplace(haut_gauche,r,ajout)
        if p%2==1:
            haut_gauche,r=avancer(l,haut_gauche,r,conduitsnarkrenverse)
            haut_gauche=deplace(haut_gauche,r,29)
            haut_gauche,r=avancer(l,haut_gauche,r,conduitsyringe)
            haut_gauche,r=avancer(l,haut_gauche,r,conduith_to_g)
            haut_gauche,r=avancer(l,haut_gauche,r,conduitsnark)
            haut_gauche,r=avancer(l,haut_gauche,r,conduitsnarkrenverse)
            haut_gauche,r=avancer(l,haut_gauche,r,conduitsnarkrenverse)
            haut_gauche=deplace(haut_gauche,r,16)
            haut_gauche,r=avancer(l,haut_gauche,r,conduitsnark)
            haut_gauche=deplace(haut_gauche,r,-5)
            haut_gauche,r=avancer(l,haut_gauche,r,conduitsnarkrenverse)
        if p%2==0:
            haut_gauche,r=avancer(l,haut_gauche,r,conduitsnarkrenverse)
            haut_gauche=deplace(haut_gauche,r,63)
            haut_gauche,r=avancer(l,haut_gauche,r,conduitsnarkrenverse)
        return l
    else:
        return oscillateur(p)

def area_final(p,x):
    if p<2000:
        return 1,1
    if x==False:
        if p>=10**5:
            print("desole, la periode est trop grande pour etre manipulée par ortools, un module utilisé pour trouver des solutions aux equations a plusieurs variables")
            return 1,1
        else:
            return 1,1
    k1,k2,k3,A,B,multiplier,ajout=x
    if p%2==0:
        periode_apparente=(p-1042-8*ajout)//multiplier
    else:
        periode_apparente=(p-1367-8*ajout)//multiplier
    x,y,d=area_max(periode_apparente,multiplier,True,k1,k2,k3,A,B)
    x,y=x+400,y+300
    return x,y,d

def area_max_peu_pres(p,a=-1,k1=-1,k2=-1,k3=-1,A=-1,B=-1):
    if p<69:
        print("oops, la periode doit etre supperieure a 69!")
        return 0
    if p<245:
        return area_naif(p)
    if a==-1:
        a=divise(p)
        i=p//a
    else:
        i=p
    if k1==-1:
        nimporte,k1,k2,k3,A,B=plus_petits(i)
    x,y=limit_de_oscillateur(k1,k2,k3,A,B)
    x=50+50+59*(int(math.log2(a))+1)+x
    n=50+100-y
    if n<0:
        n=0
    y=75+y+n
    return x,y

def area_final_peu_pres(p,x):
    if p<2000:
        return 1,1
    if x==False:
        if p>=10**5:
            print("desole, la periode est trop grande pour etre manipulée par ortools, un module utilisé pour trouver des solutions aux equations a plusieurs variables")
            return 1,1
        else:
            return 1,1
    k1,k2,k3,A,B,multiplier,ajout=x
    if p%2==0:
        periode_apparente=(p-1042-8*ajout)//multiplier
    else:
        periode_apparente=(p-1367-8*ajout)//multiplier
    x,y=area_max_peu_pres(periode_apparente,multiplier,k1,k2,k3,A,B)
    x,y=x+400,y+300
    return x,y

def oscillateur_final_test(p,x,l,d):
    if p>=2000 and x!=False:
        a=1
        k1,k2,k3,A,B,multiplier,ajout=x
        if p%2==0:
            periode_apparente=(p-1042-8*ajout)//multiplier
        else:
            periode_apparente=(p-1367-8*ajout)//multiplier
        haut_gauche=(210+d+59*(int(math.log2(multiplier))+1),60+max(0,d-50))
        x2,y2=haut_gauche
        haut_gauche_ressortissant=(x2+29,y2+66)
        haut_gauche_apparent=(422+d+59*(int(math.log2(multiplier))+1),294+max(0,d-50))
        r = "droit"
        liste=creer_liste_pour_oscillateur(k1,k2,k3,A,B)
        n=len(liste)
        for x in range(2):
            if x==0 and a<=2 :
                for i in range(len(herschel)):
                    for j in range(len(herschel[0])):
                        l[haut_gauche[0]+i][haut_gauche[1]+j]=herschel[i][j]
            if x==1 and a==2 :
                h=tourner_droite(tourner_droite(herschel))
                for i in range(len(h)):
                    for j in range(len(h[0])):
                        l[haut_gauche[0]+i][haut_gauche[1]+j]=h[i][j]
            haut_gauche,r=avancer(l,haut_gauche,r,conduith_to_g)
            if p%2==0:
                haut_gauche,r=avancer(l,haut_gauche,r,conduitmega_bistable_sans_sortie)
            else:
                haut_gauche,r=avancer(l,haut_gauche,r,conduitmega_bistabledecale_sans_sortie)
            haut_gauche=deplace(haut_gauche,r,50)
            haut_gauche,r=avancer(l,haut_gauche,r,conduitsyringe)
            for i in range(n//2):
                j=liste[x*n//2+i]
                haut_gauche,r=avancer(l,haut_gauche,r,liste_de_conduit[j])
        for i in range(404+d+59*(int(math.log2(multiplier))+1),412+d+59*(int(math.log2(multiplier))+1)):
            for j in range(307+max(0,d-50),315+max(0,d-50)):
                l[i][j]=0
        x1,y1=haut_gauche_apparent
        haut_gauche_glider,r=(x1-25,y1+5),"a l'envers"
        haut_gauche_glider=deplace(haut_gauche_glider,r,10)
        haut_gauche_glider,r=avancer(l,haut_gauche_glider,r,conduitsnarkrenverse)
        haut_gauche_glider=deplace(haut_gauche_glider,r,78)
        haut_gauche_glider,r=avancer(l,haut_gauche_glider,r,conduitsnark)
        haut_gauche_glider=deplace(haut_gauche_glider,r,119)
        ticks=1180+127+560+4*50
        haut_gauche_glider,r,ticks_en_plus=period_multiplier(l,haut_gauche_glider,r,multiplier,d,True)
        ticks+=ticks_en_plus
        ticks+=400
        le_suivant=ticks%periode_apparente
        if le_suivant<200 or le_suivant>periode_apparente-80 :
            if ajout<30:
                haut_gauche_glider=deplace(haut_gauche_glider,r,25)
            else:
                haut_gauche_glider=deplace(haut_gauche_glider,r,45)
            haut_gauche_glider,r=avancer(l,haut_gauche_glider,r,conduitsnarkrenverse)
            haut_gauche_glider=deplace(haut_gauche_glider,r,5)
            haut_gauche_glider,r=avancer(l,haut_gauche_glider,r,conduitsnark)
            haut_gauche_glider,r=avancer(l,haut_gauche_glider,r,conduitsnark)
            haut_gauche_glider,r=avancer(l,haut_gauche_glider,r,conduitsnarkrenverse)
        haut_gauche,r=haut_gauche_ressortissant,"gauche"
        haut_gauche=deplace(haut_gauche,r,ajout)
        if p%2==1:
            haut_gauche,r=avancer(l,haut_gauche,r,conduitsnarkrenverse)
            haut_gauche=deplace(haut_gauche,r,29)
            haut_gauche,r=avancer(l,haut_gauche,r,conduitsyringe)
            haut_gauche,r=avancer(l,haut_gauche,r,conduith_to_g)
            haut_gauche,r=avancer(l,haut_gauche,r,conduitsnark)
            haut_gauche,r=avancer(l,haut_gauche,r,conduitsnarkrenverse)
            haut_gauche,r=avancer(l,haut_gauche,r,conduitsnarkrenverse)
            haut_gauche=deplace(haut_gauche,r,16)
            haut_gauche,r=avancer(l,haut_gauche,r,conduitsnark)
            haut_gauche=deplace(haut_gauche,r,-5)
            haut_gauche,r=avancer(l,haut_gauche,r,conduitsnarkrenverse)
        if p%2==0:
            haut_gauche,r=avancer(l,haut_gauche,r,conduitsnarkrenverse)
            haut_gauche=deplace(haut_gauche,r,63)
            haut_gauche,r=avancer(l,haut_gauche,r,conduitsnarkrenverse)
        return l
    else:
        return None
#
# import time
# f=open("test_final_parallel","w")
# f.write("[(")
# for x in range(140,200):
#     debut=int(math.exp(x/10))
#     for p in range(debut,debut+10000):
#         t=time.time_ns()
#         x=trouver_sans_sat(p)
#         if x!=False:
#             t1=time.time_ns()
#             x1,y1,d=area_final(p,x)
#             t2=time.time_ns()
#             l=[[0 for i in range(y1)] for j in range(x1)]
#             t3=time.time_ns()
#             oscillateur_final_test(p,x,l,d)
#             t4=time.time_ns()
#             f.write(""+str(p)+","+str(t1-t)+","+str(t2-t1)+","+str(t3-t2)+","+str(t4-t3)+"),(")
#             f.flush()
# f.close()