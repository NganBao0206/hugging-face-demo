from flask import Flask, request, jsonify
from flask import render_template
from utils import analyze_sentiment 

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/api/predict', methods=['POST'])
def predict():
    comment = request.json['comment']

    # Đánh giá cảm xúc của bình luận
    result = analyze_sentiment(comment)

    # Trả về kết quả
    return jsonify(result)

if __name__ == '__main__':
    app.run(port=5000)