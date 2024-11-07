import requests
from decouple import config

#Retreive API Key
ELEVEN_LABS_API_KEY = config('ELEVEN_LABS_API_KEY')

#Convert text to speech
def convert_text_to_speech(message):

    #Define body
    body = {
        "text": message,
        "voice_settings": {
            "stability": 0,
            "similarity_boost": 0,
        }

    }

    #Define voice
    voice_rachel = "21m00Tcm4TlvDq8ikWAM"


    #Define headers and endpoint
    #"https://api.elevensynth.com/v1/voice/" + voice_rachel + "/synthesize"

    headers = {"xi-api-key": ELEVEN_LABS_API_KEY, "Content-Type": "application/json", "Accept": "audio/mpeg"}
    endpoint = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_rachel}"

    #Send request

    try:
        response = requests.post(endpoint, json=body, headers=headers)
        #return response.content
    except Exception as e:
        # print(e)
        # return {"message": "error"}
        return
    
    #handle response
    if(response.status_code == 200):
        return response.content
    else:
        return
