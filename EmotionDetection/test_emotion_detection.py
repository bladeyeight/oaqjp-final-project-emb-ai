import unittest
from emotion_detection import emotion_predictor

class TestEmotionPredictor(unittest.TestCase):
    def test1(self):
        testResponse = emotion_predictor('I am glad this happened')
        self.assertEqual(testResponse['dominant_emotion'], 'joy')
    def test2(self):
        testResponse = emotion_predictor('I am really mad about this')
        self.assertEqual(testResponse['dominant_emotion'], 'anger')
    def test3(self):
        testResponse = emotion_predictor('I feel disgusted just hearing about this')
        self.assertEqual(testResponse['dominant_emotion'], 'disgust')
    def test4(self):
        testResponse = emotion_predictor('I am so sad about this')
        self.assertEqual(testResponse['dominant_emotion'], 'sadness')
    def test5(self):
        testResponse = emotion_predictor('I am really afraid that this will happen')
        self.assertEqual(testResponse['dominant_emotion'], 'fear')
        
unittest.main()