from flask import Flask,render_template,request
from cartoon import display
from werkzeug.utils import secure_filename
app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/uploader',methods=['POST','GET'])
def getValue():
    if request.method=='POST' :
        f = request.files['infile']
        f.save(secure_filename(f.filename))
        print('filename',f.filename)
        display(f)
        return render_template("index1.html")
    
    
if __name__ == "__main__":
    app.run(debug=True)