# 🚀 EvoCelestial - Backend 💻

## 📝 Description

EvoCelestial est une application de 💬 chat permettant aux 👥 utilisateurs de communiquer en temps réel. Ce projet utilise un backend en 🐍 Python et est conçu pour fonctionner avec 🐳 Docker. (On aime les emojis 😊)

## ⚙️ Installation

### 📌 Prérequis

- 🐍 Python 3.11 (3.13 préféré)
- 🐳 Docker

### 🛠️ Étapes d'installation

1. **📥 Cloner les dépôts**
   ```sh
   git clone https://github.com/EvoCelestial/backend
   git clone https://github.com/EvoCelestial/FrontEnd
   ```
2. **🔧 Créer l'image Docker et la lancer 🐋**
   ```sh
   cd backend
   docker image -t backend:latest .
   docker run -d \
   ```
   ```sh
     --name backend_container \
     -e DB_HOST=82.65.174.2 \
     -e DB_NAME=default \
     -e DB_PASSWORD=xj9Yvh7vvDCx7O9vHBa9Gihxl0nBNzuDRkOODxz8P2H9DFxBqxJs5RGQnPamnbYN \
     -e DB_PORT=15800 \
     -e DB_USER=root \
     -e PRIVATE_fastapi_token=Pa$$wd \
     -p 8000:8000 \
     backend:latest
   ```

   ```sh
      cd frontend
      docker image -t frontend:latest .
      docker run -d \
      --name frontend_coontainer \
      -e API_URL=localhost:8000 \
      -p 40120:40120 \
       frontend:latest
   ```
   **Sans docker**
   ```sh
      cd backend
      pip3 install -r requirements.txt
      touch .env
      nano .env
      fastapi dev main.py
   ```

   ```sh
      cd frontend
      pip3 install -r requirements.txt
      touch .env
      nano .env
      python3 main.py
   ```
⚠️ Penser à bien mettre les bonnes valeurs dans les variables d'environnement.

3. **⚙️ Configurer l'application**
   - 📄 Copier le fichier `.env.exemple` en `.env` et ajuster les ⚙️ variables selon votre environnement.



## 🛠️ Technologies utilisées

- 🐍 Python (Flask et FastAPI)
- 🌐 WebSockets pour la communication en temps réel
- 💻 Base de donnée MySQL
- 🐳 Docker pour la 📦 conteneurisation
