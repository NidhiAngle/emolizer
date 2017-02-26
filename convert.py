import os
from FM17 import to_text 
import sys
import json
from watson_developer_cloud import ToneAnalyzerV3
import matplotlib.pyplot as plt

#def parse_json():


def main(file_path):
    new_path=file_path.split(".")[0]
    os.system("ffmpeg -i "+file_path+" -f s16le -ar 16000 -acodec pcm_s16le "+new_path+".raw")
    text=to_text(new_path+".raw")

    tone_analyzer = ToneAnalyzerV3(
    username='964d575c-2cb2-4a96-ba0c-05885cb91293',
    password='DAs7gLZj8VXg',
    version='2016-05-19 ')


    
    x=tone_analyzer.tone(text)
    colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral', 'lightgreen']
    print x
    for type_tone in x["document_tone"]["tone_categories"]:
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
        plt.show()


if __name__ == '__main__':
    
    args = sys.argv[1]
    main(args)
