# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the characters.

define u = Character(None, image="non", kind=bubble)
define nar = nvl_narrator
define kin = Character("Kinito", kind=nvl)
define s = Character("Sam", kind=nvl)
define j = Character("Jade", kind=nvl)

# The game starts here.
label start:
    scene bg room

    "???" "ok"

    "???" "Well..."
    "???" "Just here to warn you that this is not the actual KinitoPET."
    "???" "It has spoilers and is not official."
    "???" "I just really wanted to make things more accessable. That's why I made this."
    "???" "I won't talk further. Let's go!"

    jump westart

    return
