#!/usr/bin/env python
# coding: utf-8

# In[ ]:


La fonction dico_reseau fonctionne en parcourant plusieurs fois le tableau des couples d'amis pour trouver les amis de chaque personne, tandis que la fonction create_network fonctionne en parcourant une seule fois le tableau des couples d'amis pour créer le réseau. La fonction create_network devrait donc être plus efficace en termes de temps d'exécution. Il serait cependant possible de mesurer l'efficacité des deux fonctions en comparant le temps d'exécution pour différentes entrées de tailles variables.


La complexité théorique des deux heuristiques est similaire. En effet, pour trouver une communauté maximale, il faut considérer toutes les personnes du réseau, et pour chacune d'entre elles, vérifier si elle est amie avec tous les membres de la communauté déjà créée.
La complexité de la fonction find_community_by_decreasing_popularity est donc de l'ordre de O(n^2) où n est le nombre de personnes dans le réseau, car pour chaque personne, il faut vérifier si elle est amie avec tous les membres de la communauté déjà créée.
La complexité de la fonction find_community_from_person est également de l'ordre de O(n^2) car pour chaque personne, il faut considérer tous ses amis pour vérifier s'ils peuvent être ajoutés à la communauté. Cependant, il faut ajouter la complexité de la recherche de la personne la plus populaire qui est de l'ordre de O(n)

Il est possible de mesurer expérimentalement les performances des deux fonctions en utilisant le module time de python pour mesurer le temps d'exécution de chaque fonction pour différentes tailles de réseau. On peut ensuite tracer les résultats obtenus pour visualiser les performances de chaque fonction.

