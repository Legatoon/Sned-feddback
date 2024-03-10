#print = demander a l'ordinateur de m'ecrire ce qui se retrouvent dans la parenthese.
print('Veux tu jouer')

#Input permet a l'utilisateur d'ecrire dans le programme. Ca reponse va etre stocke dans la variable 'response/
response = input('Reponder pas Oui ou par Non ')

#If = si. On mets 'response.lower()' parce que sa transforme la reponse de l'utilisateur en minuscule-
# Donc si l'utilisateur mets 'OuI', l'ordianteur va transformer cela en 'oui'. j'ai mis == parce que je comapre la reponse
#pour voir si il sont equivalent. J'aurais seulement utilise = pour definir une variable. Sighifie que le prochain code
#sera lie a la condition 'if'
 if response.lower() == 'oui':
    print('Parfait nous allons commencer')
    #Si l'utilisateur ne repond pas oui, j'utilise la fonction else.
else:
    print('pas de problem.Aurevoir!')

#Je fais une variable qui dit combien de nombre je peux mettre
nombre_dessaie = 5

#J'ajoute une nouvelle variable 'numbers'. Je mets 'int' parce que l'utilisateur va mettre des nombres. Je met 'input' pour-
#que l'utilisateur puissent ecrire.Je mets le 'f' pour que la ligne de code sois plus lisibles et simple a ecrire. je-
#Mets le {i + 1} parce que au lieux de m'ecrire 'entrer le nombre 0', il va me dire 'entrer le nombre 1'. le 'for i in range-
#c'est pour dire que pour chaque nombre_d'essaie bah je fais +1.

nombres = [int(input(f"Entrez le nombre {i + 1}: ")) for i in range(nombre_dessaie)]

#def = mot qui introduit une fonction, Sommre_nombres_paires=Nom de ma fonction, lst = toutes cette fonction on la mets dans une liste
#Je rammene la variable nombre_dessaie
#For nombres in lst: pour chaque nombres dans la liste, si le nombre est divisible par 2 et il y a aucun reste
#nombre_dessaie += nombres == si le nombre est paires ajoute le
#return nombre_dessaie == envoie la somme des nombres paires
def somme_nombres_paires(lst):
    nombre_dessaie = 5
    for nombres in lst:
        if nombres % 2 == 0:
            nombre_dessaie += nombres
    return nombre_dessaie

#Je demande a l'ordi d'ecrire un message final puis de me donner la reponse finaL(somme_nomrbes)
print(f'La somme des nombres paire est: {somme_nombres_paires(nombres)}')


