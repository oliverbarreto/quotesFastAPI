from fastapi import FastAPI
from refran import Refran
from starlette.responses import RedirectResponse

from enum import Enum


class QuoteLanguage(str, Enum):
    spanish = "es_ES"
    english_US = "en_US"


app = FastAPI(
    title= "Random Quotes API",
    description="Random traditional quotes in Spanish and English",
    version="0.0.2"
)

@app.get('/')
def index():
    return RedirectResponse(url="/docs/")

@app.get('/randomquote/{language}')
def randomrefran(language: QuoteLanguage):
    quote = ""
    if language == QuoteLanguage.spanish: 
        quote = Refran.getRandomRefran()    
    if language == QuoteLanguage.english_US:
        quote = Refran.getRandomSaying()
    return {
        "language": language,
        "text": quote
    }
    	

@app.get('/randomrefran/')
def randomrefran():
    refran_message = Refran.getRandomRefran()
    return {
        "language": "es/ES",
        "type": "refran",
        "text": refran_message
    }
    		

@app.get('/randomsaying/')
def randomsaying():
    saying_message = Refran.getRandomSaying()
    return {  
        "language": "en/US",
        "type": "saying",
        "text": saying_message
    }
    		
