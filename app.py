from flask import Flask 

app = Flask(__name__) 

@app.route('/') 

def hello_World() :

  return 'AlphaDevloper'

if __name__ == "__main__":
  app.run() 
