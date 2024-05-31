import tkinter as tk

continue_button_clicked = False
good_player_name = ''
evil_player_name = ''


def create_good_player_input(window):
    frame = tk.Frame(window, name="good_player_frame", bg="black", padx=20, pady=20)
    frame.pack(side=tk.LEFT)

    label = tk.Label(
        frame, text="Good Player Name:", fg="white", bg="black", font=("Arial", 20)
    )
    label.pack()

    entry = tk.Entry(frame, name='good_player_entry', font=("Arial", 16))
    entry.pack()

    name_label = tk.Label(frame, text="", fg="blue", bg="black", font=("Arial", 14))
    name_label.pack()


def create_evil_player_input(window):
    frame = tk.Frame(window, name="evil_player_frame", bg="black", padx=20, pady=20)
    frame.pack(side=tk.RIGHT)

    label = tk.Label(
        frame, text="Evil Player Name:", fg="white", bg="black", font=("Arial", 20)
    )
    label.pack()

    entry = tk.Entry(frame, name='evil_player_entry', font=("Arial", 16))
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
    global continue_button_clicked, good_player_name, evil_player_name

    good_player_name = window.nametowidget('good_player_frame.good_player_entry').get()
    evil_player_name = window.nametowidget('evil_player_frame.evil_player_entry').get()
    if not good_player_name or not evil_player_name:
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

    create_good_player_input(window)
    create_evil_player_input(window)

    create_continue_button(window)

    window.mainloop()

    return continue_button_clicked, good_player_name, evil_player_name
