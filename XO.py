import tkinter
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk

# Create instance
root = tk.Tk()

# Add a title
root.title('Tic-Tac-Toe')



player = 1
text_button = 'X'
number_button_dict = {}
list_shomare_player_1 = []
list_shomare_player_2 = []
color_button = 'Red'

def click_me(Button_user, number_button):

    global player
    if player == 1:
        text_button = 'X'
        list_shomare_player_1.append(number_button)
        color_button = 'Blue'
    else:
        text_button = 'O'
        list_shomare_player_2.append(number_button)
        color_button = 'Gold'

    Button_user['text'] = text_button
    Button_user.configure(state='disabled')
    Button_user.configure(background=color_button)
    number_button_dict[number_button] = Button_user['text']

    test_barande(player)


def test_barande(number_player):

    global player
    if number_player == 1:
        player = 2
        list_shomare_button = list_shomare_player_1
    if number_player == 2:
        list_shomare_button = list_shomare_player_2
        player = 1

    for i in (1,4,7):
        if i in list_shomare_button and i+1 in list_shomare_button and i+2 in list_shomare_button:
            print(f'{number_player} barande')
            display_all_button(number_player)

    for i in (1,2,3):
        if i in list_shomare_button and i + 3 in list_shomare_button and i + 6 in list_shomare_button:
            print(f'{number_player} barande')
            display_all_button(number_player)

    if 1 in list_shomare_button and 5 in list_shomare_button and 9 in list_shomare_button:
        print(f'{number_player} barande')
        display_all_button(number_player)

    if 3 in list_shomare_button and 5 in list_shomare_button and 7 in list_shomare_button:
        print(f'{number_player} barande')
        display_all_button(number_player)



def display_all_button(number_player):

    for i in (b1,b2,b3,b4,b5,b6,b7,b8,b9):
        i.configure(state='disabled')

    messagebox.showinfo('Finish!',message=f'player number {number_player} won!      ')








b1 = tk.Button(root, text="1", width=20,height=10, command=lambda : click_me(b1,1))
b2 = tk.Button(root, text="2", width=20,height=10, command=lambda : click_me(b2,2))
b3 = tk.Button(root, text="3", width=20,height=10, command=lambda : click_me(b3,3))
b4 = tk.Button(root, text="4", width=20,height=10, command=lambda : click_me(b4,4))
b5 = tk.Button(root, text="5", width=20,height=10, command=lambda : click_me(b5,5))
b6 = tk.Button(root, text="6", width=20,height=10, command=lambda : click_me(b6,6))
b7 = tk.Button(root, text="7", width=20,height=10, command=lambda : click_me(b7,7))
b8 = tk.Button(root, text="8", width=20,height=10, command=lambda : click_me(b8,8))
b9 = tk.Button(root, text="9", width=20,height=10, command=lambda : click_me(b9,9))



b1.grid(column=0, row=0)
b2.grid(column=1, row=0)
b3.grid(column=2, row=0)
b4.grid(column=0, row=1)
b5.grid(column=1, row=1)
b6.grid(column=2, row=1)
b7.grid(column=0, row=2)
b8.grid(column=1, row=2)
b9.grid(column=2, row=2)



root.mainloop()
