import flask
from flask import request, jsonify, redirect
from flask import Flask,render_template,url_for,flash
from forms import SentimentForm,ResultForm
import pickle
import nltk
from nltk.tokenize import word_tokenize
#nltk.download("punkt")
filename = 'word_features_final.txt'
with open(filename,'rb') as fp:
  featureset = pickle.load(fp)
with open("SentiAnalysisfinal.sav",'rb') as fp:
  loaded_model = pickle.load(fp)


risk_words = {
    'not good' : 'bad',
    'not bad' : 'good',
    'not nice' : 'bad',
    'hate' : 'bad'
}

def find_features(word_features,document):
    document = document.lower()
    words = word_tokenize(document)
    document_words = set(words)
    features = {}
    for w in word_features:
        features['contains({})'.format(w)] = (w in document_words)
    for w in risk_words.keys():
        if w in document:
          features['contains({})'.format(risk_words[w])] = (w in document)
          if w != 'hate':
            features['contains({})'.format(w.split()[1])] = False
    return features

def show_features(word_features,document):
    document = document.lower()
    words = word_tokenize(document)
    document_words = set(words)
    features = {}
    for w in word_features:
        features['contains({})'.format(w)] = (w in document_words)
    for w in risk_words.keys():
        if w in document:
          features['contains({})'.format(risk_words[w])] = (w in document)
          if w != 'hate':
            features['contains({})'.format(w.split()[1])] = False
    for w in features.keys():
      if features[w] == True:
        print(w)

def sentiment(classifier,text):
    feats = find_features(featureset,text)
    return classifier.classify(feats)

app = flask.Flask(__name__)
app.config["DEBUG"] = True

app.config['SECRET_KEY'] = '864abf070fef2ca6107c79211dd4ea8b'
mapper = {'positive':'success','negative':'error'}
@app.route("/",methods = ['GET','POST'])
@app.route("/home",methods = ['GET','POST'])
def home():
  form = SentimentForm()
  if form.validate_on_submit():
    #flash('Your feedback was {}'.format(sentiment(loaded_model,form.sent_inp.data)),mapper[sentiment(loaded_model,form.sent_inp.data)])
    global doc,res 
    doc = form.sent_inp.data
    res = sentiment(loaded_model,form.sent_inp.data)
    
    #print(document)
    return redirect('/result')
  return render_template('home.html',form = form)
  
  #return render_template('home.html')
  #if form.validate_on_submit():
  # flash('Computing Result...')
  
  
@app.route("/result",methods = ['GET','POST'])
def result():
  return render_template('result.html',result = res)

if __name__ == '__main__':
  app.run(debug=True)