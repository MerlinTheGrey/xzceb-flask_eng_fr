"This is a Translator"
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
authenticator=authenticator
)

language_translator.set_service_url(url)

def english_to_french(english_text):
    """ function to convert Eng to French"""
    if english_text=="":
        french_text = "Null input"
    else:
        language_translator.translate(english_text)
        french_text=(english_text["translations"][0]["translation"])
    return french_text
def french_to_english(french_text):
    """ function to convert Fremch to Eng"""
    if french_text=="":
        english_text="Null input"
    else:
        language_translator.translate(french_text)
        english_text=(french_text["translations"][0]["translation"])
    return english_text