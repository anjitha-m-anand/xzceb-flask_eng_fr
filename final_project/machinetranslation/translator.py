import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

def englishToFrench(englishText):
    result = language_translator.translate(text=englishText,model_id='en-fr').get_result()
    msg = ( [t['translation'] for t in result['translations']])
    frenchText = msg[0]
    return frenchText

def frenchToEnglish(frenchText):
    result = language_translator.translate(text=frenchText,model_id='fr-en').get_result()
    msg = ( [t['translation'] for t in result['translations']])
    englishText = msg[0]
    return englishText

apikey = os.environ['apikey']
url = os.environ['url']
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

# print(englishToFrench('Hello'))
# print(frenchToEnglish('Bonjour'))