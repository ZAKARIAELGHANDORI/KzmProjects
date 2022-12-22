#! /bin/bash

touch /home/zakaria2001/Bureau/MyProjects/KzmProjects/fichier_`date +%M`.txt


## on crée un fichier sous le nom fichier_minutes comme ca on va avoir un nom qui se change a chaque lancement de cron

###
#pour lancer la création d'un fichier chaque -6heures on utilise la commande :
#* */6 * * * path/to/script2.sh
###
