
# [START import_libraries]
import argparse
import base64
import json
import sys
import googleapiclient.discovery
# [END import_libraries]





def to_text(speech_file):
    

    with open(speech_file, 'rb') as speech:
        # Base64 encode the binary audio file for inclusion in the JSON
        # request.
        speech_content = base64.b64encode(speech.read())

    service = googleapiclient.discovery.build('speech', 'v1beta1')
    service_request = service.speech().syncrecognize(
        body={
            'config': {
                'encoding': 'LINEAR16',  
                'sampleRate': 16000,  
                'languageCode': 'en-US', 
            },
            'audio': {
                'content': speech_content.decode('UTF-8')
                }
            })
    
    response = service_request.execute()

    
    target=open(speech_file.split(".")[0]+".txt",'w')
    to_return=""
    for result in response.get('results', []):
        print('Result:')
        for alternative in result['alternatives']:
            print(u'  Alternative: {}'.format(alternative['transcript']))
	    to_return+=('{}'.format(alternative['transcript']))
    target.close()
    return to_return
    # [END send_request]



