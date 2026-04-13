from flask import Flask, request, jsonify, render_template

from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/analyze', methods=['POST'])
def analyze():
    try:
        data = request.get_json()

        if not data:
            return jsonify({"error": "No data received"}), 400

        marks = data.get("marks")

        if not marks or not isinstance(marks, list):
            return jsonify({"error": "Marks must be a list"}), 400

        # Convert safely
        marks = [int(m) for m in marks]

        avg = sum(marks) / len(marks)

        if avg > 75:
            result = "Excellent"
        elif avg > 50:
            result = "Average"
        else:
            result = "Needs Improvement"

        return jsonify({"result": result})

    except Exception as e:
        print("ERROR:", e)  # 🔥 important
        return jsonify({"error": "Server error"}), 500


if __name__ == "__main__":
    app.run(debug=True)
