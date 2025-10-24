# Goban Technical Test - Java Version

This is the Java version of the Goban technical test. The goal is to implement the `is_taken` method in the `Goban.java` file.

## How to launch the project

To start and launch tests:

```bash
./gradlew build
./gradlew test
```

## Technical Test

The theme of this test is the game of go.

The goal is to write a function that determines whether the stone at an x, y position on a goban is taken or not.

### Vocabulary:
- **Goban**: the board on which stones are placed to play
- **Shape**: a group of one or more adjacent stones of the same color (adjacent: stones that are left, right, top, bottom of each other, diagonals do not count)
- **Liberty**: empty space adjacent to a shape

### Reminder of the rules:

1. The goban has an indefinite size
2. There are two players and everyone plays a stone color: black or white
3. The stones are laid one after the other each turn
4. When a form has no more freedom it is taken

The objective of the test is to write an `isTaken` function which takes in parameter x, y and which returns true if the stone with the position x, is taken there and false otherwise. To do this function we use a function `getStatus(x, y)` which returns:

- `Status.BLACK`: when the stone at position x, y is black
- `Status.WHITE`: when the stone at the x position, y is white
- `Status.EMPTY`: when there is no stone at position x, y
- `Status.OUT`: when the position x, y is out of the goban

Complete the `Goban.isTaken` method with your solution (you can add parameters to the method if needed). This one must respect the good practices of Java. You can test your solution at any time with `./gradlew test` (the tests are in the file `src/test/java/com/example/goban/GobanTest.java`).

### Examples:
```
# = black
o = white
. = empty


.#.
#o#    <= o is taken because she has no freedom, she has no adjacent empty space
.#.


...
#o#    <= o is not taken because she has a freedom over
.#.


o#    <= o is taken because she has no freedom (the top and the left are out of the goban so they are not freedoms)
#.


oo.
##o    <= the form # is taken because it has no freedom
o#o
.o.


oo.
##.   <= the form # is not taken because it has a freedom in x=2, y=1 (0, 0 on the top left)
o#o
.o.
```

---

# Test Technique Goban - Version Java

Ceci est la version Java du test technique Goban. L'objectif est d'implémenter la méthode `is_taken` dans le fichier `Goban.java`.

## Comment lancer le projet

Pour démarrer et lancer les tests :

```bash
./gradlew build
./gradlew test
```

## Test Technique

Le thème de ce test est le jeu de go.

Le but est d'écrire une fonction qui détermine si la pierre à une position x, y sur un goban est prise ou pas.

### Vocabulaire :
- **Goban** : le plateau sur lequel on place des pierres pour jouer
- **Forme** : un groupe d'une ou plusieurs pierres adjacentes de la même couleur (adjacentes : des pierres qui sont à gauche, droite, dessus, dessous l'une de l'autre, les diagonales ne comptent pas)
- **Liberté** : espace vide adjacent à une forme

### Rappel des règles :

1. Le goban a une taille indéfinie
2. Il y a deux joueurs et chacun joue une couleur de pierre : noir ou blanc
3. Les pierres sont posées les unes après les autres chacun son tour
4. Lorsqu'une forme n'a plus de liberté elle est prise

L'objectif du test est d'écrire une fonction `isTaken` qui prend en paramètre x, y et qui retourne vrai si la pierre à la position x, y est prise et faux sinon. Pour faire cette fonction on se base sur une fonction `getStatus(x, y)` qui retourne :

- `Status.BLACK` : quand la pierre à la position x, y est noire
- `Status.WHITE` : quand la pierre à la position x, y est blanche
- `Status.EMPTY` : quand il n'y a pas de pierre à la position x, y
- `Status.OUT` : quand la position x, y est hors du goban

Complétez la méthode `Goban.isTaken` avec votre solution (vous pouvez ajouter des paramètres à la méthode si besoin). Celle-ci doit respecter les bonnes pratiques de Java. Vous pouvez tester votre solution à tout moment avec `./gradlew test` (les tests sont dans le fichier `src/test/java/com/example/goban/GobanTest.java`).

### Exemples :
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