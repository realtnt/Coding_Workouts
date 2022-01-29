from guizero import App, Text, TextBox, Box, PushButton, info
import random
import time

cell_height = 3
cell_width = 6
cell_bg_colour = "grey"
status_bg_colour = "light grey"
status_bg_warning_colour = "yellow"
status_end_of_game_colour = "sky blue"
status_bg_win_colour = "pink"
player_info_bg_warning_colour = "dark green"
border_width = 2
border_type = "ridge"  # flat, raised, sunken, ridge, solid, groove
player_1_colour = "red"
player_1_header_colour = "#ff5555"
player_1_text_colour = "white"
player_2_colour = "blue"
player_2_header_colour = "#5555ff"
player_2_text_colour = "white"
player_selected = 1
last_player_to_start = 1
number_of_moves = 0
player_1_score = 0
player_2_score = 0
player_phrase = ["make your move!",
                 "let's see what you got.",
                 "it's your turn.",
                 "hit it!",
                 "choose wisely..."]
round_finished = "Round finished!"

# Event handlers

# When a cell is clicked


def cell_clicked(event_data):
    global player_selected
    global number_of_moves

    if player_selected == 1:
        event_data.widget.bg = player_1_colour
        event_data.widget.text_color = player_1_text_colour
        event_data.widget.value = "X"
        text_player_info.bg = player_2_colour
        text_player_info.text_color = player_2_text_colour
        player_selected = 2
    else:
        event_data.widget.bg = player_2_colour
        event_data.widget.text_color = player_2_text_colour
        event_data.widget.value = "O"
        text_player_info.bg = player_1_colour
        text_player_info.text_color = player_1_text_colour
        player_selected = 1
    event_data.widget.when_left_button_released = already_selected
    text_player_info.value = "Player " + \
        str(player_selected) + " " + random.choice(player_phrase)
    text_status.value = "Ready to play"
    text_status.bg = status_bg_colour
    number_of_moves += 1
    if number_of_moves == 9:
        text_player_info.bg = player_info_bg_warning_colour
        text_player_info.value = "It's a tie!"
        text_status.value = round_finished
        text_status.bg = status_end_of_game_colour
        for cell_event in range(0, 9):
            text[cell_event].when_left_button_released = game_finished
        btn_reset.enable()
    check_for_tictactoe()

# Check if we have a winner - also updates UI and score


def check_for_tictactoe():
    global player_1_score
    global player_2_score

    if ((text[0].value == "O" and text[1].value == "O" and text[2].value == "O") or
       (text[3].value == "O" and text[4].value == "O" and text[5].value == "O") or
       (text[6].value == "O" and text[7].value == "O" and text[8].value == "O") or
       (text[0].value == "O" and text[3].value == "O" and text[6].value == "O") or
       (text[1].value == "O" and text[4].value == "O" and text[7].value == "O") or
       (text[2].value == "O" and text[5].value == "O" and text[8].value == "O") or
       (text[0].value == "O" and text[4].value == "O" and text[8].value == "O") or
       (text[2].value == "O" and text[4].value == "O" and text[6].value == "O")):
        text_status.value = round_finished
        text_status.bg = status_end_of_game_colour
        text_player_info.bg = player_info_bg_warning_colour
        text_player_info.value = "Player 2 Wins!"
        board.bg = player_2_colour
        player_2_score += 1
        text_player_2_score.value = player_2_score
        for cell_event in range(0, 9):
            text[cell_event].when_left_button_released = game_finished
        btn_reset.enable()
    if ((text[0].value == "X" and text[1].value == "X" and text[2].value == "X") or
       (text[3].value == "X" and text[4].value == "X" and text[5].value == "X") or
       (text[6].value == "X" and text[7].value == "X" and text[8].value == "X") or
       (text[0].value == "X" and text[3].value == "X" and text[6].value == "X") or
       (text[1].value == "X" and text[4].value == "X" and text[7].value == "X") or
       (text[2].value == "X" and text[5].value == "X" and text[8].value == "X") or
       (text[0].value == "X" and text[4].value == "X" and text[8].value == "X") or
       (text[2].value == "X" and text[4].value == "X" and text[6].value == "X")):
        text_status.value = round_finished
        text_status.bg = status_end_of_game_colour
        text_player_info.bg = player_info_bg_warning_colour
        text_player_info.value = "Player 1 Wins!"
        board.bg = player_1_colour
        player_1_score += 1
        text_player_1_score.value = player_1_score
        for cell_event in range(0, 9):
            text[cell_event].when_left_button_released = game_finished
        btn_reset.enable()

# Don't allow player to click a cell that is not empty


def already_selected():
    if number_of_moves < 9:
        text_status.value = "That cell is not available"
        text_status.bg = status_bg_warning_colour

# Game finished message


def game_finished():
    text_status.value = "Game finished. Reset the board or exit."
    text_status.bg = status_bg_warning_colour

# Restart Match


def restart_match():
    global player_1_score, player_2_score
    text_player_1_score.value = text_player_2_score.value = player_1_score = player_2_score = 0
    reset_board()

# Reset the board


def reset_board():
    global player_selected
    global number_of_moves
    global last_player_to_start

    if last_player_to_start == 1:
        last_player_to_start = player_selected = 2
        text_player_info.bg = player_2_colour
        text_player_info.text_color = player_2_text_colour
    else:
        last_player_to_start = player_selected = 1
        text_player_info.bg = player_1_colour
        text_player_info.text_color = player_1_text_colour
    number_of_moves = 0

    text_status.value = "Ready to play"
    text_status.bg = status_bg_colour
    text_status.text_size = 10
    text_player_info.value = "Player " + \
        str(player_selected) + " " + random.choice(player_phrase)
    for cell in range(0, 9):
        text[cell].bg = cell_bg_colour
        text[cell].value = ""
    for cell_event in range(0, 9):
        text[cell_event].when_left_button_released = cell_clicked
    btn_reset.disable()


# GUI
app = App(title="Tic Tac Toe", width=350)

# board
board = Box(app, layout="grid")
board.text_size = 23

text = []  # create an empty list for our widgets

# create all the cells - they are of type Text but they could've been PushButtons
for x in range(0, 3):
    for y in range(0, 3):
        text.append(Text(
            board, grid=[x, y], height=cell_height, width=cell_width, bg=cell_bg_colour))

# change colour and border
for cell in range(0, 9):
    text[cell].tk.config(borderwidth=border_width)
    text[cell].tk.config(relief=border_type)

# reset board button
btn_reset = PushButton(app, text="Reset Board",
                       command=reset_board, width="fill")
btn_reset.disable()

messages = Box(app, layout="grid", width="fill", height="fill")

# player 1 score box
player_1_box = Box(messages, align="left", grid=[0, 0])
text_player_1_label = Text(player_1_box, text="Player 1", width=10)
text_player_1_score = Text(player_1_box, text="0", width="fill")
text_player_1_label.bg = player_1_header_colour
text_player_1_label.text_size = 15
text_player_1_label.text_color = player_1_text_colour
text_player_1_score.bg = player_1_colour
text_player_1_score.text_size = 22
text_player_1_score.text_color = player_1_text_colour

btn_restart_match = PushButton(messages, text="Restart\nMatch", width=13, height=2, grid=[
                               1, 0], command=restart_match)

# player 2 score box
player_2_box = Box(messages, align="right", grid=[2, 0])
text_player_2_label = Text(player_2_box, text="Player 2", width=10)
text_player_2_score = Text(player_2_box, text="0", width="fill")
text_player_2_label.bg = player_2_header_colour
text_player_2_label.text_size = 15
text_player_2_label.text_color = player_2_text_colour
text_player_2_score.bg = player_2_colour
text_player_2_score.text_size = 22
text_player_2_score.text_color = player_2_text_colour

# status bar
text_status = Text(app, text="Ready to play", align="bottom", width="fill")
text_status.bg = status_bg_colour
text_status.text_size = 10

# add a little text to show who's playing
text_player_info = Text(app, text="Player 1 " + random.choice(player_phrase),
                        bg=player_1_colour, width="fill", align="bottom")
text_player_info.text_size = 18
text_player_info.text_color = "white"

# Events

# for-loop to create the click event handlers
for cell_event in range(0, 9):
    text[cell_event].when_left_button_released = cell_clicked

app.display()
