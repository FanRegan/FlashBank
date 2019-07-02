import sys
sys.path.append('./')

from flask import Flask, jsonify, request
from config import config
from qa.Key_QA import QA

app = Flask(__name__)
qa_query=QA()

@app.route('/ask', methods=['POST'])
def query():
    values = request.get_json()
    query_str = values['question']
    print(query_str)
    print('查询条件：', query_str)
    response = qa_query.Qa(query_str)
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(host=config['host'], port=config['port'])
