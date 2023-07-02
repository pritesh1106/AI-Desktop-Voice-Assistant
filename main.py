import speech_recognition as sr
import os
import webbrowser
import openai
from config import apikey
import datetime
import random
import numpy as np

chatStr = ""  # Global variable to keep track of the conversation history

def chat(query):
    global chatStr
    print(chatStr)
    openai.api_key = apikey
    chatStr += f"Pritesh: {query}\n Mac: "  # Append user query to the conversation history
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=chatStr,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    say(response["choices"][0]["text"])  # Speak the AI response
    chatStr += f"{response['choices'][0]['text']}\n"  # Append AI response to the conversation history
    return response["choices"][0]["text"]

def ai(prompt):
    openai.api_key = apikey
    text = f"OpenAI response for Prompt: {prompt} \n *************************\n\n"

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    text += response["choices"][0]["text"]
    if not os.path.exists("Openai"):
        os.mkdir("Openai")

    with open(f"Openai/{''.join(prompt.split('intelligence')[1:]).strip() }.txt", "w") as f:
        f.write(text)

def say(text):
    os.system(f'say "{text}"')  # Use macOS 'say' command to speak the given text

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")  # Convert speech to text using Google Speech Recognition API
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some Error Occurred. Sorry from Mac"

if __name__ == '__main__':
    print('Welcome to Mac A.I')
    say("Mac A.I")
    while True:
        print("Listening...")
        query = takeCommand()

        # Handle different commands
        sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.com"], ["google", "https://www.google.com"], ["github", "https://www.github.com"]]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]} sir...")
                webbrowser.open(site[1])  # Open the specified website in a web browser

        if "open music" in query:
            musicPath = "/Users/Pritesh/Downloads/weird fishes - radiohead.mp3"
            os.system(f"open {musicPath}")  # Open the specified music file

        elif "the time" in query:
            musicPath = "/Users/Pritesh/Downloads/weird fishes - radiohead.mp3"
            hour = datetime.datetime.now().strftime("%H")
            min = datetime.datetime.now().strftime("%M")
            say(f"Sir time is {hour} hours and {min} minutes")  # Speak the current time

        elif "open whatsapp".lower() in query.lower():
            os.system(f"open /System/Applications/WhatsApp.app")  # Open WhatsApp application

        elif "open facetime".lower() in query.lower():
            os.system(f"open /Applications/FaceTime.app")  # Open FaceTime application

        elif "Using ChatGPT".lower() in query.lower():
            ai(prompt=query)  # Invoke AI to respond to a specific prompt

        elif "Mac Quit".lower() in query.lower():
            exit()  # Quit the application

        elif "reset chat".lower() in query.lower():
            chatStr = ""  # Reset the conversation history

        else:
            print("Chatting...")
            chat(query)  # Engage in a general chat with AI