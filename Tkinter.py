'''
Author - Bharat Vyas
Description- Playing with Tkinter
To be made:

Tkinter window- DONE
frame- DONE
checkbuttons-DONE
buttons- DONE
widget- DONE
Label-DONE
menu-DONE
Image-DONE


'''

from tkinter import *
root = Tk()
root.geometry("500x600")
root.title("JARVIS")

root.configure(bg='skyblue')


def myfun():
    print("you clicked on button")
    exit(Tk)


def accept():
    print("Entered username is: {} \n and password is: {}\n".format(
        label1Ent.get(), label2Ent.get()))


lable_photo = Label(root, font=12, text="Welcome to my world!")
photo = PhotoImage(file="jar.png")  # image
bharat_lable2 = Label(image=photo)

bharat_lable2.grid(row=4, column=5)  # for packing in the window


lable_photo.grid(row=1, column=13)
frame = Frame(root, borderwidth=10, bg="red", relief=SUNKEN)
frame.grid(row=10, column=10)

checkB = Checkbutton(text="Do you like this GUI?", fg='red')
checkB.grid(row=10, column=5)

mybutton = Button(root, text='bye bye',
                  font="helvetica", command=myfun)
mybutton.grid(row=11, column=100)

label1 = Label(root, text='username',
               font="helvetica 20", background='skyblue')
label1.grid(row=5)

label2 = Label(root, text='password',
               background='skyblue', font="helvetica 20")
label2.grid(row=6)

label1val = StringVar()
lable2val = IntVar() and StringVar()

label1Ent = Entry(root, textvariable=label1val)
label2Ent = Entry(root, textvariable=lable2val)

label1Ent.grid(row=5, column=5)
label2Ent.grid(row=6, column=5)

# Button for accepting usename and password:

button_UP = Button(root, text='submit',
                   activebackground='red', font=20, command=accept)
button_UP.grid(row=8, column=5)

# let us create menus

mymenu = Menu(root)
m1 = Menu(mymenu)
m1.add_command(label="File", command=myfun)
m1.add_command(label="Save as")
root.config(menu=mymenu)

mymenu.add_cascade(label="file", menu=m1)

root.mainloop()
