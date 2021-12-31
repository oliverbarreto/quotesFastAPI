from fastapi import FastAPI
from refran import Refran
from starlette.responses import RedirectResponse

app = FastAPI()

@app.get('/')
def index():
    return RedirectResponse(url="/docs/")

@app.get('/randomrefran/')
def randomrefran():
    refran_message = Refran.getRandomRefran()
    return {
        "refran": refran_message
    }
    		

@app.get('/randomsaying/')
def randomsaying():
    saying_message = Refran.getRandomSaying()
    return {  
        "saying": saying_message
    }
    		
