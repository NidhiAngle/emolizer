# emolyzer
Analyzes an audio file of a conversation snippet to output a piechart indicating levels of emotion (sadness, disgust, fear, joy and  anger) detected. Uses the Google Cloud Speech API and IBM Watson's Tone Analyser.

Before using, will need to pip install watson-developer-cloud,google-cloud-speech. Also needs the installation of the Google cloud SDK, and setting of the environement variable GOOGLE_APPLICATION_CREDENTIALS=/path_to_authentication_file

python convert.py audio_file

Also includes a demo kivy app which integrates the conversion functions into a Python-kivy app. Enter the file name into the GUI textbox (with its extension) and hit the Analyze button.

python emolyzerMain.py 


See https://devpost.com/software/emolyzer for a live demo.
