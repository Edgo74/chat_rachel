import json
import random

# Get recent messages
def get_recent_messages():
    # Define the file and the learn instructions
    file_name = "stored_data.json"
    learn_instructions = {
        "role": "system",
        "content": "You are a helpful assistant."
    }

    # Initialize messages
    messages = []

    # Add a random element to the messages
    x = random.uniform(0, 1)

    if x > 0.5:
        learn_instructions["content"] = learn_instructions["content"] 
    else:
        learn_instructions["content"] = learn_instructions["content"] 

    # Append instructions to message
    messages.append(learn_instructions)

    # Get last messages
    try:
        with open(file_name) as file:
            data = json.load(file)

            # Append last 5 items of data
            if data:
                if len(data) < 5:
                    for item in data:
                        messages.append(item)
                else:
                    for item in data[-5:]:
                        messages.append(item)
    except Exception as e:
        print(e)
        pass
        # return {"message": "error"}

    # Return messages
    return messages


# Store messages

def store_messages(request_message, response_message):
    
    #Define the file name 
    file_name = "stored_data.json"

    #Get recent messages
    messages = get_recent_messages()[1:]

    #Add messages to data
    user_message = {"role": "user", "content" : request_message}
    assistant_message = {"role": "assistant", "content" : response_message}
    messages.append(user_message)
    messages.append(assistant_message)

    #Save the updated file 
    with open(file_name, 'w') as file:
        json.dump(messages, file)


#Reset messages 
def reset_messages():

    #Owerwrite the file with empty list
    open("stored_data.json", "w")

        