# projet sytème  
Nischal DHUNGANA  
Antoine CHARVIN

## MOTEUR DE RECHERCHE

### A PROPOS
Ce script va parcourir une arborescence de fichiers texte afin de rechercher les phrases correspondant aux mots clés entrés par l'utilisateurs dans
l'interface graphique.

### PRE REQUIS
installation customtkinter : pip install customtkinter  
installation pil : pip install pillow
installation scikit-learn : pip install -U scikit-learn
insatllation stanza : pip insatll stanza

### UTILISATION 
Il faut avoir une arborescence de fichiers texte dans le même répertoire que le script.
Le script va extraire tout les phrases des fichiers ainsi que les indexer. Il va ensuite garder uniquement les mots significatifs c'est-à-dire
les mots de plus de 4 lettres et ceux commençant par une majuscule.
Il retournera alors la ou les phrases correspondant ainsi que le numéro du fichiers auxquelles elles appartiennent.  

### CONSTRUCTION ET METHODES
Le coeur du programme se situe dans le fichier parse.py. Il contient les méthodes : 
#### PARSE
Cette méthode permet de séparer toutes les phrases que contiennent les documents. Cela génère un fichier .json afin de voir les phrases séparées.

#### INDEX
Cette méthode permet de d'indexer chaque phrases. Il retourne un dictionnaire avec les phrases et leurs index.

#### WORDINDEX
Cette méthode permet de généner une dictionnaire de mots significatifs suivant les phrases passée en argument. Les mots signifacitifs sont filtrés comme suit : une TF-IDF, les mots de moins de 4 lettres sont supprimer et nous gardons tout les mots commençant par une majuscule. Cela retourne un fichier .json avec les mots clés retenus.

#### LESSTHAN, STARTCAPITAL, TFIDF
Ces methodes perrmettent de mettre en place les filtres évoqués ci-dessus. La tfidf est réalisé à l'aide du package scikit-learn.

#### SEARCH
Cette méthode sera appelée par l'interface graphique afin de rechercher les matchs entre les mots clés de l'utilisateur avec les mots significtifs. Au final la méthode retourne la ou les phrases qui matchs avec le ou les mots clés ainsi que le documents dont appartient ces phrases. Grâce au package stanza il est possible à l'utilisateur de rentrer par exemple un verbe à l'infinitif et la methode va aussi chercher toutes les conjugaisons de ce verbe. Il en va de même pour pour les pluriels.  
Exemple :  
mots clés entrés : "manger"  
mots pouvant matcher avec "manger" : "mangeait", "manges", "mangeons, ... 

La partie visible du programme par l'utilisateur est le fichier gui.py. Il permet une utilisation plus commode qu'un terminal pour quelqu'un qui n'y est pas habitué. Plusieurs mots clés peuvent être entrés, ils seront séparés par un split afin de faire la recherche. Exemple :  
mots clés entrés : "légers brebis"  
mots clés retenu par le programme : "légers" "brebis"  


## AJOUT DEPUIS LA PRESENTATION SUR MACHINE DU MARDI 13 DECEMBRE
Ajout de la méthode "tfidf" dans le fichier parse.py afin de faire la tfidf sur les documents, grâce au package scikit-learn.  
Ajout de stanza pour gérer les cas des singuliers/pluriels ainsi que les conjugaison

