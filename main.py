from controller.adviceController import get_advice
from flask import Flask, jsonify
 
app = Flask(__name__)

@app.route('/advices', methods=['GET'])
def advices():
    advice = get_advice()
    if advice:
        return jsonify({"ID": advice.phrase_id, "Advice": advice.phrase_advice})
    else:
        return jsonify({"error": "request falied"})

if __name__ == "__main__":
    app.run(debug=True)