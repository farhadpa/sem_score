from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import calculate_score

app = Flask(__name__)
cors = CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"


@app.route("/")
@cross_origin()
def calculate_student_engagement_score():
    try :
        # Get the values from the query string. If the values are not present or not convertable to float, set them to 0.
        total_lecture_attendance = request.args.get("lecture_attendance", 0, type=float)
        total_lab_attendance = request.args.get("lab_attendance", 0, type=float)
        total_support_attendance = request.args.get("support_attendance", 0, type=float)
        total_canvas_activity = request.args.get("canvas_activity", 0, type=float)

        # Call the calculate_engagement_score function from calculate_score.py
        result = calculate_score.calculate_engagement_score(
            total_attendance_lectures=total_lecture_attendance,
            total_attendance_lab=total_lab_attendance,
            total_attendance_support=total_support_attendance,
            total_canvas_activity=total_canvas_activity
        )
        # If the result starts with "Error:", return a 400 status code.
        if result.startswith("Error:"):
            return jsonify(result="Error: Invalid input. Please enter numeric values.", status=400)
        return jsonify(result=result, status=200)
    except Exception as e:
        return jsonify(result=str(e), status=500)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
