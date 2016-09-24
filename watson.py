import json
from watson_developer_cloud import ToneAnalyzerV3


tone_analyzer = ToneAnalyzerV3(
   username='f74339b8-848d-4622-9e43-2fe02e958b0c',
   password='pKZ4jVwiJzV7',
   version='2016-05-19')

print(json.dumps(tone_analyzer.tone(text='A word is dead when it is said, some say. Emily Dickinson'), indent=2))