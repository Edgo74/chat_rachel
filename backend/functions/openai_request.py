import openai 
from decouple import config
from functions.database import get_recent_messages 

#Retreive API Key

openai.organization = config('OPEN_AI_ORG')
openai.api_key = config('OPEN_AI_KEY')

#openai whisper

#conert audio to text

def convert_audio_to_text(audio_file):
    #print("hello")
    try:
        transcript = openai.Audio.transcribe("whisper-1", audio_file)
        print(transcript)
        message_text = transcript['text']
        print(message_text)
        return message_text
    except Exception as e:
        print(e)
        return None
    


#OpenAi Chatgpt
    
def get_chat_response(message_input):
    messages = get_recent_messages()
    user_message = {"role": "user", "content" : message_input}
    messages.append(user_message)
    print(messages)


    try:
        response = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo",
            messages = messages,
        )
        #delete
        print(response)
        message_text = response['choices'][0]['message']["content"]
        return message_text
    except Exception as e:
        print(e)
        return 
        # return {"message": "error"}