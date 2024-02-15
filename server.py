from flask import Flask, render_template, request
import EmotionDetection

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/emotionDetector')
def detect_emotion():
    text_param = request.args.get('textToAnalyze')
    response = EmotionDetection.emotion_detection.emotion_predictor(text_param)
    return f"""For the given statement, the system response is 'anger': {response['anger']},
    'disgust': {response['disgust']}, 'fear': {response['fear']}, 'joy': {response['joy']},
    and 'sadness':{response['sadness']}, The dominant emotion is {response['dominant_emotion']}.""", 200

if __name__ == '__main__':
    app.run(debug=True)