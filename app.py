import pandas as pd
from flask import Flask, jsonify, request
import pickle
import keras
from keras.preprocessing import sequence

# load models
model = pickle.load(open('model.pkl','rb'))
app = Flask(__name__)

@app.route("/dgaCheck",methods=['GET'])
def app():
    domain=request.args['domain']
    X = {'j', '8', 'n', '-', 'm', 't', 'q', 'a', '7', 'p', 'x', 'f', 'w', 'k', '6', '1', 'c', '9', 'r', '2', 'h', '3', '4', 'g', 'y', 'b', 'u', 'e', 'l', '5', 'v', 'z', 'i', 'o', '0', 'd', 's'}
    valid_chars = {x:idx+1 for idx, x in enumerate(X)}
    print("Domain name:",domain)
    print(valid_chars)
    g = [[valid_chars[y] for y in domain]]
    g = sequence.pad_sequences(g, maxlen=31)
    # make predictions
    print(g)
    proba = model.predict_proba(g[0:1])
    p = int(proba[0]*100)
    final=''
    if proba[0]>=0.5:
      print("DGA:",p ,"%")
      #blacklist = open("/content/drive/My Drive/file/blacklist.txt","a")
      #blacklist.write(domain)
      #blacklist.write(",")
      final='DGA : Caution!!!'
    else:
      print("Good:",100-p ,"%")
      #whitelist = open("/content/drive/My Drive/file/whitelist.txt","a")
      #whitelist.write(domain)
      #whitelist.write(",")
      final='Non DGA : Safe!!!'
    return {'message': final}
    
@app.route('/',methods=['GET'])
def index():
    return "<h1>The Cloud based Realtime DGA Detection Engine is Deployed.</h1>"
    
if __name__ == "__main__":
    app.run(debug=False,threaded=False)