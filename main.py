from tkinter import *
import pandas as pd
import random as rand

BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = ("Ariel", 30, "italic")
WORD_FONT = ("Ariel", 50, "bold")
try:
    words = pd.read_csv("data\\words_to_learn.csv").to_dict(orient="records")
    words[0]
except (FileNotFoundError, pd.errors.EmptyDataError):
    words = pd.read_csv("data\\french_words.csv").to_dict(orient="records")
print(words)


def random_word(side):
    global random_index
    if side == "front":
        random_index = rand.randint(0, len(words) - 1)
        new_word = words[random_index]["French"]
        canvas.itemconfig(word_text, text=new_word, fill="black")
        canvas.itemconfig(language_text, text="French", fill="black")
    else:
        new_word = words[random_index]["English"]
        canvas.itemconfig(word_text, text=new_word, fill="white")
        canvas.itemconfig(language_text, text="English", fill="white")


def flip_front_correct():
    words.pop(random_index)
    if len(words) == 0:
        window.destroy()
    else:
        flip_front()


def flip_front():
    global flip
    canvas.itemconfig(canvas_image, image=FLASHCARD_FRONT)
    random_word("front")
    window.after_cancel(flip)
    flip = window.after(3000, flip_back)


def flip_back():
    canvas.itemconfig(canvas_image, image=FLASHCARD_BACK)
    random_word("back")


window = Tk()
FLASHCARD_FRONT = PhotoImage(file="images\\card_front.png")
FLASHCARD_BACK = PhotoImage(file="images\\card_back.png")

window.title("FlashPoint")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
canvas = Canvas(width=800, height=555, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_image = canvas.create_image(400, 263, image=FLASHCARD_FRONT)
canvas.grid(row=0, column=0, columnspan=2)

right_image = PhotoImage(file="images\\right.png")
right_button = Button(image=right_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=flip_front_correct)
right_button.grid(row=1, column=1)

wrong_image = PhotoImage(file="images\\wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, bg=BACKGROUND_COLOR, command=flip_front)
wrong_button.grid(row=1, column=0)

language_text = canvas.create_text(375, 100, text="French", font=LANGUAGE_FONT)

random_index = rand.randint(0, len(words) - 1)
start_word = words[random_index]["French"]
word_text = canvas.create_text(375, 250, text=start_word, font=WORD_FONT)
flip = window.after(3000, flip_back)
window.mainloop()
not_known_words = pd.DataFrame(words)
not_known_words.to_csv("data\\words_to_learn.csv", index=False)

