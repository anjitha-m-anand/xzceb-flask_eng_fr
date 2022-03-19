"""
A sample translation project
"""

import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

def english_to_french(english_text):
    """ Returns French translation"""
    result = language_translator.translate(text=english_text,model_id='en-fr').get_result()
    msg = ( [t['translation'] for t in result['translations']])
    french_text = msg[0]
    return french_text

def french_to_english(french_text):
    """ Returns English translation"""
    result = language_translator.translate(text=french_text,model_id='fr-en').get_result()
    msg = ( [t['translation'] for t in result['translations']])
    english_text = msg[0]
    return english_text

apikey = os.environ['apikey']
url = os.environ['url']
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)
