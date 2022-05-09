from urllib import response
from flask import Flask,request,jsonify
import util

app = Flask(__name__)

@app.route('/classify_image',methods = ['GET','POST'])
def classify_image():
    image_data =request.form['image_data']
#   print('Image data:',image_data)
    response =jsonify(util.classify_image(image_data))
   # print(response)
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

    

if __name__ == "__main__":
    print('Starting Python Flask Server for Sports Celebrity Image Classification')
    util.load_saved_artifacts()
    app.run(debug=True,port =5000)