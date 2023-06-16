#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def create_network1(amis):
    """ 
      Cette fonction retourne un dictionnaire dont les clés 
      sont les prénoms des membres du réseau et les valeurs 
      le tableau de leurs amis.

    """
    reseau = {}
    for i in range(0, len(amis), 2):
        p1 = amis[i]
        p2 = amis[i+1]
        if p1 in reseau:
            reseau[p1].append(p2)
        else:
            network[p1] = [p2]
        if p2 in reseau:
            reseau[p2].append(p1)
        else:
            reseau[p2] = [p1]
    return reseau
    
def get_people(reseau):
     """ 
      Cette fonction retourne la liste
      des personnes de ce réseau dans un tableau.

    """
    return(list(reseau))
    
def are_friends(reseau,p1,p2):
    """ 
      Cette fonction retourne True si les deux
      personnes sont amies, et False sinon.

    """
    if not p2 in reseau[p1]:
        return False
    return True

def all_his_friends(reseau,p1,groupe):
    """ 
      Cette fonction prend en paramètre
      réseau, une personne et un groupe de
      personnes et retourne True si la 
      personne est amie avec toutes les personnes
      du groupe, et False sinon.

    """
    for i in groupe:
        if i not in reseau[p1]:
            return False
    return True
    
def is_a_community(network, groupe):
    """ 
      Cette fonction prend en paramètre 
      un dictionnaire modélisant le réseau 
      et un groupe de personnes (tableau de personnes) 
      et retourne True si ce groupe est une communauté,
      et False sinon.

    """
    for personne in groupe:
        if personne not in reseau:
            return False
    for personne in groupe:
        for ami in reseau[personne]:
            if ami not in groupe:
                return False
    return True

def find_community(reseau, groupe):
     """ 
      Cette fonction prend en paramètre un réseau
      et un groupe de personnes et retourne 
      une communauté 

    """
    com = []
    for personne in groupe:
        continu= True
        for ami in com:
            if personne not in reseau[ami]:
                continu = False
        if continu:
            com.append(personne)
    return com

def order_by_decreasing_popularity(reseau,groupe):
     """ 
      Cette fonction prend en paramètre
      un réseau et un groupe de personnes
      et trie le groupe de personnes selon
      la popularité (nombre d'amis) décroissante.

    """
    tab=[]
    i=0
    while i<len(groupe):
        tab.append(groupe[i])
        i+=1
    j=0
    while not len(reseau[tab[j]])<len(reseau[tab[j+1]]) and j<len(tab)-1:
        if len(reseau[tab[j]])<len(reseau[tab[j+1]]):
            tab[j],tab[j+1]=tab[j+1],tab[j]
        j+=1
    return tab
    
def find_community_from_person(d,p):
    com=[p]
    com+=find_community(d,(order_by_decreasing_popularity(d,d[p])))
    return com
    
def find_max_community(network):
    max= []
    for p in reseau:
        comm = find_community_from_person(reseau, p)
        if len(com) > len(max_com):
            max= com
    return max_community

