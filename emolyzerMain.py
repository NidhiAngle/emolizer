from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import NumericProperty


import textEmolyzer 
import os
from speechToText import to_text 
import sys
import json
from watson_developer_cloud import ToneAnalyzerV3
import matplotlib.pyplot as plt

class EmolyzerLayout(FloatLayout):
    def __init__(self, **kwargs):
        super(EmolyzerLayout, self).__init__(**kwargs)

        self.textinput = TextInput(size_hint = (.5,.1),pos_hint={'bottom': 1.0})
        btn = Button(text = "Analyze",size_hint = (.5,.1),pos_hint={'right': 1.0})
        btn.bind(on_press=self.processVoice)

        self.add_widget(self.textinput)        
        self.add_widget(btn)
        
    def processVoice(self, obj):
        file_path = self.textinput.text #'v.m4a'
        new_path=file_path.split(".")[0]
        os.system("ffmpeg -i "+file_path+" -f s16le -ar 16000 -acodec pcm_s16le "+new_path+".raw")
        text=to_text(new_path+".raw")
    
        tone_analyzer = ToneAnalyzerV3(
        username='964d575c-2cb2-4a96-ba0c-05885cb91293',
        password='DAs7gLZj8VXg',
        version='2016-05-19 ')
    
        x=tone_analyzer.tone(text)
        colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral', 'lightgreen']
        for type_tone in x["document_tone"]["tone_categories"][0:1]:
            labels=[]
            sizes=[]
            i=0
            print type_tone
            for tone in type_tone['tones']:
                labels.append(tone['tone_name'])
                sizes.append(tone['score'])
                i+=1
            patches, texts = plt.pie(sizes, colors=colors[:i], shadow=True, startangle=90)
            plt.legend(patches, labels, loc="best")
            plt.title(type_tone['category_name'])
            plt.axis('equal')
            plt.tight_layout()
            plt.savefig('output'+type_tone['category_id']+'.jpg')
            myImg = Image(source='output'+type_tone['category_id']+'.jpg')
            self.add_widget(myImg)
        os.remove(new_path+".raw")

class EmolyzerApp(App):
    def build(self):
        mL = EmolyzerLayout(size=(300,300))
        return mL
        
if __name__ == "__main__":
    EmolyzerApp().run()

    