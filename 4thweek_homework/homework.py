from flask import Flask, render_template, jsonify, request

homework = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta


@homework.route('/')
def home():
    return render_template('index.html')


@homework.route('/orders', methods=['POST'])
def give_order():
    name_receive = request.form['name_give']
    count_receive = request.form['count_give']
    add_receive = request.form['add_give']
    phone_receive = request.form['phone_give']

    doc = {
        'name': name_receive,
        'count': count_receive,
        'address': add_receive,
        'phone': phone_receive
    }

    db.orders.insert(doc)
    return jsonify({'result': 'success', 'msg': '주문이 성공적으로 작성되었습니다'})


@homework.route('/orders', methods=['GET'])
def receive_order():
    info = list(db.orders.find({}, {'_id': False}))
    return jsonify({'result': 'success', 'orders': info})


if __name__ == '__main__':
    homework.run('127.0.0.1', port=5003, debug=True)