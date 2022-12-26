import requests
import os
import tkinter as tk
from dotenv import load_dotenv

load_dotenv()


class API:
    url = "https://random-words5.p.rapidapi.com/getRandom"
    headers = {
        "X-RapidAPI-Key": os.getenv('KEY'),
        "X-RapidAPI-Host": os.getenv('HOST')
    }

    def get_word(self):
        return requests.request("GET", self.url, headers=self.headers).text


class Game(API):
    m = tk.Tk(className='words')
    m.geometry('960x960')
    frame = tk.Frame(m)
    frame.pack(expand=True, padx=50, pady=20)
    button = tk.Button(frame, text='Submit', background='black', foreground='white', width=25,padx=10)
    e1 = tk.Entry(frame,background='green')
    e1.grid(row=1)
    button.grid(row=2)

    def start(self):
        self.m.mainloop()


if __name__ == '__main__':
    G1 = Game()
    G1.start()
