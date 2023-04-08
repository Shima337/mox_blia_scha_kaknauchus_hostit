from flask import Flask, render_template, request, Response, jsonify
from ask_ai import run_llm
import time


app = Flask(__name__)


def wait_funk(input_text):
    time.sleep(2)
    result = {'input': 'whose president Mexic', 'output': 'Andrés Manuel López Obrador'}
    return result

@app.route('/', methods=['GET', 'POST'])
def index():
    result = ""
    if request.method == 'POST':
        input_text = request.form['input_text']
        template = "GDP of the US 2022 multiplying by 3"
        result= run_llm(input_text)
        # result = f"Processed: {input_text}"
        # result =  wait_funk(input_text)
        return jsonify(result)
        # return Response(result, content_type='aplication/json')
    return render_template('index.html')
    
    

if __name__ == '__main__':
    app.run(debug=True)




