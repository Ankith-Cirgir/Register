from tkinter import *

def main_screen():
    global screen
    screen = Tk()
    screen.geometry("600x600")
    screen.title("MAIN")
    Label(text="LOGIN",bg = "grey", height = '2', width = '600', font = ("calibri", 13)).pack()
    Label(text = "").pack()
    Button(text = "LOGIN", height = '2', width = '30', command = login).pack()
    Label(text = "").pack()
    Button(text = 'NEW USER !',height = '2', width = '30',command = register).pack()


def register():
    global Rscreen,Username_val,Password_val,Username,Password
    Rscreen = Toplevel (screen)
    Rscreen.title("REGISTER")
    Rscreen.geometry('600x600')
    Username = StringVar()
    Password = StringVar()
    Label(Rscreen,text = 'Please fill your details: ').pack()
    Label(Rscreen,text = '').pack()
    Label(Rscreen,text = "Username: ").pack()
    Username_val = Entry(Rscreen,textvariable = Username)
    Username_val.pack()
    Label(Rscreen,text = "").pack()
    Label(Rscreen,text = "Password: ").pack()
    Password_val = Entry(Rscreen,textvariable = Password)
    Password_val.pack()
    Label(Rscreen,text = "").pack()
    Button(Rscreen,text = 'Register',height = '1', width = '10', command = register_user).pack()


def register_user():
    u = Username.get()
    p = Password.get()
    fname = 'U&P.txt' 
    f = open(fname, "a")
    f.write('Username:'+u+"\n"+'Password:'+p+'\n')
    f.close()
    Username_val.delete(0, END)
    Password_val.delete(0, END)
    Label(Rscreen,text = 'Registration Succesful !!', fg = 'green', font = ("calibri", 11)).pack()
    
def login():
    global Lscreen,Username_verify,Username_val1,Password_verify,Password_val1
    Lscreen = Toplevel(screen)
    Lscreen.title("LOGIN")
    Lscreen.geometry("600x600")
    Username_verify = StringVar()
    Password_verify = StringVar()
    Label(Lscreen,text = 'Username:').pack()
    Username_val1 = Entry(Lscreen, textvariable = Username_verify)
    Username_val1.pack()
    Label(Lscreen,text = "").pack()
    Label(Lscreen,text = 'Password:').pack()
    Password_val1 = Entry(Lscreen, textvariable = Password_verify)
    Password_val1.pack()
    Label(Lscreen,text = "").pack()
    Button(Lscreen,text = 'Login',height = '1', width = '10',command = login_verify).pack()

def login_verify():
    U = Username_verify.get()
    P = Password_verify.get()
    fname = 'U&P.txt'
    file = open(fname, 'r+')
    flag = 1
    exist = 0
    for line in file:
        flag += 1
        if flag == 0:
            if 'Password:'+P+'\n' == line:
                Label(Lscreen,text = 'Correct Password...', fg ="green").pack()
                print("Correct password")
            else:
                Label(Lscreen,text = 'Wrong Password !!!', fg = 'red').pack()
                print("Wrong Password")
        if 'Username:'+U+'\n' == line:
            Label(Lscreen,text = "User Exist...", fg = 'green').pack()
            exist = 1
            print("Username exist")
            flag = -1
    if exist == 0:
        Label(Lscreen, text = 'User don\'t exist !!!', fg = 'red').pack()
        print("User don\'t exist !!!")

    
    Username_val1.delete(0, END)
    Password_val1.delete(0, END)

    
main_screen()
