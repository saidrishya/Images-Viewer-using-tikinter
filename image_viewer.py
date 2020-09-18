from tkinter import *
from PIL import ImageTk, Image

root = Tk()

root.title("Image Viewer")
root.iconbitmap('emoji.ico')


img1 = ImageTk.PhotoImage(Image.open("1.jpg").resize((450,450)))
img2 = ImageTk.PhotoImage(Image.open("2.jpg").resize((450,450)))
img3 = ImageTk.PhotoImage(Image.open("3.jpg").resize((450,450)))
img4 = ImageTk.PhotoImage(Image.open("4.jpg").resize((450,450)))
img5 = ImageTk.PhotoImage(Image.open("5.jpg").resize((450,450)))

image_list = [img1, img2, img3, img4, img5]

status = Label(root, text = "Image 1 of " + str(len(image_list)), bd=1, relief = SUNKEN)

    


label = Label(image = img1)
label.grid(row=0, column=0, columnspan=3)
status.grid(row = 2, column = 2, columnspan=3)



def forward(number):
    global label
    global button_left
    global button_right
    global status
    #delete what's currently there
    label.grid_forget()
    label = Label(image = image_list[number-1])
    button_right = Button(root, text = ">", command = lambda: forward(number+1))
    button_left = Button(root, text = "<", command = lambda: backward(number-1))
    
    if number == 5:
        button_right = Button(root, text=">", state = DISABLED)

    button_left.grid(row=1, column=0)
    button_right.grid(row=1, column=2)
    label.grid(row=0, column=0, columnspan=3)
    status = Label(root, text = "Image " + str(number) + " of " + str(len(image_list)), bd=1, relief = SUNKEN)
    status.grid(row = 2, column = 2, columnspan=3)

   


def backward(number):
    global label
    global button_left
    global button_right
    global status

    label.grid_forget()
    label = Label(image = image_list[number-1])
    button_right = Button(root, text = ">", command = lambda: forward(number+1))
    button_left = Button(root, text = "<", command = lambda: backward(number-1))

    if number == 1:
        button_left = Button(root, text="<", state = DISABLED)

    button_left.grid(row=1, column=0)
    button_right.grid(row=1, column=2)
    label.grid(row=0, column=0, columnspan=3)
    status = Label(root, text = "Image " + str(number) + " of " + str(len(image_list)), bd=1, relief = SUNKEN)
    status.grid(row = 2, column = 2, columnspan=3)



    


button_left = Button(root, text = "<", command = backward)
button_quit = Button(root, text = "Exit Program", command = root.quit)
# 2 because we're currently on the first image and we will be moving forward to 2
button_right = Button(root, text = ">", command = lambda: forward(2))



button_left.grid(row=1, column=0)
button_quit.grid(row =1 , column=1)
button_right.grid(row=1, column=2)







root.mainloop()