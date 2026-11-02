from flask import Flask, request, jsonify

app = Flask(__name__)

def calculate_attendance(attended, total):
    if total <= 0 or attended < 0:
        raise ValueError("Invalid values")
    return (attended / total) * 100

@app.route("/")
def home():
    return "Student Attendance System is running!"

@app.route("/attendance")
def attendance():
    try:
        attended = int(request.args.get("attended", 0))
        total    = int(request.args.get("total", 0))
        percent  = calculate_attendance(attended, total)
        return jsonify({"attended": attended, "total": total, "percentage": percent})
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
