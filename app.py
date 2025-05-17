from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)

CORS(app)

parsed_data = {
    "resume_text": "",
    "jd_text": ""
}

@app.route('/upload', methods=['POST'])
def upload_files():
    resume_file = request.files.get('resume')
    jd_file = request.files.get('job_desc')

    if not resume_file or not jd_file:
        return jsonify({'error':'both resume and job descriptions are required'})
    
    resume_path = os.path.join('sample_docs','uploaded_resume.pdf')
    jd_path = os.path.join('sample_docs','uploaded_jd.pdf')


    resume_file.save(resume_path)
    jd_file.save(jd_path)

    return jsonify({'message': 'Files received successfully.'})


if __name__ == "__main__":
    app.run(debug=True)