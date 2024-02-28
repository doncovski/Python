from tkinter import *
import pandas
import random
import time

# ---------------------------- CONSTANTS ------------------------------- #
BACKGROUND_COLOR = "#B1DDC6"
W_PADDING = 50
FONT_NAME = "Arial"
SIZE_TITLE = 40
SIZE_WORD = 60
REPS = 3000
current_card = {}
to_learn = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    orig_data = pandas.read_csv("data/french_words.csv")
    to_learn = orig_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global flip_timer, current_card
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(word_text, text=f"{current_card['French']}", fill="black")
    canvas.itemconfig(title_text, text=f"French", fill="black")
    canvas.itemconfig(front_canvas, image=front_img)
    flip_timer = window.after(REPS, flip_card)


def flip_card():
    canvas.itemconfig(word_text, text=f"{current_card['English']}", fill="white")
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(front_canvas, image=back_img)


def remove_card():
    global to_learn, current_card
    to_learn.remove(current_card)
    next_card()
    new_learn = pandas.DataFrame(to_learn)
    new_learn.to_csv("data/words_to_learn.csv", index=False)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=W_PADDING, pady=W_PADDING, bg=BACKGROUND_COLOR)
flip_timer = window.after(REPS, flip_card)
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_img = PhotoImage(file="images/card_front.png")
back_img = PhotoImage(file="images/card_back.png")
front_canvas = canvas.create_image(400, 263, image=front_img)
title_text = canvas.create_text(400, 150, text="", font=(FONT_NAME, SIZE_TITLE, "italic"))
word_text = canvas.create_text(400, 263, text="", font=(FONT_NAME, SIZE_WORD, "bold"))
canvas.grid(row=0, column=0, columnspan=2)
wrong_button = PhotoImage(file="images/wrong.png")
right_button = PhotoImage(file="images/right.png")
button_left = Button(image=wrong_button, command=next_card, highlightthickness=0)
button_right = Button(image=right_button, command=remove_card, highlightthickness=0)
button_left.grid(row=1, column=0)
button_right.grid(row=1, column=1)
next_card()

window.mainloop()
