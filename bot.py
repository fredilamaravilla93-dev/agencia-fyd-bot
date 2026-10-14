import os
from flask import Flask, request, jsonify
from supabase import create_client

app = Flask(__name__)

# Configuración de Supabase (aquí van tus credenciales)
SUPABASE_URL = "https://qhxycvhdyafcxjozfyhk.supabase.co/rest/v1/"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InFoeHljdmhkeWFmY3hqb3pmeWhrIiwicm9sZSI6ImFub24iLCJpYXQiOjE3OTE5MTU5NzYsImV4cCI6MjEwNzQ5MTk3Nn0.WCWLF0mYNzzzqB6v9g4o8QgbkMlSlQYfrxdKFJ8jIHM"

supabase = create_client(SUPABASE_URL.replace("/rest/v1/", ""), SUPABASE_KEY)

@app.route("/", methods=["GET"])
def inicio():
    return "¡El robot de Agencia FyD está encendido y funcionando correctamente!", 200

# Ruta para recibir los mensajes de WhatsApp (Webhook)
@app.route("/webhook", methods=["GET", "IFACE", "POST"])
def webhook():
    if request.method == "GET":
        # Verificación de WhatsApp
        VERIFY_TOKEN = "agencia_fyd_token_seguro"
        mode = request.args.get("hub.mode")
        token = request.args.get("hub.verify_token")
        challenge = request.args.get("hub.challenge")

        if mode and token:
            if mode == "subscribe" and token == VERIFY_TOKEN:
                return challenge, 200
            else:
                return "Error de verificación", 403
        return "Hola desde el webhook de WhatsApp", 200

    elif request.method == "POST":
        # Aquí recibiremos los mensajes e imágenes del cliente más adelante
        data = request.json
        print("Mensaje recibido de WhatsApp:", data)
        return jsonify({"status": "recibido"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)