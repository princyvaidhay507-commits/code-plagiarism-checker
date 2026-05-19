import difflib

from flask import Flask, render_template, request

from checker import calculate_similarity


app = Flask(__name__)


# 🔥 Difference Highlight Function
def highlight_diff(code1, code2):

    diff = difflib.ndiff(

        code1.splitlines(),
        code2.splitlines()

    )

    return "\n".join(diff)


# 🔥 HOME PAGE
@app.route("/", methods=["GET", "POST"])
def index():

    results = []

    # ====================================
    # MULTIPLE TEXT CODE COMPARISON
    # ====================================
    if request.method == "POST":

        codes = request.form.getlist("codes")

        # Remove empty boxes
        codes = [

            code for code in codes

            if code.strip() != ""
        ]

        # Compare all codes
        for i in range(len(codes)):

            for j in range(i + 1, len(codes)):

                similarity = calculate_similarity(

                    codes[i],
                    codes[j]

                )

                diff_result = highlight_diff(

                    codes[i],
                    codes[j]

                )

                results.append({

                    "name1": f"Code {i+1}",
                    "name2": f"Code {j+1}",
                    "similarity": similarity,
                    "diff": diff_result

                })

    return render_template(

        "index.html",
        results=results

    )


# 🔥 MULTIPLE FILE UPLOAD
@app.route("/upload", methods=["POST"])
def upload():

    uploaded_files = request.files.getlist("files")

    file_data = []

    results = []

    # Read files
    for file in uploaded_files:

        code = file.read().decode(

            "utf-8",
            errors="ignore"

        )

        file_data.append({

            "filename": file.filename,
            "code": code

        })

    # Compare files
    for i in range(len(file_data)):

        for j in range(i + 1, len(file_data)):

            similarity = calculate_similarity(

                file_data[i]["code"],
                file_data[j]["code"]

            )

            diff_result = highlight_diff(

                file_data[i]["code"],
                file_data[j]["code"]

            )

            results.append({

                "name1": file_data[i]["filename"],
                "name2": file_data[j]["filename"],
                "similarity": similarity,
                "diff": diff_result

            })

    return render_template(

        "index.html",
        results=results

    )


# 🔥 RUN APP
if __name__ == "__main__":

    app.run(

        debug=True,
        host="0.0.0.0",
        port=5000

    )