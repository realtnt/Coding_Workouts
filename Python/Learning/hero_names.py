# guizero - Hero name generator
from guizero import App, Text, Combo, PushButton, TextBox, CheckBox, Box
import random

dark_bg = "Black"
light_bg = "White"
colour1 = "#D4F0F0"
colour2 = "#ABDEE6"
colour3 = "#A2E1DB"
colour4 = "#8FCACA"
colour5 = "#55CBCD"
colour6 = "#FFCBA2"
colour7 = "#FF968A"


app = App(title="Hero-o-matic", width=400, height=800)

colour_options = ["Red", "Gold", "Blue", "Yellow", "Silver", "Black", "Pink", "White", "Brown", "Purple"]
animal_options = ["Avocado", "Badger", "Cat", "Rabbit", "Dolphin", "Velociraptor", "Mouse", "Hamster", "Hawk", "Eagle", "Slug", "Tortoise", "Dog", "Pigeon", "Unicorn", "Horse"]
adjective_options = ["Amazing", "Brainless", "Bonny", "Charming", "Delightful", "Scrawny", "Dirty", "Powerful", "Sorry", "Unstoppable", "Terrible"]
adjective2_options = ["Hyper", "Super", "Uber", "Ultra", "Mega", "Micro", "Mini", "Crazy"]

# Function definitions for your events go here.
def make_hero_name():
    if check_random.value == 1:
        adjective = random.choice(adjective_options)
        colour = random.choice(colour_options)
        animal = random.choice(animal_options)
        adjective2 = random.choice(adjective2_options)
    else:
        adjective = cmb_adjective.value
        colour = cmb_colour.value
        animal = cmb_animal.value
        adjective2 = cmb_adjective2.value
    if colour == "Gold" or colour == "Yellow" or colour == "Silver" or colour == "Pink" or colour == "White":
        lbl_herooutput.bg = dark_bg
        lbl_name.bg = dark_bg
    else:
        lbl_herooutput.bg = light_bg
        lbl_name.bg = light_bg
    lbl_name.value = txtbox_name.value+" the"
    lbl_name.text_color = colour
    hero = adjective2 + " " + adjective + " " + colour + " " + animal
    lbl_herooutput.value = hero
    lbl_herooutput.text_color = colour

# Toggle controls
def toggle_controls():
    if check_random.value == 1:
        cmb_adjective.disable()
        cmb_colour.disable()
        cmb_animal.disable()
        cmb_adjective2.disable()
        btn_make_name.text = "AI taking over!"
    else:
        cmb_adjective.enable()
        cmb_colour.enable()
        cmb_animal.enable()
        cmb_adjective2.enable()
        btn_make_name.text = "Compile name"

# Check for name
def check_for_name():
    if txtbox_name.value != "":
        btn_make_name.enable()
    else:
        btn_make_name.disable()

# Your GUI widgets go here
box1 = Box(app, width="fill")
box1.bg = colour1
message1 = Text(box1, text="Choose a prefix:", size=12, font="Arial Black", align="left")
cmb_adjective2 = Combo(box1, options=adjective2_options, selected="Super", width=11, height=3, align="right")
cmb_adjective2.font = "Arial Black"
cmb_adjective2.text_size = 12

box2 = Box(app, width="fill")
box2.bg = colour2
message2 = Text(box2, text="Choose an adjective:", size=12, font="Arial Black", align="left")
cmb_adjective = Combo(box2, options=adjective_options, selected="Amazing", width=11, height=3, align="right")
cmb_adjective.font = "Arial Black"
cmb_adjective.text_size = 12

box3 = Box(app, width="fill")
box3.bg = colour3
message3 = Text(box3, text="Pick a colour:", size=12, font="Arial Black", align="left")
cmb_colour = Combo(box3, options=colour_options, selected="Black", width=11, height=3, align="right")
cmb_colour.font = "Arial Black"
cmb_colour.text_size = 12

box4 = Box(app, width="fill")
box4.bg = colour4
message4 = Text(box4, text="Pick an animal:", size=12, font="Arial Black", align="left")
cmb_animal = Combo(box4, options=animal_options, selected="Aardvark", width=11, height=3, align="right")
cmb_animal.font = "Arial Black"
cmb_animal.text_size = 12

box5 = Box(app, width="fill")
box5.bg = colour5
name = Text(box5, text="What is your name?", size=12, font="Arial Black", height=3, align="left")
txtbox_name = TextBox(box5, width=14, align="right")
txtbox_name.text_size="16"

check_random = CheckBox(app, text="Randomise", command=toggle_controls, height=3, width="fill")
check_random.font="Arial Black"
check_random.text_size=12
check_random.bg = colour6

box6 = Box(app, width="fill")
box6.bg = colour7
lbl_pressbutton = Text(box6, text="Press the button below\nto get your hero name:", height=3, width="fill", size=14, font="Arial Black")
btn_make_name = PushButton(box6, text="Make me a hero!", command=make_hero_name)
btn_make_name.disable()
btn_make_name.font="Arial Black"
btn_make_name.text_size=12

lbl_output = Text(app, text="You are...", height=1, width="fill", size=24, font="Impact")
lbl_name = Text(app, text=" ", height=1, width="fill", size=20, font="Impact")
lbl_herooutput = Text(app, text=" ", color=cmb_colour.value, height=1, width="fill", size=20, font="Impact")

# Set up event triggers here
txtbox_name.when_key_released = check_for_name

# Show the GUI on the screen, start listening to events.
app.display()