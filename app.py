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
    data = request.json
    marks = data['marks']
    result = analyze_student(marks)
    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)