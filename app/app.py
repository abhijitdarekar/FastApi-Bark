from fastapi import FastAPI
from fastapi.responses import JSONResponse, FileResponse

from bark import  generate_audio, SAMPLE_RATE, preload_models
from scipy.io.wavfile import write as write_wav
from .Models.models import InputPrompt
from datetime import datetime

import base64

app = FastAPI()

preload_models()

@app.get("/")
async def root() :
    return {"status":"online"}

@app.post("/api/text_to_speech/")
async def predict(Prompt:InputPrompt):
    Language=Prompt.language.lower()
        
    input_text=Prompt.data
    history_p=f"{Language}_speaker_1"
    output=generate_audio(input_text)

    time= datetime.now()
    time=time.strftime("%Y-%m-%d_%H-%M-%S")
    file_name=f"./app/Audio_files/Audio_{time}.wav"
    write_wav(file_name, SAMPLE_RATE, output)

    with open(file_name,"rb") as file:
        myObj = base64.b64encode(file.read())

    return {"speech": FileResponse(
					     path=file_name,
					     media_type="audio/mpeg",
                                   filename='speech.mp3'
					),
            "data":input_text
    }

    
