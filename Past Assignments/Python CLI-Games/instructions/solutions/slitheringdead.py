
def makeChoice(prompt, options):
    print(prompt)
    print(options)
    choice = input("> ")
    return choice


story = """You wake up in a hospital bed.
You were in a car accident and must have slipped into a coma.
You look down at your wrist and see your name on your hosptial bracelet."""

print(story)

playerName = input("What is your name, survivor? > ")
print(f"Ok, {playerName}. The room is in disarray. You hear a shout and people running outside the door.")
print(
    """
    What do you do next?
    1) Get out of bed and look around.
    2) Stay in bed and wait for someone to come.
    """
)
firstChoice = input("> ")

if firstChoice == '1':
    print("""
    You get up, slip on some water and fall to the floor.
    Under the foot of your bed you see what looks like a coil of black hose.
    You start when it begins to move. The head a greyblack python emerges.
    This is not a hose. Its red eyes fix on you and it slithers at you. Fast.
    """)
    print(
    """
    What do you do next?
    1) Scramble back up into bed.
    2) Reach over and grab a fallen food tray and wack the oncoming snake.
    """
    )
    secondChoice = input("> ")
    if secondChoice == '1':
        print("""
    As you haul yourself up into bed, you feel a white hot flash of pain
    in the heel of your foot. Lava flows into your veins, and you feel
    your heart constrict.
    You go into shock, sieze, and then foam at the mouth.
    Moments later, you are a still. Frozen. Everything goes dark.
    Later, you awake. You taste the air around you with a flick of your tongue...
        """)
    else:
        print("""
You slice at the snake with the twisted tray, and catch it right below
the head neatly cutting off its head. The eyes grow dim. The mouth lols
open revealing terrible long white fangs.
        """)
else:
    print('The noise in the hallway fades. You hear a distant scream. Then nothing. After a few moments, you hear something like papers ruffling under your bed.')
