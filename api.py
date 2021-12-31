from fastapi import FastAPI
from refran import Refran

app = FastAPI()

@app.get('/')
def index():
    # refran_message = Refran.getRandomRefran()
    refran_message = Refran.getRandomRefran()
    saying_message = Refran.getRandomSaying()
    return {"welcome":  {
        "refran": refran_message,
        "saying": saying_message
        }
    }
    		

