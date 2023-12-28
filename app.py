from flask import Flask, jsonify,render_template
import openai
import os
from dotenv import load_dotenv

load_dotenv() 
openai.api_key = os.getenv('OPENAI_API_KEY')

app = Flask(__name__)


@app.route('/')
def index():
  return render_template('index.html', )
  
@app.route('/generateimages/<prompt>')
def generate(prompt):
  response = openai.Image.create(prompt=prompt, n=1, size="1024x1024") 
  return jsonify(response)

if __name__ == '__main__':  
   app.run()