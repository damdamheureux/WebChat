# 🚀 EvoCelestial - Backend 💻

## 📝 Description

EvoCelestial est une application de 💬 chat permettant aux 👥 utilisateurs de communiquer en temps réel. Ce projet utilise un backend en 🐍 Python et est conçu pour fonctionner avec 🐳 Docker. (On aime les emojis 😊)

## ⚙️ Installation

### 📌 Prérequis

- 🐍 Python 3.11 (3.13 préféré)
- 🐳 Docker

### 🛠️ Étapes d'installation

#### 1. 📥 Cloner les dépôts
```sh
git clone https://github.com/EvoCelestial/backend
git clone https://github.com/EvoCelestial/FrontEnd
```

#### 2. 🔧 Construire et exécuter le backend 🐋
Assurez-vous d'être dans le dossier `backend` :
```sh
cd backend
```
Construire l'image Docker du backend :
```sh
docker build -t backend:latest .
```
Exécuter le conteneur avec les variables d'environnement :
```sh
docker run -d \
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

#### 3. 🔧 Construire et exécuter le frontend 🐋
Naviguez dans le dossier `frontend` :
```sh
cd ../frontend
```
Construire l'image Docker du frontend :
```sh
docker build -t frontend:latest .
```
Exécuter le conteneur :
```sh
docker run -d \
  --name frontend_container \
  -e API_URL=http://localhost:8000 \
  -p 40120:40120 \
  frontend:latest
```

#### 4. ⚡ Exécution sans Docker
Si vous souhaitez exécuter le projet sans Docker, suivez ces étapes :

**Backend :**
```sh
cd backend
pip3 install -r requirements.txt
touch .env
nano .env
fastapi dev main.py
```

**Frontend :**
```sh
cd frontend
pip3 install -r requirements.txt
touch .env
nano .env
python3 main.py
```
⚠️ Pensez à bien configurer les variables d'environnement.

#### 5. ⚙️ Configurer l'application
- 📄 Copier le fichier `.env.exemple` en `.env` et ajuster les ⚙️ variables selon votre environnement.

#### 6. ✅ Vérification
- Vérifiez que les conteneurs tournent :
  ```sh
  docker ps
  ```
- Accédez à l'API backend sur [http://localhost:8000](http://localhost:8000)
- Accédez à l'interface frontend sur [http://localhost:40120](http://localhost:40120)

#### 7. 🛑 Arrêter et nettoyer les conteneurs
Si vous souhaitez arrêter et supprimer les conteneurs, exécutez :
```sh
docker stop backend_container frontend_container
docker rm backend_container frontend_container
```

Si vous souhaitez également supprimer les images Docker :
```sh
docker rmi backend:latest frontend:latest
```

## 🛠️ Technologies utilisées

- 🐍 Python (FastAPI)
- 🌐 WebSockets pour la communication en temps réel
- 💻 Base de données MySQL
- 🐳 Docker pour la 📦 conteneurisation

