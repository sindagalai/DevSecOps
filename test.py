# test.py - Exemples de mauvaises pratiques pour Bandit et Semgrep

import subprocess

# ❌ Mauvaise pratique #1 : utilisation de shell=True (risque d'injection de commande)
# Bandit va lever B602 (subprocess with shell=True)
subprocess.Popen("ls -la /tmp", shell=True)

# ❌ Mauvaise pratique #2 : secret codé en dur (API key)
# Semgrep / SonarLint vont détecter la présence d'un secret hardcoded
API_KEY = "SAMPLE-SECRET-12345"
print("Using API_KEY:", API_KEY)

# ❌ Mauvaise pratique #3 : exécution dynamique de code (danger si input non contrôlé)
# Semgrep ou SonarLint peuvent signaler l'usage d'exec/eval en Python
user_input = "print('hello')"
exec(user_input)

# ❌ Exemple de secret codé en dur (pour test)
AWS_SECRET_KEY = "AKIA1234567890EXEMPLECLE"

# test.py - Version corrigée (code sécurisé)

#import subprocess
#import os

# ✅ Bonne pratique : pas de shell=True (évite l’injection de commande)
#subprocess.run(["ls", "-la", "/tmp"], check=True)

# ✅ Bonne pratique : lire la clé API depuis une variable d'environnement
#API_KEY = os.getenv("API_KEY", "clé non fournie")
#print("Clé API utilisée (masquée) :", "*" * len(API_KEY))

# ✅ Bonne pratique : ne pas exécuter de code non contrôlé
#user_input = "hello"
#print("Entrée utilisateur :", user_input)

