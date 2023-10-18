from speech_recognition import Recognizer, AudioFile
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

recognizer = Recognizer()

with AudioFile('chile.wav') as audio_file:
  audio = recognizer.record(audio_file)

text = recognizer.recognize_google(audio)

nltk.download('vader_lexicon')

analyzer = SentimentIntensityAnalyzer()
scores = analyzer.polarity_scores(text)
print(scores)

if scores['compound'] > 0:
  print('Positive Speech')
else:
  print('Negative Speech')