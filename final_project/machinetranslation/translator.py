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

def englishToFrench(englishText):
	if englishText == None or englishText == "" : return "Error: no input"
    frenchText = language_translator.translate(
			text = englishText, model_id = 'en-fr').get_result()
    return frenchText.get("translations")[0].get("translation")

def frenchToEnglish(frenchText):
	if frenchText == None or frenchText == "" : return "Error: no input"
    englishText = language_translator.translate(
			text = frenchText, model_id = 'fr-en').get_result()
    return englishText.get("translations")[0].get("translation")