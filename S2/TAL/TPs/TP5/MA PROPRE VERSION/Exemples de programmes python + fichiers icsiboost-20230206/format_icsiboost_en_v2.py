# Traduction d'un corpus annote en entite nomme dans un format icsiboost en selectionnant uniquement les lignes marquee 'hyp'
# exemple d'utilisation avec la commande 'marque_patron_en.py'
# cat corpus_en.txt | python3 ./marque_patron_en.py patron_en.txt | python3 ./format_icsiboost_en_v2.py 
# dans cette version, seule les lignes ayant le label 'hyp' en 5e colonne sont considérées
# on rajoute aussi un champs : index-ligne qui contient le numero de ligne dans le fichier original
#
# le fichier patron_en.txt contient par exemple :
# np
# adj np

import sys

tphrase=[]; indice=0

def traite_phrase():
    global indice,tphrase
    chmot=""; chpos=""
    for x in range(0,len(tphrase)):
        if (tphrase[x][4]=="hyp"):
            print("{},{}".format(indice,tphrase[x][0]),end="")
            print(",{},{}".format(tphrase[x-2][1],tphrase[x-2][2]),end="") if (x>=2) else print(",XX,XX",end="");
            print(",{},{}".format(tphrase[x-1][1],tphrase[x-1][2]),end="") if (x>=1) else print(",XX,XX",end="");
            print(",{},{}".format(tphrase[x][1],tphrase[x][2]),end="")
            print(",{},{}".format(tphrase[x+1][1],tphrase[x+1][2]),end="") if (x<(len(tphrase)-1)) else print(",XX,XX",end="");
            print(",{},{}".format(tphrase[x+2][1],tphrase[x+2][2]),end="") if (x<(len(tphrase)-2)) else print(",XX,XX",end="");
            print(",{}".format(tphrase[x][3]),end=".\n")
        indice+=1

l1 = sys.stdin.readline()
while l1 :
    if (len(l1)>2): # pas de saut de ligne
        t1=l1[:-1].split("\t")
        if (t1[1]==','): t1[1]="VIRGULE"
        if (t1[1]=='.'): t1[1]="POINT"
        tphrase.append(t1.copy())
    else :
        traite_phrase()
        tphrase.clear();
        indice+=1
    l1 = sys.stdin.readline()
traite_phrase();
