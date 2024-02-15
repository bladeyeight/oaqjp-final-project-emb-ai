import requests
import json

# def emotion_detector(text_to_analyse):
#     url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
#     myobj = { "raw_document": { "text": text_to_analyse } }
#     header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
#     response = requests.post(url, json = myobj, headers=header)
#     return response.text

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = myobj, headers=header)
    if response.status_code == 400:
        prediction_data = {
        'anger': None,
        'disgust': None,
        'fear': None,
        'joy': None,
        'sadness': None,
        'dominant_emotion': None
        }
        print('function', prediction_data)
        return prediction_data 
    responseJSON = response.json()
    emotion_data = responseJSON['emotionPredictions'][0]['emotion']
    maxEmotion = max(emotion_data, key=emotion_data.get)
    prediction_data = {
        'anger': emotion_data['anger'],
        'disgust': emotion_data['disgust'],
        'fear': emotion_data['fear'],
        'joy': emotion_data['joy'],
        'sadness':emotion_data['sadness'],
        'dominant_emotion': maxEmotion
    }
    return prediction_data