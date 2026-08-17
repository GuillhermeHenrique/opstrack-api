from flask import Flask

app = Flask(__name__)

@app.route("/", methods=["GET"])
def inicio():
    return {
        "status": "ok",
        "message": "Aplicação Flask funcionando",
        "version": "1.0.0",
        "environment": "development",
        "data": {
            "id": 8472,
            "name": "OpsTrack",
            "active": True
        }
    }

if __name__ == "__main__":
    app.run(debug=True)