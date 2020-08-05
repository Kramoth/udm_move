# udm_move

Dans ce package se trouve deux noeuds:
- move_circle.py
- telop_pose.py

## move_circle

Ce noeud publie sur un topic un poseStamped, cette pose evolue suivant les equations d'un cercle.

## telop_pose

Ce noeud publie sur un topic un poseStamped et souscrit au topic cmd_vel, en fonction de ce qui est publie sur cmd_vel, la pose evoluera.

# Installation

Pour installer ce noeud il faut le cloner dans le dossier src de votre catkin workspace (catkin_ws)

```sh
cd catkin_ws/src
git clone https://github.com/Kramoth/udm_move.git
catkin build
cd ..
source devel/setup.bash
```
# Execution

Pour lancer les noeuds, il y a deux launch files:
- circle.launch
- teleop.launch

Dans un terminal, apres avoir sourcer devel/setup.bash

```sh
roslaunch udm_move move_circle.launch speed:=0.2 radius:=1
```
Modifier speed et radius afin de modifier le rayon du cercle et la vitesse du point

Dans un terminal, apres avoir sourcer devel/setup.bash

```sh
roslaunch udm_move move_teleop.launch
```
Dans le terminal suivre les indications (pour le straffing) afin d'observer le deplacement du point dans rviz