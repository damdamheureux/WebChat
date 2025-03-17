Les websockets doivent suivre le format suivant:

1.0 Charset = UTF-8
2.0 Format JSON
2.1. Le contenu du message doit suivre la forme: 
```json
{Type: [INFO | SYSTEM | WARN | ERROR | PRIVATE | CHANNEL | BROADCAST], Author: ["SYSTEM" | STRING], Data: {...}}
```
2.2. Lors d'un envoi de message, le champ Data doit être: {message: "", room_id: "", timestamp: os.time()}

