import sys
import speech_recognition as sr
import webbrowser
import sounddevice as sd
import numpy as np
import time
import comtypes.client
import music_libarary
import os
import requests
from dotenv import load_dotenv
from google import genai
load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
print("Gemini key loaded:", bool(GEMINI_API_KEY))
print("News key loaded:", bool(NEWS_API_KEY))

if not GEMINI_API_KEY:
    print("Warning: GEMINI_API_KEY not found in .env file")

if not NEWS_API_KEY:
    print("Warning: NEWS_API_KEY not found in .env file")


recognizer = sr.Recognizer()
speaker = comtypes.client.CreateObject("SAPI.SpVoice")
#gemini client
ai_client = genai.Client(api_key=GEMINI_API_KEY) if GEMINI_API_KEY else None
def speak(text):
    print("Jarvis:", text)
    speaker.Speak(str(text))
def get_ai_response(question):
    """Ask Gemini AI and speak its short answer."""
    if not ai_client:
        speak("Gemini API key is missing.")
        return

    try:
        response = ai_client.models.generate_content(
            model="gemini-3.6-flash",
            contents=(
                "You are Jarvis, a helpful voice assistant. "
                "Answer briefly and clearly. "
                "If the user speaks Urdu or Roman Urdu, reply in Roman Urdu.\n"
                f"User question: {question}"
            ),
            config={
                "automatic_function_calling": {
                    "disable": True
                }
            }
        )

        answer = (response.text or "").strip()
        speak(answer if answer else "I did not receive an answer.")

    except Exception as error:
        print("Gemini error:", error)
        speak("Sorry, AI service is not available right now.")
def get_news():
    """Fetch and speak five latest news headlines."""
    if not NEWS_API_KEY:
        speak("News API key is missing.")
        return

    try:
        url = "https://newsapi.org/v2/top-headlines"

        parameters = {
            "country": "us",
            "pageSize": 5,
            "apiKey": NEWS_API_KEY,
        }

        response = requests.get(url, params=parameters, timeout=15)
        data = response.json()

        if data.get("status") != "ok":
            print("News API response:", data)
            speak("Sorry, news could not be fetched.")
            return

        articles = data.get("articles", [])

        if not articles:
            speak("No news headlines were found.")
            return

        speak("Here are the latest news headlines.")

        for number, article in enumerate(articles, start=1):
            title = article.get("title")

            if title:
                print(f"{number}. {title}")
                speak(f"News {number}. {title}")

    except Exception as error:
        print("News error:", error)
        speak("Sorry, I could not fetch the news.")
def processcommands(command):
    command = command.lower().strip()

    websites = {
        "open google": "https://www.google.com",
        "open youtube": "https://www.youtube.com",
        "open facebook": "https://www.facebook.com",
        "open instagram": "https://www.instagram.com",
    }

    for phrase, url in websites.items():
        if phrase in command:
            speak(f"Opening {phrase.replace('open ', '')}")
            webbrowser.open(url)
            return

    if command.startswith("play "):
        song = command.replace("play ", "", 1).strip()

        if song in music_libarary.musics:
            speak(f"Playing {song}")
            webbrowser.open(music_libarary.musics[song])
        else:
            speak("Song not found in music library.")
        return

    if "news" in command:
        get_news()
        return

    # "ask ..." or any unknown command goes to Gemini
    if command.startswith("ask "):
        question = command.replace("ask ", "", 1).strip()
    else:
        question = command

    if question:
        get_ai_response(question)
def listen():
    sample_rate = 16000
    silence_limit = 1.2
    max_recording = 10
    threshold = 500

    chunks = []
    spoken = False
    last_sound = time.time()
    start_time = time.time()

    def callback(indata, frames, time_info, status):
        nonlocal spoken, last_sound
        chunks.append(indata.copy())

        if np.max(np.abs(indata)) > threshold:
            spoken = True
            last_sound = time.time()

    print("\nListening... speak now")

    with sd.InputStream(
        samplerate=sample_rate,
        channels=1,
        dtype="int16",
        callback=callback
    ):
        while time.time() - start_time < max_recording:
            if spoken and time.time() - last_sound > silence_limit:
                break
            time.sleep(0.1)
    if not chunks:
        return None

    recording = np.concatenate(chunks, axis=0)
    return sr.AudioData(recording.tobytes(), sample_rate, 2)


if __name__=="__main__":
    speak("initializing jarvis.....")
    jarvis_active = False
    while True:
        try:
            audio = listen()
            command = recognizer.recognize_google(audio)
            print("You said:", command)
            command = command.lower().strip()
            if "jarvis" in command or "jervis" in command:
                speak("yes....")
                command = command.replace("jarvis","").replace("jervis","").strip()
                if command:
                    processcommands(command)
                else:
                    jarvis_active = True
            elif jarvis_active:
                processcommands(command)
                jarvis_active = False
            else:
                print("wake word not detected")
        except sr.UnknownValueError:
            print("Could not understand audio")

        except sr.RequestError as error:
            print("Google service error:", error)
        except KeyboardInterrupt:
            speak("Goodbye.")
            break

        except Exception as error:
            print("Unexpected error:", error)
