from flask import Flask, render_template, request
import os
from parser import parse_resume
from werkzeug.utils import secure_filename

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# ✅ Ensure uploads folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


@app.route("/", methods=["GET", "POST"])
def index():
    data = None
    error = None

    if request.method == "POST":
        if "resume" not in request.files:
            error = "No file uploaded"
            return render_template("index.html", data=data, error=error)

        file = request.files["resume"]

        if file.filename == "":
            error = "No file selected"
            return render_template("index.html", data=data, error=error)

        # ✅ Allow only PDF files
        if not file.filename.lower().endswith(".pdf"):
            error = "Only PDF files are allowed"
            return render_template("index.html", data=data, error=error)

        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
        file.save(filepath)

        try:
            data = parse_resume(filepath)
        except Exception as e:
            error = f"Error parsing resume: {str(e)}"

    return render_template("index.html", data=data, error=error)


if __name__ == "__main__":
    app.run(debug=True)