from flask import Flask, request, render_template
from llm_invoker import get_answer
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    query = request.get_json()
    return get_answer(query['query'])

if __name__ == '__main__':
    app.run()