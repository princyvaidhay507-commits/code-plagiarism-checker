import difflib


def highlight_diff(code1, code2):
    diff = difflib.ndiff(code1.splitlines(), code2.splitlines())
    return "\n".join(diff)


from flask import Flask, render_template, request
from checker import calculate_similarity

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    similarity = None

    if request.method == "POST":
        code1 = request.form["code1"]
        code2 = request.form["code2"]
        similarity = calculate_similarity(code1, code2)

    return render_template("index.html", similarity=similarity)


# 🔥 NEW FEATURE: FILE UPLOAD
@app.route("/upload", methods=["POST"])
def upload():
    file1 = request.files["file1"]
    file2 = request.files["file2"]

    code1 = file1.read().decode("utf-8")
    code2 = file2.read().decode("utf-8")

    similarity = calculate_similarity(code1, code2)

    return render_template("index.html", similarity=similarity)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)