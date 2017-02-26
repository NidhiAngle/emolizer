#!/usr/bin/env python
# Copyright 2016 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Google Cloud Speech API sample application using the REST API for batch
processing.
Example usage: python transcribe.py resources/audio.raw
"""

# [START import_libraries]
import argparse
import base64
import json
import sys
import googleapiclient.discovery
# [END import_libraries]





def to_text(speech_file):
    """Transcribe the given audio file.
    Args:
        speech_file: the name of the audio file.
    """
    # [START construct_request]
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



