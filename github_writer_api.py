import os
import requests
import json
import base64
from flask import Flask, request, jsonify

app = Flask(__name__)

# --- ⚠️ REMPLACEZ CES VALEURS ---

# 1. ⚠️ À REMPLACER: Jeton secret de communication (DOIT ÊTRE IDENTIQUE à celui du script Bot)
API_SECRET_TOKEN = "UN_JETON_SECRET_FORT_QUE_VOUS_DEFINISSEZ" 

# 2. ⚠️ À REMPLACER: Votre nom d'utilisateur GitHub
REPO_OWNER = "Elyseproduction" 
# 3. ⚠️ À REMPLACER: Le nom de votre dépôt (celui de l'application : bot-telegram_codes-uniques)
REPO_NAME = "bot-telegram_codes-uniques" 
# 4. ⚠️ À REMPLACER: Le jeton obtenu à l'ÉTAPE 1 (Jeton d'Accès Personnel GitHub PAT)
GITHUB_TOKEN = "votre_jeton_github_personnel_copie_de_letape_1"

BRANCH_NAME = "main" 
# Fichier cible (doit correspondre à l'application elyse_app.py)
FILE_PATH = "license_codes.txt" 
# ---------------------------------
@app.route('/register_key', methods=['POST'])
def register_key():
    """Endpoint pour recevoir la clé du bot et l'ajouter au fichier GitHub."""
    data = request.json
    
    # 1. Vérification du jeton secret
    if data.get('secret_token') != API_SECRET_TOKEN:
        return jsonify({"status": "error", "message": "Jeton secret non valide"}), 403

    new_key = data.get('key')
    
    # 2. Récupérer le contenu actuel du fichier (avec le GITHUB_TOKEN)
    # ... (Logique de requête GET à l'API GitHub pour obtenir le SHA et le contenu) ...
    
    # 3. Ajouter la nouvelle clé et encoder en Base64
    # ... (Logique d'ajout et d'encodage) ...

    # 4. Mettre à jour le fichier (Requête PUT à l'API GitHub)
    # ... (Logique d'envoi du Commit) ...
    
    return jsonify({"status": "success", "message": "Clé ajoutée avec succès à license_codes.txt"}), 200

# ... (Le reste du code pour lancer l'application Flask) ...
