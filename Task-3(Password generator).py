from tkinter import *
import string
import random
import pyperclip


def generator():
    passwordField.delete(0,END)
    small_alphabets=string.ascii_lowercase
    capital_alphabets=string.ascii_uppercase
    numbers=string.digits
    special_charecters=string.punctuation

    all=small_alphabets+capital_alphabets+numbers+special_charecters
    password_length=int(length_Box.get())

    if choice.get()==1:
        passwordField.insert(0,random.sample(small_alphabets,password_length))

    if choice.get()==2:
        passwordField.insert(0,random.sample(small_alphabets+capital_alphabets,password_length))

    if choice.get()==3:
        passwordField.insert(0,random.sample(all,password_length))


def copy():
    random_password=passwordField.get()
    pyperclip.copy(random_password)

def clear():
    passwordField.delete(0,END)

root=Tk()
root.config(bg='lightgray')
root.geometry("350x280")
root.title("Password generator by NA")
choice=IntVar()
Font=('arial',13,'bold')
passwordLabel=Label(root,text='🔑 Password Generator',font=('times new roman',20,'bold'),bg='lightgray',fg='black')
passwordLabel.place(x=30,y=10)
weakradioButton=Radiobutton(root,text='Weak',value=1,variable=choice,font=Font,bg='lightgray')
weakradioButton.place(x=25,y=60)
mediumradioButton=Radiobutton(root,text='Medium',value=2,variable=choice,font=Font,bg='lightgray')
mediumradioButton.place(x=115,y=60)

strongradioButton=Radiobutton(root,text='Strong',value=3,variable=choice,font=Font,bg='lightgray')
strongradioButton.place(x=215,y=60)

lengthLabel=Label(root,text='Password Length :',font=Font,bg='lightgray',fg='black')
lengthLabel.place(x=30,y=100)

length_Box=Spinbox(root,from_=5,to_=18,width=5,font=Font)
length_Box.place(x=200,y=100)

generateButton=Button(root,text='Generate',font=Font,command=generator)
generateButton.place(x=130,y=140)

passwordField=Entry(root,width=25,bd=2,font=('times new roman',18,'bold'))
passwordField.place(x=22,y=180)

copyButton=Button(root,text='Copy',font=Font,command=copy)
copyButton.place(x=115,y=230)

clearButton=Button(root,text='Clear',font=Font,command=clear)
clearButton.place(x=180,y=230)

root.mainloop()


