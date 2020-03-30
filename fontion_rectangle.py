def rectangle(largeur,longueur):
    #fonction qui retourne l'aire d'un rectangle
    a=largeur*longueur
    return a



def affiche_rect(n):
    #fonction qui affiche un triangle rectangle  de longueur n
    for i in range(1,n+1):
        print("*"*i)

if __name__ == '__main__':
    affiche_rect(5) #appel de la fonction 
    res=rectangle(2,4)
    print(res)
