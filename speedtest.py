import random
import timeit
from tkinter import *

class SpeedGame:
    def __init__(self):
        self.word_list = []
        self.word = None
        self.entry = None

    def generate_words(self, test_duration, words_per_second):
        total_words = test_duration * words_per_second
        required_word_list_size = total_words + 100
        self.word_list = self.extend_word_list([], required_word_list_size)
        chosen_words = random.sample(self.word_list, total_words)
        return chosen_words

    def extend_word_list(self, word_list, required_size):
        if len(word_list) < required_size:
            for i in range(required_size - len(word_list)):
                word_list.append(f"word_{i + 1}")
        return word_list

    def check_result(self):
        if self.entry.get() == self.word_list[self.word]:
            end = timeit.default_timer()
            print(end-self.start)
        else:
            print("Wrong Input")

    def game(self):
        self.word_list = self.generate_words(30, 10)
        self.word = random.randint(0, (len(self.word_list)-1))

        # start timer using timeit function
        self.start = timeit.default_timer()
        windows = Tk()
        windows.geometry("450x200")

        # use label method of tkinter for labeling in window
        x2 = Label(windows, text=self.word_list[self.word], font="times 20")

        # place of labeling in window
        x2.place(x=150, y=10)
        x3 = Label(windows, text="Start Typing", font="times 20")
        x3.place(x=10, y=50)

        entry = Entry(windows)
        self.entry = entry
        entry.place(x=280, y=55)

        # buttons to submit output and check results
        b2 = Button(windows, text="Done",
                    command=self.check_result, width=12, bg='grey')
        b2.place(x=150, y=100)

        b3 = Button(windows, text="Try Again", 
                    command=self.game, width=12, bg='grey')
        b3.place(x=250, y=100)
        windows.mainloop()

speed_game = SpeedGame()
speed_game.game()
