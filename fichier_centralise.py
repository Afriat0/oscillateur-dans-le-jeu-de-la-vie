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

import repertoire_complet as repertoire

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

scorbiesplitteroff=repertoire.scorbieoff
scorbiesplitteron=repertoire.scorbieon
scorbiesplitterrenverseoff=repertoire.scorbierenverseoff
scorbiesplitterrenverseon=repertoire.scorbierenverseon

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

conduitscorbiesplitteroff={"droit":scorbiesplitteroff,"dx,dy":(59,0),"rotation":"droit","positionne":(18,-12),"dimension_de_l'entree":(3,3),"emission":[],"ticks":378}
conduitscorbiesplitterrenverseoff={"droit":scorbiesplitterrenverseoff,"dx,dy":(0,59),"rotation":"droit","positionne":(-11,18),"dimension_de_l'entree":(3,3),"emission":[],"ticks":378}

conduitscorbiesplitteron={"droit":scorbiesplitteron,"dx,dy":(59,0),"rotation":"droit","positionne":(18,-22),"dimension_de_l'entree":(3,3),"emission":[("glider","gauche",395,(39,-14))],"ticks":378}
conduitscorbiesplitterrenverseon={"droit":scorbiesplitterrenverseon,"dx,dy":(0,59),"rotation":"droit","positionne":(-21,18),"dimension_de_l'entree":(3,3),"emission":[("glider","gauche",395,(39,-14))],"ticks":350}


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

liste_de_conduit={64:conduit64,112:conduit112,116:conduit116,117:conduit117,154:conduit154,282:conduit282,155:conduit154degun,190:conduit190,"semisnark":conduitsemisnark,"semisnarkrenverse":conduitsemisnarkrenverse}

"""positionner prend en entrée une grille l, la position du haut gauche d'une figure ainsi que son orientation representée par un string"""

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
    dx,dy=conduit["dx,dy"]
    x,y=haut_gauche
    if conduit["rotation"]=="droit":
        if r=="droite":
            dx,dy=dy,-dx
        elif r=="gauche":
            dx,dy=-dy,dx
        elif r=="a l'envers":
            dx,dy=-dx,-dy
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


def liste_pour_diviser_m_par_une_puissance_de_2(m,y):
    lemax=(y-100)//(17)
    lemax=lemax+lemax%2-1
    if lemax<=1 or m<4:
        l=[]
        for i in range(m):
            if i%2==0:
                l.append(("semisnarkrenverse",0))
            else:
                l.append(("semisnark",0))
        return l,min(1,lemax)
    l=[("semisnarkrenverse",15),("semisnarkrenverse",0)]
    verite=False
    compteur=2
    d=0
    for i in range(m-3):
        verite=not verite
        if compteur<lemax:
            if verite:
                l.append(("semisnark",d))
            else:
                l.append(("semisnarkrenverse",d))
            compteur+=1
            d=0
        elif compteur==lemax:
            compteur=1
            if not verite:
                l.append(("semisnark",35))
            else:
                l.append(("semisnarkrenverse",35))
            d=10
    x=(m-1)%lemax
    if x%2==0:
        if not verite:
            l.append(("semisnark",0))
        else:
            l.append(("semisnarkrenverse",0))
    else:
        if verite:
            l.append(("semisnark",0))
        else:
            l.append(("semisnarkrenverse",0))
    return l,lemax

def deplace(haut_gauche,r,d):
    if r=="droit":
        return (haut_gauche[0]+d, haut_gauche[1]+d)
    elif r=="gauche":
        return (haut_gauche[0]-d, haut_gauche[1]+d)
    elif r=="droite":
        return (haut_gauche[0]+d, haut_gauche[1]-d)
    elif r=="a l'envers":
        return (haut_gauche[0]-d, haut_gauche[1]-d)


def positioner_de_liste(haut_gauche,liste,lmodifier,r):
    for x,d in liste:
        haut_gauche=deplace(haut_gauche,r,d)
        haut_gauche,r=avancer(lmodifier, haut_gauche,r,liste_de_conduit[x])
    return haut_gauche,r


"""existe_selon_pa cherche a verifier si il existe un circuit de Herschel de longueur
pa qui n'utilise que des circuits de repeat time inférieurs à p.
On recherche donc k1,k2,k3,A et B, sachant que C=A+B-2, qui vérifient la relation
pa==2*(k1*154+k2*116+k3*117+A*64+B*190+(A+B-2)*112)"""

from ortools.sat.python import cp_model

def plus_petits_primaire(p):
    if p%7!=0 and p%11!=0:
        model = cp_model.CpModel()
        a=model.NewIntVar(1,1000,'a')
        k1 = model.NewIntVar(1, p, 'k1')
        model.Add(2*154*k1+4*64== p*a)
        model.Minimize(k1)
        solver = cp_model.CpSolver()
        status = solver.Solve(model)
        if status in (cp_model.OPTIMAL, cp_model.FEASIBLE):
            return solver.Value(a),solver.Value(k1),0,0,2,0
        else:
            return False
    else:
        model = cp_model.CpModel()
        a=model.NewIntVar(1,1000,'a')
        k1 = model.NewIntVar(2, p, 'k1')
        model.Add(2*154*k1+2*76*282+4*64== p*a)
        model.Minimize(k1)
        solver = cp_model.CpSolver()
        status = solver.Solve(model)
        if status in (cp_model.OPTIMAL, cp_model.FEASIBLE):
            return solver.Value(a),solver.Value(k1),0,0,2,0
        else:
            return False
def plus_petits(p):
    def existe_selon_pa(periode:int,pa:int):
        p=pa//2
        for k2 in range(p//116 +1):
            if periode>=138 or k2==0:
                p=pa//2-k2*116
                for k1 in range(1,p//154+1):
                    p=pa//2-k1*154-k2*116
                    for k3 in range(p//117+1):
                        p=pa//2-k1*154-k2*116-k3*117
                        if periode>=63 or k3==0:
                            for A in range(p//64+1):
                                p=pa//2-k1*154-k2*116-k3*117-A*64
                                if periode>=62 or A==2:
                                    for B in range(p//190+1):
                                        if periode>=107 or B==0:
                                            if k1+k2+k3>=2*(A+B) and A+B>=2 and pa==2*(k1*154+k2*116+k3*117+A*64+B*190+(A+B-2)*112):
                                                return (k1,k2,k3,A,B)
        return False
    """plus_petits essaye de trouver a tel que existe_selon_pa(p*a) trouve une solution
    k1,k2,k3,A,B, en testant toutes les valeures de a jusqu'à ce que le programme finisse,
    et renvoie (a,k1,k2,k3,A,B).
    En pratique, cette boucle while finit toujours. On sait deja qu'une solution existe
    si p n'est divisible ni par 7, ni par 11, en n'utilisant que F154 et R64. La principale
    contrainte est en fait k1,k2,k3,A,B sont positifs."""

    def plus_petits_naif(p:int)->(int,int,int,int,int,int):
        a=p%2
        verite=True
        while verite:
            a+=1
            x=existe_selon_pa(p,p*a)
            if x!= False:
                k1,k2,k3,A,B=x
                return (a,k1,k2,k3,A,B)

    def existe_selon_pa_sat(pa):
        model = cp_model.CpModel()
        p_max = pa // 2
        k1 = model.NewIntVar(1, p_max//154, 'k1')
        k2 = model.NewIntVar(0, p_max//116, 'k2')
        k3 = model.NewIntVar(0, p_max//117, 'k3')
        A  = model.NewIntVar(0, p_max//64,  'A')
        B  = model.NewIntVar(0, p_max//190, 'B')
        model.Add(2*(k1*154 + k2*116 + k3*117 + A*64 + B*190 + (A+B-2)*112) == pa)
        model.Add(A + B >= 2)
        model.Add(k1 + k2 + k3 >= 2*(A+B))
        model.Minimize(k2)
        model.Minimize(A+B)
        model.Minimize(k2)
        solver = cp_model.CpSolver()
        status = solver.Solve(model)
        if status in (cp_model.OPTIMAL, cp_model.FEASIBLE):
            return solver.Value(k1), solver.Value(k2), solver.Value(k3), solver.Value(A), solver.Value(B)
        else:
            return False

    def plus_petit_sat(p:int)->(int,int,int,int,int,int):
        a=p%2
        verite=True
        while verite:
            a+=1
            x=existe_selon_pa_sat(p*a)
            if x!= False:
                k1,k2,k3,A,B=x
                return (a,k1,k2,k3,A,B)

    if p>=138:
        return plus_petit_sat(p)
    return plus_petits_naif(p)


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

"""la derniere fonction auxilliaire, et la plus couteuse en calcul. C'est pour eviter
son utilisation que l'on cherche à lineariser le placement des Herschels, c'est a dire a=1 ou a=2.
C'est pour cela que la complexité est bien plus importante pour a>2.
remplir_le_chemin prend en entrée une grille l contenant un circuit de herschel encore vide,
a le nombre d'Herschel a placer et p l'espacement entre deux Herschel. On présuppose que
le circuit est de longueur p*a, ce cricuit vide étant genéré grace au fonctions avancer.
l'idée de remplir_le_chemin est de rajouter un Herschel au début du circuit que l'on a
copié dans la grille l1, puis de faire évoluer a fois la grille l1 de p ticks.
Entre chaque évolution de p ticks, on prend une "photo" de la grillel1. On repére
alors sa difference avec l, et l'on modifie l pour faire disparaitre cette différence.
Mais, si l avait déja été modifié en certaines cases, on ne considére plus ces cases.
Ainsi, on fait d'abord évoluer le Herschel de p étapes. On le place  dans l.
Puis, on fait évoluer le Herschel de p autres ticks, donc en tout de 2*p étapes.
On le rajoute encore dans l. On en fait de même pour 3*p,4*p,...,a*p.
Ainsi, on remplit bien le chemin ou le circuit de a Herschel éspacés entre eux de p ticks. """

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

"""étape élementaire pour construire un circuit de Herschel. un_des_F prend en entrée
une grille l, des coordonnées hautgauche, une orientation r et trois compteurs.
Un appel à un_des_F a le même effet qu'un appel à la fonction avancer154 ou avancer116
ou avancer 117, en appelant le premier avancer_n_ tel que a_n_ est non nul. On diminue
alors de 1 le compteur du conduit qui a été ajouté, et on renvoie
haut_gauche , a154 , a116 , a117 """


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

"""Enfin oscillateur qui recolle les bouts, et renvoie une grille contenant un oscillateur p.
-Un appel à plus_petits(p) fournit a,k1,k2,k3,A,B tels que
    p*a= 2 * [ k1*154 + k2*116 + k3*117 + A*64 + B*190 + (A+B-2)*112 ]
-Un appel à limit_de_oscillateur nous donne la taille d'une grille dont le p-oscillateur induit
    par p,a,k1,k2,k3,A,B ne sortira jamais.
-On crée une grille vide de cette taille, et on place un Herschel droit imaginaire en
    haut_gauche=(50,50)
-Puis, a deux reprises, on ajoute un demi-circuit à partie de haut gauche, obtenu en
    ajoutant par un_des_F un F au départ et en avancant le Herschel imaginaire. On voit
    ensuite quels R vont être utiliser seuls, c'est a dire ne sont pas compensés par des L112.
    Puis, pour touts les R restants, et un par un jusqu'à les avoir épuisés:
        --on ajoute R par avancer en faisant avancer le Herschel imaginaire
        --on ajoute un F par un_des_F en faisant avancer le Herschel imaginaire
        --on ajoute L112 par avancer en faisant avancer le Herschel imaginaire
        --on ajoute un F par un_des_F en faisant avancer le Herschel imaginaire
    On ajoute un des deux R choisis plus tôt par avancer en faisant avancer le herschel imaginaire
    puis on ajoute tout les F restants par un_des_R en faisant avancer le herschel imaginaire.
    On rajoute enfin le deuxième R choisi précedement.
    On a bien placé dans chaque demi-circuit
    k1 F154, k2 F116, k3 F117, A R64, B R190 et (A+B-2) L112,
    donc la taille du circuit total est
    2 * [ k1*154 + k2*116 + k3*117 + A*64 + B*190 + (A+B-2)*112 ]
    donc p*a
-Enfin, si a>2, on appele remplir_le_chemin et sinon, si a=1 on place un seul Herschel droit
    au début du circuit, et si a=2 on ajoute également un Herschel à l'envers à un bout du
    demi-circuit, car la taille du demi-circuit est p*a/2=p*1

->On a bien construit un oscillateur de période p. En soit, le choix de l'ordre dans lequel
les conduits sont placé est presque sans conséquence, mais placer des RFLF composés dés
que possible et finir par un R permet de s'assurer que la cellule vivante la plus à gauche et
la plus haute soit dans le R de fin ou le F de début, car si on finit par un R cela signifie
que le Herschel vient d'en bas avant le R. De plus F116 , lorsqu'il est droit, fait avancer
un Herschel vers la droite et le haut, tandis qu'un RFlF fait avancer un Herschel vers la
droite et vers le bas. Ainsi, on est sur de redescendre, et d'aller vers la droite, il
suffit de savoir ou est la limite a droite et en bas pour s'assurer que l'oscillateur
ne dépasse pas de la grille. Mais on pourrait tout aussi bien determiner
quel F placer en premier puis quels RFLF, puis quel R, puis quels F, puis quel R placer en dernier
totalement au hasard
->La nescessité d'intercaller un F entre un R et un R, un R et un L ou un L et un L
vient de la necessité d'écarter ces circuits qui sinon interferent entre eux.
Cette condition n'est en fait pas contraignante pour notre usage car a=1 (ou a=2), qui est la
meilleur solution possible pour un circuit car la taille de ce circuit sera toujours au moins
égale a p, est tout de même vérifié à partir d'un certain rang """

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

def oscillateur_de_liste(p,a,liste,lmodifier,haut_gauche=(50,50)):
    if p>=61:
        l=lmodifier
        n=len(liste)
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
            for i in range(n//2):
                j=liste[x*n//2+i]
                haut_gauche,r=avancer(l,haut_gauche,r,liste_de_conduit[j])
        if a>2:
            remplir_le_chemin(l,p,a,haut_gauche)
        return l
    else:
        pass

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

def creer_liste_pour_oscillateur_primaire(p,k1,k2,k3,A,B):
    liste=[154]
    if p%7==0 or p%11==0:
        liste+=[282 for i in range(76)]
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

def oscillateur_avec_liste(p):
    a,k1,k2,k3,A,B=plus_petits(p)
    x,y=limit_de_oscillateur(k1,k2,k3,A,B)
    l=[[0 for j in range(y)] for i in range(x)]
    liste=creer_liste_pour_oscillateur(k1,k2,k3,A,B)
    return oscillateur_de_liste(p,a,liste,l)

def oscillateur_primaire(p):
    a,k1,k2,k3,A,B=plus_petits_primaire(p)
    x,y=limit_de_oscillateur(k1,k2,k3,A,B)
    if p%7==0 or p%11==0:
        x,y=x+76*53,y+76*53
    l=[[0 for j in range(y)] for i in range(x)]
    liste=creer_liste_pour_oscillateur_primaire(p,k1,k2,k3,A,B)
    return oscillateur_de_liste(p,a,liste,l)

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
def canon_booste_2_0(p,ind=False,ind2=False):
    m=0
    while p%(2**(m+2))==0 and (p//(2**(m+1))>1395 or (ind2 and p//2**(m+1)>69)):
        m+=1
    l1=canon_naif(p//2**m)
    l=[[l1[i][j] for j in range(len(l1[0]))]+[0 for i in range(35*(int(math.sqrt(m))))] for i in range(len(l1))]
    liste,lemax=liste_pour_diviser_m_par_une_puissance_de_2(m,len(l[0]))
    print(liste,lemax)
    x=m//lemax+1
    l=[[0 for i in range(len(l[0]))] for j in range(70*x)]+l
    haut_gauche,r=(25+70*x,55),"a l'envers"
    haut_gauche,r=positioner_de_liste(haut_gauche,liste,l,r)
    if ind:
        return l,haut_gauche,r
    return l

def oscillateur_booste(p):
    l,haut_gauche,r=canon_booste(p,True)
    positionner(l,haut_gauche,r,conduiteater)
    return l

def oscillateur_booste_2_0(p):
    l,haut_gauche,r=canon_booste_2_0(p,True)
    positionner(l,haut_gauche,r,conduiteater)
    return l

#nouvelle partie tres tres performante

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
            haut_gauche,r=avancer(l,haut_gauche,r,conduitscorbiesplitterrenverseoff)
        if i==1:
            haut_gauche,r=avancer(l,haut_gauche,r,conduitscorbiesplitterrenverseon)
    return haut_gauche,r

def period_multiplier(l,haut_gauche,r,n,d=0):
    haut_gauche=deplace(haut_gauche,r,15)
    a=math.log2(n)
    if a%1==0:
        liste=[0 for i in range(int(a))]
    else:
        a=int(a)-1
        b=int(2**(a+2)-n)
        liste=[0]+ecriture_binaire(b,a)
    for i in range(len(liste)-1):
        i=len(liste)-i-1
        haut_gauche,r=place_etape_de_bit(l,haut_gauche,r,liste[i])
    haut_gauche,r=place_etape_de_bit(l,haut_gauche,r,liste[0],d)
    haut_gauche=deplace(haut_gauche,r,1)
    haut_gauche,r=fin_de_bit(l,haut_gauche,r,liste,d)
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

def divise(p):
    if p<245:
        return False
    model = cp_model.CpModel()
    multiplier = model.NewIntVar(1, p//245, 'multiplier')
    periode = model.NewIntVar(245, p, 'periode')
    model.AddMultiplicationEquality(p, [periode, multiplier])
    model.Minimize(periode)
    solver = cp_model.CpSolver()
    status = solver.Solve(model)
    if status in (cp_model.OPTIMAL, cp_model.FEASIBLE):
        return solver.Value(multiplier)
    else:
        return False

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

def area_max(p):
    if p<69:
        print("oops, la periode doit etre supperieure a 69!")
        return 0
    if p<245:
        return area_naif(p)
    a=divise(p)
    d=cherche((p//a),a)
    nimporte,k1,k2,k3,A,B=plus_petits(p//a)
    x,y=limit_de_oscillateur(k1,k2,k3,A,B)
    x=50+d+59*(int(math.log2(a))+1)+x
    n=d+100-y
    if n<0:
        n=0
    y=75+y+n
    return x,y
