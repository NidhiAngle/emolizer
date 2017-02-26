# emolizer
Analyzes an audio file of a conversation snippet to output a piechart indicating levels of emotion (sadness, disgust, fear, joy and  anger) detected. Uses the Google Cloud Speech API and IBM Watson's Tone Analyser.

Before using, will need to pip install watson-developer-cloud,google-cloud-speech. Also needs the installation of the Google cloud SDK, and setting of the environement variable GOOGLE_APPLICATION_CREDENTIALS=/path_to_authentication_file

Does  not include the code used to run on kivy, will update soon.
Run as:

python convert.py audio_file

See https://devpost.com/software/emolyzer for a live demo.
