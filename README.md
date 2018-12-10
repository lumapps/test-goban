# Comment lancer le projet

Pour commencer et lancer les tests : 

```
$ git clone https://github.com/lumapps/test-goban.git
$ cd test-goban
$ virtualenv env
$ source env/bin/activate
$ pip install -r requirements.txt
$ pytest .
```

# Test technique

Le thème de ce test est le jeu de go.

Le but est d'écrire une fonction qui détermine si la pierre à une position x, y sur un goban est prise ou pas.

Vocabulaire :

* Goban : le plateau sur lequel on place des pierres pour jouer
* Forme : un groupe d'une ou plusieurs pierres adjacente de la même couleur (adjacente : des pierres qui sont à gauche, droite, dessus, dessous l'une de l'autre, les diagonales ne comptent pas)
* Liberté : espace vide adjacent à une forme

Rappel des règles :

1. Le goban a une taille indéfinie
2. Il y a deux joueurs et chacun joue une couleur de pierre : noir ou blanc
3. Les pierres sont posées les unes après les autres chacun son tour
5. Lorsqu'une forme n'a plus de liberté elle est prise

L'objectif du test est d'écrire une fonction `is_taken` qui prend en paramètre x, y et qui retourne vrai si la pierre à la position x, y est prise et faux sinon.
Pour faire cette fonction on se base sur une fonction `get_status(x, y)` qui retourne :

* Status.BLACK : quand la pierre à la position x, y est noire
* Status.WHITE : quand la pierre à la position x, y est blanche
* Status.EMPTY : quand il n'y a pas de pierre à la position x, y
* Status.OUT : quand la position x, y est hors du goban


Complétez la méthode `Goban.is_taken` avec votre solution (vous pouvez ajouter des paramètres à la méthode si besoin). Celle-ci doit respecter les bonnes pratiques du Python.
Vous pouvez tester votre solution à tout moment avec `py.test` (les tests sont dans le fichier test_goban.py).

Exemples :

```
# = noir
o = blanc
. = vide


.#.
#o#    <= o est prise parce qu'elle n'a pas de liberté, elle n'a aucun espace vide adjacent
.#.


...
#o#    <= o n'est pas prise parce qu'elle a une liberté au dessus
.#.


o#    <= o est prise parce qu'elle n'a pas de liberté (le haut et la gauche sont hors du goban donc ce ne sont pas des libertés)
#.


oo.
##o    <= la forme # est prise parce qu'elle n'a pas de liberté
o#o
.o.


oo.
##.   <= la forme # n'est pas prise parce qu'elle a une liberté en x=2, y=1 (0, 0 en haut à gauche)
o#o
.o.
```
