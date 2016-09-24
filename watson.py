import json
from watson_developer_cloud import ToneAnalyzerV3


tone_analyzer = ToneAnalyzerV3(
   username='YOUR SERVICE USERNAME',
   password='YOUR SERVICE PASSWORD',
   version='2016-05-19 ')

print(json.dumps(tone_analyzer.tone(text='A word is dead when it is said, some say. Emily Dickinson'), indent=2))