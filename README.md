# MACGYVER'S LABYRINTH

MacGyver's labyrinth is a little game coded in Python using object-oriented programmation in which the player must guide MacGyver to escape a Labyrinth. To achieve this he has to collect different object before confronting the guard which keeps the exit. This project is part of a learning path "Python applicaton developper" which you can find on [OpenClassrooms](https://openclassrooms.com/paths/developpeur-se-dapplication-python) web site.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine.

### Prerequisites

First you need to have Python 3 installed on your system. 

For this project I used Pipenv to create a virtual env that can be easily recreated on your environment. First you need to install Pipenv if you don't already have it :

```
pip install pipenv
```

Then you will have to download the source code of the project, unload it inside a folder and from this folder use the command :

```
pipenv install
```

which will automatically create a virtual environment with all the packages used for this project.

Finally to launch the game in the context of its virtual environment use the command :

```
pipenv run python Labyrinth.py
```

Run Labyrinth_text.py instead if you want console mode.

### How to play

Use arrow to move MacGyver's accross the labyrinth. pick up object by walking on them. If you have all 3 items when you meet the guard u complete the level. Press 'Esc' if you want to end the game at anytime.

## Packages used 

* [pygame](https://www.pygame.org/) - Free and Open Source python programming language library for making multimedia applications
