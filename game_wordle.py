from random import randint
import tkinter as tk

win = tk.Tk()

# getting a list of possible words  C:\\myDocument\\python\\python_project_words_game\\
with open("five_letter_russian_nouns.txt", 'r', encoding="utf-8") as file_in:
    list_words = list(map(str.strip, file_in.readlines()))
# choosing a word to guess
hidden_word = list_words[randint(1, len(list_words))].lower()

guessed_word = "You guessed the word"
word_not_in_dictionary = "Word is not in dictionary"
enter_word_txt = "Enter your word: "
you_l = "YOU LOSE! it was: "
new_game = "new game -> Enter, exit the game -> Clear"

russian_keyboard_layout = ('ЙЦУКЕНГШЩЗХЪ', 'ФЫВАПРОЛДЖЭ', 'ЯЧСМТИЬБЮЁ')
list_of_keyboard_letters_label = []

list_of_attempts = [["" for i in range(5)] for k in range(6)]
list_of_attempts_label = []

list_of_entered_letter = ['', '', '', '', '']
list_of_entered_letter_labels = []

game_continues = True


def start_new_game() -> None:
    global game_continues
    game_continues = True
    global hidden_word
    hidden_word = list_words[randint(1, len(list_words))].lower()

    global list_of_attempts
    list_of_attempts = [["" for i in range(5)] for k in range(6)]

    # clear list_of_attempts_label
    for i in range(6):
        for k in range(5):
            list_of_attempts_label[i][k]["text"] = ""
            list_of_attempts_label[i][k]["bg"] = "SystemButtonFace"

    global list_of_entered_letter
    list_of_entered_letter = ['', '', '', '', '']

    # clear list_of_entered_letter_labels
    for i in range(5):
        list_of_entered_letter_labels[i]["text"] = ''

    # clear color on keyboard
    for i in range(3):
        for k in range(len(list_of_keyboard_letters_label[i])):
            list_of_keyboard_letters_label[i][k]["bg"] = "SystemButtonFace"

    # letter_instructions -> new game
    letter_instructions["text"] = enter_word_txt
    letter_instructions["bg"] = "SystemButtonFace"


def find_the_letter_to_color(letter: str, color: str) -> None:
    for i in range(3):
        for k in range(len(list_of_keyboard_letters_label[i])):
            if letter == list_of_keyboard_letters_label[i][k]["text"]:
                # check it's already painted over
                if list_of_keyboard_letters_label[i][k]["bg"] != "red":
                    list_of_keyboard_letters_label[i][k]["bg"] = color


def enter_letter(*args) -> None:
    for i in range(5):
        if list_of_entered_letter[i] == '':
            list_of_entered_letter[i] = args[0]
            list_of_entered_letter_labels[i]["text"] = args[0]
            break


def clear_letter() -> None:
    # close window
    if letter_instructions["text"] == new_game:
        win.destroy()

    else:
        for i in range(4, -1, -1):
            if list_of_entered_letter[i] != '':
                list_of_entered_letter[i] = ''
                list_of_entered_letter_labels[i]["text"] = ''
                break


def enter_word() -> None:
    if letter_instructions["text"] == new_game:
        # start new game
        start_new_game()
    elif list_of_attempts[5][0] != "" or not game_continues:
        letter_instructions["text"] = new_game
    else:
        enter_word1()


def enter_word1() -> None:
    global game_continues
    if ''.join(list_of_entered_letter).lower() not in list_words:
        letter_instructions["text"] = word_not_in_dictionary

    else:
        # check and color letters on keyboard
        # check for the presence of letters
        # write the word to the list of attempts ( list_of_attempts and list_of_attempts_label)

        for i in range(6):
            if list_of_attempts[i][0] == '':
                for k in range(5):
                    list_of_attempts[i][k] = list_of_entered_letter[k]
                for k in range(5):
                    list_of_attempts_label[i][k]["text"] = list_of_entered_letter[k]

                # color the letters
                for k in range(5):
                    if list_of_entered_letter[k].lower() in list(hidden_word):
                        list_of_attempts_label[i][k]["bg"] = "yellow"
                        find_the_letter_to_color(list_of_entered_letter[k], "yellow")
                    else:
                        list_of_attempts_label[i][k]["bg"] = "grey"
                        find_the_letter_to_color(list_of_entered_letter[k], "grey")

                    if list_of_entered_letter[k].lower() == hidden_word[k]:
                        list_of_attempts_label[i][k]["bg"] = "red"
                        find_the_letter_to_color(list_of_entered_letter[k], "red")

                # check whether you guessed the word or not
                if ''.join(list_of_entered_letter).lower() == hidden_word:
                    letter_instructions["text"] = guessed_word
                    letter_instructions["bg"] = "red"
                    game_continues = False

                # checking whether all attempts have been used
                if list_of_attempts[5][0] != "" and game_continues:
                    letter_instructions["text"] = you_l + hidden_word.upper()

                # clean list and label entered
                for k in range(5):
                    list_of_entered_letter_labels[k]["text"] = ""
                    list_of_entered_letter[k] = ""

                break

            """
            red indicates the guessed position of the letter, 
            yellow indicates the presence of the letter in the word
            gray the missing letter in the word
            """

            if letter_instructions["text"] != guessed_word and letter_instructions["text"] != you_l+hidden_word.upper():
                letter_instructions["text"] = enter_word_txt


# label for entered letters
def draw_list_of_entered_letter(list_entered_l: list) -> None:  # list_of_entered_letter
    for i in range(5):
        letter_label1 = tk.Label(win, text=list_entered_l[i],
                                 # bg="red",
                                 # fg="white",
                                 font=("Aril", 15, 'bold'),
                                 relief=tk.RAISED
                                 )
        list_of_entered_letter_labels.append(letter_label1)
    for i in range(5):
        list_of_entered_letter_labels[i].grid(row=7, column=7 + i, stick="nsew")


win.title("Game Wordle")
win.geometry("1050x450+50+50")
win.minsize(1050, 450)
win.maxsize(1200, 700)
win.resizable(True, True)
photo = tk.PhotoImage(file="logo-kolba-512.png")
win.iconphoto(False, photo)
win.config(bg="#B5FDF1")
minsize_label = 50

# window layout with grid
for i in range(20):
    if i == 6:
        win.grid_columnconfigure(i, minsize=100)
    else:
        win.grid_columnconfigure(i, minsize=minsize_label)

for i in range(9):
    win.grid_rowconfigure(i, minsize=minsize_label)

button_label = tk.Label(win, text="",
                        # bg="red",
                        # fg="white",
                        font=("Aril", 15, 'bold'),
                        relief=tk.RAISED
                        )

for i in range(3):
    list_of_keyboard_letters_label_row = []
    for k in range(len(russian_keyboard_layout[i])):
        letter_label = tk.Button(win, text=russian_keyboard_layout[i][k],
                                 # bg="red",
                                 # fg="white",
                                 font=("Aril", 15, 'bold'),
                                 relief=tk.RAISED,
                                 )
        letter_label.config(command=lambda ll=letter_label: enter_letter(ll['text']))
        list_of_keyboard_letters_label_row.append(letter_label)
    list_of_keyboard_letters_label.append(list_of_keyboard_letters_label_row)

for i in range(6):
    list_of_attempts_label_row = []
    for k in range(5):
        letter_label = tk.Label(win, text=list_of_attempts[i][k],
                                # bg="red",
                                # fg="white",
                                font=("Aril", 15, 'bold'),
                                relief=tk.RAISED
                                )
        list_of_attempts_label_row.append(letter_label)
    list_of_attempts_label.append(list_of_attempts_label_row)

for i in range(3):
    for k in range(len(russian_keyboard_layout[i])):
        list_of_keyboard_letters_label[i][k].grid(row=i + 1, column=k + 7, stick="nsew")

for i in range(6):
    for k in range(5):
        list_of_attempts_label[i][k].grid(row=i + 1, column=k + 1, stick="nsew")

# label for instructions
letter_instructions = tk.Label(win, text=enter_word_txt,
                               # bg="red",
                               # fg="white",
                               font=("Aril", 15, 'bold'),
                               relief=tk.RAISED
                               )

letter_instructions.grid(row=5, column=7, columnspan=9, stick="nsew")

# button for reaction
button_of_enter = tk.Button(win, text="ENTER", command=enter_word)

button_of_enter.grid(row=7, column=14, columnspan=2, stick="nsew")

# button for clear
button_of_enter = tk.Button(win, text="CLEAR", command=clear_letter)

button_of_enter.grid(row=7, column=17, columnspan=2, stick="nsew")

# draw label for entered letters
draw_list_of_entered_letter(list_of_entered_letter)

win.mainloop()
