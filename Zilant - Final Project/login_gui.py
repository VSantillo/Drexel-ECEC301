from Tkinter import *
import tkMessageBox
from topsecret import *
import time

wrong_pass = 0


def open_game(currentplay,user):
    temp = open('temppass.txt','w')
    name = user + "\n"
    temp.write(name)
    if currentplay == 'current':
        items = player_stats[user].values() # loads up all of the item VALUES
        print items
        for item in items:
            object = str(item) + '\n'
            temp.write(object) # dump into a new file, to be called in game GUI
        temp.close()
    else:
        temp.write('100\n') # number of new crystals
        temp.write('0\n') # score number
        temp.write('1\n') # current level
        temp.close()
    lw.destroy()
    import game_GUI

def check_pass(user,word):
    global wrong_pass
    player_list = player.keys()
    if word != player[user]:
        password.config(show="")
        message = "INCORRECT PASSWORD"
        password.delete(0,END)
        password.config(background='red')
        wrong_pass += 1
        password.insert(0,message)
    elif word == player[user]:
        password.config(background='green')
        return 1
    if wrong_pass == 3:
        title = "!!!!! WARNING !!!!!"
        message = "HACKER DETECTED\nSHUTTING DOWN"
        tkMessageBox.showwarning(title,message, parent=lw)
        lw.after(5000,lw.destroy())

def check_user(name):
    player_list = player.keys()
    if name not in player_list:
        message = "INCORRECT USERNAME"
        username.delete(0,END)
        username.config(background='red')
        username.insert(0,message)
        if password.get():
            password.config(show="")
            message = "INCORRECT PASSWORD"
            password.delete(0,END)
            password.config(background='red')
            password.insert(0,message)
    else:
        username.config(background='green')
        return 1

def login_func():
    user = username.get()
    word = password.get()

    valid_player = check_user(user)
    if valid_player == 1:
        valid_pass = check_pass(user,word)
        if valid_pass == 1:
            open_game('current',user)
        else:
            lw.after(2000,reset_password)
    else:
        lw.after(2000,reset_user)

def reset_user():
    username.config(background='white')
    username.delete(0,END)
    password.config(background='white',show="*")
    password.delete(0,END)

def reset_password():
    password.config(background='white',show="*")
    password.delete(0,END)

def new_user():
    user = username.get()
    word = password.get()
    player_list = player.keys()
    if user in player_list:
        message="Sorry! That name is taken! Please Try Another"
        tkMessageBox.showwarning("Taken Name",message,parent=lw)
        print message
    else:
        new_player = "{'" + user  + "':'" + word +  "'}"
        with open('topsecret.py','ab') as fo:
            new_player='\nplayer.update(' + new_player + ')'
            new_stats='\nplayer_stats.update({"' + user + '": {"score":"0", "level":"1", "crystals":"100"} })\n'
            fo.write(new_player)
            fo.write(new_stats)
        fo.close()
        open_game('new',user)

lw = Tk()
lw.title('ZILANT LOGIN')
lw.attributes('-topmost',1)
lw.configure(background='black')
Label(lw, text="Player Name",bg='black',fg='white',justify='left').grid(row=7,column=3)
Label(lw, text="Password",bg='black',fg='white',anchor='e').grid(row=8,column=3)
new_player_label = Label(lw, text="Please enter your user name, or if you're a new player, type your desired username and password in the text boxes below and hit 'New Player'",bg='black',fg='white',justify='center').grid(row=6,column=3,columnspan=7)

username = Entry(lw)
password = Entry(lw)

password.config(show="*") # hides the password)

username.grid(row=7,column=4)
password.grid(row=8,column=4)

Button(lw, text="Login", command=login_func).grid(row=9,column=3)
Button(lw, text="New Player", command=new_user).grid(row=9, column=4)
Button(lw, text="Quit",command=lw.quit).grid(row=9, column=5)

my_image = PhotoImage(file="images/Zilant.gif")
photo_label = Label(lw, bg="black", image=my_image)
photo_label.grid(row=0, rowspan=5, column=3,columnspan=3)


lw.mainloop()

