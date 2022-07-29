'''
This is the translator module for the IBM python project course
Author: Naervern (Antonio Maximiano)
Done for IBM's Python Project for AI & App Dev course
'''

import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv
# import json only when making the server ##

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
    '''translates english to french'''
    if english_text is None or english_text == "" :
        return "Error: no input"
    french_text = language_translator.translate(
        text = english_text, model_id = 'en-fr').get_result()
    return french_text.get("translations")[0].get("translation")

def french_to_english(french_text):
    '''translates french to english'''
    if french_text is None or french_text == "" :
        return "Error: no input"
    english_text = language_translator.translate(
        text = french_text, model_id = 'fr-en').get_result()
    return english_text.get("translations")[0].get("translation")
