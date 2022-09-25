from tkinter import *
import pandas as pd
import random as rand

BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = ("Ariel", 30, "italic")
WORD_FONT = ("Ariel", 50, "bold")
words = pd.read_csv("data\\french_words.csv").to_dict()


def random_word():
    new_word = words["French"][rand.randint(0, len(words["French"]) - 1)]
    word_label.config(text=new_word)


window = Tk()
window.title("FlashPoint")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=555, bg=BACKGROUND_COLOR, highlightthickness=0)
flashcard_front = PhotoImage(file="images\\card_front.png")
canvas.create_image(400, 263, image=flashcard_front)
canvas.grid(row=0, column=0, columnspan=2)

right_image = PhotoImage(file="images\\right.png")
right_button = Button(image=right_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=random_word)
right_button.grid(row=1, column=1)

wrong_image = PhotoImage(file="images\\wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=random_word)
wrong_button.grid(row=1, column=0)

language_label = Label(text="French", font=LANGUAGE_FONT, bg="#FFFFFF")
language_label.place(x=325, y=100)

start_word = words["French"][rand.randint(0, len(words["French"]) - 1)]
word_label = Label(text=start_word, font=WORD_FONT, bg="#FFFFFF")
word_label.place(x=300, y=200)

window.mainloop()
