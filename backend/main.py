
#uvicorn main:app 
# uvicorn main:app --reload

#main imports 
from fastapi import FastAPI
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from decouple import config
import openai
from pydub import AudioSegment

#Custom function imports
from functions.database import store_messages, reset_messages
from functions.openai_request import convert_audio_to_text , get_chat_response
from functions.text_to_speech import convert_text_to_speech

#initiate main app
app = FastAPI()

#CORS Origins

origins = [
    "http://localhost:5173",
    "http://localhost:5174",
    "http://localhost:4173",
    "http://localhost:4174",
    "http://localhost:3000",
]

#CORS Middleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#Check Healthy
@app.get("/health")
async def check_health():
    return {"message": {"message": "healthy"}}  


#Check Healthy
@app.get("/reset")
async def reset_conversation():
    reset_messages()
    return {"message": {"message": "conversation reset"}}  


@app.post("/post-audio/")
async def post_audio(file: UploadFile = File(...)):

    # #Get saved audio file
    # audio_input = open("voice2.mp3", "rb")


    #Save file from frontend
    with open(file.filename, "wb") as buffer:
        buffer.write(file.file.read())
    audio_input = open(file.filename, "rb")
    #Decoded audio file
    message_decoded = convert_audio_to_text(audio_input)
    # print(message_decoded )
    print( message_decoded)  


    if not message_decoded:
        return HTTPException(status_code=400, detail="Fail to get audio response")
    

    #Get chat response
    chat_response = get_chat_response(message_decoded)
    print(chat_response)

    if not chat_response:
        return HTTPException(status_code=400, detail="Fail to get chat response")


    #Store messages
    store_messages(message_decoded, chat_response)

    #convert chat response to audio
    #print(chat_response)
    audio_output = convert_text_to_speech(chat_response)
    #print(audio_output)

    if not audio_output:
        return HTTPException(status_code=400, detail="Fail to get Eleven labs audio response")
    

    #Create a generator that yields chunks of data

    def iterfile():
       yield audio_output

    #Return audio file
    return StreamingResponse(iterfile(), media_type="audio/mpeg")
       
    # return StreamingResponse(iterfile(), media_type="application/octet-stream")   



#Post bot response 
# @app.post("/post-audio/")
# async def post_audio(file: UploadFile = File(...)):

#     print("hello"); 