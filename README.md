# Projet full stack E5


Ce projet à pour but de développer une application full stack en utilisant une base de donnée (postgresql), une api (fastapi) et un front (nginx) bien séparés, le tout initialisé et lancé depuis un docker compose.

## Notre projet :

Sur le site web, vous pourrez trouver un restaurant sur Paris. Vous pourrez donc faire une recherche par quartier, ou directement par le nom du restaurant si vous le connaissez. Lorsque vous faites une recherche, vous obtiendrez les informations du ou des restaurants qui correspondent à votre recherche, comme par exemple, le quartier, les coordonnées ou le type de restaurant. Si vous connaissez un restaurant qui n'est pas dans notre base de données il y a aussi la possibilité de le rajouter. 

Dans le futur nous voulons étendre notre projet à plus de ville et donc il sera possible de faire des recherches par ville ainsi que des recherches combinées par exemple par ville et par quartier en même temps pour ne sélectionner que les quartiers de la ville sélectionnée. Nous allons aussi rajouter un onglet qui permettra de montrer tous les restaurants présents dans la base de données ou/et un bouton permettant de sélectionner aléatoirement un restaurant pour ne pas avoir à prendre de décision et se laisser guider. Il pourrait aussi être utile de rajouter une fonction avis.

Lien vers la source de la base de données : https://opendata.paris.fr/explore/dataset/restaurants-casvp/table/?disjunctive.code&disjunctive.nom_restaurant&disjunctive.type

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

![alt text](https://github.com/JAndretti/Projet_full_stack_E5/blob/main/Resto/photos/accueil.png)

Nous vous invitons à naviguer à travers le site pour découvrire les fonctionalités citées précédement.


## Architechture du site : 

![alt text](https://github.com/JAndretti/Projet_full_stack_E5/blob/main/Resto/photos/sch%C3%A9ma.png)

## Axes d'amélioration : 

Lors de l'ajout d'un nouveau restaurant, nous rencontrons plusieurs soucis, le nom du restaurant n'est pas correctement enregistré et nous ne pouvons pas afficher le restaurant si nous le recherchons par nom alors qu'il apparait correctement si nous réalisons une recherche par quartier.



