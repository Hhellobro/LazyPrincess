from flask import Flask 

app = Flask(name) 

@app.route('/') 

def hello_World() :

  return 'AlphaDevloper'

if name == "main":
  app.run() 
