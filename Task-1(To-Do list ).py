import customtkinter as ctk
from tkinter import*
from tkinter import messagebox
# from PIL import Image,ImageTk
color1='#190482'
app=ctk.CTk()
app.title("To-Do List")
app.geometry('350x500')
app.resizable('false','false')
app.config(bg=color1)

font1=('roboto',30,'bold')
font2=('arial',18,'bold')
font3=('arial',11,'bold')


# functions;
def add_task():
    task=task_entry.get()
    
    if task:
        task_list.insert(0,f"{task}.")
        task_entry.delete(0,END)
        # save_tasks()
    else:
        messagebox.showerror('error','Enter a task.')
    save_task()

def remove_task():
    selected= task_list.curselection()
    if selected:
        task_list.delete(selected[0])
    else:
        messagebox.showerror('error','Choose a task to delete')
    save_task()

def remove_all_task():
   task_list.delete(0,END)
   save_task()
       
def save_task():
    with open("tasks.txt","w") as f:
        tasks=task_list.get(0,END)
        for task in tasks:
           f.write(task+"\n")  
        f.close()

def load_task():
    try:
        with open("tasks.txt","r") as f:
            tasks=f.readlines()
            for task in tasks:
                task_list.insert(0,task.strip())
            f.close()
    except FileNotFoundError:
        pass
title_label=ctk.CTkLabel(app,font=font1,text="To-Do list",text_color='#fff',bg_color=color1)
title_label.place(x=140,y=10)

title_label1=ctk.CTkLabel(app,font=font1,text="📝",bg_color=color1,text_color='#fff')
title_label1.place(x=100,y=8)

# title_img=Image.open("asset\image1.png").resize((40,40))
# Label(app,image=title_img,bg='#09112e').place(x=20,y=10)

add_btn=ctk.CTkButton(app,command=add_task,font=font2,text_color='#fff',text='Add Task',fg_color='#63cc1d',hover_color='#06911f',bg_color=color1,cursor='hand2',corner_radius=5,width=120)
add_btn.place(x=40,y=110)


delete_btn=ctk.CTkButton(app,command=remove_task,font=font2,text_color='#fff',text='Remove Task',fg_color='#ff1717',hover_color='#ba0404',bg_color=color1,cursor='hand2',corner_radius=5,width=120)
delete_btn.place(x=170,y=110)

task_entry=ctk.CTkEntry(app,font=font2,text_color='#000',fg_color='#fff',border_color='#000',width=300,bg_color=color1)
task_entry.place(x=25 , y=70)

task_list=Listbox(app,font=font3,height=15,width=37)
task_list.place(x=25,y=150)

remove_all_btn=ctk.CTkButton(app,command=remove_all_task,font=font2,text_color='#fff',text='Remove All',fg_color='#ff1717',hover_color='#ba0404',bg_color=color1,cursor='hand2',corner_radius=5,width=120)
remove_all_btn.place(x=100,y=450)


load_task()
app.mainloop()