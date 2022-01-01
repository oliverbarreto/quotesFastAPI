from fastapi import FastAPI
from refran import Refran
from starlette.responses import RedirectResponse


app = FastAPI(
    title= "Random Quotes API",
    description="Random traditional quotes in Spanish and English",
    version="0.0.1"
)

@app.get('/')
def index():
    return RedirectResponse(url="/docs/")

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
    		
