from Tkinter import *
import random
from knowledge_dictionaries import *

class PictureQuestion(object):
    def __init__(self, dictionary_with_data, root, photo_label):
        self.key = random.choice(dictionary_with_data.keys())
        self.root = root
        self.photo_label = photo_label

        if dictionary_with_data == LOL_item:
            self.question = "What item from League of Legends is pictured below?"
            self.my_image = PhotoImage(file=self.key)
            self.photo_label = Label(self.root, image=self.my_image, bg="black")
            self.photo_label.image = self.my_image
            self.photo_label.grid(row=6, column=0, columnspan=4)

        # Add additional if statements for each dictionary.
        if dictionary_with_data == NBA_STAR:
            self.question = "What NBA Star is pictured below?"
            self.my_image = PhotoImage(file=self.key)
            self.photo_label = Label(self.root, image=self.my_image, bg="black")
            self.photo_label.image = self.my_image
            self.photo_label.grid(row=6, column=0, columnspan=4)

        if dictionary_with_data == NBA_TEAM_LOGO:
            self.question = "What NBA team uses this logo?"
            self.my_image = PhotoImage(file=self.key)
            self.photo_label = Label(self.root, image=self.my_image, bg="black")
            self.photo_label.image = self.my_image
            self.photo_label.grid(row=6, column=0, columnspan=4)

        self.correct_answer=dictionary_with_data.get(self.key)

        # 2. Generate three additional random answers, then append the correct answer.
        self.answer_option = random.sample(dictionary_with_data.values(), 3)  # Must use values instead of keys here.
        while self.correct_answer in self.answer_option:
            self.answer_option = (random.sample(dictionary_with_data.values(),3))

        self.answer_option.append(self.correct_answer)
        random.shuffle(self.answer_option) # Scramble the answer options.

    # This method only used in the console for testing purposes. Never used in the GUI.
    def print_question(self):
        print self.question
        print "\tA.", self.answer_option[0]
        print "\tB.", self.answer_option[1]
        print "\tC.", self.answer_option[2]
        print "\tD.", self.answer_option[3]

    # This method should work in both the console and the GUI.
    # The user answer is always 'A', 'B', 'C' or 'D'.
    def check_answer(self, user_answer):  # self refers to the current multiple choice question.
        global score
        user_answer = user_answer.upper()  # Just in case it is given in lower case.
        if user_answer not in ['A', 'B', 'C', 'D']:
            print "That's not a valid answer! Must choose A, B, C or D."
            return False
        # OK, now we know the answer is at least legal.
        answer_index = ord(user_answer)-ord('A')  # 'A' -> 0, 'B' -> 1, 'C' -> 2, 'D' -> 3
        if self.answer_option[answer_index] == self.correct_answer:
            print "That's Correct!\n"
            return True
        else:
            print "Wrong! The correct answer is %s.\n" % self.correct_answer
            return False

