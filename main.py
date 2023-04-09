from flask import Flask, render_template, request, Response, jsonify
from ask_ai import run_llm
import time


app = Flask(__name__)

@app.route('/test', methods=['GET'])
def test():
    return "HELLO WORLD"




@app.route('/', methods=['GET', 'POST'])
def index():
    result = ""
    if request.method == 'POST':
        if request.form["input_text"]:
            input_text = request.form['input_text']
        else:
            input_text = request.data['input_text']
        result= run_llm(input_text)
        return jsonify(result)
    return render_template('index.html')
    
    

if __name__ == '__main__':
    app.run(host ='0.0.0.0', port=5000)




