nom ="storm"

if len(nom) > 2:
    print(" longeur sup "+nom+" à 2")
else:
    print('longeur inferieur à 2')

def afficherLongeur(chaine):
    print('la longeur de la chaine '+  chaine +" est ", len(chaine))

afficherLongeur('Tiana')
afficherLongeur('Vecchia')
afficherLongeur("mamitiana")