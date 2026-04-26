import math
"""On accéde aux listes encodant les figures que je souhaite traiter.
Ces dernieres sont:
    Des conduits de Herschel, representés par une lettre indiquant la rotation qu'ils effectuent, R pour Right, L pour Left et F pour Forward, et le temps qu'ils prennent a modifier le Herschel.
    Snark et Semi-Snark, qui sont des reflécteurs de planeurs, Snark etant un reflecteur typique et Semi-Snark un multiplicateur de période, c'est à dire qu'il agit comme un Snark à ceci prés qu'il consome un planeur sur 2.
    Le syringe, qui permet de transformer un glider en Herschel, un H_to_G qui transforme un herschel en glider, une figure sur mesure appelée Mega_bistable ainsi que scorbie_splitter sont utilisées.
    Le eater, une figure qui absorbe et détruit un planeur incident, sans se modifier
Quelques unes de ces figures peuvent presenter des variations, selon qu'elles soient renversées ou sous une forme active ou passive par exemple."""

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
-La clé "dimension_de_la_sortie" donne la dimension de la sortie dans le cas où la sortie diffère de l'entrée.
-La clé "emission", toujours pour être general, précise si ce conduit libére un element en meme temps qu'il modifie quelqu'un. C'est une liste
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
conduitscorbie_splitter_renverse_on={"droit":scorbie_splitter_renverse_on,"dx,dy":(0,59),"rotation":"droit","positionne":(-21,18),"dimension_de_l'entree":(3,3),"emission":[("glider","gauche",395,(39,-14))],"ticks":378}


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

liste_de_conduit={64:conduit64,112:conduit112,116:conduit116,117:conduit117,154:conduit154,282:conduit282,155:conduit154degun,190:conduit190,"semisnark":conduitsemisnark,"semisnarkrenverse":conduitsemisnarkrenverse,"snark":conduitsnark,"snarkrenverse":conduitsnarkrenverse,"semisnarkactif":conduitsemisnarkactif,"semisnarkrenverseactif":conduitsemisnarkrenverseactif,"scorbieon":conduitscorbie_splitter_on,"scorbieoff":conduitscorbie_splitter_off,"scorbierenverseon":conduitscorbie_splitter_renverse_on,"scorbierenverseoff":conduitscorbie_splitter_renverse_off,"syringe":conduitsyringe,"h_to_g":conduith_to_g,"mega_bistable":conduitmega_bistable,"mega_bistabledecale":conduitmega_bistabledecale,"mega_bistable_sans_sortie":conduitmega_bistable_sans_sortie,"mega_bistable_decale_sans_sortie":conduitmega_bistabledecale_sans_sortie}

""" creer_liste_pour_oscillateur prend en entrée k1,k2,k3,A,et B et renvoie une liste contenant 154,116,117,64 et 192 ainsi que 112 selon les regles:
1-il y a k1 F154, k2 F116, k3 F117, A R64, B R192 et A+B-2 L112
2-On commence par F154 si possible pour l[0]
3-On utilise autant de fois que nescessaire R64 puis un F puis L112 puis un F
4-On utilise ensuite autant de fois que nescessaire R192, puis F puis L112 puis F
5-Apres cela, il reste 2 R disponibles, on place un R puis tout les F restants puis le dernier R
6-On utilise d'abord tout les F117 puis les F154 et enfin les F116"""

def creer_liste_pour_oscillateur(k1,k2,k3,A,B):
    if k1>0:
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

"""place prend en entrée une grille l, une figure, la position où le haut gauche de cette figure doit se trouver dans la grille ainsi que son orientation representée par un string r, et ajoute cette figure en modifiant l en consequence"""

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

"""positionner prend en entrée une grille l, la position du haut gauche d'une figure ainsi que son orientation representée par un string r, et un conduit qui prend pour entrée cette figure, et modifie l en ajoutant ce conduit afin qu'il agisse sur la figure placée en haut_gauche et d'orientation r"""

def positionner(l,haut_gauche,r,conduit):
    a,b=conduit["dimension_de_l'entree"]
    x,y=conduit["positionne"]
    l1=conduit["droit"]
    n,m=len(l1),len(l1[0])
    if r=="droit":
        x,y=haut_gauche[0]+x,haut_gauche[1]+y
        for i in range(n):
            for j in range(m):
                l[x+i][y+j]=l1[i][j]+l[x+i][y+j]*(1-l1[i][j])
    elif r=="droite":
        x,y=y,a-x-n
        x,y=haut_gauche[0]+x,haut_gauche[1]+y
        for i in range(m):
            for j in range(n):
                l[x+i][y+j]=l1[n-1-j][i]+l[x+i][y+j]*(1-l1[n-1-j][i])
    elif r=="gauche":
        x,y=b-y-m,x
        x,y=haut_gauche[0]+x,haut_gauche[1]+y
        for i in range(m):
            for j in range(n):
                l[x+i][y+j]=l1[j][m-1-i]+l[x+i][y+j]*(1-l1[j][m-1-i])
    elif r=="a l'envers":
        x,y=a-x-n,b-y-m
        x,y=haut_gauche[0]+x,haut_gauche[1]+y
        for i in range(n):
            for j in range(m):
                l[x+i][y+j]=l1[n-1-i][m-1-j]+l[x+i][y+j]*(1-l1[n-1-i][m-1-j])
    else:
        pass

"""avancer prend en entrée une grille l, la position du haut gauche d'une figure ainsi que son orientation representée par un string r, et un conduit qui prend pour entrée cette figure, et modifie l en ajoutant ce conduit afin qu'il agissent sur la figure placée en haut_gauche et d'orientation r, puis renvoie l'emplacement et l'orientation de la figure apres sa modification par le conduit"""


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

"""deplace prend en entree une position haut gauche, une orientation d'un glider et un entier d, et renvoie la position du haut_gauche duglider apre 4*d ticks"""


def deplace(haut_gauche,r,d):
    if r=="droit":
        return (haut_gauche[0]+d, haut_gauche[1]+d)
    elif r=="gauche":
        return (haut_gauche[0]-d, haut_gauche[1]+d)
    elif r=="droite":
        return (haut_gauche[0]+d, haut_gauche[1]-d)
    elif r=="a l'envers":
        return (haut_gauche[0]-d, haut_gauche[1]-d)



"""tourner_droite et tourner_gauche renvoient la rotation d'une grille l en entrée sans la modifier
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

"""simplifie prend en entrée une grille l et renvoie cette même grille apres avoir rogné les bords jusqu'à trouver une cellule vivante, sans modifier la grille en entrée"""

def simplifie(l):
    minx,maxx,miny,maxy=len(l),0,len(l[0]),0
    for i in range(min(len(l),5000)):
        for j in range(len(l[0])):
            if l[i][j]==1:
                minx=min(minx,i)
                maxx=max(maxx,i)
                miny=min(miny,j)
                maxy=max(maxy,j)
    for i in range(max(0,len(l)-1000),len(l)):
        for j in range(len(l[0])):
            if l[i][j]==1:
                minx=min(minx,i)
                maxx=max(maxx,i)
                miny=min(miny,j)
                maxy=max(maxy,j)
    l1=[]
    for i in range(minx,maxx+1):
        l1.append([l[i][j] for j in range(miny,maxy+1)])
        if i%10**5==0:
            print(i,end=",")
    return l1

"""limit_de_oscillateur evalue la taille de l'oscillateur cree par la solution naive associé à k1,k2,k3,A et B"""

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

"""tous_a_cote prend en entrée la liste des coordonnées d'une partie M de la grille
et renvoie la liste des coordonnées des cellules voisines de M.
Ainsi, si seul un certain nombre de cellules ont changé d'état au dernier tick,
on peut savoir grace a tous_a_cote quelles cellules sont succeptibles de changer d'état
au prochain tick."""

def tous_a_cote(l1:list[int,int])->list[int,int]:
    l={(a[0],a[1]) for a in l1}
    for a in l1:
        i,j=a
        for x in range(i-1,i+2):
            for y in range(j-1,j+2):
                if (x,y) not in l:
                    l.add((x,y))
    return list(l)

"""etat_suivant prend en entrée une grille et une liste des coordonnées des cellules
qui sont succeptibles d'etre modiffié au prochain tick, et fait évoluer la grille d'un tick,
et la renvoie. si ind=True, il renvoie aussi la liste des coordonnées des cellules
ayant été modifiées"""


def etat_suivant(l,l1=[[]],ind=False)->int:
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

"""une autre fonction auxilliaire, et la plus couteuse en calcul. C'est pour eviter
son utilisation que l'on cherche à lineariser le placement des Herschels, c'est a dire a=1 ou a=2.
C'est pour cela que la complexité est bien plus importante pour a>2.
remplir_le_chemin prend en entrée une grille l contenant un circuit de herschel encore vide,
a le nombre d'Herschel a placer et p l'espacement entre deux Herschel. On présuppose que
le circuit est de longueur p*a, ce cricuit vide étant genéré grace à avancer.
l'idée de remplir_le_chemin est de rajouter un Herschel au début du circuit que l'on a
copié dans la grille l1, puis de faire évoluer a fois la grille l1 de p ticks.
Entre chaque évolution de p ticks, on prend une "photo" de la grille l1. On repére
alors sa difference avec l, et l'on modifie l pour faire disparaitre cette différence.
Mais, si l avait déja été modifié en certaines cases, on ne considére plus ces cases.
Ainsi, on fait d'abord évoluer le Herschel de p étapes. On le place  dans l.
Puis, on fait évoluer le Herschel de p autres ticks, donc en tout de 2*p étapes.
On le rajoute encore dans l. On en fait de même pour 3*p,4*p,...,a*p.
Ainsi, on remplit bien le circuit de a Herschel espacés entre eux de p ticks. """

def remplir_le_chemin(l:list[list[int]],p:int,a:int,haut_gauche:(int,int))->None:
    h=haut_gauche
    bon=[(h[0]+i,h[1]+j) for i in range(len(herschel)) for j in range(len(herschel[0])) ]
    for i in range(len(herschel)):
        for j in range(len(herschel[0])):
            l[h[0]+i][h[1]+j] = herschel[i][j]
    bouge=[(h[0]+i,h[1]+j) for i in range(len(herschel)) for j in range(len(herschel[0])) ]
    l1=[[l[i][j] for j in range(len(l[0]))] for i in range(len(l))]
    for d in range(a-1):
        change=[]
        for c in range(p):
            bouge=tous_a_cote(bouge)
            l1,bouge=etat_suivant(l1,bouge,True)
            for i in bouge:
                if i not in change:
                    change.append(i)
        for i in change:
            if i not in bon:
                l[i[0]][i[1]] = l1[i[0]][i[1]]
            if i in bon:
                l1[i[0]][i[1]] = l[i[0]][i[1]]
        bon=[(i[0],i[1]) for i in change]
    for i in range(len(herschel)):
        for j in range(len(herschel[0])):
            l[h[0]+i][h[1]+j] = herschel[i][j]
    #print("les herschels ont été placés!")
    return None

"""un_des_f prend en entrée une grille l, un haout_gauche, une orientation r et trois entiers a154, a116 et a117, et appele avancer pour le conduit F117 si a117>0, sinon pour le conduit F154 si a154>0 et sinon pour le conduit 116. elle renvoie alors le nouveau haut_gauche, ainsi que a154, a117 et a116 actualisés en diminuant le a de la figure ajoutée"""

def un_des_F(l,haut_gauche,r,a154,a116,a117):
    c=True
    if c and a117>0:
        haut_gauche,r=avancer(l,haut_gauche,r,conduit117)
        c=False
        a117-=1
    if c and a154>0:
        haut_gauche,r=avancer(l,haut_gauche,r,conduit154)
        a154-=1
        c=False
    if c and a116>0:
        haut_gauche,r=avancer(l,haut_gauche,r,conduit116)
        a116-=1
        c=False
    return haut_gauche,a154,a116,a117

"""renvoie l'oscillateur naif associé a k1,k2,k3,A et B ainsi que a. les conduits sont ajoutés en suivant les règles de créer_liste_pour_oscillateur"""

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

"""existe_selon_pa renvoie (k1,k2,k3,A,B) tels que pa=2*(k1*154+k2*116+k3*113+A*64+B*192+(A+B-2)*112) s'ils existent et False sinon. On impose:
    1-On n'utilise que des conduits de repeat time superieurs à periode
    2-A+B=2 (bien que non nescessaire)
    3-k1>=1, et on minimise k2 puis k3"""

def existe_selon_pa(periode:int,pa:int):
    p=pa//2
    for k2 in range(p//116 +1):
        if periode>=138 or k2==0:
            p=pa//2-k2*116
            for k3 in range(p//117+1):
                p=pa//2-k2*116-k3*117
                if periode>=63 or k3==0:
                    for k1 in range(1,p//154+1):
                        p=pa//2-k1*154-k2*116-k3*117
                        for A in range(3):
                            p=pa//2-k1*154-k2*116-k3*117-A*64
                            B=2-A
                            if periode>=107 or B==0:
                                if k1+k2+k3>=2*(A+B) and A+B>=2 and pa==2*(k1*154+k2*116+k3*117+A*64+B*190+(A+B-2)*112):
                                    return (k1,k2,k3,A,B)
    return False

"""plus_petit prend en entrée p un entier et renvoie a,k1,k2,k3,A,B tels que existe_selon_pa(p,p*a) trouve k1,k2,k,A et B, avec a minimal"""

def plus_petits(p:int)->(int,int,int,int,int,int):
    a=p%2
    verite=True
    while verite:
        a+=1
        x=existe_selon_pa(p,p*a)
        if x!= False:
            k1,k2,k3,A,B=x
            return (a,k1,k2,k3,A,B)

"""oscillateur prend en entree un entier p et renvoie une grille contenant un oscillateur de periode p, selon la methode naive"""

def oscillateur(p):
    a,k1,k2,k3,A,B=plus_petits(p)
    return oscillateur_de_constante(p,a,k1,k2,k3,A,B)

"""canon_naif prend en entrée un entier p et renvoie une grille contenant un canon de période p, obtenu en appelant oscillateur(p) puis en retirant le eater du premier F154, placé au début car k1>=1"""

def canon_naif(p):
    if p>=69:
        l=oscillateur(p)
        for i in range(32,40):
            for j in range(63,71):
                l[i][j]=0
        return l

"""canon_booste_puissance_2 prend en entree un entier p et un booléen ind, et renvoie une grille contenant un oscillateur de période P et m Semi_Snark chainé en sorte que p=P*2^m.
Si ind vaut True, la position et l'orientation d'un glider qui a passé tout les Semi_Snark est egalement renvoyée, permettant de rajouter un eater à cet emplacement"""

def canon_booste_puissance_2(p,ind=False):
    m=0
    while p%(2**(m+2))==0 and p//(2**(m+1))>2132:
        m+=1
    l=canon_naif(p//2**m)
    l=[[0 for i in range(len(l[0]))] for j in range(17*m+50)]+l
    haut_gauche,r=(75+17*m,55),"a l'envers"
    for i in range(m):
        if r=="a l'envers":
            haut_gauche,r=avancer(l,haut_gauche,r,conduitsemisnarkrenverseactif)
        elif r=="gauche":
            haut_gauche,r=avancer(l,haut_gauche,r,conduitsemisnarkactif)
    if ind:
        return l,haut_gauche,r
    return l

"""oscillateur_booste_puissance_2 prend en entrée un entier p et renvoie un grille contenant un oscillateur de période p, obtenu par ajout d'un eater à la sortie du canon renvoyé par canon_booste_puissance_2(p)"""

def oscillateur_booste_puissance_2(p):
    l,haut_gauche,r=canon_booste_puissance_2(p,True)
    positionner(l,haut_gauche,r,conduiteater)
    return l

"""prend en entrée une position haut_gauche et une orientation r, une grille l ainsi qu'une liste contenat des couples ( noms de conduit de glider, entier d ), et modifie la liste en ajoutant à partir de haut_gauche successivement les conduits de la liste, en déplaceant avant chaque ajout le glider de d cases """

def positioner_de_liste(haut_gauche,liste,l,r):
    for x,d in liste:
        haut_gauche=deplace(haut_gauche,r,d)
        haut_gauche,r=avancer(l, haut_gauche,r,liste_de_conduit[x])
    return haut_gauche,r

"""fonction auxilliaire qui prend en entrée un entier m et une largeur y et renvoie sous fome de liste adaptée a positioner_de_liste un chainage compact de m Semi_Snark """

def liste_pour_diviser_m_par_une_puissance_de_2(m,y):
    lemax=(y-100)//(17)
    lemax=lemax+lemax%2-1
    if lemax<=1 or m<4:
        l=[]
        for i in range(m):
            if i%2==0:
                l.append(("semisnarkrenverseactif",0))
            else:
                l.append(("semisnarkactif",0))
        return l,min(1,lemax)
    l=[("semisnarkrenverseactif",15),("semisnarkrenverseactif",0)]
    verite=False
    compteur=2
    d=0
    for i in range(m-3):
        verite=not verite
        if compteur<lemax:
            if verite:
                l.append(("semisnarkactif",d))
            else:
                l.append(("semisnarkrenverseactif",d))
            compteur+=1
            d=0
        elif compteur==lemax:
            compteur=1
            if not verite:
                l.append(("semisnarkactif",35))
            else:
                l.append(("semisnarkrenverseactif",35))
            d=10
    x=(m-1)%lemax
    if x%2==0:
        if not verite:
            l.append(("semisnarkactif",0))
        else:
            l.append(("semisnarkrenverseactif",0))
    else:
        if verite:
            l.append(("semisnarkactif",0))
        else:
            l.append(("semisnarkrenverseactif",0))
    return l,lemax


"""ces deux fonctions font exactement la même chose que les deux fonctions précedentes, àcela prés que les Semi_Snark sont positionés de manière plus compact"""

def canon_booste_puissance_2_compact(p,ind=False,ind2=False):
    m=0
    while p%(2**(m+2))==0 and (p//(2**(m+1))>1395 or (ind2 and p//2**(m+1)>69)):
        m+=1
    l1=canon_naif(p//2**m)
    l=[[l1[i][j] for j in range(len(l1[0]))]+[0 for i in range(32*(int(math.sqrt(m))))] for i in range(len(l1))]
    liste,lemax=liste_pour_diviser_m_par_une_puissance_de_2(m,len(l[0]))
    x=m//lemax+1
    l=[[0 for i in range(len(l[0]))] for j in range(70*x)]+l
    haut_gauche,r=(25+70*x,55),"a l'envers"
    haut_gauche,r=positioner_de_liste(haut_gauche,liste,l,r)
    if ind:
        return l,haut_gauche,r
    return l

def oscillateur_booste_puissance_2_compact(p):
    l,haut_gauche,r=canon_booste_puissance_2_compact(p,True)
    positionner(l,haut_gauche,r,conduiteater)
    return l

"""ecriture binaire prend en entree un entier x et a  (par defaut la partie entiere de log2(x) ) et renvoie sous forme de liste l'ecriture de x en  binaire, en allant jusqu'à 2**a"""

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

"""place_etape_de_bit prend en entrée une grille, une position de glider, une orientation r, un bit x et une distance d valant par défaut 0 et modifie l en y ajoutant 1 Snark et 1 SemiSnark, activé si x=0 et désactivé si x=0. la distance entre le Snark et le SemiSnark est augmentée de d. le nouveau haut_gauche et r sont renvoyés."""

def place_etape_de_bit(l,haut_gauche,r,x,d=0):
    haut_gauche=deplace(haut_gauche,r,17)
    haut_gauche,r=avancer(l,haut_gauche,r,conduitsnarkrenverse)
    haut_gauche=deplace(haut_gauche,r,d+10)
    if x==1:
        haut_gauche,r=avancer(l,haut_gauche,r,conduitsemisnark)
    if x==0:
        haut_gauche,r=avancer(l,haut_gauche,r,conduitsemisnarkactif)
    haut_gauche=deplace(haut_gauche,r,-6)
    return haut_gauche,r

"""fin_de_bit prend en entrée une grille l, la position d'un glider, son orientaion, une liste de bit et une distance d, par défaut valant 0, et modifie l pour terminer le period multiplier, en effectuant une rotaion puis en ajoutant les Scorbie Splitter pour chaque x dans liste, 1 pour off et 0 pour on."""

def fin_de_bit(l,haut_gauche,r,liste,d=0):
    haut_gauche=deplace(haut_gauche,r,8)
    haut_gauche,r=avancer(l,haut_gauche,r,conduitsnark)
    haut_gauche=deplace(haut_gauche,r,2+d)
    for i in liste:
        if i==1:
            haut_gauche,r=avancer(l,haut_gauche,r,conduitscorbie_splitter_renverse_off)
        if i==0:
            haut_gauche,r=avancer(l,haut_gauche,r,conduitscorbie_splitter_renverse_on)
    return haut_gauche,r

"""period_multiplier prend en entrée une grille l, la position d'un glider, son orientaion, un entier n et une distance d, par défaut valant 0, et modifie l en ajoutant un n-multiplicateur de période pour glider. en effet, si on écrit x en base 2 et qu'on utilise des Semi Snark off pour les 1 et des SemiSnark on pour les 0, en les chainant pour écrire x en base 2 on bloque exactement x gliders avant d'en laisser passer 1, soit un (x+1) multiplicateur à usage unique, et les Scorbie Splitter permettent de maintenir cet arrangement """

def period_multiplier(l,haut_gauche,r,n,d=0):
    haut_gauche=deplace(haut_gauche,r,15)
    a=math.log2(n)
    if n==1:
        liste=[0]
    elif a%1==0:
        liste=[1 for i in range(int(a))]
    else:
        a=int(a)
        liste=ecriture_binaire(n-1,a)
    for i in range(len(liste)-1):
        i=len(liste)-i-1
        haut_gauche,r=place_etape_de_bit(l,haut_gauche,r,liste[i])
    haut_gauche,r=place_etape_de_bit(l,haut_gauche,r,liste[0],d)
    haut_gauche=deplace(haut_gauche,r,1)
    haut_gauche,r=fin_de_bit(l,haut_gauche,r,liste,d)
    return haut_gauche,r

"""period_multiplier_actif fait de même, mais tout les Semi_Snark sont initalement activés"""

def period_multiplier_actif(l,haut_gauche,r,n,d=0):
    haut_gauche=deplace(haut_gauche,r,15)
    a=math.log2(n)
    if n==1:
        liste=[0]
    elif a%1==0:
        liste=[1 for i in range(int(a))]
    else:
        a=int(a)
        liste=ecriture_binaire(n-1,a)
    for i in range(len(liste)-1):
        i=len(liste)-i-1
        haut_gauche,r=place_etape_de_bit(l,haut_gauche,r,0)
    haut_gauche,r=place_etape_de_bit(l,haut_gauche,r,0,d)
    haut_gauche=deplace(haut_gauche,r,1)
    haut_gauche,r=fin_de_bit(l,haut_gauche,r,liste,d)
    return haut_gauche,r

"""cherche_si_z_existe et cherche ont pour but de vérifier que les gliders parcourant dans les deux sens le period multiplier n'interferent pas, en renvoyant un entier d tel qu'en ajoutant un décalage de 8*d par un deplacement de d cases des Snark, on évite toute collision"""

def check_si_z_existe(p,d,n):
    for i in range(n):
        y=616*(n-i)+8*d+72
        if 2**i==1:
            a=2**i
        else:
            a=2**i-1
        z=y%(p*a)
        if z<=20 or z>=p*a-175:
            return True
        if z==y:
            return False
    return False

def cherche(p,a):
    b=math.log2(a)
    if b==0:
        n=1
    if b%1==0:
        n=int(b)
    else:
        n=int(b)+1
    for d in range(1000):
        if not check_si_z_existe(p,d,n):
            return d
    return -20

"""touve un diviseur de p supérieur à 272 car empiriquement pour periode>271 et a entier, cherche(periode,a) trouve un d fonctionel"""

def divise(p):
    if p<272:
        return False
    for multiplier in range(p//272):
        multiplier=p//272 -multiplier
        if p%multiplier==0:
            return multiplier

"""canon_booste_max qui utilise period_multiplier pour créer un oscillateur de période p, d pouvant être donné, par défaut d est obtenu avec cherche"""

def canon_booste_max(p,d=-1):
    if p<69:
        print("oops, la periode doit etre supperieure a 69!")
        return glider
    if p<300:
        return canon_naif(p)
    a=divise(p)
    if a==1:
        return canon_naif(p)
    x=math.log2(a)
    if x%1==0:
        return canon_booste_puissance_2_compact(p)
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

"""identique à canon_booste_max, mais un eater est ajouté à la fin, transformant le canon en oscillateur"""

def oscillateur_booste_max(p,d=-1):
    if p<61:
        print("oops, la periode doit etre superieure a 61")
        return glider
    if p>=61 and p<69:
        return oscillateur(p)
    if p<300:
        return oscillateur(p)
    a=divise(p)
    if a==1:
        return oscillateur(p)
    x=math.log2(a)
    if x%1==0:
        return oscillateur_booste_puissance_2_compact(p)
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

"""area_naif prend en entrée un entier p et renvoie la taille de l'oscillateur naif qui lui est associé"""

def area_naif(p):
    a,k1,k2,k3,A,B=plus_petits(p)
    x,y=limit_de_oscillateur(k1,k2,k3,A,B)
    return x,y

"""area_max prend en entrée un entier p, possiblement un entier a par lequel multiplier p, par défaut on multiplie p//a par a avec a=divise(p), un booleen Id qui indique si le d du period_multiplier doit également être renvoyé, des aractéristiques d'oscillateur k1,...,B, qui sont par défaut obtenues par un appel à plus_petit, et enfin d, qui est par défaut obtenu par cherche. area_max renvoie alors la taille de l'oscillateur_booste_max obtenu avec ces caracteristiques"""

def area_max(p,a=-1,Id=False,k1=-1,k2=-1,k3=-1,A=-1,B=-1,d=-1):
    if p<69:
        print("oops, la periode doit etre supperieure a 69!")
        return 0
    if p<272:
        return area_naif(p)
    if a==-1:
        a=divise(p)
        i=p//a
    else:
        i=p
    if d==-1:
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

"""trier_l1_selon_l2 prend en entrée deux listes l1,l2 et renvoie (sans la modifier) la liste l1 triée selon l2"""

def trier_l1_selon_l2(l1,l2):
    l3=[x for x in l1]
    l4=[x for x in l2]
    def min(l,j):
        m=l[j]
        for i in range(j,len(l)):
            if l[i]<m:
                m,j=l[i],i
        return j
    for i in range(len(l4)):
        x=min(l4,i)
        a,b=l3[i],l4[i]
        l3[i],l4[i]=l3[x],l4[x]
        l3[x],l4[x]=a,b
    return l3

"""on créé ici dico, les_clefs, les_y et les_clefs_top, qui sont:
    -un dictionnaire dont les clés sont des pértiode apparente de circuit de Herschel combinés avec un petit ajout dû à la transformation h_to_g, au passage par le conduit mega_bistable et à la retransformation par le syringe de glider à herschel. on associe à chaque clé les caractéristiques k1,k2,k3,A,et B permettant d'obtenir cette periode apparente
    -une liste des clés ainsi obtenues, que l'on peut élaguer en retirant toute clés divisible par une clé precedente
    -on trie ensuite ces clefs pour minimiser la largeur y, par un appel à trier_l1_selon_l2. on obtient aisni les_clefs_top"""

"""création de les_clefs et de dico"""
dico={}
for sum in range(0,96):
    for k2 in range(0,min(sum+1,11)):
        for k1 in range(1,min(sum-k2+1,36)):
            k3=sum-k1-k2
            for A in range(3):
                for B in range(3):
                    if A+B>=2 and k1+k2+k3>=2*(A+B+2):
                        p_apparent=2*(973+k1*154 + k2*116 + k3*117 + A*64 + B*190 + (A+B-2)*112)
                        if p_apparent not in dico:
                            dico[p_apparent]=(k1,k2,k3,A,B)
les_clefs=list(dico.keys())

"""création de les_y, puis de les_clefs_top"""

les_y=[]
for i in les_clefs:
    k1,k2,k3,A,B=dico[i]
    x,y=limit_de_oscillateur(k1,k2,k3,A,B)
    les_y.append(y)

les_clefs_top=trier_l1_selon_l2(les_clefs,les_y)

"""on diminue la taille de dico en retirant toute période apparente divisible par une autre periode apparente de plus petite taille"""
for i in range(len(les_clefs_top)):
    i=len(les_clefs_top)-i-1
    p_app=les_clefs_top[i]
    x=0
    while x<i:
        if p_app%les_clefs_top[x]==0:
            del dico[p_app]
            x=i+1
        x+=1
les_clefs=list(dico.keys())

"""on recréé les_y puis les_clefs_top aprés l'élaguation"""

les_y=[]
for i in les_clefs:
    k1,k2,k3,A,B=dico[i]
    x,y=limit_de_oscillateur(k1,k2,k3,A,B)
    les_y.append(y)

les_clefs_top=trier_l1_selon_l2(les_clefs,les_y)
les_clefs.sort()

"""trouver_sans_sat_top doit trouver pour p un entier une periode apparente dans dico p_app, un entier multiplier et un entier ajout<=50 tel que p=delta+multiplier*p_app, avec delta qui vaut 1042+8*ajout si p est pair (car p_app est toujours pair) et delta qui vaut 1467+8*ajout si p est impair.
trouver_san_sat_top renvoie alors k1,k2,k3,A,B,multiplier,ajout avec k1,..,B associé à p_app dans dico.
cette fonction est ainsi de même compléxité que l'opération p%p_app avec p_app borné.
Empiriquement, pur p>5000, p_app existe toujours."""

def trouver_sans_sat_top(p):
    for p_app in les_clefs_top:
        if p%2==0:
            acc=p-1042
        else:
            acc=p-1367
        if acc>0:
            a=acc%p_app
            if a%8==0 and a<=8*50:
                k1,k2,k3,A,B=dico[p_app]
                # print(p_app)
                return k1,k2,k3,A,B,acc//p_app,a//8
    return False

"""canon_optimal prend en entrée un entier p et renvoie un canon de période p, de taille et en complexité logarithmique"""

def canon_optimal(p):
    if p>=2000:
        x=trouver_sans_sat_top(p)
        if x==False:
            if p>=10**5:
                print("desole, la periode est trop grande pour etre manipulée par ortools, un module utilisé pour trouver des solutions aux equations a plusieurs variables")
            else:
                return canon_booste_max(p)
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

            haut_gauche,r=avancer(l,haut_gauche,r,conduith_to_g)
            if p%2==0:
                haut_gauche,r=avancer(l,haut_gauche,r,conduitmega_bistable)
            else:
                haut_gauche,r=avancer(l,haut_gauche,r,conduitmega_bistabledecale)
            haut_gauche=deplace(haut_gauche,r,50)
            haut_gauche,r=avancer(l,haut_gauche,r,conduitsyringe)

            if x==0 :
                for i in range(len(herschel)):
                    for j in range(len(herschel[0])):
                        l[haut_gauche[0]+i][haut_gauche[1]+j]=herschel[i][j]
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

        haut_gauche_glider,r=period_multiplier_actif(l,haut_gauche_glider,r,multiplier,d)
        x=math.log2(multiplier)
        if multiplier==1:
            e=1
        elif x%1==0:
            e=int(x)
        else:
            e=int(x)+1
        ticks_en_plus=190+e*(266+350)+8*d
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
        return canon_booste_max(p)

"""oscillateur_optimal prend en entrée un entier p et renvoie un oscillateur de période p en temps et taille logarithmique"""

def oscillateur_optimal(p):
    if p>=2000:
        x=trouver_sans_sat_top(p)
        if x==False:
            if p>=10**5:
                print("desole, la periode est trop grande pour etre manipulée par ortools, un module utilisé pour trouver des solutions aux equations a plusieurs variables")
                return []
            else:
                return oscillateur(p)
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
            haut_gauche,r=avancer(l,haut_gauche,r,conduith_to_g)
            if p%2==0:
                haut_gauche,r=avancer(l,haut_gauche,r,conduitmega_bistable_sans_sortie)
            else:
                haut_gauche,r=avancer(l,haut_gauche,r,conduitmega_bistabledecale_sans_sortie)
            haut_gauche=deplace(haut_gauche,r,50)
            haut_gauche,r=avancer(l,haut_gauche,r,conduitsyringe)
            if x==0 :
                for i in range(len(herschel)):
                    for j in range(len(herschel[0])):
                        l[haut_gauche[0]+i][haut_gauche[1]+j]=herschel[i][j]
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
        haut_gauche_glider,r=period_multiplier_actif(l,haut_gauche_glider,r,multiplier,d)
        x=math.log2(multiplier)
        if multiplier==1:
            e=1
        elif x%1==0:
            e=int(x)
        else:
            e=int(x)+1
        ticks_en_plus=190+e*(266+350)+8*d
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
        return oscillateur_booste_max(p)

"""area_optimal prend en entrée un entier p et x dans le format de trouver_sans_sat_top(p) associé à p, et renvoie une évaluation de la taille de de l'oscillateur fourni par la solution optimale associé à x """

def area_optimal(p,x):
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

"""area_max_peu_prés donne une borne de la taille de l'oscillateur de la solution boostée en considérant que d est plus petit que 50, ce qui est empiriquement vérifié"""

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

"""area_optimal_peu_pres agit de même, en utilisant area_max_peu_pres"""
def area_optimal_peu_pres(p,x):
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

"""ligne_to_rle puis matrix_to_rle ont pour but de transformer une grille l de format matrice en sa representation rle qui est la representation canonique, car étant plus compact"""

def ligne_to_rle(l):
    r = []
    c = l[0]
    n = 1
    for x in l[1:]:
        if x == c:
            n += 1
        else:
            if n > 1:
                r.append(str(n))
            r.append('o' if c else 'b')
            c = x
            n = 1
    if n > 1:
        r.append(str(n))
    r.append('o' if c else 'b')
    return ''.join(r)

def matrix_to_rle(l, en_tete=True, fin=True):
    print("let's go")
    n = len(l)
    m = len(l[0])
    r = []
    copteur=0
    if en_tete:
        r.append(f"x={m}, y={n}, rule=B3/S23\n")
    for i, row in enumerate(l[:-1]):
        if i%10**5==0:
            print(i,end=",",flush=True)
        a=ligne_to_rle(row)
        compteur+=len(a)
        r.append(a)
        r.append('$')
        if compteur>100:
            r.append("\n")
            compteur=0
    r.append(ligne_to_rle(l[-1]))
    r.append('!' if fin else '$')
    return ''.join(r)

def oscillateur_final(p):
    l=oscillateur_optimal(p)
    return matrix_to_rle(simplifie(l))

def canon_final(p):
    l=canon_optimal(p)
    return matrix_to_rle(simplifie(l))
