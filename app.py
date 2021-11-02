from flask import *  
app = Flask(__name__)  
import os

UPLOAD_FOLDER = './images'

@app.route('/')  
def upload():  
    return render_template("file_upload_form.html")  

@app.route('/success', methods = ['POST'])  
def success():  
    if request.method == 'POST':  
        f = request.files['file']  
        path = os.path.join(UPLOAD_FOLDER, f.filename)
        f.save(path)
        return render_template("success.html", name = f.filename)  

@app.route('/getImages')  
def getImages():
    return send_file(
        'vcfb3.jpeg',
        as_attachment=True,
        attachment_filename=UPLOAD_FOLDER+'/vcfb3.jpeg',
        mimetype='image/jpeg'
    )


if __name__ == '__main__':  
    app.run(debug = True)