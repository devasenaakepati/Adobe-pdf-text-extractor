
from flask import Flask, request, render_template, jsonify, send_file
import os
import time
import json
from processor.extractor import extract_sections
from processor.ranker import rank_sections

app = Flask(__name__)
UPLOAD_FOLDER = "uploaded_pdfs"
OUTPUT_PATH = "output.json"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET"])
def index():
    return render_template("upload.html")

@app.route("/process", methods=["POST"])
def process():
    persona = request.form.get("persona")
    job = request.form.get("job")
    files = request.files.getlist("pdfs")

    pdf_paths = []
    for f in files:
        path = os.path.join(UPLOAD_FOLDER, f.filename)
        f.save(path)
        pdf_paths.append(path)

    extracted = extract_sections(pdf_paths)
    ranked = rank_sections(extracted, persona, job)

    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    response = {
        "metadata": {
            "documents": [os.path.basename(p) for p in pdf_paths],
            "persona": persona,
            "job_to_be_done": job,
            "timestamp": timestamp
        },
        "sections": ranked
    }

    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(response, f, indent=2)

    result_json = json.dumps(response, indent=2)
    return render_template("result.html", result_json=result_json)

@app.route("/download", methods=["GET"])
def download():
    return send_file(OUTPUT_PATH, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
