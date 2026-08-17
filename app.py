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

@app.route("/usuarios", methods=["GET"])
def usuarios():
    return {
        "status": "ok",
        "data": {
            "total": 128,
            "ativos": 96,
            "inativos": 32
        }
    }

@app.route("/produtos", methods=["GET"])
def produtos():
    return {
        "status": "ok",
        "data": {
            "total": 45,
            "disponiveis": 38,
            "indisponiveis": 7
        }
    }

if __name__ == "__main__":
    app.run(debug=True)