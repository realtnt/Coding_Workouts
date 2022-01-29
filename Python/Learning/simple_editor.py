from guizero import App, Text, TextBox, PushButton, Box, Combo, CheckBox, Slider, MenuBar, info, select_file
import re
import os

status_saved = "Saved"
status_not_saved = "Changed"

# List for fonts
fonts = ["Courier", "Times New Roman", "Verdana", "Arial", "Arial Black"]
colours = ["Black", "Blue", "Red", "Yellow", "Green"]
font_size = [8, 10, 12, 14, 16, 18, 20, 22, 25, 28, 31, 35, 40]

# Functions


def set_filename(file_name):
    filename.value = file_name
    app.title = os.path.basename(file_name)


def open_file():
    file_name = select_file(title="Select file", folder=".", filetypes=[
                            ["txt", "*.txt"], ["All files", "*.*"]], save=False)
    if file_name:
        try:
            with open(file_name, "r") as f:
                editor.value = f.read()
        except IOError:
            print("Could not read file:", file_name)
        set_filename(file_name)
        set_file_saved()


def save_file():
    file_name = app.title
    if file_name and (file_name == "textzero" or file_name == "New file"):
        save_file_as()
    else:
        try:
            with open(file_name, "w") as f:
                f.write(editor.value)
        except IOError:
            print("Could not save file: ", file_name)
        set_file_saved()


def change_font():
    editor.font = font.value


def change_text_size():
    editor.text_size = size.value
    editor.resize(1, 1)
    editor.resize("fill", "fill")


def change_colour():
    editor.text_color = colour.value


def new_file():
    editor.clear()
    app.title = "New file"


def save_file_as():
    file_name = select_file(title="Select file", folder=".", filetypes=[
                            ["txt", "*.txt"], ["All files", "*.*"]], save=True)
    if file_name:
        try:
            with open(file_name, "w") as f:
                f.write(editor.value)
        except IOError:
            print("Could not save file:", file_name)
        set_file_saved()
        set_filename(file_name)


def exit_app():
    if status.value == status_not_saved:
        save_and_exit = app.yesno(
            "File not saved", "Do you want to Save and Exit?")
        if save_and_exit:
            save_file()
            if status.value == status_saved:
                app.info(title="File", text="File saved.")
    app.destroy()


def clear_editor():
    editor.clear()


def count_chars():
    # don't count spaces/carriage returns
    chars = len(editor.value) - len(re.findall(r'\w+', editor.value))
    info(title="Characters", text=chars)


def count_words():
    info(title="Words", text=len(re.findall(r'\w+', editor.value)))


def set_file_not_saved():
    status.value = status_not_saved
    status.bg = "#FFCBC1"


def set_file_saved():
    status.value = status_saved
    status.bg = "#DBFFD6"


def toggle_theme():
    if editor.bg == "White":
        editor.bg = "#222222"
        editor.text_color = "#dddddd"
    else:
        editor.bg = "White"
        editor.text_color = "Black"


# Menus
top_menu = ["File", "Edit"]
file_menu = [["New", new_file],
             ["Open...", open_file],
             ["Save", save_file],
             ["Save As...", save_file_as],
             ["Exit", exit_app]]
edit_menu = [["Clear", clear_editor],
             ["Count Characters", count_chars],
             ["Count Words", count_words]]

# Widgets
app = App(title="textzero")

menubar = MenuBar(app,
                  toplevel=top_menu,
                  options=[file_menu, edit_menu])

preferences_controls = Box(app,
                           align="top",
                           width="fill",
                           border=True)
font = Combo(preferences_controls,
             options=fonts,
             align="left",
             command=change_font,
             height=2,
             width=10)
size = Combo(preferences_controls,
             options=font_size,
             align="left",
             selected="12",
             command=change_text_size,
             height=2,
             width=10)
colour = Combo(preferences_controls,
               options=colours,
               align="left",
               selected="Black",
               command=change_colour,
               height=2,
               width=10)
theme = PushButton(preferences_controls,
                   text="DarkUI",
                   command=toggle_theme,
                   width=7,
                   height=1,
                   align="right")

editor = TextBox(app,
                 multiline=True,
                 height="fill",
                 width="fill")
editor.bg = "White"

box_status = Box(app, width="fill")
box_status.text_size = 8
filename = Text(box_status, height=1, text="---", align="left")
status = Text(box_status, height=1, text=status_saved, align="right")
status.bg = "#DBFFD6"

# Events
editor.when_key_released = set_file_not_saved

app.display()
