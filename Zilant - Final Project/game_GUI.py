from Tkinter import *
import tkMessageBox
from knowledge_dictionaries import *
from multiple_choice_question import *
from picture_choice_question import *
from player import Player
import os
import sys
import login_gui

try:
    temp = open('temppass.txt','r')
    AuthorizedPlayer = Player()
    AuthorizedPlayer.user_name = temp.readline()[:-1] #don't read the new line character
    AuthorizedPlayer.number_of_crystals = int(temp.readline())
    AuthorizedPlayer.score = int(temp.readline())
    AuthorizedPlayer.level = int(temp.readline())
    temp.close()
    os.remove('temppass.txt')
except Exception as e:
    sys.exit() # dumb error handling - the game will run twice, once when log in, then when closing



root = Tk()
root.title("Zilant Team's Game")  # <-- Replace with your team's name.
root.minsize(500,500)

mb = Menubutton(root, text="Select Quiz Topic", relief=RAISED, padx=2, pady=2 )
mb.grid()
mb.menu = Menu ( mb, tearoff = 0 )
mb["menu"] = mb.menu

quizVar = IntVar()  # An integer specifying the selected quiz.



question_label = Label(root, text="Question will appear here.", bg="beige", width = 60)
question_label.grid(columnspan=4, sticky=EW)

def save(close):
    fo = open('topsecret.py','r+')
    string = AuthorizedPlayer.user_name
    str_check = 0
    latest_str = 0
    for line in fo:
        if string in line:
            latest_str += 1
    fo.seek(0)
    for line in fo:
        if string in line:
            str_check += 1
            if str_check == latest_str:
                fo.write('player_stats.update({"' + string +'": {"score":"' + str(AuthorizedPlayer.score) +
                         '", "level":"' + str(AuthorizedPlayer.level) + '", "crystals":"' +
                         str(AuthorizedPlayer.number_of_crystals) + '"} })\n'
                         )
                print "Saved"
                break
    fo.close()
    if close == 1:
        root.destroy()
        sys.exit()

def get_hint():
    if hint_label.cget('text') != correct_answer and AuthorizedPlayer.number_of_crystals >= 5:
        hint_label.config(text=correct_answer,bg='green')
        AuthorizedPlayer.number_of_crystals -= 5
        crystal_label.config(text=AuthorizedPlayer.number_of_crystals,bg='red')
    else:
        message="Sorry! You don't have enough crystals!"
        hint_label.config(text=message,bg='red')
    root.after(2000, reset_crystal_color)

def crystal_mod():
    score = AuthorizedPlayer.score
    if score % 5 == 0 and score > 0:
        AuthorizedPlayer.number_of_crystals += 5
        crystal_label.config(bg='purple',text=AuthorizedPlayer.number_of_crystals)
    root.after(2000, reset_crystal_color)

def level_mod():
    level_func = 3*AuthorizedPlayer.level
    if AuthorizedPlayer.score/level_func == 1:
        AuthorizedPlayer.level += 1
        level_label.config(bg='blue',fg='white')
    else:
        pass
    level_label.config(text=AuthorizedPlayer.level)
    root.after(2000,reset_level_color)

def points_mod(answer):
    if answer == 1:
        AuthorizedPlayer.score += 1
        score_label.config(text=AuthorizedPlayer.score,bg='green')
    elif AuthorizedPlayer.score > 0:
        AuthorizedPlayer.score -= 1
        score_label.config(text=AuthorizedPlayer.score,bg='red')
    else:
        score_label.config(text=AuthorizedPlayer.score,bg='red')
    level_mod()
    crystal_mod()
    reset_hint()
    root.after(2000,reset_score_color)

def check_Level(req_lv):
    if AuthorizedPlayer.level >= req_lv :
        return True
    else:
        Message= "Sorry! You're not leveled up enough to play yet! You need to be level %s. Keep playing and come back soon!" % req_lv
        tkMessageBox.showwarning("Not Unlocked",Message,parent=root)
        return False

def reset_score_color():
    score_label.config(bg='white')

def reset_level_color():
    level_label.config(bg='white',fg='black')

def reset_crystal_color():
    crystal_label.config(bg='white')

def reset_hint():
    hint_label.config(text="\t\t\t",bg="white")

def change_image(game):
    global photo_display_label
    image='images/CoverImages/' + game + '.gif'
    cover_image = PhotoImage(master=root, file=image)
    photo_display_label = Label(root, bg="white", image=cover_image)
    photo_display_label.image = cover_image
    photo_display_label.grid(row=6, column=0, columnspan=4, sticky=EW)


def check_answer():
    ABCD = ["A","B","C","D" ]
    answer_index = answerVar.get() # Returns 0, 1, 2 or 3
    print "You selected answer", ABCD[answer_index]

    if correct_answer in answer_option[answer_index]:
        message_label.config(text="Correct!")
        points_mod(1)
    else:
        message_label.config(text="Wrong!")
        points_mod(0)
    ok_button.configure(text="Next", command = state_capital_game)

def state_flowers_game_check_answer():
    ABCD = ["A","B","C","D" ]
    answer_index = answerVar.get() # Returns 0, 1, 2 or 3
    print "You selected answer", ABCD[answer_index]

    if correct_answer in answer_option[answer_index]:
        message_label.config(text="Correct!")
        points_mod(1)
    else:
        message_label.config(text="Wrong!")
        points_mod(0)
    ok_button.configure(text="Next", command = state_flowers_game)

def double_game_check_answer():
    ABCD = ["A","B","C","D" ]
    answer_index = answerVar.get() # Returns 0, 1, 2 or 3
    print "You selected answer", ABCD[answer_index]

    if str(correct_answer) in str(answer_option[answer_index]):
        message_label.config(text="Correct!")
        points_mod(1)
    else:
        message_label.config(text="Wrong!")
        points_mod(0)
    ok_button.configure(text="Next", command = double_game)

def Vegetable_species_name_check_answer():
    ABCD = ["A","B","C","D" ]
    answer_index = answerVar.get() # Returns 0, 1, 2 or 3
    print "You selected answer", ABCD[answer_index]

    if correct_answer in answer_option[answer_index]:
        message_label.config(text="Correct!")
        points_mod(1)
    else:
        message_label.config(text="Wrong!")
        points_mod(0)
    ok_button.configure(text="Next", command = Vegetable_species_name_game)

def NBA_team_game_check_answer():
    ABCD = ["A","B","C","D" ]
    answer_index = answerVar.get() # Returns 0, 1, 2 or 3
    print "You selected answer", ABCD[answer_index]

    if correct_answer in answer_option[answer_index]:
        message_label.config(text="Correct!")
        points_mod(1)
    else:
        message_label.config(text="Wrong!")
        points_mod(0)
    ok_button.configure(text="Next", command = NBA_team_game)

def NFL_team_game_check_answer():
    ABCD = ["A","B","C","D" ]
    answer_index = answerVar.get() # Returns 0, 1, 2 or 3
    print "You selected answer", ABCD[answer_index]

    if correct_answer in answer_option[answer_index]:
        message_label.config(text="Correct!")
        points_mod(1)
    else:
        message_label.config(text="Wrong!")
        points_mod(0)
    ok_button.configure(text="Next", command = NFL_team_game)

def MLB_team_game_check_answer():
    ABCD = ["A","B","C","D" ]
    answer_index = answerVar.get() # Returns 0, 1, 2 or 3
    print "You selected answer", ABCD[answer_index]

    if correct_answer in answer_option[answer_index]:
        message_label.config(text="Correct!")
        points_mod(1)
    else:
        message_label.config(text="Wrong!")
        points_mod(0)
    ok_button.configure(text="Next", command = MLB_team_game)

def LOL_check_answer():
    ABCD = ["A","B","C","D" ]
    answer_index = answerVar.get() # Returns 0, 1, 2 or 3
    print "You selected answer", ABCD[answer_index]

    if correct_answer in answer_option[answer_index]:
        message_label.config(text="Correct!")
        points_mod(1)
    else:
        message_label.config(text="Wrong!")
        points_mod(0)
    ok_button.configure(text="Next", command = LOL_game)

def power_rangers_check_answer():

    ABCD = ["A","B","C","D" ]
    answer_index = answerVar.get() # Returns 0, 1, 2 or 3
    print "You selected answer", ABCD[answer_index]

    if correct_answer in answer_option[answer_index]:
        message_label.config(text="Correct!")
        points_mod(1)
    else:
        message_label.config(text="Wrong!")
        points_mod(0)
    ok_button.configure(text="Next", command = power_rangers_game)

def grammys_check_answer():
    ABCD = ["A","B","C","D" ]
    answer_index = answerVar.get() # Returns 0, 1, 2 or 3
    print "You selected answer", ABCD[answer_index]

    if correct_answer in answer_option[answer_index]:
        message_label.config(text="Correct!")
        points_mod(1)
    else:
        message_label.config(text="Wrong!")
        points_mod(0)
    ok_button.configure(text="Next", command = grammys_game)

def LOL_item_check_answer():
    ABCD = ["A","B","C","D" ]
    answer_index = answerVar.get() # Returns 0, 1, 2 or 3
    print "You selected answer", ABCD[answer_index]

    if correct_answer in answer_option[answer_index]:
        message_label.config(text="Correct!")
        points_mod(1)
    else:
        message_label.config(text="Wrong!")
        points_mod(0)
    ok_button.configure(text="Next", command = LOL_item_game)

def NBA_Star_check_answer():
    ABCD = ["A","B","C","D" ]
    answer_index = answerVar.get() # Returns 0, 1, 2 or 3
    print "You selected answer", ABCD[answer_index]

    if correct_answer in answer_option[answer_index]:
        message_label.config(text="Correct!")
        points_mod(1)
    else:
        message_label.config(text="Wrong!")
        points_mod(0)
    ok_button.configure(text="Next", command = NBA_Star_game)

def NBA_TEAM_LOGO_check_answer():
    ABCD = ["A","B","C","D" ]
    answer_index = answerVar.get() # Returns 0, 1, 2 or 3
    print "You selected answer", ABCD[answer_index]

    if correct_answer in answer_option[answer_index]:
        message_label.config(text="Correct!")
        points_mod(1)
    else:
        message_label.config(text="Wrong!")
        points_mod(0)
    ok_button.configure(text="Next", command = NBA_TEAM_LOGO_game)

def state_capital_game():
    if check_Level(3) == True:
        global correct_answer
        global answer_option
        ok_button.configure(text="OK", command = check_answer)
        change_image('state_capitol')

        next_question = MultipleChoiceQuestion(state_capitals)  # <- Generates a random question.
        question_label.config(text=next_question.question)  # Display the question in the GUI

        correct_answer = next_question.correct_answer
        print "The correct answer is:", correct_answer  # Solely for debugging.
        answer_option = next_question.answer_option
        print next_question.answer_option

        ABCD = ["A","B","C","D" ]
        for k in range(0,4):
            answer_button[k].config(text = ABCD[k] + ". " + answer_option[k])
        message_label.configure(text="Press OK to submit your answer.")
    else:
        pass

def double_game():
    if check_Level(1) == True:
        global correct_answer
        global answer_option
        change_image('double_game')
        ok_button.configure(text="OK", command = double_game_check_answer)

        next_question = MultipleChoiceQuestion(double_data)  # <- Generates a random question.
        question_label.config(text=next_question.question)  # Display the question in the GUI

        correct_answer = next_question.correct_answer
        print "The correct answer is:", correct_answer  # Solely for debugging.
        answer_option = next_question.answer_option
        print next_question.answer_option

        ABCD = ["A","B","C","D" ]
        for k in range(0,4):
            answer_button[k].config(text = ABCD[k] + ". " + str(answer_option[k]))
        message_label.configure(text="Press OK to submit your answer.")
    else:
        pass

def state_flowers_game():
    if check_Level(3) == True:
        global correct_answer
        global answer_option
        change_image('state_flower')
        ok_button.configure(text="OK", command = state_flowers_game_check_answer)

        next_question = MultipleChoiceQuestion(state_flowers)  # <- Generates a random question.
        question_label.config(text=next_question.question)  # Display the question in the GUI

        correct_answer = next_question.correct_answer
        print "The correct answer is:", correct_answer  # Solely for debugging.
        answer_option = next_question.answer_option
        print next_question.answer_option

        ABCD = ["A","B","C","D" ]
        for k in range(0,4):
            answer_button[k].config(text = ABCD[k] + ". " + answer_option[k])
        message_label.configure(text="Press OK to submit your answer.")
    else:
        pass

def Vegetable_species_name_game():
    if check_Level(4) == True:
        global correct_answer
        global answer_option
        change_image('vegetable')

        ok_button.configure(text="OK", command = Vegetable_species_name_check_answer)

        next_question = MultipleChoiceQuestion(Vegetable_species_name)  # <- Generates a random question.
        question_label.config(text=next_question.question)  # Display the question in the GUI

        correct_answer = next_question.correct_answer
        print "The correct answer is:", correct_answer  # Solely for debugging.
        answer_option = next_question.answer_option
        print next_question.answer_option

        ABCD = ["A","B","C","D" ]
        for k in range(0,4):
            answer_button[k].config(text = ABCD[k] + ". " + answer_option[k])
        message_label.configure(text="Press OK to submit your answer.")
    else:
        pass

def NBA_team_game():
    if check_Level(2) == True:
        global correct_answer
        global answer_option
        ok_button.configure(text="OK", command = NBA_team_game_check_answer)
        change_image('nba_team')

        next_question = MultipleChoiceQuestion(NBA_team)  # <- Generates a random question.
        question_label.config(text=next_question.question)  # Display the question in the GUI

        correct_answer = next_question.correct_answer
        print "The correct answer is:", correct_answer  # Solely for debugging.
        answer_option = next_question.answer_option
        print next_question.answer_option

        ABCD = ["A","B","C","D" ]
        for k in range(0,4):
            answer_button[k].config(text = ABCD[k] + ". " + answer_option[k])
        message_label.configure(text="Press OK to submit your answer.")
    else:
        pass

def NFL_team_game():
    if check_Level(2) == True:
        global correct_answer
        global answer_option
        ok_button.configure(text="OK", command = NFL_team_game_check_answer)
        change_image('nfl_team')

        next_question = MultipleChoiceQuestion(NFL_team)  # <- Generates a random question.
        question_label.config(text=next_question.question)  # Display the question in the GUI

        correct_answer = next_question.correct_answer
        print "The correct answer is:", correct_answer  # Solely for debugging.
        answer_option = next_question.answer_option
        print next_question.answer_option

        ABCD = ["A","B","C","D" ]
        for k in range(0,4):
            answer_button[k].config(text = ABCD[k] + ". " + answer_option[k])
        message_label.configure(text="Press OK to submit your answer.")
    else:
        pass

def MLB_team_game():
    if check_Level(2) == True :
        global correct_answer
        global answer_option
        ok_button.configure(text="OK", command = MLB_team_game_check_answer)
        change_image('mlb_team')

        next_question = MultipleChoiceQuestion(MLB_team)  # <- Generates a random question.
        question_label.config(text=next_question.question)  # Display the question in the GUI

        correct_answer = next_question.correct_answer
        print "The correct answer is:", correct_answer  # Solely for debugging.
        answer_option = next_question.answer_option
        print next_question.answer_option

        ABCD = ["A","B","C","D" ]
        for k in range(0,4):
            answer_button[k].config(text = ABCD[k] + ". " + answer_option[k])
        message_label.configure(text="Press OK to submit your answer.")
    else:
        pass

def LOL_game():
    if check_Level(2) == True:
        global correct_answer
        global answer_option
        ok_button.configure(text="OK", command = LOL_check_answer)
        change_image('league')

        next_question = MultipleChoiceQuestion(LOL)  # <- Generates a random question.
        question_label.config(text=next_question.question)  # Display the question in the GUI

        correct_answer = next_question.correct_answer
        print "The correct answer is:", correct_answer  # Solely for debugging.
        answer_option = next_question.answer_option
        print next_question.answer_option

        ABCD = ["A","B","C","D" ]
        for k in range(0,4):
            answer_button[k].config(text = ABCD[k] + ". " + answer_option[k])
        message_label.configure(text="Press OK to submit your answer.")
    else:
        pass

def power_rangers_game():
    if check_Level(4) == True:
        global correct_answer
        global answer_option
        ok_button.configure(text="OK", command = power_rangers_check_answer)
        change_image('red_rangers')

        next_question = MultipleChoiceQuestion(power_rangers)  # <- Generates a random question.
        question_label.config(text=next_question.question)  # Display the question in the GUI

        correct_answer = next_question.correct_answer
        print "The correct answer is:", correct_answer  # Solely for debugging.
        answer_option = next_question.answer_option
        print next_question.answer_option

        ABCD = ["A","B","C","D" ]
        for k in range(0,4):
            answer_button[k].config(text = ABCD[k] + ". " + answer_option[k])
        message_label.configure(text="Press OK to submit your answer.")
    else:
        pass

def grammys_game():
    if check_Level(4) == True:
        global correct_answer
        global answer_option
        ok_button.configure(text="OK", command = grammys_check_answer)
        change_image('grammy')
        next_question = MultipleChoiceQuestion(grammys)  # <- Generates a random question.
        question_label.config(text=next_question.question)  # Display the question in the GUI

        correct_answer = next_question.correct_answer
        print "The correct answer is:", correct_answer  # Solely for debugging.
        answer_option = next_question.answer_option
        print next_question.answer_option

        ABCD = ["A","B","C","D" ]
        for k in range(0,4):
            answer_button[k].config(text = ABCD[k] + ". " + answer_option[k])
        message_label.configure(text="Press OK to submit your answer.")
    else:
        pass

def LOL_item_game():
    if check_Level(3) == True:
        global correct_answer
        global answer_option
        change_image('blank')

        ok_button.configure(text="OK", command = LOL_item_check_answer)
        next_question = PictureQuestion(LOL_item,root,photo_display_label)  # <- Generates a random question.
        question_label.config(text=next_question.question)  # Display the question in the GUI

        correct_answer = next_question.correct_answer
        print "The correct answer is:", correct_answer  # Solely for debugging.
        answer_option = next_question.answer_option
        print next_question.answer_option

        ABCD = ["A","B","C","D" ]
        for k in range(0,4):
            answer_button[k].config(text = ABCD[k] + ". " + answer_option[k])
        message_label.configure(text="Press OK to submit your answer.")
    else:
        pass

def NBA_Star_game():
    if check_Level(4) == True:
        global correct_answer
        global answer_option
        ok_button.configure(text="OK", command = NBA_Star_check_answer)
        change_image('blank')

        next_question = PictureQuestion(NBA_STAR,root,photo_display_label)  # <- Generates a random question.
        question_label.config(text=next_question.question)  # Display the question in the GUI

        correct_answer = next_question.correct_answer
        print "The correct answer is:", correct_answer  # Solely for debugging.
        answer_option = next_question.answer_option
        print next_question.answer_option

        ABCD = ["A","B","C","D" ]
        for k in range(0,4):
            answer_button[k].config(text = ABCD[k] + ". " + answer_option[k])
        message_label.configure(text="Press OK to submit your answer.")
    else:
        pass

def NBA_TEAM_LOGO_game():
    if check_Level(1) == True:
        global correct_answer
        global answer_option
        ok_button.configure(text="OK", command = NBA_TEAM_LOGO_check_answer)
        change_image('blank')

        next_question = PictureQuestion(NBA_TEAM_LOGO,root,photo_display_label)  # <- Generates a random question.
        question_label.config(text=next_question.question)  # Display the question in the GUI

        correct_answer = next_question.correct_answer
        print "The correct answer is:", correct_answer  # Solely for debugging.
        answer_option = next_question.answer_option
        print next_question.answer_option

        ABCD = ["A","B","C","D" ]
        for k in range(0,4):
            answer_button[k].config(text = ABCD[k] + ". " + answer_option[k])
        message_label.configure(text="Press OK to submit your answer.")
    else:
        pass

mb.menu.add_radiobutton ( label="Double Trouble", variable=quizVar, command = double_game )
mb.menu.add_radiobutton ( label="NBA Team - Logo", variable=quizVar, command = NBA_TEAM_LOGO_game )
mb.menu.add_radiobutton ( label="NBA Team - City", variable=quizVar, command = NBA_team_game )
mb.menu.add_radiobutton ( label="NFL Team - City", variable=quizVar, command = NFL_team_game )
mb.menu.add_radiobutton ( label="MLB Team - City", variable=quizVar, command = MLB_team_game )
mb.menu.add_radiobutton ( label="League of Legends Champions", variable=quizVar, command = LOL_game )
mb.menu.add_radiobutton ( label="State Capitals", variable=quizVar, command = state_capital_game )
mb.menu.add_radiobutton ( label="State Flowers",  variable=quizVar, command = state_flowers_game )
mb.menu.add_radiobutton ( label="LOL Items", variable=quizVar, command = LOL_item_game )
mb.menu.add_radiobutton ( label="Vegetable Species Name", variable=quizVar, command = Vegetable_species_name_game )
mb.menu.add_radiobutton ( label="Power Rangers - Red Rangers", variable=quizVar, command = power_rangers_game )
mb.menu.add_radiobutton ( label="1987 Grammys", variable=quizVar, command = grammys_game )
mb.menu.add_radiobutton ( label="NBA Stars", variable=quizVar, command = NBA_Star_game )


# Add four radio buttons for the multiple choice answers.
answerVar = IntVar()  # A multiple choice answer corresponsing to A, B, C or D.
R1 = Radiobutton(root, text="A", variable=answerVar, value=0, command=None)
R1.grid(row=2, column=0, sticky=W, columnspan=2)

R2 = Radiobutton(root, text="B", variable=answerVar, value=1, command=None)
R2.grid(row=2, column=2, sticky=W, columnspan=2)

R3 = Radiobutton(root, text="C", variable=answerVar, value=2, command=None)
R3.grid(row=3, column=0, sticky=W, columnspan=2)

R4 = Radiobutton(root, text="D", variable=answerVar, value=3, command=None)
R4.grid(row=3, column=2, sticky=W, columnspan=2)
answer_button = [R1, R2, R3, R4]

message_label = Label(root, text="Press OK to submit your answer.", bg="gold", width = 50)
message_label.grid(row=5, columnspan=3, sticky=EW)

ok_button = Button(root, text="OK",  width = 20, command = check_answer)
ok_button.grid(row=5, column=3, sticky=EW)

change_image('Honolulu')

actual_name_label = Label(root, text=AuthorizedPlayer.user_name,bg='yellow',relief='raised').grid(row=7,column=1,columnspan=2)

Label(root, text="Score").grid(row=8,column=0)
score_label = Label(root, text=AuthorizedPlayer.score,relief='raised')
score_label.grid(row=8,column=1,columnspan=2)

Label(root, text="Level").grid(row=9, column=0)
level_label = Label(root, text=AuthorizedPlayer.level,relief='raised')
level_label.grid(row=9, column=1,columnspan=2)

Label(root, text='Crystals').grid(row=10,column=0)
crystal_label = Label(root, text=AuthorizedPlayer.number_of_crystals,relief='raised')
crystal_label.grid(row=10, column=1,columnspan=2)

Label(root, text='Hint').grid(row=11,column=0)
hint_label = Label(root, text='\t\t\t',relief='raised')
hint_label.grid(row=11,column=1,columnspan=2)
hint_button = Button(root, text="Need Hint?", command=get_hint).grid(row=11, column=3)

save_button = Button(root, text="Save", command=lambda x=0: save(x)).grid(row=12, column=0)
save_and_quit = Button(root, text="Save and Quit", command=lambda x=1: save(x)).grid(row=12, column=3)

root.mainloop()


