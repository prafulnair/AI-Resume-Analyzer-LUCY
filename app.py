from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from resume_parser import extract_text_from_pdf

app = Flask(__name__)

CORS(app)

parsed_data = {
    "resume_text": "",
    "jd_text": ""
}
@app.route('/upload', methods=['POST'])
def upload_files():
    print("Upload route hit")

    # DEBUG: print what we received
    print("form keys:", request.form.keys())
    print("files keys:", request.files.keys())

    resume_text = request.form.get('resume_text', '').strip()
    jd_text = request.form.get('job_desc_text', '').strip()
    resume_file = request.files.get('resume')
    jd_file = request.files.get('job_desc')

    print("resume_text:", resume_text)
    print("jd_text:", jd_text)
    print("resume_file:", resume_file)
    print("jd_file:", jd_file)

    # The same validation logic
    if not (resume_text or resume_file):
        return jsonify({'error': 'Either resume text or resume file is required.'}), 400
    if not (jd_text or jd_file):
        return jsonify({'error': 'Either job description text or JD file is required.'}), 400

    # Save files
    resume_path = jd_path = None
    if resume_file:
        resume_path = os.path.join('sample_docs','uploaded_resume.pdf')
        resume_file.save(resume_path)
    if jd_file:
        jd_path = os.path.join('sample_docs','uploaded_jd.pdf')
        jd_file.save(jd_path)

    # Parse PDFs
    if not resume_text and resume_path:
        resume_text = extract_text_from_pdf(resume_path)
    if not jd_text and jd_path:
        jd_text = extract_text_from_pdf(jd_path)

    parsed_data["resume_text"] = resume_text
    parsed_data["jd_text"] = jd_text

    return jsonify({'message': 'Files received successfully.'})

if __name__ == "__main__":
    app.run(debug=True)