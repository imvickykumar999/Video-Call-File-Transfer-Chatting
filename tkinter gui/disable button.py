from tkinter import Tk, Button, GROOVE

root = Tk()

def appear(index, letter):
    # This line would be where you insert the letter in the textbox
    print(letter)

    # Disable the button by index
    buttons[index].config(state="disabled")

letters=["A", "T", "D", "M", "E", "A", "S", "R", "M"]

# A collection (list) to hold the references to the buttons created below
buttons = []

for index in range(9):
    n=letters[index]

    button = Button(root, bg="White", text=n, width=5, height=1, relief=GROOVE,
                    command=lambda index=index, n=n: appear(index, n))

    # Add the button to the window
    button.grid(padx=2, pady=2, row=int(index%3), column=int(index/3))

    # Add a reference to the button to 'buttons'
    buttons.append(button)

root.mainloop()
