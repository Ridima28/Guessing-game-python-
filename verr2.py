from tkinter import  *
import random

window = Tk()
window.title("Guess The Number Game")
window.configure(bg="#0b1220")   
window.geometry("600x500")


welcome = Frame(window, bg = "black")
welcome.pack(fill="both", expand=True)

top_spacer = Frame(welcome, bg="black")
top_spacer.pack(fill="both", expand=True)

label1 = Label(welcome, text = "Welcome to guessing game!",
            bg = "black",
            fg = "#4cc9ff",
            font = ("Arial", 25, "bold"))
label1.pack()

label2 = Label(welcome, text = "Press start button",
            bg = "black",
            fg = "#bdebff",
            font = ("Arial", 15, "bold"))
label2.pack()
num = None
chances = 10

def start():
    global num
    num = random.randint(1,50)
    chances = 10
    result_label.config(text="You have 10 chances.")
    entry.delete(0, END)

    welcome.pack_forget()
    title_frame.pack(fill = "x")

button = Button(welcome, text = "start", font = ("Arial", 20),
                bg = "#1C4D8D",
                 fg = "white" ,
                 command = start)
button.pack()
bottom_spacer = Frame(welcome, bg="black")
bottom_spacer.pack(fill="both", expand=True)


title_frame = Frame(window, bg="#0b1220")

label = Label(
    title_frame,
    text="Guess number between 1-50!",
    font= ("Arial", 25, "bold"),
    fg="#4cc9ff",   
    bg="#0b1220")
label.pack()

entry = Entry(
    title_frame,
    font=("Arial", 15),
    bg="#BDE8F5",
    fg="black",
    width=15,
    justify="center"
)
entry.pack(pady=5)


result_label = Label(
    title_frame,
    text="",
    bg="#0b1220",
    fg="white",
    font=("Arial", 12)
)
result_label.pack(pady=5)


def game():
    global num, chances
    guess = entry.get()
    if not guess.isdigit():
        result_label.config(text="Enter a valid number.")
        return
    user_guess = int(guess)

    if user_guess == num:
       result_label.config(text = "You gussed it right, You WON! ")
       return

    elif user_guess<num:
        chances -= 1 
        result_label.config(text =f"Your guess is too low, chances left:  {chances}")
        
    elif user_guess > num: 
        chances -= 1
        result_label.config(text = f"Your guess is too high, chances left:  {chances}")
        
    if chances <= 0 and user_guess!= num:
        result_label.config(text =f"You lost all chances, number was:  {num}")
        
    entry.delete(0, END)


button2 = Button(title_frame , text = "Check", 
                 bg = "#79C9C5",
                 fg = "white",
                 command = game)

button2.pack(pady  = 10)


window.mainloop()
