import requests
import os
import tkinter as tk
from dotenv import load_dotenv
import random

load_dotenv()


class API:
    url = "https://random-words5.p.rapidapi.com/getRandom"
    headers = {
        "X-RapidAPI-Key": os.getenv('KEY'),
        "X-RapidAPI-Host": os.getenv('HOST')
    }

    def get_word(self):
        return requests.request("GET", self.url, headers=self.headers).text

    def get_jumble(self):
        word = API.get_word(API)
        return [random.sample(word, len(word)), word]


scr = 0


def check(en, obj, sc,m):
    if en.get() == ''.join(obj[1]):
        sc+=1
        tk.Label(m, text=f'The score is: {scr}', background='beige', font=('Times New Roman', 30, 'bold',)).pack(
            side='top',
            pady=40)


class Game(API):
    m = tk.Tk(className='words')
    m.geometry('960x560')
    m.configure(bg='beige')
    name = tk.Label(m, text="WORDS", background='beige', font=('Times New Roman', 30, 'bold', 'underline'))
    name.pack(side='top', pady=30, )

    tk.Label(m, text=f'The score is: {scr}', background='beige', font=('Times New Roman', 30, 'bold',)).pack(side='top',
                                                                                                             pady=40)

    frame = tk.Frame(m, background='beige')
    frame.pack(expand=True)
    ent = tk.Entry(frame, background='white', foreground='black', width=55)
    obj = API.get_jumble(API)
    print(obj[1])
    label = tk.Label(frame, text=''.join(obj[0]).upper(), background='beige',
                     font=('Times New Roman', 30, 'bold', 'underline'))
    label.grid(row=1, column=5, pady=20)
    ent.grid(row=7, column=5, pady=20)
    sub = tk.Button(frame, text='Submit', width=25, background='black', foreground='yellow', activebackground='white',
                    activeforeground='black', command=check(ent, obj,scr,m))
    sub.grid(row=10, column=5, pady=20)

    def start(self):
        self.m.mainloop()


if __name__ == '__main__':
    G1 = Game()
    G1.start()
