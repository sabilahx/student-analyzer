from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

def analyze_student(marks):
    avg = sum(marks) / len(marks)
    if avg > 75:
        return "Excellent"
    elif avg > 50:
        return "Average"
    else:
        return "Needs Improvement"

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()

    if not data or 'marks' not in data:
        return jsonify({"error": "Invalid input"}), 400

    marks = data['marks']

    if not isinstance(marks, list) or len(marks) == 0:
        return jsonify({"error": "Marks must be a non-empty list"}), 400

    try:
        marks = [int(m) for m in marks]
    except:
        return jsonify({"error": "Marks must be numbers"}), 400

    result = analyze_student(marks)

    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(debug=True)
