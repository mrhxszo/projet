# projet sytème

## MOTEUR DE RECHERCHE

### A PROPOS
Ce script va parcourir une arborescence de fichiers texte afin de rechercher les phrases correspondant aux mots clés entrés par l'utilisateurs dans
l'interface graphique.

### PRE REQUIS
installation customtkinter : pip install customtkinter
installation pil : pip install pillow

### UTILISATION 
Il faut avoir une arborescence de fichiers texte dans le même répertoire que le script.
Le script va extraire tout les phrases des fichiers ainsi que les indexer. Il va ensuite garder uniquement les mots significatifs c'est-à-dire
les mots de plus de 4 lettres et ceux commençant par une majuscule.
Il retournera alors la ou les phrases correspondant ainsi que le numéro du fichiers auxquelles elles appartiennent.
