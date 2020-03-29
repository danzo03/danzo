def rectangle(largeur,longueur):
    #fonction qui retourne l'aire d'un rectangle
    a=largeur*longueur
    return a



def affiche_rect(n):
    for i in range(1,n+1):
        print("*"*i)

affiche_rect(5)
res=rectangle(2,4)
print(res)
