import requests
import os
import tkinter as tk
from dotenv import load_dotenv
load_dotenv()


class Game:
    pass


url = "https://random-words5.p.rapidapi.com/getRandom"

headers = {
    "X-RapidAPI-Key": os.getenv('KEY'),
    "X-RapidAPI-Host": os.getenv('HOST')
}

response = requests.request("GET", url, headers=headers)

print(response.text)
