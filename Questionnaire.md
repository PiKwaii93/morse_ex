# Épreuve Dev. Mobile, durée 40h.

## Partie 1


### 1. Qu'est-ce qu'une application hybride et en quoi diffère-t-elle d'une application PWA ?

Les PWAs sont basées sur des technologies web et ne nécessitent pas d'installation depuis un store, on récupère le code directement via le navigateur ; tandis que les applications hybrides sont des applications natives contenant du code web (HTML, CSS, JavaScript) et doivent être téléchargées depuis un store.

### 2. Quelle différence faites-vous entre le DART et flutter ?

Dart est un langage de programmation tandis que Flutter est un framework qui utilise Dart pour développer des interfaces utilisateur.

### 3. Qu’est-ce qu’un logiciel libre ?

Un logiciel libre (ou Open source) est un logiciel qui donne aux utilisateurs la liberté d'exécuter, d'étudier, de modifier et de distribuer le code source. Les utilisateurs peuvent accéder et partager le logiciel sous certaines conditions.

### 4. Qu'appelle-t-on architecture client-serveur ?

L'architecture client-serveur est un modèle où les tâches sont réparties entre les serveurs (back) et les applications côtés clients (front). Ces derniers envoient des requêtes au serveur, qui les traite avant de les renvoyer au client le résultats.

### 5. Qu'appelle-t-on architecture Pub/Sub ?

L'architecture Pub/Sub est un modèle de communication où les éditeurs publient des messages dans un canal, et les abonnées doivent faire parti du canal pour recevoir les messages. Cette architecture découple les producteurs et les consommateurs, cela permets alors de choisir librement quelles informations on souhaite recevoir et ce instantanément.

### 6. Qu'est-ce qu’une requête REST et en quoi diffère-t-elle d'une websocket ?

REST est basé sur des requêtes HTTP, tandis que le WebSocket permet une connexion persistante et bidirectionnelle pour des communications en temps réel. On l'utilise notamment dans les systèmes de messageries entre plusieurs individus, cela donne alors une disponibilité permanente de la réception de nouveaux messages ; là où le premier devrait se rafraichir couramment pour vérifier la venue de nouveau message.  

### 7. Qu'est-ce qu’une application native ?

Une application native est développée spécifiquement pour un système d’exploitation : iOS ou Android. Elle est installée directement sur le téléphone via un store et peut fonctionner sans connexion Internet, selon son objectif.

### 8. Que désigne SwiftUI et Storyboard dans le développement iOS ?

Le premier est un framework où les interfaces sont directement programmer par la personne, tandis que le second se présente sous la forme d'un outil visuel pour les concevoir de manière graphique.

---
## Partie 2

1. **Dart (Flutter), Kotlin et Swift sont des langages de programmation libres et propriétaires.**  
   **Faux** : Ce sont des logiciels Open source

2. **Dans un projet Flutter, le fichier “pubspec.yaml” permet l’import d’assets statiques.**  
   **Vrai** 

3. **WebSocket est un framework permettant de créer facilement des chats et applications web.**  
   **Faux** : WebSocket est un protocole de communication, pas un framework. Il permet une connexion bidirectionnelle entre un client et un serveur.

4. **En développement mobile, l’opérateur “** ** **” permet une division du float par zéro.**  
   **Faux** : L'opérateur "**" n'existe pas pour la division et il est impossible de diviser par zéro.

5. **En Swift, pour faire le lien entre les éléments graphiques et le code, on utilise “findViewById”.**  
   **Faux** : En Swift, on utilise les outlets pour faire le lien entre les éléments graphiques et le code.

6. **En Flutter, “setOnClickListener” est une méthode qui s'exécute au click de l’élément auquel il est rattaché.**  
   **Faux** : En Flutter, on utilise "onPressed" ou d'autres propriétés similaires pour gérer les événements de clic

7. **La fonctionnalité d’installation automatique d’une application PWA depuis un navigateur est disponible sur l’ensemble des plateformes sans aucune restriction.**  
   **Faux** :  Il est compliqué d'en installer sur Safari (impossible de base).

8. **Break permet de sortir d’une boucle WHILE.**  
   **Vrai** 


---
## Partie 3

1. **Lesquels des éléments suivants sont des libertés de l’open source ?**  
   a. Utiliser  
   b. Modifier  
   d. Étudier  
   e. Copier

2. **Lesquels des éléments suivants sont des concepts de la programmation orientée objets ?**  
   a. Objet  
   b. Héritage  
   c. Encapsulation  
   d. Abstraction

3. **Les systèmes de versionning comme Git, SVN permettent :**  
   a. La gestion des versions  
   d. Une approche collaborative
   
4. **Lesquels des éléments suivants sont des opérateurs d'affectation ?**  
   a. /=  
   c. **=  
   d. -=

5. **Le framework “FLUTTER” permet :**  
   c. L’échange avec un objet connecté via Bluetooth Low Energy

6. **Lesquels des éléments suivants sont des types primitifs de Dart (Flutter) ?**  
   a. Numérique (int, double)  
   d. Chaîne de caractère (String)  
   e. Booléen (true/false)

7. **Parmi les concepts suivants, lesquels n'existent pas dans Swift ?**  
   a. Manifests  
   c. Gradle

---

### Partie 4 
#### Partie B 
#### main.py

    # Dictionnaire de traduction du code Morse

	MORSE_CODE_DICT  = {

	'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',

	'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',

	'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',

	'Y': '-.--', 'Z': '--..',

	'1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',

	'8': '---..', '9': '----.', '0': '-----',

	' ': ' / '

	}

	  

	def  text_to_morse(text):

	morse_code  = []

	for  char  in  text.upper():

	if  char  in  MORSE_CODE_DICT:

	morse_code.append(MORSE_CODE_DICT[char])

	else:

	morse_code.append('?') # Pour les caractères non reconnus

	return  ' '.join(morse_code)

	  

	text  =  'Hello EEMI'

	morse_translation  =  text_to_morse(text)

	print(morse_translation)

	  

	# Inverser le dictionnaire pour la traduction Morse -> Texte

	REVERSE_MORSE_CODE_DICT  = {value: key  for  key, value  in  MORSE_CODE_DICT.items()}

	  

	def  morse_to_text(morse_code):

	words  =  morse_code.split(' / ')

	text  = []

	for  word  in  words:

	letters  =  word.split(' ')

	decoded_word  =  ''.join(REVERSE_MORSE_CODE_DICT.get(letter, '?') for  letter  in  letters)

	text.append(decoded_word)

	return  ' '.join(text)

	  

	morse_code  =  '.... . .-.. .-.. --- / . . -- ..'

	text_translation  =  morse_to_text(morse_code)

	print(text_translation)


