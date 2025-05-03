from flask import Flask, request, jsonify
from core.processor import Processor  # İşlemciyi içe aktar

app = Flask(__name__)

@app.route("/execute", methods=["POST"])
def execute():
    data = request.json
    command = data.get("command", "")
    processor = Processor()
    result = processor.execute(command)  # Komutu çalıştır
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)

class APIServer:
    def __init__(self):
        self.app = Flask(__name__)
        self.setup_routes()

    def setup_routes(self):
        @self.app.route('/')
        def home():
            return "RISC-V API Sunucusu Çalışıyor!"

    def start(self):
        self.app.run(debug=True)