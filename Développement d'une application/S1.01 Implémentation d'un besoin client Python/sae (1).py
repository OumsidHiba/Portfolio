#!/usr/bin/env python
# coding: utf-8

# # <center> Etude de communautés dans un réseau social</center>
# <center> SAE 1.01 / 2022 - 23 </center>
# 
# 

# Cette SAE est à faire en **binôme**.
# 
# **Calendrier**
# - Un contrôle de 2h en lien avec le contenu de cette SAE aura lieu le mercredi **26 octobre** 2022.
# - Le projet est à rendre le vendredi **28 octobre** 2022. Les modalités de rendu vous seront précisées par votre enseignant.
# 
# **Evaluation**
# - Le projet comptera pour 40% de la note de SAE 1.01. <BR>
#     Il sera particulièrement tenu compte de la qualité du code, des **commentaires** et **docstrings**, des fonctions de **tests unitaires** pour les fonctions renvoyant des résultats. <BR><BR>
#     
# - Le contrôle compte pour 60% de la note finale.

# ## <center> Sujet </center>
# 
# Une *communauté* est un ensemble de personnes développant des interactions dans un réseau social.
# 
# Dans ce projet, on étudie des communautés modélisées sous différentes formes. Pour cela, on développe des fonctions permettant d'extraire des informations relatives à ces réseaux. 

# On modélise, dans un premier temps, les interactions entre personnes dans un tableau `amis` de chaînes de caractères contenant les prénoms des membres du réseau et tel que `amis[2*i]` a des interactions avec `amis[2*i+1]`.
# 
# On suppose que chaque interaction n'est décrite qu'une seule fois dans le tableau, et qu'une personne n'a pas d'interaction avec elle-même.
# 
# **Exemple** : 

# In[2]:


amis = ["Alice", "Bob", "Alice", "Charlie", "Bob", "Denis"]


# Ici, 
# - Alice a des interactions Bob et Charlie, 
# - Bob a des intractions avec Alice et Denis,
# - Charlie a des interactions avec Alice et
# - Denis a des interactions avec Bob.

# #### Question préliminaire : Modélisation d'un réseau par un tableau
# 
# Muriel, Yasmine et Joël sont amis. Yasmine est amie avec Thomas. 
# Joël, Nassim, Andrea et Ali sont amis. Thomas est ami de Daria et Carole. Thierry, Axel et Léo sont amis. Léo est ami de Valentin qui est ami d'Andrea.
# 
# - Construire un tableau `p_amis` qui modélise ce réseau d'amitié en selon le principe qui vient d'être décrit.

# In[43]:


amis=["Thomas","Yasmine", "Muriel" , "Joel", "Nassim","Andrea", "Joel", "Ali", "Nassim", "Ali", "Andrea", "Valentin",
   "Leo",  "Axel","Thierry","Leo","Valentin", "Andrea",  "Joel", "Yasmine", "Thomas", "Daria", "Thomas",
   "Carole","Daria"]




# #### Question 1 : Nombre d'amis d'une personne
# 
# - Étant donné un tableau `amis`, écrire une fonction `nb_amis(amis, prenom)` qui retourne le nombre d'amis de `prenom` à partir des données du tableau `amis`. 

# In[21]:




def nb_amis(amis,prenom):
    
    """ 
     cette fonction permet le calcule du nombre d'amis
     du prenom mis en paramétre de la fonction
     
    """

    i=1
    nombre=0
    tab=[]
    a=len(p_amis)
    while i < a:
        
        if i!=a-1:
            if p_amis[i]==prenom:
                    if p_amis[i-1]!=prenom and not p_amis[i-1] in tab:
                     
                        tab.append(p_amis[i-1])
                    if p_amis[i+1]!=prenom and p_amis[i+1]!= p_amis[i-1] and not p_amis[i+1] in tab:
                     
                        tab.append(p_amis[i+1])
                        
        else:
            if p_amis[i]==prenom:
                p_amis[i-1]!=prenom
              
                tab.append(p_amis[i-1])
        i+=1  
    return len(tab)




def test_nb_amis():
    
    """
    cette fonction est une fonction test qui va controler si
    vraiment le prénom à exactement le même nombre d'amis indiqué par la fonction ci dessus 
    """
    assert  nb_amis(p_amis,"Valentin")==2
    assert  nb_amis(p_amis,"Leo")==3
    assert  nb_amis(p_amis,"Muriel")==2
    assert not nb_amis(p_amis, "Joel") == 3
    print("===fonction ok===")
    
test_nb_amis()
nb_amis(p_amis,"Yasmine")



# #### Question 2 : Nombre de membres d'un réseau social 
# 
# - Ecrire une fonction `taille_reseau(amis)` qui à partir d'un tableau `amis`retourne le nombre de personnes distinctes participant à ce réseau social.

# In[31]:



def taille_reseau(amis): 
     """
     cette fonction retourne le nombre de personne 
     distinct sur le tableau amis.   
     """
    s = []
    for g in amis:
        if not g in s:
            s.append(g)
    return len(s)

taille_reseau(p)

def test_amis():
    
    """cette fonction pérmet de verifier si vraiment le nombre indiqué est 
       le nombre de prénoms distincts dans le tableau
    """
    assert taille_reseau(amis) == 5
    assert not taille_reseau(p) == 2
    assert taille_reseau(p) == 13
    assert taille_reseau(["lola","muriel","bob","lola","ali"])
    print("===ok===")
test_amis()


# #### Question 3 :  Lecture des données d'un réseau à partir d'un fichier
# On suppose que les données sur un réseau social sont stockées dans un fichier CSV de la manière suivante :
# ```
# prenom1;prenom2
# prenom3;prenom4
# prenom5;prenom6
# ...
# ```
# Autrement dit, chaque ligne du fichier contient une paire de prénoms séparés par un `';'` correspondant à deux personnes ayant des interactions. 
# 
# **NB** : Quatre fichiers CSV de ce type sont fournis dans le répertoire `files/`, il s'agit des fichiers`Communaute1.csv`, `Communaute2.csv`,`Communaute3.csv` et `Communaute4.csv`. 
# Il est recommandé d'en fabriquer d'autres. 
# 
# - Ecrire une fonction `lecture_reseau(path)` prenant en paramètre un chemin vers un tel fichier CSV et retournant un tableau modélisant les interactions entre les personnes du fichier.

# In[37]:



from json import *
path = "C:/Users/Hiba/Disktop/python/Communaute1.csv" 
def lecture_reseau(path):
    
    """cette fonction lit le fichier Communaute3.csv
       et retourne un tableu où il indique les interactions 
       entre les personnes du fichier.
    """
    tab=[]
    f=open(path, encoding="utf-8", mode="r")
    a=True
    while a :
        a=f.readline()
        tab.append(a.strip())
    f.close()
      return tab
lecture_reseau(path)

def test_lecture():
    """ Cette fonction vérifie si la sortie de la
    fonction lecture_reseu est bien ce qui est dans le fichier
    """
    assert load(f) == lecture_reseau(path)

    print("===ok===")


  


# #### Question 4 : Modélisation d'un réseau par un dictionnaire
# On préfère pour la suite, utiliser une modélisation du réseau social par un dictionnaire dont où les clés sont les prénoms des personnes du réseau et la valeur associé à une clé est le tableau des amis de la personne indiquée par la clé.
# 
# - A partir d'un tableau `amis` modélisant les interactions entre personnes d'un réseau, écrire une fonction `dico_reseau(amis)` qui retourne un dictionnaire dont les clés sont les prénoms des membres du réseau et les valeurs le tableau de leurs amis.

# In[40]:


def dico(amis):
    """ 
       cette fonction permet de retourner un dictionnaire où
       les clés sont les prénoms du tableau amis et les valeurs
       sont sous forme d'un tableau qui représente les amis des clés
       """
    i=1
    
    dico={}
    nombre=0
    a=len(amis)
    while i < a:
        tab = []
        if i!=a-1:
            
            
            if amis[i+1]!=amis[i] and amis[i-1]!= amis[i]:
                    tab.append(amis[i+1]),tab.append(amis[i-1])
                    dico[amis[i]]=tab
            if amis[i+1] == amis[i-1]:
                
                tab.append(amis[i-1])
            
        else:
            if amis[i]!=amis[i-1]:
                tab.append(amis[i-1])
                dico[amis[i]]=tab
        i+=1
        
    return dico


dico(amis)

def test_dico():
    
    """cette fonction va verifier si la fonction a vraiment retourner 
    un dictionnaire où les clés sont les prenoms  et les valeurs sont
    les tableau des amis du prenom
    """
    assert dico['Yasmine'] == ["Thomas", "joel", "Muriel"]
    assert not len(dico["Muriel"]) == 2
    assert dico["Valentin"] == ["Andre","Leo"]
    print("===OK===")

    
test_dico()
    


# #### Question 5 : Nombre d'amis des personnes les plus populaires
# 
# - A partir d'un dictionnaire `dico_reseau` modélisant les interactions dans un réseau d'amis, écrire une fonction `nb_amis_plus_pop (dico_reseau)` qui retourne le nombre d'amis des personnes les plus populaires du réseau.

# In[42]:




def nb_amis_pop(dico):
    
    """cette fonction permet de parcourir le dictionnaire 
       de la fonction precedante et retourne le plus grand 
       nombres d'amis des tableu càd: le nombre d'amis des
       personnes populaires
      
    """
    maxi = 0
    for i in dico:
        if len(dico[i])>maxi:
            maxi = len(dico[i])
    return maxi
nb_amis_pop(dico)


def test_nb_pop():
    """" 
        cette fonction s'assure que le nobres des personnes 
        populaires est exactemnt celle fournit par a fonction
        nb_amis_pop 
    """
    assert nb_amis_pop(amis) == 5
    assert not nb_amis_pop(amis) == 2
    print("===OK===")






# #### Question 6 : Personnes les plus populaires
# 
# - A partir d'un dictionnaire `dico_reseau` modélisant les interactions dans un réseau d'amis, écrire une fonction `les_plus_pop (dico_reseau)` qui retourne un tableau contenant les prénoms de toutes les personnes les plus populaires du réseau.

# In[ ]:


def les_plus_pop(dico_reseau):
    """ 
    cette fonction retourne
    untableau contenant les 
    amis des personnes populaires 
    """
    max = nb_amis_pop(dico_reseau)
    tab = []
    for i in dico_reseau:
        if len(dico_reseau[i])>= max:
            tab.append(i)
    return ",".join(tab)
les_plus_pop(dico_reseau)


def test_les_plus_pop():
    """"
    cette fonction si le tableau emit par 
    la fonction précédantee est bien
    """
    assert les_plus_pop(dico_reseau) ==["Muriel","Thomas","Daria","Charol","Nassim","Andrea","Ali"]
    assert not les_plus_pop(dico_reseau) == ["joel","Yasmine"]
    print("===OK===")




