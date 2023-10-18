from tkinter import *
from tkinter import ttk
import tkinter
from PIL import Image, ImageTk
from customtkinter import *
from dark_title_bar import *

# Define functions
def BMI():
    h = float(Height.get())
    w = float(Weight.get())
    m = h / 100  # convert height into meters
    bmi = round(float(w / m**2), 1)
    label1.config(text=bmi)
    
    # Get the selected gender
    if gender_var.get() == "Male":
        if bmi <= 18.5:
            label3.config(text='''You have lower weight than
normal body for a Male.''')
            label2.config(text="Underweight!")
        elif bmi > 18.5 and bmi <= 25:
            label3.config(text="You have a normal \nbody weight for a Male.")
            label2.config(text="Normalweight!")
        else:
            label3.config(text="You have higher weight than\n normal body for a Male.")
            label2.config(text="Overweight!")
    else:
        if bmi <= 18.5:
            label3.config(text="You have lower weight than \nnormal body for a Female.")
            label2.config(text="Underweight!")
        elif bmi > 18.5 and bmi <= 25:
            label3.config(text="You have a normal body\n weight for a Female.")
            label2.config(text="Normalweight!")
        else:
            label3.config(text="You have higher weight than\n normal body for a Female.")
            label2.config(text="Overweight!")

def get_current_value():
    return '{:.0f}'.format(current_value.get())

def slider_changed(event):
    Height.set(get_current_value())
    size = int(float(get_current_value()))
    img = Image.open("Images/man.png")
    resized_image = img.resize((60, 75 + size)) 
    photo2 = ImageTk.PhotoImage(resized_image)
    secondimage.config(image=photo2)
    secondimage.place(x=70, y=493-size)
    secondimage.image = photo2

def get_current_value2():
    return '{:.0f}'.format(current_value2.get())

def slider_changed2(event):
    Weight.set(get_current_value2())

# Create the root window
root = Tk()
root.title("BMI Calculator")
root.geometry("470x580")  # Increased height to accommodate radio buttons
root.resizable(False, False)
dark_title_bar(root)

set_appearance_mode(root)

# Icon
image_icon = PhotoImage(file="Images/icon.png")
root.iconphoto(False, image_icon)

# Background Image
background_image = Image.open("images/BMI (2).png")
background_photo = ImageTk.PhotoImage(background_image)
background_label = Label(root, image=background_photo)
background_label.place(relwidth=1, relheight=1)

# Slider1
current_value = tkinter.DoubleVar()

slider = CTkSlider(master=root, from_=0, to=200, width=150, number_of_steps=200, command=slider_changed, variable=current_value,
                   button_color="#0097B2", bg_color="#191919", orientation="horizontal")
slider.place(x=31, y=235)

# Slider2
current_value2 = tkinter.DoubleVar()

slider2 = CTkSlider(master=root, from_=0, to=200, number_of_steps=200, width=150, command=slider_changed2, variable=current_value2,
                   button_color="#0097B2", bg_color="#191919", orientation="horizontal")
slider2.place(x=293, y=235)

# Entry boxes
Height = StringVar()
Weight = StringVar()
height = CTkEntry(master=root, textvariable=Height, placeholder_text="Start typing...", font=('Segoe Ui Blod', 70), width=148, fg_color="#181818", height=90,
                text_color="#0097B2", border_color="#181818", bg_color="#181818")
height.place(x=31, y=120)
weight = CTkEntry(master=root, textvariable=Weight, placeholder_text="Start typing...", font=('Segoe Ui Blod', 70), width=148, fg_color="#181818", height=93,
                text_color="#0097B2", border_color="#181818", bg_color="#181818")
weight.place(x=293, y=120)

# Man image
secondimage = Label(root, bg="#0097B2")
secondimage.place(x=70, y=530)

# Radio Buttons
gender_var = StringVar()
male_radio = CTkRadioButton(master=root, text="Male", variable=gender_var, value="Male", fg_color="#0097B2", font=("Segoe Ui", 12), bg_color="#191919",height=35, width=5,)
male_radio.place(x=195, y=200)
female_radio = CTkRadioButton(master=root, text="Female", variable=gender_var, value="Female", fg_color="#0097B2", font=("Segoe Ui", 12), bg_color="#191919",height=35, width=5,)
female_radio.place(x=195, y=165)

# Button
btn = CTkButton(master=root, text="View BMI", corner_radius=15, fg_color="#1B4A9B", height=35, width=5,
                font=("Segoe Ui",13),hover_color="#0097B2", bg_color="#191919", command=BMI)
btn.place(x=191, y=125)

# Labels
label1 = Label(root, font="arial 23 bold", fg="#0097B2", bg="#1B4A9B")
label1.place(x=322, y=350)
label2 = Label(root, font="arial 20 bold", fg="#0097B2", bg="#1B4A9B")
label2.place(x=250, y=410)
label3 = Label(root, font="arial 13 bold", fg="#0097B2", bg="#1B4A9B")
label3.place(x=226, y=490)

def open_link():
    import webbrowser
    webbrowser.open("https://www.youtube.com")

img = Image.open("images/info.png")

btn = CTkButton(master=root, text="", corner_radius=5, fg_color="#191919",
                hover_color="#1B4A9B", bg_color="#191919", height=5, width=5,
                image=CTkImage(dark_image=img, light_image=img), command=open_link)
btn.place(x=440, y=0)

# Start the main loop
root.mainloop()
