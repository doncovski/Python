from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
W_PADDING = 20
FONT_NAME = "Arial"
SIZE_TITLE = 20

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=W_PADDING, pady=W_PADDING, bg=THEME_COLOR)
        self.score_text = Label(text=f"Score: 0", background=THEME_COLOR, font=(FONT_NAME, 16, "bold"), foreground="#FFFFFF", pady=20)
        self.score_text.grid(row=0, column=1)
        self.canvas = Canvas(width=300, height=300, highlightthickness=0, background="white")
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        true_img = PhotoImage(file="images/true.png")
        false_img = PhotoImage(file="images/false.png")
        self.question = self.canvas.create_text(150, 150, text="Sample", font=(FONT_NAME, SIZE_TITLE, "italic"), fill=THEME_COLOR, width=280)
        self.button_true = Button(image=true_img, command=self.true_command, highlightthickness=0)
        self.button_false = Button(image=false_img, command=self.false_command, highlightthickness=0)
        self.button_true.grid(row=2, column=0)
        self.button_false.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_text.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=q_text)
        else:
            self.canvas.itemconfig(self.question, text="You've reqched the end of the questions")
            self.button_true.config(state="disabled")
            self.button_false.config(state="disabled")


    def true_command(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_command(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)

    def recolor(self, color="green"):
        self.canvas.itemconfig(bg=color)


#front_canvas = canvas.create_image(400, 263, image=front_img)
#canvas.create_image(400, 263, image=back_img)
# title_text = canvas.create_text(400, 150, text="", font=(FONT_NAME, SIZE_TITLE, "italic"))
# word_text = canvas.create_text(400, 263, text="", font=(FONT_NAME, SIZE_WORD, "bold"))
# canvas.grid(row=0, column=0, columnspan=2)
#
# button_left.grid(row=1, column=0)
# button_right.grid(row=1, column=1)
