import tkinter as tk

continue_button_clicked = False
player1_name = ''
player2_name = ''


def create_player1_input(window):
    frame = tk.Frame(window, name="player1_frame", bg="black", padx=20, pady=20)
    frame.pack(side=tk.LEFT)

    label = tk.Label(
        frame, text="Player 1 Name:", fg="white", bg="black", font=("Arial", 20)
    )
    label.pack()

    entry = tk.Entry(frame, name='player1_entry', font=("Arial", 16))
    entry.pack()

    name_label = tk.Label(frame, text="", fg="blue", bg="black", font=("Arial", 14))
    name_label.pack()


def create_player2_input(window):
    frame = tk.Frame(window, name="player2_frame", bg="black", padx=20, pady=20)
    frame.pack(side=tk.RIGHT)

    label = tk.Label(
        frame, text="Player 2 Name:", fg="white", bg="black", font=("Arial", 20)
    )
    label.pack()

    entry = tk.Entry(frame, name='player2_entry', font=("Arial", 16))
    entry.pack()

    name_label = tk.Label(frame, text="", fg="blue", bg="black", font=("Arial", 14))
    name_label.pack()


def create_continue_button(window):
    button = tk.Button(
        window,
        text="CONTINUE",
        command=lambda: handle_continue_button(window),
        font=("Arial", 20),
        bg="white",
        padx=10,
        pady=5,
    )
    button.pack()
    button.place(relx=0.5, rely=0.5, anchor="center")


def handle_continue_button(window):
    global continue_button_clicked, player1_name, player2_name

    player1_name = window.nametowidget('player1_frame.player1_entry').get()
    player2_name = window.nametowidget('player2_frame.player2_entry').get()
    if not player1_name or not player2_name:
        return

    continue_button_clicked = True
    window.destroy()


def display_name_selection():
    window = tk.Tk()

    width = window.winfo_screenwidth()
    height = window.winfo_screenheight()
    window.geometry(f'{width}x{height}')
    window.configure(bg="black")

    window.title("Player Names")

    create_player1_input(window)
    create_player2_input(window)

    create_continue_button(window)

    window.mainloop()

    return continue_button_clicked, player1_name, player2_name
