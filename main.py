from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
  return "MD OMOR FARUK HACKER"


if __name__=="__main__":
  os.system("python script.py &")
  app.run(host="0.0.0.0", port=80)