# Projet full stack E5


Ce projet à pour but de dévelloper une application full stack en utilisant une base de donnée (postgresql) une api (fastapi) et un front (ngnix) bien séparés, le tous initialisé et lancé depuis un docker compose.

## Notre projet :

Sur le site web vous pourrez trouver un restaurant sur paris. Vous pourrez donc faire ne recherche par quartier, ou directement par le nom du restaurant si vous le connaissez. Lorsque vous faites une recherche vous allez tomber sur les infos du ou des restaurants qui correspondent à votre recherche, comme par exemple, le quartier, les coordonnées, le type de restaurant. Si vous connaissez un restaurant qui n'est pas dans notre base de données il y a aussi la possibilité de le rajouter. 

Dans le futur nous voulons étendre notre projet à plus de ville et donc il sera possible de faire des recherches par ville ainsi que des recherches combinées par exemple par ville et par quartier en même temps pour ne sélectionner que les quartiers de la villes sélectionnées. Nous allons aussi rajouter un onglet qui permettra de montrer tous les restaurants présent dans la base de données ou/et un bouton permettant de sélectionner aléatoirement un restaurant pour ne pas à avoir de prendre de décision et de se laisser guider. Il pourrait aussi être utile de rajouter une fonction avis.

## Pour lancer le projet :

### Pré-requis
Il suffit simplement d'installer docker sur votre machine

### Initialisation
Tous d'abord clonez le repository : 

``git clone https://github.com/JAndretti/Projet_full_stack_E5.git``

Ensuite, dans un terminal placez vous dans le répertoire : ``Resto``

Et enfin lancez le projet : 

``docker compose up --build``

Rendez-vous à l'adresse : http://localhost:8000/


## Une fois que vous êtes à cette adresse vous devriez voir ceci :

#Insert photos

Nous vous invitons à naviguer à travers le site pour découvire toutes les fonctionalités citée précédement.


## Architechture du site : 

#Insert photos lucid chart

## Problème : 

Lors de l'ajout d'un nouvau restaurant, nous rencontrons plusieurs problèmes, le nom du restaurant n'est pas correctement enregistré et nous ne pouvons pas afficher le restaurant si on le recherche par nom alors que si on le recherche par quartier il apparait.



