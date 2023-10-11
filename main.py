from flask import Flask,render_template,request,send_from_directory
import requests
import os
import json
import logging
logging.basicConfig(filename='flask_app.log', level=logging.DEBUG)
app=Flask(__name__,static_folder='static')
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/get')
def get_bot():
    userText=str(request.args.get('msg'))
    data=json.dumps({"sender":"Rasa","message":userText})
    headers={'Content-Type': 'application/json','Accept': 'text/plain'}
    response=requests.post("http://localhost:5005/webhooks/rest/webhook",data=data,headers=headers)
    response=response.json()
    #return str(response[0]['text'])
    # Check if the response has an image key
    if 'image' in response:
        return send_from_directory(app.static_folder, response['image'])
    else:
        return str(response[0]['text'])


app.run(debug=True)